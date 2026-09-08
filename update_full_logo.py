import bs4

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

# 1. Header logo
header = soup.find('header')
if header:
    brand_a = header.find('a', class_=lambda c: c and 'group' in c and 'shrink-0' in c)
    if brand_a:
        new_brand_html = '''
        <a class="flex items-center shrink-0 hover:scale-[1.02] transition-transform duration-200" href="index.html">
          <img alt="Vanishka Enterprises Logo" class="h-16 sm:h-20 w-auto object-contain" src="images/ve_full_logo_cropped.png"/>
        </a>
        '''
        brand_a.replace_with(bs4.BeautifulSoup(new_brand_html, 'html.parser'))

# 2. Footer logo
footer = soup.find('footer')
if footer:
    footer_brand_a = footer.find('a', class_=lambda c: c and 'mb-6' in c)
    if footer_brand_a:
        new_footer_brand_html = '''
        <a class="inline-block mb-6 hover:scale-[1.02] transition-transform duration-200" href="index.html">
          <img alt="Vanishka Enterprises Logo" class="h-16 sm:h-20 w-auto object-contain filter drop-shadow-[0_0_8px_rgba(255,255,255,0.1)]" src="images/ve_full_logo_cropped.png"/>
        </a>
        '''
        footer_brand_a.replace_with(bs4.BeautifulSoup(new_footer_brand_html, 'html.parser'))

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Logo updated successfully in header and footer!")
