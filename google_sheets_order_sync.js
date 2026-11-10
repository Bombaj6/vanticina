/**
 * =========================================================================
 * VANTACIN+ Google Sheets + Instant Email Automation Script
 * =========================================================================
 * 
 * HOW TO INSTALL IN 60 SECONDS:
 * 1. Open your Google Drive -> Create a new Google Sheet (e.g. named "Vantacin+ Orders").
 * 2. In Row 1, add these headers:
 *    A1: Timestamp
 *    B1: Order Ref
 *    C1: Customer Name
 *    D1: Phone Number
 *    E1: Alt / WhatsApp Phone
 *    F1: Delivery Address
 *    G1: City
 *    H1: State
 *    I1: Package
 *    J1: Amount (NGN)
 *    K1: Payment Method
 *    L1: Dispatch Status
 * 
 * 3. Go to "Extensions" (top menu) -> Click "Apps Script".
 * 4. Delete any code in the editor and PASTE this entire script.
 * 5. Change NOTIFICATION_EMAIL below to your email (defaults to bombaj6@gmail.com).
 * 6. Click "Deploy" (blue button at top right) -> "New deployment".
 * 7. Click the gear icon next to "Select type" -> choose "Web app".
 * 8. Set:
 *    - Description: "Vantacin Orders Webhook"
 *    - Execute as: "Me"
 *    - Who has access: "Anyone" (IMPORTANT: select Anyone so Cloudflare can post to it)
 * 9. Click "Deploy" -> Authorize permissions.
 * 10. Copy the "Web app URL" (starts with https://script.google.com/macros/s/...)
 * =========================================================================
 */

const NOTIFICATION_EMAIL = "bombaj6@gmail.com";

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = JSON.parse(e.postData.contents);

    const timestamp = Utilities.formatDate(new Date(), "Africa/Lagos", "yyyy-MM-dd HH:mm:ss");
    const orderRef = data.orderRef || "VAN-" + new Date().getTime();
    const name = data.name || "Customer";
    const phone = data.phone || "";
    const altPhone = data.altPhone || data.alt_phone || "";
    const address = data.address || "";
    const city = data.city || "";
    const state = data.state || "";
    const packageLabel = data.packageLabel || data.plan || "";
    const amount = data.amount ? "₦" + Number(data.amount).toLocaleString() : "";
    const paymentMethod = data.paymentMethod || "Cash on Delivery (COD)";

    // Append row to Google Sheet
    sheet.appendRow([
      timestamp,
      orderRef,
      name,
      phone,
      altPhone,
      address,
      city,
      state,
      packageLabel,
      amount,
      paymentMethod,
      "Pending Call"
    ]);

    // Send Instant Email Notification
    if (NOTIFICATION_EMAIL) {
      const emailSubject = `🚨 NEW ORDER: ${packageLabel} - ${name} (${state})`;
      const emailBody = `
========================================
           NEW VANTACIN+ ORDER
========================================

📦 PACKAGE: ${packageLabel}
💰 TOTAL AMOUNT: ${amount}
🚚 PAYMENT METHOD: ${paymentMethod}
🆔 ORDER REF: ${orderRef}
⏰ TIME: ${timestamp}

---------------- CUSTOMER INFO ----------------
👤 NAME: ${name}
📞 PHONE: ${phone}
📱 ALT / WHATSAPP: ${altPhone}
📍 DELIVERY ADDRESS: ${address}
🏙️ CITY: ${city}
🗺️ STATE: ${state}

👉 Open your Google Sheet to view and update dispatch status.
WhatsApp Customer Link: https://wa.me/${phone.replace(/[^0-9]/g, "")}
`;

      MailApp.sendEmail({
        to: NOTIFICATION_EMAIL,
        subject: emailSubject,
        body: emailBody
      });
    }

    return ContentService.createTextOutput(JSON.stringify({
      result: "success",
      orderRef: orderRef
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      result: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("Vantacin+ Webhook is running active!");
}
