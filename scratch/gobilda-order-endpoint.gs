/**
 * goBILDA Group Order — submission endpoint
 * ------------------------------------------------------------------
 * Catches each order from the hosted form and writes it into a Google
 * Sheet that OnTalent and the fulfillment team both work from.
 *
 * SETUP (5 minutes):
 *   1. Open the Google Sheet you want orders written into.
 *   2. Copy its ID from the URL — the long part between /d/ and /edit:
 *        https://docs.google.com/spreadsheets/d/THIS_IS_THE_ID/edit
 *      Paste it into SHEET_ID below.
 *   3. Extensions > Apps Script. Delete the sample code, paste this whole
 *      file in, and Save.
 *   4. Deploy > New deployment > (gear) Web app.
 *        - Execute as:      Me
 *        - Who has access:  Anyone
 *      Deploy, authorize when prompted, and COPY the Web app URL (/exec).
 *   5. Paste that URL into the form's CONFIG.submitEndpoint.
 *   6. TEST: open the /exec URL in a browser — it should say
 *        "OK — writing to: <your sheet name>"
 *      Then submit a test order; rows appear in the two tabs below.
 *
 * IMPORTANT: every time you edit this script you must redeploy a NEW
 * VERSION, or the web app keeps running the old code:
 *   Deploy > Manage deployments > (pencil) Edit > Version: New version > Deploy
 *
 * Two tabs are filled automatically:
 *   "Order Lines" — one row per part  (pivot by Part # = bulk quantities)
 *   "Orders"      — one row per person (order list + group total)
 * ------------------------------------------------------------------
 */

// Paste your Google Sheet ID here (recommended — removes all ambiguity).
// Leave "" to fall back to the sheet this script is bound to.
var SHEET_ID = "";

// Get an email for every order. Set to "" to turn off.
var NOTIFY_EMAIL = "info@ontalent.org";
// Email each participant a confirmation copy of their order.
var SEND_CONFIRMATION = true;

// Resolve the target spreadsheet explicitly, with a clear error if missing.
function getSpreadsheet_() {
  if (SHEET_ID) return SpreadsheetApp.openById(SHEET_ID);
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    throw new Error("No spreadsheet found. This script is not bound to a Sheet — set SHEET_ID at the top.");
  }
  return ss;
}

// Health check: open the /exec URL in a browser to confirm the deployment
// is live AND pointed at the right spreadsheet.
function doGet() {
  try {
    var ss = getSpreadsheet_();
    return ContentService.createTextOutput("OK — writing to: " + ss.getName());
  } catch (err) {
    return ContentService.createTextOutput("NOT READY — " + String(err));
  }
}

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    // Honeypot: silently ignore bot submissions.
    if (data.company) { return ok_(); }

    var ss = getSpreadsheet_();
    var orderId = "GB-" + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyyMMdd-HHmmss");

    // ---- Order Lines: one row per item ----
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

    // ---- Orders: one summary row per order ----
    var orders = ss.getSheetByName("Orders") || ss.insertSheet("Orders");
    if (orders.getLastRow() === 0) {
      orders.appendRow(["Submitted", "Order ID", "Name", "Email", "Phone", "Team",
        "Fulfillment", "Postal", "# items", "Subtotal", "Shipping", "Total", "Currency", "Status", "Notes"]);
    }
    orders.appendRow([new Date(), orderId, data.name, data.email, data.phone, data.team,
      data.fulfillment, data.postal, items.length, data.subtotal, data.shipping, data.total,
      data.currency, "New", data.notes]);

    // ---- Notifications ----
    if (NOTIFY_EMAIL) {
      MailApp.sendEmail(NOTIFY_EMAIL, "New goBILDA group order — " + data.name, data.summary);
    }
    if (SEND_CONFIRMATION && data.email) {
      MailApp.sendEmail(data.email, "Your goBILDA group order — " + data.org,
        "Thanks, " + data.name + " — your order is in.\n\n" + data.summary);
    }

    return ok_();
  } catch (err) {
    // Surface failures instead of failing silently (the form can't read the response).
    if (NOTIFY_EMAIL) {
      try {
        MailApp.sendEmail(NOTIFY_EMAIL, "goBILDA order ERROR — not written to Sheet",
          String(err) + "\n\n--- raw payload ---\n" + ((e && e.postData) ? e.postData.contents : "(none)"));
      } catch (e2) {}
    }
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function ok_() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}
