#!/usr/bin/env python3
"""Generate website images via Google Imagen 4.0"""

import os
import time
from google import genai
from google.genai import types

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyD4Fmt2syP7SUVOYvYtpXOjGyYjITcmMzM")
client = genai.Client(api_key=GOOGLE_API_KEY)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website-assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMAGES = [
    {
        "filename": "hero-homepage.png",
        "prompt": "Ultra photorealistic editorial beauty photograph. Beautiful Black woman, early 30s, deep rich brown skin with visible healthy dewy glow. Wearing a plush white spa robe, relaxed confident expression, soft natural smile. Natural hair in a protective silk wrap, gold stud earrings. Setting: upscale spa treatment room with warm ambient lighting. Soft bokeh of warm candlelight and greenery behind her, blurred treatment bed with white linens. Golden hour warmth, soft diffused key light from the left, warm fill from candles, subtle rim light on cheekbones. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Medium close-up, slightly off-center to the right, leaving negative space on left. Warm color grade, slight film grain, natural skin texture with visible pores, no airbrushing. Color palette: warm beige, burgundy accents, white linens, gold details.",
        "aspect": "16:9"
    },
    {
        "filename": "hero-facials.png",
        "prompt": "Ultra photorealistic beauty photograph. Licensed esthetician's gloved hands gently applying treatment serum to a Black woman's face. Client lying on spa treatment bed, eyes closed, peaceful serene expression. Client has deep brown melanin-rich skin, clear complexion. Esthetician wearing black medical-grade gloves. Professional spa treatment room with warm pendant lighting overhead, burgundy accent wall, white linens. Soft overhead ring light for even facial illumination, warm ambient side lighting. Shot on Sony A7IV, 50mm f/1.8 at f/2.8. Wide shot from slightly above showing both hands and full face. Warm color grade, natural skin texture, realistic glove texture.",
        "aspect": "16:9"
    },
    {
        "filename": "hero-microneedling.png",
        "prompt": "Ultra photorealistic medical spa photograph. Professional microneedling pen device held by gloved hands near a Black woman's cheek. Client lying on treatment bed, calm expression. The device is sleek silver and white, medical-grade. Client's skin is deep brown, smooth. Modern medical-spa treatment room with LED panel light overhead, skincare products on stainless steel cart, white walls with warm wood accents. Bright even clinical lighting with warm undertone. Shot on Sony A7IV, 70mm f/2.8 at f/3.5. Close-up showing device and cheek area from side angle. Clean, bright, warm whites, professional.",
        "aspect": "16:9"
    },
    {
        "filename": "hero-waxing.png",
        "prompt": "Ultra photorealistic interior photography. Elegant spa treatment room prepared for a body treatment service. Clean treatment bed with crisp white linens and a folded warm towel. Professional spa supplies arranged neatly on a side table. A small vase with a single red rose on the side table. Intimate private treatment room with warm beige walls, sheer curtains with soft natural light filtering through, LED candles, eucalyptus sprig. Soft warm diffused natural light from window. Shot on Sony A7IV, 35mm f/1.4 at f/2.8. Wide shot from doorway perspective. Warm color grade, soft vignette, dreamy warmth.",
        "aspect": "16:9"
    },
    {
        "filename": "hero-about.png",
        "prompt": "Ultra photorealistic editorial portrait. Confident Black woman esthetician, early 30s, standing in her spa treatment room. Wearing a professional burgundy spa coat, arms crossed confidently. Warm genuine smile, direct eye contact with camera. Deep rich brown skin, natural makeup, gold hoop earrings, neat professional hair in a low bun. Treatment room visible behind her with professional equipment, treatment bed, skincare products on shelves, warm pendant lights. Soft natural window light from the left, warm fill light. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Three-quarter length portrait, eyes at upper third line. Warm editorial grade, natural contrast.",
        "aspect": "3:4"
    },
    {
        "filename": "before-after-hyperpigmentation.png",
        "prompt": "Ultra photorealistic clinical skin comparison photograph. Close-up of a Black woman's cheek showing corrective skincare results. Left area of the cheek shows visible dark spots and hyperpigmentation patches on deep brown melanin-rich skin. Right area of the same cheek shows dramatically improved, even-toned, clear, radiant skin. Clinical beauty lighting, clean warm beige background. Shot on Canon R5, 100mm macro at f/5.6. Ultra sharp skin detail showing natural pores, honest documentation style.",
        "aspect": "1:1"
    },
    {
        "filename": "before-after-acne-scarring.png",
        "prompt": "Ultra photorealistic clinical skin photograph. Close-up of a Black woman's cheek showing acne scar treatment results. Visible improvement from textured, scarred skin to significantly smoother, even-toned melanin-rich skin with healthy radiance. Even diffused clinical lighting, clean warm beige background. Shot on Canon R5, 100mm macro at f/5.6. Extremely detailed skin texture, realistic on both areas, documentation style.",
        "aspect": "1:1"
    },
    {
        "filename": "before-after-uneven-tone.png",
        "prompt": "Ultra photorealistic clinical beauty photograph. Close-up portrait of a Black woman's face showing beautifully even, radiant, glowing melanin-rich skin with uniform tone and healthy luminosity. Makeup-free, neutral expression. Clean warm beige background. Even diffused beauty dish lighting. Shot on Canon R5, 85mm at f/4.0. Natural skin detail, smooth even radiance, healthy glow.",
        "aspect": "1:1"
    },
    {
        "filename": "card-body-treatment.png",
        "prompt": "Ultra photorealistic beauty photograph. Black woman's bare shoulders and upper back, deep rich brown skin with a luminous healthy glow. Skin looks hydrated, even-toned, radiant. White spa towel draped loosely below the shoulders. Subtle gold body shimmer catching the light on collarbones. Spa treatment room with soft warm beige wall out of focus behind. Soft warm side light emphasizing skin glow, subtle rim light on shoulders. Shot on Sony A7IV, 85mm f/1.4 at f/2.0. Close-up from behind showing shoulders, upper back, and neck. Warm tone, golden glow emphasis.",
        "aspect": "3:4"
    },
    {
        "filename": "card-packages-gifts.png",
        "prompt": "Ultra photorealistic luxury product photography. Elegant gift-wrapped skincare set on a white marble surface. Small luxury skincare bottles and jars arranged artfully in amber glass with gold caps. A burgundy satin ribbon bow tying the set together. A small dried flower arrangement beside it. Soft diffused natural window light from the left, warm bounce fill from right. White marble surface with warm veining, warm beige backdrop. Shot on Sony A7IV, 50mm f/1.8 at f/4.0. Overhead at 45-degree angle, editorial product shot. Clean, bright, warm whites, luxury feel.",
        "aspect": "3:4"
    },
    {
        "filename": "blog-skincare-routine.png",
        "prompt": "Ultra photorealistic lifestyle flatlay photograph. Complete skincare routine products arranged on warm marble surface. Products in order: gentle cleanser, vitamin C serum in amber dropper bottle, moisturizer in white jar, SPF in sleek tube. A small jade roller and a folded soft towel accent the arrangement. Morning light casting soft shadows. White marble surface with warm veining, warm beige linen underneath. Soft morning natural light from upper left. Shot on Sony A7IV, 35mm f/1.4 at f/4.0. True overhead flatlay, products in a flowing diagonal line. Bright warm lifestyle editorial.",
        "aspect": "16:9"
    },
    {
        "filename": "blog-first-facial.png",
        "prompt": "Ultra photorealistic spa photograph. Young Black woman lying on spa treatment bed, eyes gently closed, completely relaxed peaceful expression. Face has a thin layer of treatment product with slightly dewy translucent appearance. Hair wrapped in a soft white headband, white spa towel at shoulders. Deep brown melanin-rich skin, natural beauty, no makeup. Spa treatment room, soft warm lighting, blurred skincare bottles, warm wood accent wall. Soft diffused overhead light, warm ambient fill. Shot on Sony A7IV, 50mm f/1.8 at f/2.8. Medium close-up from slightly above. Soft, warm, dreamy, gentle contrast.",
        "aspect": "16:9"
    },
    {
        "filename": "blog-microneedling-safety.png",
        "prompt": "Ultra photorealistic medical spa photograph. Close-up of a professional skincare treatment being performed on a Black woman's forehead. Gloved hands holding a small medical device with precision and care. Serum product glistening on the treatment area. Deep brown melanin-rich skin. Medical spa treatment room with warm tones. Bright even clinical light with warm undertone focused on treatment area. Shot on Canon R5, 100mm f/2.8 macro at f/4.0. Close-up at skin level. Clean clinical but warm, professional.",
        "aspect": "16:9"
    },
    {
        "filename": "og-social-share.png",
        "prompt": "Professional social media card design for a beauty spa. Left half shows a close-up photograph of a Black woman's glowing cheek and jawline with radiant dewy melanin-rich skin in warm golden lighting. Right half is a warm beige panel. Clean graphic design layout optimized for social media sharing. Warm editorial photography, luxury spa brand feel. Burgundy and warm beige color palette.",
        "aspect": "16:9"
    }
]

def generate_image(prompt_data):
    filename = prompt_data["filename"]
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
        print(f"  ✓ {filename} already exists ({os.path.getsize(filepath)//1024}KB) — skipping", flush=True)
        return True

    print(f"  ⏳ Generating {filename}...", flush=True)

    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt_data["prompt"],
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=prompt_data["aspect"],
                person_generation="ALLOW_ADULT",
            )
        )

        if response.generated_images:
            img_bytes = response.generated_images[0].image.image_bytes
            with open(filepath, "wb") as f:
                f.write(img_bytes)
            size_kb = os.path.getsize(filepath) // 1024
            print(f"  ✓ {filename} saved ({size_kb}KB)", flush=True)
            return True
        else:
            print(f"  ✗ {filename} — no images returned", flush=True)
            return False

    except Exception as e:
        print(f"  ✗ {filename} — {str(e)[:150]}", flush=True)
        return False

def main():
    print(f"\n{'='*60}")
    print(f"  Rosie's Beauty Spa — Imagen 4.0 Generation")
    print(f"  Generating {len(IMAGES)} images")
    print(f"  Output: {OUTPUT_DIR}")
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
            time.sleep(5)

    print(f"\n{'='*60}")
    print(f"  Done! ✓ {success} succeeded, ✗ {failed} failed")
    if failed_list:
        print(f"  Failed: {', '.join(failed_list)}")
    print(f"  Files in: {OUTPUT_DIR}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
