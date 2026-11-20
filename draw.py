# Draws entry.png: a one-page newspaper front page summing up the world news
# of Friday 20 November 2026. Pure Pillow, deterministic (no network, no
# randomness, fixed fonts). Run: python3 draw.py  -> writes entry.png (1024x1024).
# Every fact below was verified against reporting of 20 Nov 2026 (One Turn's
# day page, Open Chronicle, Bangladesh Chronicle, Cognoscere, each cross-checked
# against BBC / The Guardian / Al Jazeera / CNBC / UN News sourcing).

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (178, 32, 44)
NAVY = (31, 56, 100)
GOLD = (201, 162, 39)
GREY = (90, 86, 78)
TEAL = (18, 110, 105)
MAROON = (122, 32, 48)
GREEN = (46, 125, 50)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def block_h(d, text, fnt, max_w, leading):
    return len(wrap(d, text, fnt, max_w)) * leading


def draw_block(d, x, y, text, fnt, color, max_w, leading):
    for ln in wrap(d, text, fnt, max_w):
        d.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer frame ----
d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
d.rectangle([18, 18, W - 19, H - 19], outline=INK, width=1)

# ================= MASTHEAD =================
cx = W // 2
d.text((cx, 34), "THE WORLD IN ONE DAY", font=font(SERIF_B, 62),
       fill=INK, anchor="ma")
d.text((cx, 108), "FRIDAY  ·  20 NOVEMBER 2026", font=font(SANS_B, 27),
       fill=RED, anchor="ma")
d.text((cx, 140), "ONE DAY'S NEWS, IN ONE IMAGE", font=font(SANS, 15),
       fill=GREY, anchor="ma")
d.line([(48, 168), (W - 48, 168)], fill=INK, width=3)
d.line([(48, 173), (W - 48, 173)], fill=INK, width=1)


# ================= ICONS (simple discs, drawn shapes only) =================
def icon_scales(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD)
    c = (255, 255, 255)
    d.line([(x, y - r + 22), (x, y + r - 22)], fill=c, width=5)
    d.line([(x - r + 26, y - r + 34), (x + r - 26, y - r + 34)], fill=c, width=5)
    for sx in (-1, 1):
        px = x + sx * (r - 34)
        d.line([(px, y - r + 34), (px, y - r + 60)], fill=c, width=4)
        d.arc([px - 20, y - r + 50, px + 20, y - r + 90], 0, 180, fill=c, width=4)
    d.ellipse([x - 7, y - r + 14, x + 7, y - r + 28], fill=c)


def icon_globe(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=NAVY)
    c = (255, 255, 255)
    d.ellipse([x - r + 9, y - r + 9, x + r - 9, y + r - 9], outline=c, width=4)
    d.ellipse([x - r // 2, y - r + 9, x + r // 2, y + r - 9], outline=c, width=3)
    d.line([(x - r + 9, y), (x + r - 9, y)], fill=c, width=3)


def icon_tower(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=MAROON)
    c = (255, 255, 255)
    d.rectangle([x - 15, y - r + 32, x + 15, y + r - 16], fill=c)
    d.polygon([(x - 15, y - r + 32), (x + 15, y - r + 32), (x, y - r + 12)], fill=c)
    for wy in range(y - r + 50, y + r - 22, 15):
        d.rectangle([x - 8, wy, x - 2, wy + 7], fill=MAROON)
        d.rectangle([x + 2, wy, x + 8, wy + 7], fill=MAROON)


def icon_bridge(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=TEAL)
    c = (255, 255, 255)
    d.line([(x - r + 14, y + 12), (x + r - 14, y + 12)], fill=c, width=5)
    d.arc([x - r + 16, y - r + 24, x + r - 16, y + 28], 180, 360, fill=c, width=4)
    for px in (x - 32, x, x + 32):
        d.line([(px, y - 10), (px, y + 12)], fill=c, width=3)


def icon_chart(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
    c = (255, 255, 255)
    pts = [(x - r + 18, y - 8), (x - 14, y - 22), (x + 2, y - 4),
           (x + 18, y - 12), (x + r - 20, y + 20)]
    d.line(pts, fill=c, width=5, joint="curve")
    d.polygon([(x + r - 18, y + 22), (x + r - 32, y + 12), (x + r - 28, y + 28)],
              fill=c)


# ================= LEAD STORY (flow layout) =================
y = 190
d.text((48, y), "THE HAGUE  ·  JUSTICE", font=font(SANS_B, 20), fill=RED)
icon_scales(d, 880, 292, 74)
y += 30
y = draw_block(d, 48, y, "World Court rules Myanmar committed",
               font(SERIF_B, 44), INK, 660, 52)
y = draw_block(d, 48, y, "genocide against the Rohingya",
               font(SERIF_B, 44), INK, 660, 52)
y += 8
y = draw_block(
    d, 48, y,
    "In a 9–6 ruling, the International Court of Justice holds a state "
    "responsible for genocide for the first time — over the 2017 campaign "
    "that drove hundreds of thousands of Rohingya into Bangladesh.",
    font(SERIF, 20), INK, 928, 27)
print("lead ends at y =", y)
d.line([(48, y + 12), (W - 48, y + 12)], fill=INK, width=2)


def panel(x, y, w, kicker, color, headline, deck, icon):
    """Draw one story panel; return the y just below it."""
    d.text((x, y), kicker, font=font(SANS_B, 18), fill=color)
    if icon:
        icon(d, x + w - 32, y + 26, 32)
        tw = w - 80
    else:
        tw = w
    yy = y + 28
    yy = draw_block(d, x, yy, headline, font(SERIF_B, 28), INK, tw, 34)
    yy += 5
    yy = draw_block(d, x, yy, deck, font(SERIF, 18), INK, w, 24)
    return yy


# ---- row 2 ----
y2 = y + 26
e1 = panel(48, y2, 452, "SHENZHEN  ·  DIPLOMACY", NAVY,
           "Trump, Xi and Putin sign a peace declaration",
           "First three-way summit of the US, China and Russia ends after "
           "about 70 minutes. It says nothing about Ukraine or Iran.",
           icon_globe)
e2 = panel(524, y2, 452, "RIYADH  ·  CONFLICT", MAROON,
           "Houthi missile damages Riyadh's tallest tower",
           "A missile struck the Public Investment Fund tower in the "
           "financial district. No injuries were reported.",
           icon_tower)
row2_end = max(e1, e2)
print("row2 ends at y =", row2_end)
d.line([(48, row2_end + 12), (W - 48, row2_end + 12)], fill=INK, width=1)

# ---- row 3 ----
y3 = row2_end + 24
e3 = panel(48, y3, 452, "KYIV  ·  WAR", TEAL,
           "Kyiv hit again as Ukraine strikes Crimea Bridge",
           "Overnight missiles struck Kyiv; Ukraine hit the Kerch Bridge "
           "for a third time in four days, halting rail traffic.",
           icon_bridge)
e4 = panel(524, y3, 452, "MARKETS  ·  ECONOMY", RED,
           "Stocks slide; Anthropic debut can't lift AI shares",
           "S&P 500 −2% for a fifth straight day; Nikkei −4.8%. Anthropic "
           "closed 17% above its $83 IPO price, at about $97.",
           icon_chart)
row3_end = max(e3, e4)
print("row3 ends at y =", row3_end)
d.line([(48, row3_end + 12), (W - 48, row3_end + 12)], fill=INK, width=2)

# ---- bottom strip: also on 20 November ----
y4 = row3_end + 22
d.text((48, y4), "ALSO ON 20 NOVEMBER", font=font(SANS_B, 18), fill=RED)
y4 += 28
strip_items = [
    (48, 452, "KENYA — Last Ebola patient goes home, 37 days after the "
              "first case; a 42-day countdown to Ebola-free begins."),
    (524, 452, "COP31 — Draft deal in Antalya drops the call to phase out "
              "fossil fuels."),
    (48, 452, "GTA 6 — Launch tops $2.3bn, the biggest entertainment "
             "launch ever."),
    (524, 452, "SPACE — Voyager 1 reaches one light-day from Earth, "
              "26bn km out."),
]
yy = y4
for i, (x, w, txt) in enumerate(strip_items):
    yy = max(yy, draw_block(d, x, y4 + (i // 2) * 48, txt,
                            font(SERIF, 17), INK, w, 22))
print("strip ends at y =", yy)
d.line([(48, yy + 8), (W - 48, yy + 8)], fill=INK, width=1)
fy = yy + 16
d.text((cx, fy), "Events of Friday 20 November 2026, as reported that day",
       font=font(SERIF_I, 16), fill=GREY, anchor="ma")
d.text((cx, fy + 22),
       "Sources: BBC · The Guardian · Al Jazeera · CNBC · UN News · The Hindu · France 24",
       font=font(SANS, 12), fill=GREY, anchor="ma")
print("footer ends at y =", fy + 38)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
