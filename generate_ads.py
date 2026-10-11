import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_story_ad():
    target_w, target_h = 1080, 1920
    src_path = r'C:\Users\at781\Desktop\Voltara-Web-Studio\voltara-insta-ad.jpg'
    src = Image.open(src_path).convert('RGBA')
    
    scale = target_w / src.width
    scaled_w = target_w
    scaled_h = int(src.height * scale)
    src_scaled = src.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (target_w, target_h), (7, 8, 16, 255))
    canvas.paste(src_scaled, (0, 0), src_scaled)
    
    font_dir = r'C:\Windows\Fonts'
    f_brand = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 38)
    f_tagline = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 20)
    f_hero_sub = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 22)
    
    f_card_title = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 30)
    f_card_sub = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 22)
    f_contact_label = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 23)
    f_contact_val = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 28)
    f_contact_meta = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 20)
    f_cta = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 30)
    f_pill = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 20)
    f_small = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 18)

    draw = ImageDraw.Draw(canvas)
    
    # 1. TOP HEADER OVERLAY
    overlay_top = Image.new('RGBA', (target_w, 230), (6, 7, 15, 240))
    canvas.paste(overlay_top, (0, 0), overlay_top)
    
    draw.text((target_w // 2, 55), "VOLTARA WEB AGENCY", fill=(255, 255, 255, 255), font=f_brand, anchor="mm")
    draw.ellipse([target_w // 2 - 250, 48, target_w // 2 - 238, 60], fill=(99, 102, 241, 255))
    draw.ellipse([target_w // 2 + 238, 48, target_w // 2 + 250, 60], fill=(234, 179, 8, 255))
    
    draw.text((target_w // 2, 98), "PREMIER 3D WEB DESIGN & TURNKEY DEVELOPMENT COMPANY", fill=(165, 180, 252, 255), font=f_tagline, anchor="mm")
    draw.line([(60, 122), (target_w - 60, 122)], fill=(234, 179, 8, 140), width=2)
    
    draw.text((target_w // 2, 155), "UPGRADE YOUR BUSINESS TO A 3D LUXURY WEBSITE", fill=(255, 235, 160, 255), font=f_card_title, anchor="mm")
    draw.text((target_w // 2, 195), "⚡ 48-Hour Sprint • 🌐 Free .com Domain Included • 🚀 NVMe Cloud Server", fill=(203, 213, 225, 255), font=f_hero_sub, anchor="mm")

    # 2. BOTTOM CONTACT & BOOKING HUB
    card_x1, card_y1, card_x2, card_y2 = 40, 1340, target_w - 40, 1870
    card_bg = Image.new('RGBA', (card_x2 - card_x1, card_y2 - card_y1), (12, 15, 28, 250))
    canvas.paste(card_bg, (card_x1, card_y1), card_bg)
    
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=32, outline=(99, 102, 241, 255), width=3)
    draw.rounded_rectangle([card_x1 + 3, card_y1 + 3, card_x2 - 3, card_y2 - 3], radius=30, outline=(234, 179, 8, 120), width=1)
    
    # Offer Banner
    banner_h = 95
    draw.rounded_rectangle([card_x1 + 8, card_y1 + 8, card_x2 - 8, card_y1 + banner_h], radius=24, fill=(234, 179, 8, 30), outline=(234, 179, 8, 220), width=2)
    draw.text((target_w // 2, card_y1 + 38), "⚡ SPECIAL META AD DEAL: FLAT ₹2,000 OFF", fill=(254, 240, 138, 255), font=f_card_sub, anchor="mm")
    draw.text((target_w // 2, card_y1 + 72), "Use Coupon Code: INSTA2000  •  Turnkey Website At Just ₹5,999", fill=(255, 255, 255, 255), font=f_card_title, anchor="mm")
    
    # Pills row
    pills_y = card_y1 + 118
    pills = ["⚡ 48H Sprint", "🌐 Free .com Domain", "🚀 NVMe Server", "📱 3D Mobile"]
    pill_w = 220
    gap = 20
    start_x = card_x1 + ( (card_x2 - card_x1) - (len(pills)*pill_w + (len(pills)-1)*gap) ) // 2
    
    for i, p in enumerate(pills):
        px1 = start_x + i * (pill_w + gap)
        px2 = px1 + pill_w
        draw.rounded_rectangle([px1, pills_y, px2, pills_y + 38], radius=12, fill=(30, 41, 59, 220), outline=(99, 102, 241, 150), width=1)
        draw.text(((px1 + px2) // 2, pills_y + 19), p, fill=(226, 232, 240, 255), font=f_pill, anchor="mm")
    
    # Contact rows
    contact_start_y = card_y1 + 180
    row_h = 60
    
    # Row 1: WhatsApp / Phone
    draw.rounded_rectangle([card_x1 + 25, contact_start_y, card_x2 - 25, contact_start_y + row_h], radius=16, fill=(16, 185, 129, 30), outline=(16, 185, 129, 160), width=1)
    draw.text((card_x1 + 45, contact_start_y + 30), "📞 Call / WhatsApp:", fill=(52, 211, 153, 255), font=f_contact_label, anchor="lm")
    draw.text((card_x1 + 320, contact_start_y + 30), "+91 95558 38550", fill=(255, 255, 255, 255), font=f_contact_val, anchor="lm")
    draw.text((card_x2 - 45, contact_start_y + 30), "Pawan Rajput (Founder)", fill=(148, 163, 184, 255), font=f_contact_meta, anchor="rm")
    
    # Row 2: Website
    r2_y = contact_start_y + row_h + 12
    draw.rounded_rectangle([card_x1 + 25, r2_y, card_x2 - 25, r2_y + row_h], radius=16, fill=(99, 102, 241, 30), outline=(99, 102, 241, 160), width=1)
    draw.text((card_x1 + 45, r2_y + 30), "🌐 Official Website:", fill=(165, 180, 252, 255), font=f_contact_label, anchor="lm")
    draw.text((card_x1 + 320, r2_y + 30), "www.voltarawebagency.com", fill=(255, 255, 255, 255), font=f_contact_val, anchor="lm")
    draw.text((card_x2 - 45, r2_y + 30), "Live 3D Simulator", fill=(148, 163, 184, 255), font=f_contact_meta, anchor="rm")

    # Row 3: Email & Location
    r3_y = r2_y + row_h + 12
    draw.rounded_rectangle([card_x1 + 25, r3_y, card_x2 - 25, r3_y + row_h], radius=16, fill=(30, 41, 59, 200), outline=(71, 85, 105, 140), width=1)
    draw.text((card_x1 + 45, r3_y + 30), "✉️ Email Contact:", fill=(203, 213, 225, 255), font=f_contact_label, anchor="lm")
    draw.text((card_x1 + 320, r3_y + 30), "voltaramedia@gmail.com", fill=(255, 255, 255, 255), font=f_contact_val, anchor="lm")
    draw.text((card_x2 - 45, r3_y + 30), "Kanpur, UP • Pan-India", fill=(148, 163, 184, 255), font=f_contact_meta, anchor="rm")

    # Big CTA Button
    cta_y = r3_y + row_h + 20
    cta_h = 75
    draw.rounded_rectangle([card_x1 + 25, cta_y, card_x2 - 25, cta_y + cta_h], radius=20, fill=(99, 102, 241, 255), outline=(234, 179, 8, 255), width=2)
    draw.text((target_w // 2, cta_y + cta_h // 2), "⚡ TAP 'SEND MESSAGE' OR DM TO CLAIM ₹2,000 OFF ↗", fill=(255, 255, 255, 255), font=f_cta, anchor="mm")
    
    draw.text((target_w // 2, 1895), "100% Turnkey Delivery Guarantee • Direct Developer Handover • Zero Hidden Charges", fill=(100, 116, 139, 255), font=f_small, anchor="mm")

    output_path = r'C:\Users\at781\Desktop\Voltara-Web-Studio\voltara_ad_story_9x16.jpg'
    canvas.convert('RGB').save(output_path, 'JPEG', quality=95)
    print("Story Ad Saved:", output_path)


def create_feed_ad():
    target_w, target_h = 1080, 1080
    src_path = r'C:\Users\at781\Desktop\Voltara-Web-Studio\voltara-insta-ad.jpg'
    src = Image.open(src_path).convert('RGBA')
    
    # Crop the central phone region of source (width 768, height 1376)
    # Phone region is roughly y: 240 to 1050
    phone_crop = src.crop((0, 150, src.width, 1060))
    # Resize to fit right side or center of square canvas
    phone_w = 580
    phone_h = int(phone_crop.height * (phone_w / phone_crop.width))
    phone_scaled = phone_crop.resize((phone_w, phone_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (target_w, target_h), (7, 8, 16, 255))
    
    # Paste phone on the right side
    canvas.paste(phone_scaled, (target_w - phone_w + 30, (target_h - phone_h) // 2 + 20), phone_scaled)
    
    font_dir = r'C:\Windows\Fonts'
    f_brand = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 32)
    f_tagline = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 17)
    f_title = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 38)
    f_offer_code = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 26)
    f_offer_sub = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 20)
    f_val = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 22)
    f_meta = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 17)
    f_cta = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 24)
    
    draw = ImageDraw.Draw(canvas)
    
    # Left Content Container (x: 40 to 540)
    lx1 = 40
    
    # Brand Bar
    draw.text((lx1, 60), "VOLTARA WEB AGENCY", fill=(255, 255, 255, 255), font=f_brand, anchor="lm")
    draw.text((lx1, 95), "PREMIER 3D WEB DESIGN COMPANY", fill=(165, 180, 252, 255), font=f_tagline, anchor="lm")
    draw.line([(lx1, 115), (500, 115)], fill=(234, 179, 8, 140), width=2)
    
    # Big Headline
    draw.text((lx1, 165), "UPGRADE TO A", fill=(255, 255, 255, 255), font=f_title, anchor="lm")
    draw.text((lx1, 212), "3D LUXURY WEBSITE", fill=(255, 235, 160, 255), font=f_title, anchor="lm")
    draw.text((lx1, 255), "Turnkey 48-Hour Live Sprint", fill=(52, 211, 153, 255), font=f_tagline, anchor="lm")

    # Offer Box
    draw.rounded_rectangle([lx1, 290, 510, 415], radius=18, fill=(234, 179, 8, 25), outline=(234, 179, 8, 220), width=2)
    draw.text((lx1 + 20, 325), "🏷️ SPECIAL META AD OFFER", fill=(254, 240, 138, 255), font=f_offer_sub, anchor="lm")
    draw.text((lx1 + 20, 360), "USE CODE: INSTA2000", fill=(255, 255, 255, 255), font=f_offer_code, anchor="lm")
    draw.text((lx1 + 20, 392), "Flat ₹2,000 OFF • Turnkey Setup at ₹5,999", fill=(203, 213, 225, 255), font=f_meta, anchor="lm")

    # Features List
    features = [
        "✓ Guaranteed 48-Hour Delivery Sprint",
        "✓ Free .com Domain Included (1 Year)",
        "✓ NVMe Cloud Hosting + Lifetime SSL",
        "✓ 3D Interactive WebGL Physics",
        "✓ Direct WhatsApp Lead Capture Funnel"
    ]
    fy = 445
    for feat in features:
        draw.text((lx1 + 10, fy), feat, fill=(226, 232, 240, 255), font=f_val, anchor="lm")
        fy += 34

    # Bottom Contact Card
    draw.rounded_rectangle([40, target_h - 260, target_w - 40, target_h - 40], radius=24, fill=(12, 15, 28, 250), outline=(99, 102, 241, 220), width=2)
    
    cy = target_h - 225
    # Phone
    draw.text((65, cy), "📞 WhatsApp / Call:", fill=(52, 211, 153, 255), font=f_val, anchor="lm")
    draw.text((290, cy), "+91 95558 38550", fill=(255, 255, 255, 255), font=f_offer_code, anchor="lm")
    draw.text((540, cy), "(Pawan Rajput — Founder)", fill=(148, 163, 184, 255), font=f_meta, anchor="lm")
    
    # Web & Email
    cy2 = cy + 42
    draw.text((65, cy2), "🌐 Official Website:", fill=(165, 180, 252, 255), font=f_val, anchor="lm")
    draw.text((290, cy2), "www.voltarawebagency.com", fill=(255, 255, 255, 255), font=f_offer_code, anchor="lm")
    draw.text((710, cy2), "✉️ voltaramedia@gmail.com", fill=(203, 213, 225, 255), font=f_val, anchor="lm")

    # CTA Button
    draw.rounded_rectangle([65, target_h - 110, target_w - 65, target_h - 55], radius=14, fill=(99, 102, 241, 255), outline=(234, 179, 8, 255), width=2)
    draw.text((target_w // 2, target_h - 82), "⚡ TAP 'SEND WHATSAPP MESSAGE' TO CLAIM ₹2,000 OFF ↗", fill=(255, 255, 255, 255), font=f_cta, anchor="mm")

    output_path = r'C:\Users\at781\Desktop\Voltara-Web-Studio\voltara_ad_feed_1x1.jpg'
    canvas.convert('RGB').save(output_path, 'JPEG', quality=95)
    print("Feed Ad Saved:", output_path)

if __name__ == '__main__':
    create_story_ad()
    create_feed_ad()
