import bs4

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

slides = soup.find_all('div', class_='hero-slide')

services_text_1 = '''<div class="lg:col-span-7 hero-slide-text z-10">
          <div class="hero-stagger-1 inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-50/80 border border-blue-200/60 text-blue-700 text-[11px] font-bold tracking-wide mb-4 shadow-sm">
            <span class="text-amber-500">⚡</span> Established in 2013 • Premium IT Repair Partner
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Expert Laptop &amp; PC Repair <span class="text-electric">At Your Doorstep</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            Fast and reliable repair services for Apple, Dell, HP &amp; Lenovo. We provide chip-level motherboard repairs, OS tuning, and data recovery with prompt on-site support.
          </p>
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">🛡️</span> <span class="text-xs font-bold text-slate-700">90-Day Warranty</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">✔️</span> <span class="text-xs font-bold text-slate-700">OEM Spares</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">🔍</span> <span class="text-xs font-bold text-slate-700">No Fix - No Fee</span>
            </div>
          </div>
          REPLACE_BUTTONS
        </div>'''

services_text_2 = '''<div class="lg:col-span-7 hero-slide-text z-10">
          <div class="hero-stagger-1 inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-50/80 border border-blue-200/60 text-blue-700 text-[11px] font-bold tracking-wide mb-4 shadow-sm">
            <span class="text-purple-500">🖨️</span> Professional Printer Services
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Comprehensive Printer <span class="text-electric">Repair &amp; Maintenance</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            Expert servicing for Canon, HP, and Epson printers. We handle cartridge refilling, paper jam fixes, head cleaning, and network printer configuration.
          </p>
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">💧</span> <span class="text-xs font-bold text-slate-700">Quick Refills</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">✔️</span> <span class="text-xs font-bold text-slate-700">OEM Parts</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">📶</span> <span class="text-xs font-bold text-slate-700">Network Setup</span>
            </div>
          </div>
          REPLACE_BUTTONS
        </div>'''

services_text_3 = '''<div class="lg:col-span-7 hero-slide-text z-10">
          <div class="hero-stagger-1 inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-50/80 border border-blue-200/60 text-blue-700 text-[11px] font-bold tracking-wide mb-4 shadow-sm">
            <span class="text-rose-500">🎨</span> Smart Classroom &amp; AV Solutions
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Interactive Board <span class="text-electric">Installation &amp; Support</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            End-to-end setup and maintenance for interactive flat panels, projectors, and smart classroom equipment. Ideal for schools and corporate boardrooms.
          </p>
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">🛠️</span> <span class="text-xs font-bold text-slate-700">On-site Install</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">🔌</span> <span class="text-xs font-bold text-slate-700">Cabling &amp; Setup</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">👨‍🏫</span> <span class="text-xs font-bold text-slate-700">Training Provided</span>
            </div>
          </div>
          REPLACE_BUTTONS
        </div>'''

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

services_text_1 = services_text_1.replace('REPLACE_BUTTONS', buttons_html)
services_text_2 = services_text_2.replace('REPLACE_BUTTONS', buttons_html)
services_text_3 = services_text_3.replace('REPLACE_BUTTONS', buttons_html)

for i, text in enumerate([services_text_1, services_text_2, services_text_3]):
    if i < len(slides):
        left_col = slides[i].find('div', class_='hero-slide-text')
        if left_col:
            left_col.replace_with(bs4.BeautifulSoup(text, 'html.parser'))

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully replaced left columns ONLY!")
