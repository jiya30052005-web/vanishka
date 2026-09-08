import re
with open('sharon_main2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see the sections
sections = re.findall(r'<section.*?>.*?</section>', html, flags=re.DOTALL)
print(f'Total sections: {len(sections)}')
for i, sec in enumerate(sections):
    print(f'Section {i} length: {len(sec)}')
    if 'iframe' in sec:
        print(f'  -> Has iframe (Map)')
