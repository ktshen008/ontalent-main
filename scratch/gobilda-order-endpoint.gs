/**
 * goBILDA Group Order — submission endpoint
 * ------------------------------------------------------------------
 * This catches each order from the hosted form and writes it into THIS
 * Google Sheet, which becomes the single shared record ontalent and the
 * fulfillment team both work from.
 *
 * SETUP (5 minutes):
 *   1. Make a new Google Sheet — this is your shared order record.
 *   2. In that Sheet: Extensions > Apps Script. Delete the sample code,
 *      paste this whole file in, and Save.
 *   3. Deploy > New deployment > (gear) Web app.
 *        - Execute as:      Me
 *        - Who has access:  Anyone
 *      Deploy, authorize when prompted, and COPY the Web app URL.
 *   4. Paste that URL into the form's CONFIG.submitEndpoint, then
 *      re-upload the HTML to the ontalent website.
 *   5. Submit a test order — a row should appear in the Sheet.
 *
 * The form posts JSON; this script fills two tabs automatically:
 *   "Order Lines" — one row per part  (pivot by Part # = bulk quantities)
 *   "Orders"      — one row per person (order list + group total)
 * ------------------------------------------------------------------
 */

// Get an email for every order. Set to "" to turn off.
var NOTIFY_EMAIL = "orders@ontalent.org";
// Email each participant a confirmation copy of their order.
var SEND_CONFIRMATION = true;

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    // Honeypot: silently ignore bot submissions.
    if (data.company) { return ok_(); }

    var ss = SpreadsheetApp.getActiveSpreadsheet();
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
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function ok_() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}
