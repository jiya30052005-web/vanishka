import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open('vanishka_main.html', 'r', encoding='utf-8') as f:
    main_html = f.read()

# Replace everything from </header> to <!-- ============ FOOTER ============ -->
# We need to find </header> and <!-- ============ FOOTER ============ -->
start_str = '</header>'
end_str = '<!-- ============ FOOTER ============ -->'

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx + len(start_str)] + '\n' + main_html + '\n  ' + html[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced body with vanishka_main.html successfully!")
else:
    print("Could not find start or end tags")
