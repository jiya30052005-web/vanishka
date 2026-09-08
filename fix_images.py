import re
from urllib.parse import unquote

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace next image URLs with actual URLs
def replace_next_img(match):
    src = match.group(0)
    # Extract url=...
    url_match = re.search(r'url=([^&"\'\s]+)', src)
    if url_match:
        actual_url = unquote(url_match.group(1))
        # We replace the whole src="..." with src="actual_url"
        return 'src="' + actual_url + '"'
    return src

html = re.sub(r'src="/_next/image[^"]+"', replace_next_img, html)

# Remove srcset and sizes because they contain Next.js optimized links
html = re.sub(r'srcset="[^"]+"', '', html)
html = re.sub(r'sizes="[^"]+"', '', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Images fixed!")
