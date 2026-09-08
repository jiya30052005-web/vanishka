import os

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the header logo background
old_header_bg = 'bg-gradient-to-br from-slate-900 via-slate-800 to-slate-950 border border-slate-700/80 flex items-center justify-center p-2 shadow-md shadow-slate-900/30'
new_header_bg = 'bg-white border border-slate-200 flex items-center justify-center p-2 shadow-sm'
html = html.replace(old_header_bg, new_header_bg)

# Replace the footer logo background
old_footer_bg = 'bg-gradient-to-br from-slate-900 via-slate-800 to-slate-950 border border-slate-700/80 flex items-center justify-center p-1.5 shadow-sm'
new_footer_bg = 'bg-white border border-slate-200 flex items-center justify-center p-1.5 shadow-sm'
html = html.replace(old_footer_bg, new_footer_bg)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Successfully replaced logo backgrounds.")
