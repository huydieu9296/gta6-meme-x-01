#!/usr/bin/env python3
"""Overlay meme captions onto the generated base image.

Base image: 1600x1600, scene occupies y~310..1310, dark bands top/bottom.
Output: 1024x1024 meme.png with Impact-style captions (DejaVu Sans Bold,
white fill, black outline) in the dark bands. Run: python3 overlay-caption.py
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "media-generation-gta6-meme-base-0-6c613663-8276-49b0-be2d-f966f8ff6c78.png"
OUT = "meme.png"
SIZE = 1024
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP = "GTA 6 LAUNCH NIGHT"
BOTTOM = ["ME: WASTED.", "MY AGENT: STILL GRINDING."]

im = Image.open(SRC).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
d = ImageDraw.Draw(im)


def fit_font(text, max_w, start):
    size = start
    while size > 10:
        f = ImageFont.truetype(FONT_PATH, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(FONT_PATH, 10)


def draw_centered(text, font, cy):
    w = d.textlength(text, font=font)
    x = (SIZE - w) / 2
    d.text((x, cy), text, font=font, fill="white",
           stroke_width=max(3, font.size // 12), stroke_fill="black",
           anchor="lm")


top_font = fit_font(TOP, SIZE - 60, 72)
draw_centered(TOP, top_font, 99)  # middle of top band (0..~198)

bot_font = fit_font(BOTTOM[1], SIZE - 60, 58)
# bottom band ~839..1024; two lines centred in it
draw_centered(BOTTOM[0], bot_font, 888)
draw_centered(BOTTOM[1], bot_font, 958)

im.save(OUT, "PNG")
print(f"wrote {OUT} {im.size}")
