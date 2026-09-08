import re

orig_path = r'c:\Users\KISHORI CHARPE\Downloads\temp_extract\vanishka-main\computerbaba-redesign\index.html'
with open(orig_path, 'r', encoding='utf-8') as f:
    orig_html = f.read()

slide1_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 2', orig_html, re.DOTALL)
slide2_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 3', orig_html, re.DOTALL)
slide3_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*</div>\s*<!-- Sleek', orig_html, re.DOTALL)

s1_right = slide1_right_match.group(1) + '</div></div>'
s2_right = slide2_right_match.group(1) + '</div></div>'
s3_right = slide3_right_match.group(1) + '</div></div>'

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-repo\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the literal {s1_right} placeholders with the actual HTML
html = html.replace('{s1_right}', s1_right)
html = html.replace('{s2_right}', s2_right)
html = html.replace('{s3_right}', s3_right)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed right columns!")
