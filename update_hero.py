import os

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'id="hero-slider-section"' in line and start_idx == -1:
        start_idx = i - 3
    if 'id="hero-slider-section"' in line:
        pass
    if 'TRUST BANNER BELOW HERO' in line:
        end_idx = i - 2
        break

if start_idx != -1 and end_idx != -1:
    new_hero = '''<!-- ==========================================
     HERO SECTION (Sharon Infotech Layout Style)
     ========================================== -->
<section class="relative bg-gradient-to-b from-navy-50/70 via-slate-50 to-white pt-10 pb-16 lg:pt-16 lg:pb-24 overflow-hidden" id="hero-slider-section">
  <div class="max-w-7xl mx-auto px-4 grid lg:grid-cols-12 gap-12 items-center relative z-10">
    <!-- Left Text Content -->
    <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-electric/10 border border-electric/20 text-electric text-xs sm:text-sm font-semibold tracking-wide shadow-2xs">
        <span class="text-amber-500">⚡</span>
        <span>Authorized Enterprise Hardware Partner</span>
      </div>
      
      <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-black text-navy-900 tracking-tight leading-tight">
        POWER &amp; SPEED <br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-electric via-blue-600 to-cyan">
          AT HALF THE COST
        </span>
      </h1>
      
      <p class="text-slate-600 text-base sm:text-lg max-w-2xl mx-auto lg:mx-0 leading-relaxed font-medium">
        Certified Refurbished Apple Mac Mini, Dell, HP &amp; Lenovo Workstations with 50-Point Hardware Audit, macOS / Windows 11, and 1-Year Comprehensive Warranty.
      </p>
      
      <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-2">
        <a href="our-products.html" class="primary-hero-cta bg-gradient-to-r from-electric to-cyan hover:from-blue-700 hover:to-cyan-dark text-white px-6 py-3.5 rounded-xl font-extrabold text-sm shadow-md shadow-electric/25 transition-all">
          Browse Our Lineup
        </a>
        <a href="https://wa.me/918600572488" class="bg-white hover:bg-slate-50 border border-slate-300 text-navy-900 px-6 py-3.5 rounded-xl font-bold text-sm shadow-sm transition-all flex items-center gap-2">
          Request Instant Quote
        </a>
      </div>
      
      <div class="pt-6 flex items-center justify-center lg:justify-start gap-4">
        <div class="flex -space-x-2">
          <div class="w-10 h-10 rounded-full bg-slate-200 border-2 border-white overflow-hidden shadow-sm flex items-center justify-center bg-emerald-100 text-emerald-600 text-xs font-bold">✓</div>
          <div class="w-10 h-10 rounded-full bg-slate-200 border-2 border-white overflow-hidden shadow-sm flex items-center justify-center bg-blue-100 text-blue-600 text-xs font-bold">✓</div>
          <div class="w-10 h-10 rounded-full bg-slate-200 border-2 border-white overflow-hidden shadow-sm flex items-center justify-center bg-amber-100 text-amber-600 text-xs font-bold">★</div>
        </div>
        <div class="text-xs sm:text-sm font-semibold text-slate-700 text-left">
          <span class="text-amber-400 text-lg">★★★★★</span> 4.9/5 Rating<br/>
          <span class="text-slate-500 font-medium">Trusted by 500+ Corporate Clients</span>
        </div>
      </div>
    </div>
    
    <!-- Right Visual Content -->
    <div class="lg:col-span-5 relative flex justify-center lg:justify-end">
      <div class="relative w-full max-w-md">
        <!-- Background Ambient Blur -->
        <div class="absolute inset-0 bg-gradient-to-tr from-electric/20 to-cyan/20 rounded-full blur-3xl -z-10 hero-blob-1"></div>
        <div class="absolute -bottom-10 right-10 bg-gradient-to-br from-cyan/20 to-purple-500/20 w-64 h-64 rounded-full blur-3xl -z-10 hero-blob-2"></div>
        
        <!-- Main Image -->
        <img src="images/macbook_3d_hero_cutout_transparent.png" alt="Certified Refurbished MacBooks &amp; Laptops" class="hero-product-image relative z-10 w-full h-auto" />
        
        <!-- Floating Badges -->
        <div class="spatial-chip spatial-chip-1 absolute -top-4 -left-4 z-20 px-4 py-2 text-xs font-extrabold text-navy-900 flex items-center gap-2 rounded-xl">
          <span class="text-amber-500 text-sm">⚡</span> Core i5 / i7
        </div>
        <div class="spatial-chip spatial-chip-2 absolute -bottom-4 right-0 sm:-right-4 z-20 px-4 py-2 text-xs font-extrabold text-navy-900 flex items-center gap-2 rounded-xl">
          <span class="text-blue-500 text-sm">🛡️</span> 1-Yr Warranty
        </div>
      </div>
    </div>
  </div>
</section>
'''
    new_content = ''.join(lines[:start_idx]) + new_hero + ''.join(lines[end_idx:])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Hero replaced successfully.')
else:
    print(f'Failed to find bounds. Start: {start_idx}, End: {end_idx}')
