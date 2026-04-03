#!/usr/bin/env python3
"""Regenerate website images via Gemini 2.5 Flash Image — natural skin texture"""

import os
import time
from google import genai
from google.genai import types

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyD4Fmt2syP7SUVOYvYtpXOjGyYjITcmMzM")
client = genai.Client(api_key=GOOGLE_API_KEY)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website-assets")

# Skin texture directive added to EVERY prompt
SKIN_DIRECTIVE = " The skin MUST have visible natural pores, real texture, and a healthy dewy glow — NOT plastic, NOT airbrushed, NOT smooth like wax. Think high-end Vogue editorial photography with natural melanin-rich skin. Slight film grain for editorial feel."

IMAGES = [
    {
        "filename": "hero-homepage.png",
        "prompt": "Generate an ultra photorealistic editorial beauty photograph. Beautiful Black woman, early 30s, deep rich brown skin with visible healthy dewy glow. Wearing a plush white spa robe, relaxed confident expression, soft natural smile. Natural hair in a protective silk wrap, gold stud earrings. Upscale spa treatment room with warm ambient lighting. Soft bokeh of warm candlelight and greenery behind her. Golden hour warmth, soft diffused key light from the left, warm fill from candles, subtle rim light on cheekbones. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Medium close-up, slightly off-center to the right, leaving negative space on left for text. Color palette: warm beige, burgundy accents, white linens, gold details." + SKIN_DIRECTIVE,
    },
    {
        "filename": "hero-facials.png",
        "prompt": "Generate an ultra photorealistic beauty photograph. Esthetician's gloved hands gently applying treatment serum to a Black woman's face. Client lying on spa treatment bed, eyes closed, peaceful serene expression. Client has deep brown melanin-rich skin with clear complexion. Esthetician wearing black medical-grade gloves. Professional spa treatment room with warm pendant lighting, burgundy accent wall, white linens. Soft overhead ring light, warm ambient side lighting. Shot on Sony A7IV, 50mm f/1.8 at f/2.8. Wide shot from slightly above showing both hands and full face." + SKIN_DIRECTIVE,
    },
    {
        "filename": "hero-microneedling.png",
        "prompt": "Generate an ultra photorealistic medical spa photograph. Professional microneedling pen device held by gloved hands near a Black woman's cheek. Client lying on treatment bed, calm expression. The device is sleek silver and white. Client's deep brown melanin-rich skin is smooth and prepped. Modern medical-spa treatment room with LED light, skincare products on stainless steel cart, white walls with warm wood accents. Bright even clinical lighting with warm undertone. Shot on Sony A7IV, 70mm f/2.8. Close-up from side angle." + SKIN_DIRECTIVE,
    },
    {
        "filename": "hero-waxing.png",
        "prompt": "Generate an ultra photorealistic interior photograph. Elegant spa treatment room prepared for a body treatment. Clean treatment bed with crisp white linens and a folded warm towel. A small vase with a single red rose on the side table. Intimate private room with warm beige walls, sheer curtains with soft natural light, LED candles, eucalyptus. Soft warm diffused natural window light. Shot on Sony A7IV, 35mm f/1.4 at f/2.8. Wide shot from doorway perspective. Warm dreamy atmosphere.",
    },
    {
        "filename": "hero-about.png",
        "prompt": "Generate an ultra photorealistic editorial portrait. Confident Black woman esthetician, early 30s, standing in her spa treatment room. Wearing a professional burgundy spa coat, arms crossed confidently. Warm genuine smile, direct eye contact with camera. Deep rich brown melanin-rich skin, natural makeup, gold hoop earrings, neat professional hair in a low bun. Treatment room behind her with equipment, treatment bed, skincare products, warm pendant lights. Soft natural window light from the left. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Three-quarter length portrait." + SKIN_DIRECTIVE,
    },
    {
        "filename": "before-after-hyperpigmentation.png",
        "prompt": "Generate an ultra photorealistic clinical skin comparison photograph. Close-up of a Black woman's cheek showing corrective skincare results. The left area of the cheek shows visible dark spots and hyperpigmentation patches on deep brown melanin-rich skin. The right area of the same cheek shows dramatically improved, even-toned, clear, radiant skin. Clinical beauty lighting, clean warm beige background. Shot on Canon R5, 100mm macro at f/5.6. Ultra sharp skin detail with natural pores visible on BOTH sides — real skin texture, not airbrushed. Honest documentation style.",
    },
    {
        "filename": "before-after-acne-scarring.png",
        "prompt": "Generate an ultra photorealistic clinical skin photograph. Close-up of a Black woman's cheek showing acne scar treatment results. Visible improvement from textured, scarred skin with post-inflammatory marks to significantly smoother, even-toned melanin-rich skin with healthy radiance. Even diffused clinical lighting, clean warm beige background. Shot on Canon R5, 100mm macro at f/5.6. Extremely detailed natural skin texture visible on both areas, realistic pores and micro-texture, documentation style.",
    },
    {
        "filename": "before-after-uneven-tone.png",
        "prompt": "Generate an ultra photorealistic clinical beauty photograph. Close-up portrait of a Black woman's face showing beautifully even, radiant, glowing melanin-rich skin with uniform tone and healthy luminosity. Makeup-free, neutral expression. Clean warm beige background. Even diffused beauty dish lighting. Shot on Canon R5, 85mm at f/4.0. Natural skin detail with visible pores, smooth even radiance, healthy glow. Real skin texture — NOT airbrushed or plastic.",
    },
    {
        "filename": "card-body-treatment.png",
        "prompt": "Generate an ultra photorealistic beauty photograph. Black woman's bare shoulders and upper back, deep rich brown melanin-rich skin with a luminous healthy glow. Skin looks hydrated, even-toned, radiant. White spa towel draped loosely below shoulders. Subtle gold shimmer catching light on collarbones. Soft warm beige wall out of focus. Soft warm side light emphasizing skin glow, subtle rim light on shoulders. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Close-up from behind." + SKIN_DIRECTIVE,
    },
    {
        "filename": "card-packages-gifts.png",
        "prompt": "Generate an ultra photorealistic luxury product photograph. Elegant gift-wrapped skincare set on a white marble surface. Small luxury skincare bottles and jars in amber glass with gold caps. A burgundy satin ribbon bow tying the set together. Dried flower arrangement beside it. Soft diffused natural window light from the left. White marble with warm veining, warm beige backdrop. Shot on Sony A7IV, 50mm f/1.8 at f/4.0. Overhead at 45-degree angle. Clean, bright, warm, luxury editorial feel.",
    },
    {
        "filename": "blog-skincare-routine.png",
        "prompt": "Generate an ultra photorealistic lifestyle flatlay photograph. Complete skincare routine products on warm marble surface. Gentle cleanser, vitamin C serum in amber dropper bottle, moisturizer in white jar, SPF in sleek tube. A small jade roller and soft towel. Morning light casting soft shadows. White marble with warm veining, warm beige linen underneath. Shot overhead. Bright warm lifestyle editorial.",
    },
    {
        "filename": "blog-first-facial.png",
        "prompt": "Generate an ultra photorealistic spa photograph. Young Black woman lying on spa treatment bed, eyes gently closed, completely relaxed peaceful expression. Face has a thin layer of treatment product with slightly dewy translucent appearance. Hair in a soft white headband, white spa towel at shoulders. Deep brown melanin-rich skin, no makeup. Soft warm lighting, blurred skincare bottles, warm wood accent wall. Shot on Sony A7IV, 50mm f/1.8 at f/2.8. Medium close-up from slightly above. Soft, warm, dreamy." + SKIN_DIRECTIVE,
    },
    {
        "filename": "blog-microneedling-safety.png",
        "prompt": "Generate an ultra photorealistic medical spa photograph. Close-up of a professional skincare treatment being performed on a Black woman's forehead. Gloved hands holding a small medical device with precision. Serum product glistening on the treatment area. Deep brown melanin-rich skin with real natural texture. Medical spa room with warm tones. Bright even clinical light with warm undertone. Shot on Canon R5, 100mm macro at f/4.0. Close-up at skin level. Professional documentation." + SKIN_DIRECTIVE,
    },
    {
        "filename": "og-social-share.png",
        "prompt": "Generate a professional social media card design for a beauty spa brand. Left half shows a close-up photograph of a Black woman's glowing cheek and jawline with radiant dewy melanin-rich skin in warm golden lighting — natural pores visible, not airbrushed. Right half is a warm beige panel. Clean graphic design layout for social media. Luxury spa brand aesthetic. Burgundy and warm beige color palette.",
    }
]

def generate_image(prompt_data):
    filename = prompt_data["filename"]
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Delete old version to regenerate
    if os.path.exists(filepath):
        os.remove(filepath)

    print(f"  ⏳ Generating {filename}...", flush=True)

    try:
        response = client.models.generate_content(
            model='gemini-3.1-flash-image-preview',
            contents=prompt_data["prompt"],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
            )
        )

        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data and part.inline_data.mime_type.startswith('image/'):
                with open(filepath, 'wb') as f:
                    f.write(part.inline_data.data)
                size_kb = os.path.getsize(filepath) // 1024
                print(f"  ✓ {filename} saved ({size_kb}KB)", flush=True)
                return True

        print(f"  ✗ {filename} — no image in response", flush=True)
        return False

    except Exception as e:
        print(f"  ✗ {filename} — {str(e)[:150]}", flush=True)
        return False

def main():
    print(f"\n{'='*60}")
    print(f"  Rosie's Beauty Spa — Gemini 2.5 Flash Image Generation")
    print(f"  Natural skin texture, no plastic look")
    print(f"  Regenerating {len(IMAGES)} images")
    print(f"{'='*60}\n", flush=True)

    success = 0
    failed = 0
    failed_list = []

    for i, img in enumerate(IMAGES, 1):
        print(f"\n[{i}/{len(IMAGES)}] {img['filename']}")
        if generate_image(img):
            success += 1
        else:
            failed += 1
            failed_list.append(img["filename"])
        if i < len(IMAGES):
            time.sleep(8)  # Slightly longer delay for Flash model

    print(f"\n{'='*60}")
    print(f"  Done! ✓ {success} succeeded, ✗ {failed} failed")
    if failed_list:
        print(f"  Failed: {', '.join(failed_list)}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
