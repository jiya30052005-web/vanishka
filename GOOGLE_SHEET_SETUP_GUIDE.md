# Google Sheet & Email Setup Guide (Vanishka Enterprises)
**Google Account: `vanishkaenterprises.marketing@gmail.com`**

Jab bhi koi customer aapki website ke **Contact Form** ko submit karega:
1. Wo customer ka data (Naam, Mobile, Nagpur Area, Service, Message, Timestamp) automatically aapke **Google Sheet** mein save ho jayega.
2. Usi waqt aapki Gmail **`vanishkaenterprises.marketing@gmail.com`** par instant email notification alert bhi aayega!

---

## 2 Minute Setup Steps (Bahut Aasaan Hai):

### Step 1: Google Sheet Banayein
1. Browser mein `vanishkaenterprises.marketing@gmail.com` se login kijiye.
2. Yeh link open kijiye: **[https://sheets.new](https://sheets.new)** (ek new Google Sheet open ho jayegi).
3. Sheet ka naam upar left me dijiye: **Vanishka Enterprises - Website Inquiries**

---

### Step 2: Apps Script Code Paste Kijiye
1. Upar menu mein **Extensions** par click kijiye, fir **Apps Script** select kijiye.
2. Jo code editor khulega, waha pehle se likha hua `function myFunction() {}` **delete kar dijiye**.
3. Ab project folder mein bani hui **`google-apps-script.js`** file ka pura code copy karke waha **paste kar dijiye**.
4. Upar **Save icon** (💾) par click kijiye.

---

### Step 3: Web App Deploy Kijiye (Sabse Important Step)
1. Upar right side mein blue color ka **Deploy** button hoga -> click kijiye aur **New deployment** chuniye.
2. "Select type" ke bagal mein **Gear icon (⚙️)** par click karke **Web app** select kijiye.
3. Form mein yeh fill kijiye:
   - **Description**: `Vanishka Form`
   - **Execute as**: `Me (vanishkaenterprises.marketing@gmail.com)`
   - **Who has access**: **`Anyone`** *(Yeh jarur select karein taaki website ke users bina login kiye form bhej sakein)*
4. Niche **Deploy** button dabayein.
5. Ek popup aayega **"Authorize access"**:
   - Apna Google account select kijiye (`vanishkaenterprises.marketing@gmail.com`).
   - Agar warning screen aaye ("Google hasn't verified this app"):
     - Niche **Advanced** par click karein.
     - **Go to Untitled project (unsafe)** par click karein.
     - Niche scroll karke **Allow** dabayein.
6. Ab aapko screen par ek **Web app URL** milega (jo `https://script.google.com/macros/s/.../exec` jaisa dikhega).
7. Us URL ko **Copy** kar lijiye!

---

### Step 4: contact.html mein URL Paste Karein
1. Apne `contact.html` (aur `computerbaba-redesign/contact.html`) mein niche JavaScript code mein:
   ```javascript
   const GOOGLE_SCRIPT_URL = "APNA_COPIED_URL_YAHA_PASTE_KAREIN";
   ```
   Waha apna copied URL paste kar dijiye!

---

## Testing:
- `contact.html` open karein, form fill karein aur **Send Message to Engineer** button click karein.
- Sheet check karein: Data automatically naye row mein show ho jayega.
- Gmail (`vanishkaenterprises.marketing@gmail.com`) check karein: Naya lead ka email alert aa chuka hoga!
- Saath hi user ko WhatsApp ka option bhi milega agar wo direct call/chat karna chahe.
