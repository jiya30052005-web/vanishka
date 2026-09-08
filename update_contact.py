import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the form category label and options
old_category_html = '''<label for="contactCategory" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Product Category Interested In *</label>
                <select id="contactCategory" required
                  class="w-full px-4 py-3 text-sm rounded-xl border border-slate-200 outline-none focus:border-fb focus:ring-2 focus:ring-fb/20 bg-slate-50/50 text-slate-700 font-medium">
                  <option value="Certified Refurbished Laptops (Dell, HP, Lenovo)">Certified Refurbished Laptops (Dell, HP, Lenovo)</option>
                  <option value="Canon Printers & Ink Tanks">Canon Printers &amp; Ink Tanks</option>
                  <option value="Interactive Smart Digital Boards (BenQ, LG, Cybernetyx)">Interactive Smart Digital Boards (BenQ, LG, Cybernetyx)</option>
                  <option value="Computer Hardware & Components">Computer Hardware &amp; Components</option>
                  <option value="Networking & Security Equipment (Hikvision)">Networking &amp; Security Equipment (Hikvision)</option>
                  <option value="Bulk Corporate / School Purchase">Bulk Corporate / School Purchase</option>
                  <option value="Other Product Inquiry">Other Product Inquiry</option>
                </select>'''

new_category_html = '''<label for="contactCategory" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Type of IT Service Needed *</label>
                <select id="contactCategory" required
                  class="w-full px-4 py-3 text-sm rounded-xl border border-slate-200 outline-none focus:border-fb focus:ring-2 focus:ring-fb/20 bg-slate-50/50 text-slate-700 font-medium">
                  <option value="Laptop & PC Repair">Laptop &amp; PC Repair (Motherboard, OS, Data Recovery)</option>
                  <option value="Printer Repair & Maintenance">Printer Repair &amp; Maintenance</option>
                  <option value="Smart Board Installation">Smart Board &amp; AV Installation</option>
                  <option value="Networking & Wi-Fi Setup">Networking &amp; Wi-Fi Troubleshooting</option>
                  <option value="Annual Maintenance Contract (AMC)">Annual Maintenance Contract (AMC)</option>
                  <option value="Other IT Service">Other IT Service</option>
                </select>'''
html = html.replace(old_category_html, new_category_html)

# 2. Update message label and placeholder
old_message_label = '<label for="contactMessage" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Message / Product Specification *</label>'
new_message_label = '<label for="contactMessage" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Describe the issue or service required *</label>'
html = html.replace(old_message_label, new_message_label)

old_placeholder = 'placeholder="Specify model, quantity, or any specific question you have..."'
new_placeholder = 'placeholder="Please describe the problem you are facing or the service you need..."'
html = html.replace(old_placeholder, new_placeholder)

# 3. Update the submit button text
old_btn_text = 'Send Inquiry On WhatsApp 💬'
new_btn_text = 'Send Service Request On WhatsApp 💬'
html = html.replace(old_btn_text, new_btn_text)

# 4. Update JS WhatsApp Template
old_js = '''var text = "Hello Vanishka Enterprises,\\n\\n" +
                 "I would like to place an order / inquiry:\\n" +
                 "👤  *Name:* " + name + "\\n" +
                 "📞 *Phone/WhatsApp:* " + phone + "\\n" +
                 "📦 *Category:* " + category + "\\n" +
                 "📝 *Message:* " + message;'''
# Notice the emojis were broken encoding in powershell output ("dY"), we can use literal text replacement
import re
js_pattern = r'var text = "Hello Vanishka Enterprises,\\n\\n"\s*\+\s*"I would like to place an order / inquiry:\\n"\s*\+\s*".*?\*Name:\*\s*"\s*\+\s*name\s*\+\s*"\\n"\s*\+\s*".*?\*Phone/WhatsApp:\*\s*"\s*\+\s*phone\s*\+\s*"\\n"\s*\+\s*".*?\*Category:\*\s*"\s*\+\s*category\s*\+\s*"\\n"\s*\+\s*".*?\*Message:\*\s*"\s*\+\s*message;'

new_js = '''var text = "Hello Vanishka Enterprises,\\n\\n" +
                 "I would like to request an IT service:\\n" +
                 "👤 *Name:* " + name + "\\n" +
                 "📞 *Phone/WhatsApp:* " + phone + "\\n" +
                 "🛠️ *Service Needed:* " + category + "\\n" +
                 "📝 *Description:* " + message;'''

html = re.sub(js_pattern, new_js, html, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated form in contact.html")
