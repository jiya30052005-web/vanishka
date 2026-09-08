import bs4

orig_path = r'c:\Users\KISHORI CHARPE\Downloads\temp_extract\vanishka-main\computerbaba-redesign\index.html'
with open(orig_path, 'r', encoding='utf-8') as f:
    orig_soup = bs4.BeautifulSoup(f, 'html.parser')

# MUST deepcopy or just parse string!
s1_right_str = str(orig_soup.find_all('div', class_='hero-slide')[0].find('div', class_='hero-slide-visual'))
s2_right_str = str(orig_soup.find_all('div', class_='hero-slide')[1].find('div', class_='hero-slide-visual'))
s3_right_str = str(orig_soup.find_all('div', class_='hero-slide')[2].find('div', class_='hero-slide-visual'))

buttons_html = '''<div class="hero-stagger-5 mt-6 flex flex-wrap items-center gap-3">
            <a href="#" class="bg-electric hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              Book Doorstep Visit
            </a>
            <a href="https://wa.me/918600572488" class="bg-[#0b965c] hover:bg-[#097b4b] text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"></path></svg> Instant WhatsApp Chat
            </a>
            <a href="services.html" class="bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-5 py-2.5 rounded-lg font-bold text-sm shadow-sm transition-all flex items-center gap-2">
              View All Services <span class="text-slate-400">→</span>
            </a>
          </div>'''

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    target_soup = bs4.BeautifulSoup(f, 'html.parser')

target_slides = target_soup.find_all('div', class_='hero-slide')

for i, right_str in enumerate([s1_right_str, s2_right_str, s3_right_str]):
    slide = target_slides[i]
    # left col buttons
    left_col = slide.find('div', class_='hero-slide-text')
    if left_col:
        old_buttons = left_col.find('div', class_='hero-stagger-5')
        if old_buttons:
            old_buttons.replace_with(bs4.BeautifulSoup(buttons_html, 'html.parser'))
    
    # right col
    old_right = slide.find('div', class_='hero-slide-visual')
    if old_right:
        old_right.replace_with(bs4.BeautifulSoup(right_str, 'html.parser'))

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(target_soup))

print("Fixed again with string conversions!")
