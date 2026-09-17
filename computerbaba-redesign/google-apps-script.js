/**
 * VANISHKA ENTERPRISES - GOOGLE SHEETS & EMAIL BACKEND INTEGRATION
 * Account: vanishkaenterprises.marketing@gmail.com
 * 
 * STEPS TO SETUP (2 Minutes):
 * 1. Open Google Sheets (https://sheets.new) logged in as vanishkaenterprises.marketing@gmail.com
 * 2. Name the sheet: "Vanishka Enterprises - Website Inquiries"
 * 3. Click menu "Extensions" -> "Apps Script"
 * 4. Delete any code in the editor, and PASTE this entire script.
 * 5. Click "Deploy" (top right button) -> "New deployment"
 * 6. Select type: "Web app" (click gear icon next to Select type)
 * 7. Set:
 *    - Description: "Vanishka Contact Form"
 *    - Execute as: "Me (vanishkaenterprises.marketing@gmail.com)"
 *    - Who has access: "Anyone" (IMPORTANT!)
 * 8. Click "Deploy", then "Authorize access" (choose vanishkaenterprises.marketing@gmail.com -> Advanced -> Go to ... (unsafe) -> Allow).
 * 9. Copy the "Web app URL" (looks like https://script.google.com/macros/s/AKfycb.../exec)
 * 10. Open contact.html and paste this URL into GOOGLE_SCRIPT_URL variable.
 * DONE! Every time someone submits the form, it will automatically:
 *   a) Save in your Google Sheet
 *   b) Send an instant email to vanishkaenterprises.marketing@gmail.com
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Auto-create Header Row if new sheet
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Timestamp (IST)",
        "Full Name",
        "Mobile Number",
        "Locality in Nagpur",
        "Service Needed",
        "Problem / Message",
        "Status"
      ]);
      
      // Format header row
      var headerRange = sheet.getRange(1, 1, 1, 7);
      headerRange.setFontWeight("bold");
      headerRange.setBackground("#1d65ff");
      headerRange.setFontColor("#ffffff");
      sheet.setFrozenRows(1);
    }

    var data;
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else {
      data = e.parameter || {};
    }

    var istDate = new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" });
    var name = data.name || data.fullName || "Not provided";
    var phone = data.phone || data.mobile || "Not provided";
    var locality = data.locality || "Not specified";
    var service = data.service || data.category || "General Inquiry";
    var message = data.message || "No message";

    // 1. Append Row to Google Sheet
    sheet.appendRow([
      istDate,
      name,
      phone,
      locality,
      service,
      message,
      "New"
    ]);

    // 2. Send Instant Email Alert to vanishkaenterprises.marketing@gmail.com
    var recipientEmail = "vanishkaenterprises.marketing@gmail.com";
    var emailSubject = "🔥 New Website Inquiry from " + name + " (" + locality + ")";
    
    var emailBody = 
      "Hello Vanishka Enterprises,\n\n" +
      "You have received a new customer inquiry from your website contact page!\n\n" +
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" +
      "👤 Customer Name: " + name + "\n" +
      "📞 Mobile Number: " + phone + "\n" +
      "📍 Nagpur Locality: " + locality + "\n" +
      "🛠️ Service Required: " + service + "\n" +
      "📝 Issue / Details: " + message + "\n" +
      "⏰ Date & Time: " + istDate + "\n" +
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
      "👉 This inquiry has also been automatically saved into your Google Sheet.\n" +
      "Call or WhatsApp the customer immediately for the fastest response!\n\n" +
      "— Vanishka Enterprises Automated Lead System";

    MailApp.sendEmail(recipientEmail, emailSubject, emailBody);

    return ContentService
      .createTextOutput(JSON.stringify({ result: "success", message: "Inquiry saved and emailed successfully!" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Fallback for GET request testing
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "active", message: "Vanishka Enterprises Contact API is running!" }))
    .setMimeType(ContentService.MimeType.JSON);
}
