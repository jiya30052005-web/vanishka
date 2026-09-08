import bs4

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

header = soup.find('header')

new_header_html = '''
<div>
  <!-- Top Bar (Sharon Infotech Style) -->
  <div class="bg-[#0b101e] text-white text-[11px] font-medium py-1.5 hidden lg:block border-b border-slate-800/80">
    <div class="max-w-[1400px] mx-auto px-4 flex items-center justify-between">
      <!-- Top Bar Left -->
      <div class="flex items-center gap-3 text-slate-300">
        <div class="flex items-center gap-1.5 text-emerald-400 bg-emerald-400/10 px-2 py-0.5 rounded-full border border-emerald-400/20">
          <span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-pulse"></span>
          <span>Open Today in Pune (9:30 AM - 8:30 PM)</span>
        </div>
        <span class="text-slate-600">|</span>
        <div class="flex items-center gap-1.5">
          <span class="text-amber-400">🎗️</span> Serving Pune City Since 2013 (12+ Years Trust)
        </div>
        <span class="text-slate-600">|</span>
        <a href="contact.html" class="flex items-center gap-1 hover:text-cyan-400 transition-colors">
          <span class="text-cyan-400">📍</span> Tech Hub Street Center on Maps 
          <svg class="w-2.5 h-2.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
        </a>
      </div>
      <!-- Top Bar Right -->
      <div class="flex items-center gap-3">
        <a href="tel:+918600572488" class="flex items-center gap-1.5 hover:text-white transition-colors">
          <span class="text-emerald-400">📞</span> Call: +91-8600572488
        </a>
        <span class="text-slate-600">|</span>
        <a href="https://wa.me/918600572488" class="flex items-center gap-1.5 hover:text-white transition-colors">
          <span class="text-emerald-400">💬</span> WhatsApp
        </a>
        <span class="text-slate-600">|</span>
        <div class="flex items-center gap-2.5 ml-1 text-slate-400">
          <a href="#" class="hover:text-white transition-colors"><svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.04c-5.5 0-10 4.49-10 10.02 0 5 3.66 9.15 8.44 9.9v-7H7.9v-2.9h2.54V9.85c0-2.51 1.49-3.89 3.78-3.89 1.09 0 2.23.2 2.23.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.45 2.9h-2.33v7a10 10 0 0 0 8.44-9.9c0-5.53-4.5-10.02-10-10.02Z"></path></svg></a>
          <a href="#" class="hover:text-white transition-colors"><svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.05c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23Z"></path></svg></a>
          <a href="#" class="hover:text-white transition-colors"><svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.22.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.05.41 2.22.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.22-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.05.36-2.22.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.22-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.05-.41-2.22-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.22.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.05-.36 2.22-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07c-1.28.06-2.15.27-2.91.56-.8.31-1.48.74-2.15 1.41-.67.67-1.1 1.35-1.41 2.15-.29.76-.5 1.63-.56 2.91C.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.28.27 2.15.56 2.91.31.8.74 1.48 1.41 2.15.67.67 1.35 1.1 2.15 1.41.76.29 1.63.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.28-.06 2.15-.27 2.91-.56.8-.31 1.48-.74 2.15-1.41.67-.67 1.1-1.35 1.41-2.15.29-.76.5-1.63.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.28-.27-2.15-.56-2.91-.31-.8-.74-1.48-1.41-2.15-.67-.67-1.35-1.1-2.15-1.41-.76-.29-1.63-.5-2.91-.56C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm3.98-10.7a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"></path></svg></a>
          <a href="#" class="hover:text-white transition-colors"><svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.95v5.66H9.34V9h3.42v1.56h.05c.48-.9 1.63-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.45a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zm1.78 13h-3.56V9h3.56v11.45zM22.22 0H1.77C.8 0 0 .77 0 1.72v20.56C0 23.23.8 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"></path></svg></a>
        </div>
      </div>
    </div>
  </div>

  <header class="sticky top-0 z-50 bg-white border-b border-slate-200/80 shadow-sm transition-all duration-300">
    <div class="max-w-[1400px] mx-auto px-4 py-3 sm:py-4">
      <div class="flex items-center justify-between gap-4 lg:gap-6">
        
        <!-- Mobile Menu Toggle Button -->
        <button aria-label="Toggle menu" class="lg:hidden text-slate-800 p-2 rounded-lg hover:bg-slate-100 transition" id="mobile-menu-btn">
          <svg class="w-6 h-6" fill="none" viewbox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16" stroke="currentColor" stroke-linecap="round" stroke-width="2"></path></svg>
        </button>

        <!-- Brand Logo -->
        <a class="flex items-center gap-3 shrink-0 group" href="index.html">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-slate-900 via-slate-800 to-slate-950 border border-slate-700/80 flex items-center justify-center p-2 shadow-md shadow-slate-900/30 group-hover:scale-105 transition-transform duration-200">
            <img alt="Vanishka Enterprises Logo" class="w-full h-full object-contain filter drop-shadow" src="images/ve_icon_transparent.png"/>
          </div>
          <div class="flex flex-col justify-center">
            <span class="font-display font-extrabold text-lg sm:text-xl text-electric tracking-tight leading-none transition-colors">VANISHKA ENTERPRISES</span>
            <div class="flex items-center justify-between text-[7.5px] sm:text-[8.5px] font-bold text-amber-600 uppercase tracking-wider w-full mt-0.5">
              <span>COMPUTERS</span><span class="text-amber-500/70">•</span>
              <span>LAPTOPS</span><span class="text-amber-500/70">•</span>
              <span>HARDWARE</span><span class="text-amber-500/70">•</span>
              <span>NETWORKING</span>
            </div>
          </div>
        </a>

        <!-- Center Desktop Navigation Links (Vanishka's original links, styled like Sharon Infotech) -->
        <nav class="hidden lg:flex flex-1 justify-center items-center gap-1 xl:gap-2 text-[14px] font-semibold text-slate-600">
          <a class="px-3.5 py-2 rounded-lg bg-blue-50 text-blue-600 font-extrabold transition" href="index.html">Home</a>
          <a class="px-3.5 py-2 rounded-lg hover:bg-slate-100 hover:text-navy-900 transition" href="about-us.html">About Us</a>
          <a class="px-3.5 py-2 rounded-lg hover:bg-slate-100 hover:text-navy-900 transition" href="our-products.html">Products</a>
          <a class="px-3.5 py-2 rounded-lg hover:bg-slate-100 hover:text-navy-900 transition" href="contact.html">Contact</a>
        </nav>

        <!-- Right Header Actions (WhatsApp & Call Now Buttons) -->
        <div class="hidden md:flex items-center gap-2 sm:gap-3 shrink-0">
          <a href="https://wa.me/918600572488" class="bg-[#0b965c] hover:bg-[#097b4b] text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"></path></svg>
            WhatsApp
          </a>
          <a href="tel:+918600572488" class="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-bold text-sm shadow-md transition-all flex items-center gap-2">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.36 1.9.68 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.9.32 1.85.55 2.81.68A2 2 0 0122 16.92z"></path></svg>
            Call Now
          </a>
        </div>
      </div>
    </div>
  </header>
</div>
'''

new_header = bs4.BeautifulSoup(new_header_html, 'html.parser')
header.replace_with(new_header)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Header replaced successfully!")
