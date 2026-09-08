import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update helper text
old_helper = 'Our team will verify product stock, send real photos/videos if needed, and confirm your order details instantly.'
new_helper = 'Our technical team will review your service request and get back to you instantly to schedule a visit or provide support.'
html = html.replace(old_helper, new_helper)

old_badge = 'Fast Track Form'
new_badge = 'Service Request Form'
html = html.replace(old_badge, new_badge)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated helper text!")
