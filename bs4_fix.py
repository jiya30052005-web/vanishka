import bs4

orig_path = r'c:\Users\KISHORI CHARPE\Downloads\temp_extract\vanishka-main\computerbaba-redesign\index.html'
with open(orig_path, 'r', encoding='utf-8') as f:
    orig_soup = bs4.BeautifulSoup(f, 'html.parser')

slides = orig_soup.find_all('div', class_='hero-slide')
if len(slides) >= 3:
    s1_right = slides[0].find('div', class_='lg:col-span-5')
    s2_right = slides[1].find('div', class_='lg:col-span-5')
    s3_right = slides[2].find('div', class_='lg:col-span-5')
else:
    print("Could not find slides in original html")
    exit(1)

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
buttons_soup = bs4.BeautifulSoup(buttons_html, 'html.parser')

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    target_soup = bs4.BeautifulSoup(f, 'html.parser')

target_slides = target_soup.find_all('div', class_='hero-slide')
for i, (orig_right, target_slide) in enumerate(zip([s1_right, s2_right, s3_right], target_slides)):
    # 1. Update the buttons in the left column
    left_col = target_slide.find('div', class_='lg:col-span-7')
    old_buttons = left_col.find('div', class_='hero-stagger-5')
    if old_buttons:
        old_buttons.replace_with(bs4.BeautifulSoup(buttons_html, 'html.parser'))
    
    # 2. Update the right column
    old_right = target_slide.find('div', class_='lg:col-span-5')
    if old_right:
        old_right.replace_with(orig_right)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(target_soup))

print("Successfully updated with BeautifulSoup!")
