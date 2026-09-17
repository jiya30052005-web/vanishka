import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

def create_hero_banner():
    # Target dimensions: 3072x1350
    W, H = 3072, 1350
    # 2x supersampling for razor-sharp vector antialiasing
    SCALE = 2
    SW, SH = W * SCALE, H * SCALE

    print(f"1. Loading and preparing base clean image at {SW}x{SH}...")
    base_src = 'images/hero_hd_clean_bg.png'
    raw_bg = Image.open(base_src).convert('RGBA')

    # Upscale base image to supersampled size with high-quality Lanczos
    canvas = raw_bg.resize((SW, SH), Image.Resampling.LANCZOS)

    # Enhance hardware clarity, sharpness, reflections and blue LEDs
    unsharp = canvas.filter(ImageFilter.UnsharpMask(radius=2.6 * SCALE, percent=155, threshold=2))
    sharp_enhancer = ImageEnhance.Sharpness(unsharp)
    canvas = sharp_enhancer.enhance(1.22)
    contrast_enhancer = ImageEnhance.Contrast(canvas)
    canvas = contrast_enhancer.enhance(1.05)

    draw = ImageDraw.Draw(canvas)

    # Clean the bottom trust strip area with pure white background
    bottom_y = int(1085 * SCALE)
    draw.rectangle([0, bottom_y, SW, SH], fill=(255, 255, 255, 255))
    # Soft horizontal divider above bottom strip
    draw.line([int(80 * SCALE), bottom_y, int(2990 * SCALE), bottom_y], fill=(232, 238, 248, 255), width=int(1.5 * SCALE))

    # Font definitions (Windows Segoe UI & Segoe Script)
    font_badge = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(20 * SCALE))
    font_h1 = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(70 * SCALE))
    font_sub = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', int(23 * SCALE))
    font_btn = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(22 * SCALE))
    font_btn_small = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(17 * SCALE))

    font_card_title = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(22.5 * SCALE))
    font_card_sub = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', int(16 * SCALE))
    font_card_arrow = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(26 * SCALE))

    font_trust_title = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', int(21 * SCALE))
    font_trust_sub = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', int(18 * SCALE))
    font_script = ImageFont.truetype(r'C:\Windows\Fonts\segoesc.ttf', int(32 * SCALE))

    # Colors
    NAVY = (11, 25, 48, 255)
    BLUE_ACCENT = (18, 105, 255, 255)
    BLUE_VIVID = (0, 102, 255, 255)
    GRAY_TEXT = (80, 96, 120, 255)
    WHITE = (255, 255, 255, 255)

    print("2. Rendering Left Hero Typography...")
    badge_x = int(120 * SCALE)
    badge_y = int(220 * SCALE)
    
    # Eyebrow Badge: YOUR TRUSTED TECH PARTNER —
    draw.text((badge_x, badge_y), "YOUR TRUSTED TECH PARTNER", fill=BLUE_ACCENT, font=font_badge)
    line_x1 = badge_x + int(370 * SCALE)
    line_x2 = line_x1 + int(75 * SCALE)
    line_y = badge_y + int(14 * SCALE)
    draw.line([line_x1, line_y, line_x2, line_y], fill=BLUE_ACCENT, width=int(3 * SCALE))

    # Headline:
    # Computer, Laptop
    # Hardware & Networking
    # Services
    h1_y = badge_y + int(50 * SCALE)
    line_spacing = int(88 * SCALE)
    draw.text((badge_x, h1_y), "Computer, Laptop", fill=NAVY, font=font_h1)
    draw.text((badge_x, h1_y + line_spacing), "Hardware & Networking", fill=BLUE_ACCENT, font=font_h1)
    draw.text((badge_x, h1_y + line_spacing * 2), "Services", fill=NAVY, font=font_h1)

    # Subtitle
    sub_y = h1_y + line_spacing * 3 + int(15 * SCALE)
    draw.text((badge_x, sub_y), "High-performance devices, reliable networking solutions,", fill=GRAY_TEXT, font=font_sub)
    draw.text((badge_x, sub_y + int(36 * SCALE)), "and expert support — all under one roof.", fill=GRAY_TEXT, font=font_sub)

    # Action Buttons
    btn1_x1 = badge_x
    btn1_y1 = int(772 * SCALE)
    btn1_w = int(436 * SCALE)
    btn1_h = int(100 * SCALE)
    btn1_radius = btn1_h // 2
    
    # Blue pill background with vivid gradient feel
    draw.rounded_rectangle([btn1_x1, btn1_y1, btn1_x1 + btn1_w, btn1_y1 + btn1_h], radius=btn1_radius, fill=BLUE_VIVID)
    btn1_text = "Explore Our Services  →"
    b1_bbox = draw.textbbox((0, 0), btn1_text, font=font_btn)
    b1_tw = b1_bbox[2] - b1_bbox[0]
    b1_th = b1_bbox[3] - b1_bbox[1]
    draw.text((btn1_x1 + (btn1_w - b1_tw) // 2, btn1_y1 + (btn1_h - b1_th) // 2 - int(4 * SCALE)), btn1_text, fill=WHITE, font=font_btn)

    # Button 2: Watch Our Introduction
    btn2_x1 = int(577 * SCALE)
    btn2_y1 = btn1_y1
    btn2_w = int(320 * SCALE)
    btn2_h = btn1_h
    btn2_radius = btn2_h // 2
    draw.rounded_rectangle([btn2_x1, btn2_y1, btn2_x1 + btn2_w, btn2_y1 + btn2_h], radius=btn2_radius, fill=WHITE, outline=(190, 218, 255, 255), width=int(2.5 * SCALE))
    
    # Play Icon Circle
    play_circle_r = int(28 * SCALE)
    play_circle_cx = btn2_x1 + int(48 * SCALE)
    play_circle_cy = btn2_y1 + btn2_h // 2
    draw.ellipse([play_circle_cx - play_circle_r, play_circle_cy - play_circle_r, play_circle_cx + play_circle_r, play_circle_cy + play_circle_r], fill=WHITE, outline=BLUE_ACCENT, width=int(2.8 * SCALE))
    tri_pts = [
        (play_circle_cx - int(5 * SCALE), play_circle_cy - int(10 * SCALE)),
        (play_circle_cx + int(11 * SCALE), play_circle_cy),
        (play_circle_cx - int(5 * SCALE), play_circle_cy + int(10 * SCALE))
    ]
    draw.polygon(tri_pts, fill=BLUE_ACCENT)

    draw.text((btn2_x1 + int(88 * SCALE), btn2_y1 + int(22 * SCALE)), "Watch Our", fill=BLUE_ACCENT, font=font_btn_small)
    draw.text((btn2_x1 + int(88 * SCALE), btn2_y1 + int(48 * SCALE)), "Introduction", fill=BLUE_ACCENT, font=font_btn_small)

    print("3. Rendering Right Glassmorphism Services Card...")
    card_x1 = int(2350 * SCALE)
    card_y1 = int(160 * SCALE)
    card_x2 = int(2995 * SCALE)
    card_y2 = int(1040 * SCALE)
    card_radius = int(40 * SCALE)

    # Soft drop shadow
    shadow_offset = int(10 * SCALE)
    draw.rounded_rectangle([card_x1 + shadow_offset, card_y1 + shadow_offset, card_x2 + shadow_offset, card_y2 + shadow_offset], radius=card_radius, fill=(215, 228, 245, 120))
    # Crisp white card body
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=card_radius, fill=(255, 255, 255, 248), outline=(242, 247, 255, 255), width=int(2.5 * SCALE))

    services_data = [
        ("Computer & Laptop", "Repair Service", "All brands | Hardware & Software", "laptop"),
        ("Hardware Upgrades", "& Assembly", "Better Performance | Longer Life", "gear"),
        ("Windows Installation", "& Activation", "Genuine | Safe | Hassle-Free", "windows"),
        ("Networking Solutions", "", "LAN | Wi-Fi | Router | Switches", "network"),
        ("System Maintenance", "& Troubleshooting", "Fast | Reliable | Professional", "tools"),
    ]

    card_h = card_y2 - card_y1
    row_gap = card_h / 5

    def draw_service_icon(itype, cx, cy, radius):
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(235, 244, 255, 255))
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=(200, 225, 255, 255), width=int(2 * SCALE))
        
        if itype == "laptop":
            lw, lh = int(17 * SCALE), int(12 * SCALE)
            draw.rounded_rectangle([cx - lw, cy - lh - int(2 * SCALE), cx + lw, cy + lh - int(4 * SCALE)], radius=int(3 * SCALE), outline=BLUE_ACCENT, width=int(2.5 * SCALE))
            draw.line([cx - lw - int(6 * SCALE), cy + lh - int(2 * SCALE), cx + lw + int(6 * SCALE), cy + lh - int(2 * SCALE)], fill=BLUE_ACCENT, width=int(3 * SCALE))
        elif itype == "gear":
            draw.ellipse([cx - int(9 * SCALE), cy - int(9 * SCALE), cx + int(9 * SCALE), cy + int(9 * SCALE)], outline=BLUE_ACCENT, width=int(3 * SCALE))
            for deg in [0, 45, 90, 135]:
                rad = math.radians(deg)
                dx = int(14 * SCALE * math.cos(rad))
                dy = int(14 * SCALE * math.sin(rad))
                draw.line([cx - dx, cy - dy, cx + dx, cy + dy], fill=BLUE_ACCENT, width=int(3.5 * SCALE))
        elif itype == "windows":
            qw = int(9 * SCALE)
            gap = int(3 * SCALE)
            draw.rectangle([cx - qw - gap, cy - qw - gap, cx - gap, cy - gap], fill=BLUE_ACCENT)
            draw.rectangle([cx + gap, cy - qw - gap, cx + qw + gap, cy - gap], fill=BLUE_ACCENT)
            draw.rectangle([cx - qw - gap, cy + gap, cx - gap, cy + qw + gap], fill=BLUE_ACCENT)
            draw.rectangle([cx + gap, cy + gap, cx + qw + gap, cy + qw + gap], fill=BLUE_ACCENT)
        elif itype == "network":
            draw.ellipse([cx - int(12 * SCALE), cy - int(8 * SCALE), cx - int(4 * SCALE), cy], fill=BLUE_ACCENT)
            draw.ellipse([cx + int(4 * SCALE), cy - int(8 * SCALE), cx + int(12 * SCALE), cy], fill=BLUE_ACCENT)
            draw.ellipse([cx - int(4 * SCALE), cy + int(4 * SCALE), cx + int(4 * SCALE), cy + int(12 * SCALE)], fill=BLUE_ACCENT)
            draw.line([cx - int(8 * SCALE), cy - int(4 * SCALE), cx, cy + int(8 * SCALE)], fill=BLUE_ACCENT, width=int(2.5 * SCALE))
            draw.line([cx + int(8 * SCALE), cy - int(4 * SCALE), cx, cy + int(8 * SCALE)], fill=BLUE_ACCENT, width=int(2.5 * SCALE))
        elif itype == "tools":
            # Crossed wrench and screwdriver
            draw.line([cx - int(11 * SCALE), cy - int(11 * SCALE), cx + int(11 * SCALE), cy + int(11 * SCALE)], fill=BLUE_ACCENT, width=int(3.5 * SCALE))
            draw.line([cx + int(11 * SCALE), cy - int(11 * SCALE), cx - int(11 * SCALE), cy + int(11 * SCALE)], fill=BLUE_ACCENT, width=int(3.5 * SCALE))
            draw.ellipse([cx - int(13 * SCALE), cy - int(13 * SCALE), cx - int(7 * SCALE), cy - int(7 * SCALE)], outline=BLUE_ACCENT, width=int(2.5 * SCALE))
            draw.ellipse([cx + int(7 * SCALE), cy - int(13 * SCALE), cx + int(13 * SCALE), cy - int(7 * SCALE)], outline=BLUE_ACCENT, width=int(2.5 * SCALE))

    icon_radius = int(32 * SCALE)
    for i, (t1, t2, sub, icon_type) in enumerate(services_data):
        row_cy = int(card_y1 + row_gap * (i + 0.5))
        icon_cx = card_x1 + int(52 * SCALE)
        
        draw_service_icon(icon_type, icon_cx, row_cy, icon_radius)

        text_x = icon_cx + int(46 * SCALE)
        full_title = f"{t1} {t2}".strip()
        draw.text((text_x, row_cy - int(22 * SCALE)), full_title, fill=NAVY, font=font_card_title)
        draw.text((text_x, row_cy + int(6 * SCALE)), sub, fill=GRAY_TEXT, font=font_card_sub)

        arrow_x = card_x2 - int(50 * SCALE)
        draw.text((arrow_x, row_cy - int(19 * SCALE)), "→", fill=BLUE_ACCENT, font=font_card_arrow)

        if i < 4:
            sep_y = int(card_y1 + row_gap * (i + 1))
            draw.line([card_x1 + int(24 * SCALE), sep_y, card_x2 - int(24 * SCALE), sep_y], fill=(238, 244, 252, 255), width=int(1.5 * SCALE))

    print("4. Rendering Bottom Trust Bar...")
    trust_items = [
        ("Genuine", "Products", "shield"),
        ("Fast & Reliable", "Service", "clock"),
        ("Experienced", "Technicians", "people"),
        ("Affordable", "Pricing", "tag"),
        ("Local Support", "& On-Site Service", "pin"),
    ]

    trust_y = int(1120 * SCALE)
    trust_start_x = int(120 * SCALE)
    trust_spacing = int(480 * SCALE)

    def draw_trust_icon(itype, cx, cy):
        ir = int(28 * SCALE)
        draw.ellipse([cx - ir, cy - ir, cx + ir, cy + ir], fill=(238, 246, 255, 255))
        draw.ellipse([cx - ir, cy - ir, cx + ir, cy + ir], outline=(210, 230, 255, 255), width=int(1.8 * SCALE))
        if itype == "shield":
            pts = [(cx, cy - int(12 * SCALE)), (cx + int(11 * SCALE), cy - int(7 * SCALE)), (cx + int(8 * SCALE), cy + int(9 * SCALE)), (cx, cy + int(14 * SCALE)), (cx - int(8 * SCALE), cy + int(9 * SCALE)), (cx - int(11 * SCALE), cy - int(7 * SCALE))]
            draw.polygon(pts, outline=BLUE_ACCENT, fill=None, width=int(2.5 * SCALE))
            draw.line([cx - int(4 * SCALE), cy + int(1 * SCALE), cx - int(1 * SCALE), cy + int(5 * SCALE), cx + int(6 * SCALE), cy - int(3 * SCALE)], fill=BLUE_ACCENT, width=int(2.5 * SCALE))
        elif itype == "clock":
            draw.ellipse([cx - int(11 * SCALE), cy - int(11 * SCALE), cx + int(11 * SCALE), cy + int(11 * SCALE)], outline=BLUE_ACCENT, width=int(2.5 * SCALE))
            draw.line([cx, cy, cx, cy - int(7 * SCALE)], fill=BLUE_ACCENT, width=int(2.5 * SCALE))
            draw.line([cx, cy, cx + int(6 * SCALE), cy], fill=BLUE_ACCENT, width=int(2.5 * SCALE))
        elif itype == "people":
            draw.ellipse([cx - int(6 * SCALE), cy - int(10 * SCALE), cx + int(6 * SCALE), cy - int(1 * SCALE)], fill=BLUE_ACCENT)
            draw.arc([cx - int(11 * SCALE), cy - int(3 * SCALE), cx + int(11 * SCALE), cy + int(11 * SCALE)], start=180, end=0, fill=BLUE_ACCENT, width=int(3 * SCALE))
        elif itype == "tag":
            draw.polygon([(cx - int(9 * SCALE), cy - int(9 * SCALE)), (cx + int(3 * SCALE), cy - int(9 * SCALE)), (cx + int(9 * SCALE), cy - int(3 * SCALE)), (cx - int(3 * SCALE), cy + int(9 * SCALE)), (cx - int(9 * SCALE), cy + int(3 * SCALE))], fill=BLUE_ACCENT)
            draw.ellipse([cx - int(5 * SCALE), cy - int(5 * SCALE), cx - int(2 * SCALE), cy - int(2 * SCALE)], fill=WHITE)
        elif itype == "pin":
            draw.ellipse([cx - int(8 * SCALE), cy - int(11 * SCALE), cx + int(8 * SCALE), cy + int(4 * SCALE)], fill=BLUE_ACCENT)
            draw.ellipse([cx - int(3 * SCALE), cy - int(6 * SCALE), cx + int(3 * SCALE), cy], fill=WHITE)
            draw.polygon([(cx - int(5 * SCALE), cy + int(2 * SCALE)), (cx + int(5 * SCALE), cy + int(2 * SCALE)), (cx, cy + int(11 * SCALE))], fill=BLUE_ACCENT)

    for idx, (t1, t2, itype) in enumerate(trust_items):
        item_x = trust_start_x + idx * trust_spacing
        icon_cx = item_x + int(32 * SCALE)
        icon_cy = trust_y + int(42 * SCALE)
        draw_trust_icon(itype, icon_cx, icon_cy)

        text_x = icon_cx + int(42 * SCALE)
        draw.text((text_x, trust_y + int(18 * SCALE)), t1, fill=NAVY, font=font_trust_title)
        draw.text((text_x, trust_y + int(46 * SCALE)), t2, fill=GRAY_TEXT, font=font_trust_sub)

        if idx < 4:
            sep_x = item_x + trust_spacing - int(30 * SCALE)
            draw.line([sep_x, trust_y + int(15 * SCALE), sep_x, trust_y + int(80 * SCALE)], fill=(225, 235, 248, 255), width=int(1.5 * SCALE))

    # Script signature on right: "Your Tech Needs, Our Priority"
    script_x = int(2530 * SCALE)
    script_y = trust_y + int(5 * SCALE)
    draw.text((script_x, script_y), "Your Tech Needs,", fill=BLUE_ACCENT, font=font_script)
    draw.text((script_x + int(45 * SCALE), script_y + int(46 * SCALE)), "Our Priority", fill=BLUE_ACCENT, font=font_script)

    # Underline swoop
    swoop_pts = [
        (script_x + int(40 * SCALE), script_y + int(105 * SCALE)),
        (script_x + int(170 * SCALE), script_y + int(112 * SCALE)),
        (script_x + int(310 * SCALE), script_y + int(98 * SCALE)),
    ]
    draw.line(swoop_pts, fill=BLUE_ACCENT, width=int(3 * SCALE))

    print("5. Downsampling from 2x canvas to target 3072x1350 with Lanczos...")
    final_banner = canvas.resize((W, H), Image.Resampling.LANCZOS)

    out1 = 'images/hero_crystal_hd.png'
    out2 = 'computerbaba-redesign/images/hero_crystal_hd.png'

    final_banner.save(out1, 'PNG', optimize=True)
    final_banner.save(out2, 'PNG', optimize=True)
    print(f"Done! Saved ultra-crisp banner to {out1} ({os.path.getsize(out1)/1024:.1f} KB) and {out2}!")

if __name__ == '__main__':
    create_hero_banner()
