import re

with open('sharon_main.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements
html = html.replace('Sharon Infotech', 'Vanishka Enterprises')
html = html.replace('SHARON INFOTECH', 'VANISHKA ENTERPRISES')
html = html.replace('Nagpur', 'Pune')
html = html.replace('+91-7249430043', '+91-8600572488')
html = html.replace('+917249430043', '+918600572488')
html = html.replace('7249430043', '8600572488')
html = html.replace('prabhu@sharoninfotech.com', 'hello@vanishka.com')
html = html.replace('Office No 1, Second Floor, Tilak Patrakar Bhawan, Panchasheel Square, Near Panchasheel Theater, Dhantoli', 'Tech Hub Street, Pune / MH 411001')
html = html.replace('Dhantoli', 'Pune')

# Save updated HTML
with open('vanishka_main.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved vanishka_main.html")
