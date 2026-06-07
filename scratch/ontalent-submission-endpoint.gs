/**
 * OnTalent — submission endpoint (orders + workshops + team support)
 * ------------------------------------------------------------------
 * One web app handles three kinds of submission, chosen by "type":
 *
 *   (none) / "order"  ->  goBILDA group order      (Order Lines + Orders)
 *   "workshop"        ->  workshop application      (Workshop Applications)
 *   "team"            ->  FLL/FTC team support      (Team Building)
 *
 * TO UPDATE (no new authorization needed):
 *   1. Open the SAME Sheet + Apps Script project you already deployed.
 *   2. Select all old code, delete, paste this whole file in, Save.
 *   3. Deploy > Manage deployments > (edit your web app) >
 *      Version: New version > Deploy.   Keep the SAME web app URL.
 *   4. That one URL goes in all three forms' CONFIG.submitEndpoint.
 *
 * New tabs are created automatically on first submission of each type.
 * ------------------------------------------------------------------
 */

var NOTIFY_EMAIL = "info@ontalent.org";   // email per submission; "" to disable
var SEND_CONFIRMATION = true;             // email the person a copy

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    if (data.company) { return ok_(); }                 // honeypot
    if (data.type === "workshop") { return handleWorkshop_(data); }
    if (data.type === "team")     { return handleTeam_(data); }
    return handleOrder_(data);                           // default = group order
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/* ---------------- FLL/FTC team support ---------------- */
function handleTeam_(data) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName("Team Building") || ss.insertSheet("Team Building");
  if (sh.getLastRow() === 0) {
    sh.appendRow(["Submitted", "Status", "Name", "Role", "Email", "Phone",
      "School", "School type", "City", "Board",
      "Stage", "Programs", "Grades", "# students", "Did workshop",
      "Coach experience", "Mentors lined up", "Meeting space",
      "Needs", "Detail", "Funding", "Timeline", "Notes"]);
  }
  sh.appendRow([new Date(), "New", data.name, data.role, data.email, data.phone,
    data.school, data.schoolType, data.city, data.board,
    data.stage, data.programs, data.grades, data.students, data.didWorkshop,
    data.coachExp, data.mentors, data.space,
    data.needs, data.detail, data.funding, data.timeline, data.notes]);
  notify_(data, "New OnTalent team-support request — " + data.school, "Thanks, " + data.name + " — we've received your request and will follow up.");
  return ok_();
}

/* ---------------- Workshop applications ---------------- */
function handleWorkshop_(data) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName("Workshop Applications") || ss.insertSheet("Workshop Applications");
  if (sh.getLastRow() === 0) {
    sh.appendRow(["Submitted", "Status", "Name", "Role", "Email", "Phone",
      "Sponsor name", "Sponsor role", "Sponsor email",
      "School", "School type", "City", "Board",
      "Pathways", "Grades", "# students", "Format", "Location", "Timeframe",
      "Space/equipment", "Goals", "Funding", "Notes"]);
  }
  sh.appendRow([new Date(), "New", data.name, data.role, data.email, data.phone,
    data.sponsorName, data.sponsorRole, data.sponsorEmail,
    data.school, data.schoolType, data.city, data.board,
    data.pathways, data.grades, data.students, data.format, data.location, data.timeframe,
    data.space, data.goals, data.funding, data.notes]);
  notify_(data, "New OnTalent workshop application — " + data.school, "Thanks, " + data.name + " — we've received your request and will follow up.");
  return ok_();
}

/* ---------------- goBILDA group order ---------------- */
function handleOrder_(data) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var orderId = "GB-" + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyyMMdd-HHmmss");
  var lines = ss.getSheetByName("Order Lines") || ss.insertSheet("Order Lines");
  if (lines.getLastRow() === 0) {
    lines.appendRow(["Submitted", "Order ID", "Name", "Email", "Phone", "Team",
      "Fulfillment", "Address", "Postal", "Part #", "Product", "Qty", "Unit price", "Line total", "Notes"]);
  }
  var items = data.items || [];
  for (var i = 0; i < items.length; i++) {
    var it = items[i];
    lines.appendRow([new Date(), orderId, data.name, data.email, data.phone, data.team,
      data.fulfillment, data.address, data.postal,
      it.partNo, it.name, it.qty, it.price, it.lineTotal, data.notes]);
  }
  var orders = ss.getSheetByName("Orders") || ss.insertSheet("Orders");
  if (orders.getLastRow() === 0) {
    orders.appendRow(["Submitted", "Order ID", "Name", "Email", "Phone", "Team",
      "Fulfillment", "Postal", "# items", "Subtotal", "Shipping", "Total", "Currency", "Status", "Notes"]);
  }
  orders.appendRow([new Date(), orderId, data.name, data.email, data.phone, data.team,
    data.fulfillment, data.postal, items.length, data.subtotal, data.shipping, data.total,
    data.currency, "New", data.notes]);
  notify_(data, "New goBILDA group order — " + data.name, "Thanks, " + data.name + " — your order is in.");
  return ok_();
}

/* ---------------- shared helpers ---------------- */
function notify_(data, subject, confirmIntro) {
  if (NOTIFY_EMAIL) { MailApp.sendEmail(NOTIFY_EMAIL, subject, data.summary); }
  if (SEND_CONFIRMATION && data.email) { MailApp.sendEmail(data.email, subject, confirmIntro + "\n\n" + data.summary); }
}

function authorize() {  // run once from the editor to authorize, if needed
  SpreadsheetApp.getActiveSpreadsheet().getName();
  MailApp.getRemainingDailyQuota();
}

function ok_() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
}
