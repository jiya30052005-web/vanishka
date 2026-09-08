import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

slide1_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 2', html, re.DOTALL)
slide2_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 3', html, re.DOTALL)
slide3_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*</div>\s*<!-- Sleek', html, re.DOTALL)

s1_right = slide1_right_match.group(1) + '</div></div>'
s2_right = slide2_right_match.group(1) + '</div></div>'
s3_right = slide3_right_match.group(1) + '</div></div>'

# The universal buttons HTML
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

new_hero = f'''<!-- ==========================================
     HERO SLIDER SECTION (Split 2-Column + Tech Mesh & Animated Blobs)
     ========================================== -->
<section class="relative tech-grid-pattern py-5 sm:py-7 overflow-hidden" id="hero-slider-section">

  <!-- Subtle Animated Ambient Gradient Blobs -->
  <div class="absolute -top-20 -left-20 w-96 h-96 rounded-full bg-gradient-to-tr from-electric/25 via-cyan-400/20 to-purple-500/20 blur-3xl hero-blob-1 pointer-events-none -z-10"></div>
  <div class="absolute -bottom-20 -right-20 w-[30rem] h-[30rem] rounded-full bg-gradient-to-br from-cyan-400/20 via-electric/20 to-indigo-600/20 blur-3xl hero-blob-2 pointer-events-none -z-10"></div>

  <div class="max-w-7xl mx-auto px-4 relative">

    <!-- Slides Container -->
    <div class="relative min-h-[420px] sm:min-h-[470px] flex items-center">

      <!-- SLIDE 1 -->
      <div class="hero-slide active-slide absolute inset-0 grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 hero-slide-text z-10">
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
          {{buttons_html}}
        </div>
        {{s1_right}}
      </div>

      <!-- SLIDE 2 -->
      <div class="hero-slide absolute inset-0 grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 hero-slide-text z-10">
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
          {{buttons_html}}
        </div>
        {{s2_right}}
      </div>

      <!-- SLIDE 3 -->
      <div class="hero-slide absolute inset-0 grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 hero-slide-text z-10">
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
          {{buttons_html}}
        </div>
        {{s3_right}}
      </div>

    </div>

    <!-- Sleek Slide Navigation Indicators & Controls -->
    <div class="flex items-center justify-between mt-4 pt-2 border-t border-slate-200/60">
      <div class="flex items-center gap-2" id="hero-dots-container">
        <button class="hero-dot w-8 h-2.5 rounded-full bg-electric transition-all duration-300 cursor-pointer shadow-xs" aria-label="Slide 1" aria-current="true"></button>
        <button class="hero-dot w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-electric/60 transition-all duration-300 cursor-pointer" aria-label="Slide 2"></button>
        <button class="hero-dot w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-electric/60 transition-all duration-300 cursor-pointer" aria-label="Slide 3"></button>
      </div>
      <div class="flex items-center gap-2">
        <button id="hero-prev-btn" aria-label="Previous slide" class="w-10 h-10 rounded-full bg-white border border-slate-200 shadow-md flex items-center justify-center text-slate-700 hover:bg-electric hover:text-white hover:border-electric transition-all">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none"><path d="M15 19l-7-7 7-7" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <button id="hero-next-btn" aria-label="Next slide" class="w-10 h-10 rounded-full bg-white border border-slate-200 shadow-md flex items-center justify-center text-slate-700 hover:bg-electric hover:text-white hover:border-electric transition-all">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none"><path d="M9 5l7 7-7 7" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>

  </div>
</section>'''.replace('{{buttons_html}}', buttons_html).replace('{{s1_right}}', s1_right).replace('{{s2_right}}', s2_right).replace('{{s3_right}}', s3_right)

start_idx = html.find('<!-- ==========================================\n     HERO SLIDER SECTION')
end_idx = html.find('<!-- ==========================================\n     TRUST BANNER BELOW HERO')

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_hero + '\n' + html[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced buttons.")
else:
    print("Could not find section boundaries.")
