import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open('vanishka_main.html', 'r', encoding='utf-8') as f:
    main_html = f.read()

start_str = '</header>'
end_str = '<footer'

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    # Need to find the exact comment before <footer if we can, but simply putting main_html works
    # Wait, there's a comment <!-- ========================================== \n FOOTER ...
    # Let's just use regex to replace between </header> and the footer comment block.
    
    # Simple regex
    new_html = re.sub(r'</header>.*?(?=<!--\s*==========================================\s*FOOTER)', '</header>\n' + main_html + '\n  ', html, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced body successfully using regex!")
else:
    print("Could not find tags")
