from bs4 import BeautifulSoup

# 1. Get the map section from sharon_main2.html
with open('sharon_main2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
main = soup.find('main')
children = main.find_all(recursive=False)
map_section_html = str(children[1]) if len(children) > 1 else ''

if not map_section_html:
    print("Map section not found!")
    exit(1)

# 2. Replace Sharon Infotech info with Vanishka info
# Company Info
map_section_html = map_section_html.replace('Sharon Infotech Service Center', 'Vanishka Enterprises Service Center')
map_section_html = map_section_html.replace('Sharon Infotech', 'Vanishka Enterprises')

# Address
map_section_html = map_section_html.replace('Office No 1, 2nd Floor, Tilak Patrakar Bhawan, Panchasheel Square, Near Panchasheel Theater, Dhantoli, Nagpur 440012', 'Tech Hub Street, Pune / MH 411001')
map_section_html = map_section_html.replace('Office No 1, Second Floor, Tilak Patrakar Bhawan', 'Tech Hub Street')
map_section_html = map_section_html.replace('Panchasheel Square, Near Panchasheel Theater,', 'Pune City')
map_section_html = map_section_html.replace('Dhantoli, Nagpur, Maharashtra - <strong>440012</strong>', 'Maharashtra - <strong>411001</strong>')
map_section_html = map_section_html.replace('Nagpur', 'Pune')
map_section_html = map_section_html.replace('Panchasheel Square, beside Tilak Patrakar Bhawan &amp; near Panchasheel Cinema', 'Pune Tech Hub')
map_section_html = map_section_html.replace('Sitabuldi Metro Interchange &amp; Congress Nagar Metro', 'Pune Metro Station')

# Phone & URLs
map_section_html = map_section_html.replace('+91 72494 30043', '+91 86005 72488')
map_section_html = map_section_html.replace('+917249430043', '+918600572488')
# We can just change the map iframe URL to a standard Pune map
# The old one is a specific place in Nagpur.
# Pune's generic place: https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121059.04360434035!2d73.78056541571217!3d18.52460355325519!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bf2e67461101%3A0x828d43bf9d9ee343!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000
import re
map_section_html = re.sub(r'src="https://www\.google\.com/maps/embed[^"]+"', 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121059.04360434035!2d73.78056541571217!3d18.52460355325519!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bf2e67461101%3A0x828d43bf9d9ee343!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000"', map_section_html)

# GPS Coordinates
map_section_html = map_section_html.replace('21.1388952, 79.0800974', '18.5204, 73.8567')

# 3. Append to contact.html
file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We insert map_section_html right before </main>
insert_idx = html.rfind('</main>')
if insert_idx != -1:
    new_html = html[:insert_idx] + '\n' + map_section_html + '\n' + html[insert_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Map section appended successfully!")
else:
    print("Could not find </main> tag.")

