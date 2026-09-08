import re

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the right columns from the original HTML to reuse them perfectly.
slide1_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 2', html, re.DOTALL)
slide2_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*<!-- SLIDE 3', html, re.DOTALL)
slide3_right_match = re.search(r'(<div class="lg:col-span-5 hero-slide-visual.*?)</div>\s*</div>\s*</div>\s*</div>\s*<!-- Sleek', html, re.DOTALL)

s1_right = slide1_right_match.group(1) + '</div></div>'
s2_right = slide2_right_match.group(1) + '</div></div>'
s3_right = slide3_right_match.group(1) + '</div></div>'

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
            <span class="text-amber-500">⚡</span> Established in 2013 • Premium Enterprise IT Partner
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Power &amp; Speed <span class="text-electric">At Half The Cost</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            Certified Refurbished Apple Mac Mini, Dell, HP &amp; Lenovo Workstations. Complete IT solutions with 50-Point Hardware Audit, macOS / Windows 11, and assured performance.
          </p>
          <!-- 3 small feature boxes -->
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">🛡️</span> <span class="text-xs font-bold text-slate-700">1-Yr Warranty</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">✔️</span> <span class="text-xs font-bold text-slate-700">100% Genuine</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">🔍</span> <span class="text-xs font-bold text-slate-700">50-Point Audit</span>
            </div>
          </div>
          <!-- Buttons -->
          <div class="hero-stagger-5 mt-6 flex flex-wrap items-center gap-3">
            <a href="our-products.html" class="bg-electric hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              Browse Lineup
            </a>
            <a href="https://wa.me/918600572488" class="bg-[#0b965c] hover:bg-[#097b4b] text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"></path></svg> Instant WhatsApp Chat
            </a>
            <a href="contact.html" class="bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-5 py-2.5 rounded-lg font-bold text-sm shadow-sm transition-all flex items-center gap-2">
              View All Services <span class="text-slate-400">→</span>
            </a>
          </div>
        </div>
        {s1_right}
      </div>

      <!-- SLIDE 2 -->
      <div class="hero-slide absolute inset-0 grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 hero-slide-text z-10">
          <div class="hero-stagger-1 inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-50/80 border border-blue-200/60 text-blue-700 text-[11px] font-bold tracking-wide mb-4 shadow-sm">
            <span class="text-purple-500">🖨️</span> Authorized Canon Partner
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Seamless Prints <span class="text-electric">Limitless Possibilities</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            Canon High-Efficiency Ink-tank &amp; Heavy-Duty Laser Printers with Original Manufacturer Warranty and Ultra-Low Cost Per Page.
          </p>
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">💧</span> <span class="text-xs font-bold text-slate-700">Low Cost/Page</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">✔️</span> <span class="text-xs font-bold text-slate-700">Canon Warranty</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">📶</span> <span class="text-xs font-bold text-slate-700">Wireless Print</span>
            </div>
          </div>
          <div class="hero-stagger-5 mt-6 flex flex-wrap items-center gap-3">
            <a href="our-products.html" class="bg-electric hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              Explore Printers
            </a>
            <a href="https://wa.me/918600572488" class="bg-[#0b965c] hover:bg-[#097b4b] text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"></path></svg> Instant WhatsApp Chat
            </a>
            <a href="contact.html" class="bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-5 py-2.5 rounded-lg font-bold text-sm shadow-sm transition-all flex items-center gap-2">
              View All Services <span class="text-slate-400">→</span>
            </a>
          </div>
        </div>
        {s2_right}
      </div>

      <!-- SLIDE 3 -->
      <div class="hero-slide absolute inset-0 grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 hero-slide-text z-10">
          <div class="hero-stagger-1 inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-50/80 border border-blue-200/60 text-blue-700 text-[11px] font-bold tracking-wide mb-4 shadow-sm">
            <span class="text-rose-500">🎨</span> AI Smart Classrooms &amp; Boardrooms
          </div>
          <h1 class="hero-stagger-2 font-display font-black text-3xl sm:text-4xl lg:text-5xl text-navy-900 tracking-tight leading-[1.15]">
            Future of Classrooms <span class="text-electric">&amp; Boardrooms</span>
          </h1>
          <p class="hero-stagger-3 mt-4 text-slate-600 font-medium text-sm sm:text-base max-w-xl leading-relaxed">
            BenQ, LG, Cybernetyx &amp; Logic 4K Interactive Displays (65", 75", 86") with Trolleys, Dual OS, and On-site Installation Support.
          </p>
          <div class="hero-stagger-4 mt-5 flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-emerald-500 text-sm">🖥️</span> <span class="text-xs font-bold text-slate-700">4K Ultra HD</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-blue-500 text-sm">🖐️</span> <span class="text-xs font-bold text-slate-700">Multi-Touch</span>
            </div>
            <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-2 shadow-xs">
              <span class="text-amber-500 text-sm">🛠️</span> <span class="text-xs font-bold text-slate-700">On-site Install</span>
            </div>
          </div>
          <div class="hero-stagger-5 mt-6 flex flex-wrap items-center gap-3">
            <a href="our-products.html" class="bg-electric hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              Explore Boards
            </a>
            <a href="https://wa.me/918600572488" class="bg-[#0b965c] hover:bg-[#097b4b] text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"></path></svg> Book Free Demo
            </a>
            <a href="contact.html" class="bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-5 py-2.5 rounded-lg font-bold text-sm shadow-sm transition-all flex items-center gap-2">
              View All Services <span class="text-slate-400">→</span>
            </a>
          </div>
        </div>
        {s3_right}
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
</section>'''

start_idx = html.find('<!-- ==========================================\n     HERO SLIDER SECTION')
end_idx = html.find('<!-- ==========================================\n     TRUST BANNER BELOW HERO')

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_hero + '\n' + html[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced.")
else:
    print("Could not find section boundaries.")
