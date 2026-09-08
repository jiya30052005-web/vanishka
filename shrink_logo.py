import os

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace sizes
html = html.replace('h-16 sm:h-20 w-auto', 'h-12 sm:h-14 w-auto')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo size reduced.")
