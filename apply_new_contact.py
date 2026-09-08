from bs4 import BeautifulSoup
import re

with open('sharon_main2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
main = soup.find('main')
children = main.find_all(recursive=False)

grid_html = str(children[0])

# Now replace Sharon Infotech data with Vanishka data
grid_html = grid_html.replace('Sharon Infotech', 'Vanishka Enterprises')
grid_html = grid_html.replace('sharoninfotech.com', 'vanishka.com')
grid_html = grid_html.replace('prabhu@sharoninfotech.com', 'hello@vanishka.com')
grid_html = grid_html.replace('+91-7249430043', '+91-8600572488')
grid_html = grid_html.replace('7249430043', '8600572488')
grid_html = grid_html.replace('Nagpur', 'Pune')
grid_html = grid_html.replace('Office No 1, 2nd Floor, Tilak Patrakar Bhawan, Panchasheel Square, Near Panchasheel Theater, Dhantoli, Nagpur 440012', 'Tech Hub Street, Pune / MH 411001')
grid_html = grid_html.replace('Dhantoli', 'Pune')
grid_html = grid_html.replace('Panchasheel Square', 'Tech Hub Street')

# Create the new body
new_body = f'<main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 w-full space-y-12">\n{grid_html}\n</main>'

# Now inject it into contact.html
file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'</header>.*?(?=<!--\s*==========================================\s*FOOTER)', '</header>\n' + new_body + '\n  ', html, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated contact.html with the new grid layout!")
