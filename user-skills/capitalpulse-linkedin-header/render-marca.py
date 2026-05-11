"""
Capital Pulse — Variantes da logomarca (assets de marca)

Gera 6 variantes a partir do wordmark cream raster:
- A: square 1080x1080 dark
- B1: square 800x800 dark
- B2: square 400x400 dark
- C: monograma 1080x1080 dark (só o C estilizado)
- D: OG image 1200x630 (wordmark + manifesto Construção. Conteúdo. Capital.)
- E: square 1080x1080 paper (violet wordmark sobre cream)

E SVG (variante A em formato vetorial via potrace ou embed PNG fallback).

Reusa tokens e fontes dos banners (Sistema Signal v1 do site capitalpulse-web).
"""
import base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).parent
FONTS = BASE / "fonts"
LOGO = BASE / "logo"

# Output goes to "Imagens Capital Pulse/Marca/"
OUT = Path("/sessions/intelligent-bold-allen/mnt/Imagens Capital Pulse/Marca")

# === Brand tokens ===
DARK = {
    "bg": "#0B0D12",
    "primary": "#F2F1EB",
    "secondary": "#A8AAB4",
    "signal": "#5B3BFF",
}

PAPER = {
    "bg": "#FAFAF7",
    "primary": "#0B0D12",
    "secondary": "#4A4E5A",
    "signal": "#5B3BFF",
}


def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip("#")
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))


def tint_logo(logo_img, target_hex):
    """Tonaliza a logomarca para uma cor alvo, preservando alpha."""
    target = hex_to_rgb(target_hex)
    rgba = logo_img.convert("RGBA")
    pixels = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a > 0:
                pixels[x, y] = (target[0], target[1], target[2], a)
    return rgba


def crop_monogram(wordmark_img):
    """
    Extrai apenas o 'C' estilizado do wordmark.
    O wordmark tem o C à esquerda + 'CAPITAL PULSE' texto à direita.
    Crop aproximado: primeiros ~30% da largura.
    """
    w, h = wordmark_img.size
    # O C ocupa aproximadamente os primeiros 30-32% do wordmark cream-tight
    # Wordmark cream-tight is 297x114; C está em ~0-95 horizontal
    crop_box = (0, 0, int(w * 0.30), h)
    cropped = wordmark_img.crop(crop_box)

    # Trim transparent margins ao redor
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
    return cropped


def make_square_logo(size, bg_hex, logo_color_hex, logo_padding_ratio=0.06):
    """
    Cria um quadrado com background sólido e wordmark centralizado.
    logo_padding_ratio: fração do tamanho que é margem (0.20 = 20% margin)
    """
    canvas = Image.new("RGB", (size, size), bg_hex)

    logo = Image.open(LOGO / "wordmark-cream.png").convert("RGBA")
    if logo_color_hex != "#F2F1EB" and logo_color_hex.upper() != "#F0EDE6":
        logo = tint_logo(logo, logo_color_hex)

    # Calcular tamanho do logo
    available = int(size * (1 - 2 * logo_padding_ratio))
    aspect = logo.width / logo.height

    if aspect > 1:
        new_w = available
        new_h = int(available / aspect)
    else:
        new_h = available
        new_w = int(available * aspect)

    logo = logo.resize((new_w, new_h), Image.LANCZOS)

    # Centralizar
    x = (size - new_w) // 2
    y = (size - new_h) // 2

    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(logo, (x, y), logo)
    return canvas_rgba.convert("RGB")


def make_stacked_logo(size, bg_hex, logo_color_hex):
    """
    Composição empilhada para canvas quadrado:
    - Símbolo 'C' grande no topo
    - 'CAPITAL' / 'PULSE' em duas linhas embaixo (Instrument Serif)

    Mais elegante que o wordmark wide num canvas quadrado.
    """
    canvas = Image.new("RGB", (size, size), bg_hex)
    draw = ImageDraw.Draw(canvas)

    # 1. Cropar e ampliar o C
    wordmark = Image.open(LOGO / "wordmark-cream.png").convert("RGBA")
    monogram = crop_monogram(wordmark)
    if logo_color_hex != "#F2F1EB" and logo_color_hex.upper() != "#F0EDE6":
        monogram = tint_logo(monogram, logo_color_hex)

    # C ocupa ~35% do canvas em altura
    c_height = int(size * 0.35)
    c_aspect = monogram.width / monogram.height
    c_width = int(c_height * c_aspect)
    monogram = monogram.resize((c_width, c_height), Image.LANCZOS)

    # Posicionar o C: centralizado horizontal, topo a ~18% do canvas
    c_x = (size - c_width) // 2
    c_y = int(size * 0.18)

    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(monogram, (c_x, c_y), monogram)
    canvas = canvas_rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # 2. Tipografar CAPITAL / PULSE em duas linhas usando Instrument Serif
    font_size = int(size * 0.085)  # ~92px em 1080
    font_wordmark = ImageFont.truetype(str(FONTS / "InstrumentSerif-Regular.ttf"), font_size)
    line_height = int(font_size * 1.05)

    # Posição: abaixo do C, a partir de ~60% do canvas
    text_top_y = int(size * 0.62)

    def draw_centered_tracked(text, y, tracking_em=0.08):
        """Desenha texto centralizado com tracking."""
        extra = font_size * tracking_em
        # Calcula largura total
        total_width = 0
        for ch in text:
            bbox = draw.textbbox((0, 0), ch, font=font_wordmark)
            total_width += (bbox[2] - bbox[0]) + extra
        total_width -= extra  # remove o extra do último char
        x = (size - total_width) // 2
        for ch in text:
            draw.text((x, y), ch, font=font_wordmark, fill=logo_color_hex)
            bbox = draw.textbbox((0, 0), ch, font=font_wordmark)
            x += (bbox[2] - bbox[0]) + extra

    draw_centered_tracked("CAPITAL", text_top_y)
    draw_centered_tracked("PULSE", text_top_y + line_height)

    return canvas


def make_monogram(size, bg_hex, logo_color_hex):
    """Versão só com o 'C' estilizado, centralizado."""
    return make_monogram_punch(size, bg_hex, logo_color_hex, c_ratio=0.55)


def make_monogram_punch(size, bg_hex, logo_color_hex, c_ratio=0.75):
    """
    Monograma com tamanho do C parametrizável.
    c_ratio: fração do canvas ocupada pela maior dimensão do C
    (0.55 = elegante mas tímido para avatar pequeno,
     0.75 = punch máximo para avatares e listagens em escala pequena)
    """
    canvas = Image.new("RGB", (size, size), bg_hex)
    logo = Image.open(LOGO / "wordmark-cream.png").convert("RGBA")
    monogram = crop_monogram(logo)

    if logo_color_hex != "#F2F1EB" and logo_color_hex.upper() != "#F0EDE6":
        monogram = tint_logo(monogram, logo_color_hex)

    available = int(size * c_ratio)
    aspect = monogram.width / monogram.height

    if aspect > 1:
        new_w = available
        new_h = int(available / aspect)
    else:
        new_h = available
        new_w = int(available * aspect)

    monogram = monogram.resize((new_w, new_h), Image.LANCZOS)

    x = (size - new_w) // 2
    y = (size - new_h) // 2

    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(monogram, (x, y), monogram)
    return canvas_rgba.convert("RGB")


def make_og_image(width=1200, height=630):
    """
    Open Graph image: fundo dark + wordmark à esquerda + manifesto à direita.
    Manifesto: 'Construção. Conteúdo. Capital.' (Capital em violet)
    """
    canvas = Image.new("RGB", (width, height), DARK["bg"])
    draw = ImageDraw.Draw(canvas)

    # Wordmark à esquerda — ~30% width
    logo = Image.open(LOGO / "wordmark-cream.png").convert("RGBA")
    logo_width = int(width * 0.22)
    aspect = logo.width / logo.height
    logo_height = int(logo_width / aspect)
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)

    # Posicionar logo: lateral esquerda, vertical centralizado
    margin = 80
    logo_x = margin
    logo_y = (height - logo_height) // 2

    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(logo, (logo_x, logo_y), logo)
    canvas = canvas_rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # Hairline divider vertical
    divider_x = logo_x + logo_width + 80
    draw.line(
        [(divider_x, margin + 40), (divider_x, height - margin - 40)],
        fill="#2A2E38", width=1
    )

    # Manifesto à direita — 3 linhas
    text_x = divider_x + 80
    font_manifesto = ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 72)
    font_tagline = ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), 26)
    font_eyebrow = ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), 20)

    # Eyebrow em mono uppercase
    eyebrow_y = margin + 40
    eyebrow_text = "CAPITAL PULSE"
    x = text_x
    extra = 20 * 0.14  # tracking 0.14em
    for char in eyebrow_text:
        draw.text((x, eyebrow_y), char, font=font_eyebrow, fill=DARK["secondary"])
        bbox = draw.textbbox((0, 0), char, font=font_eyebrow)
        x += (bbox[2] - bbox[0]) + extra

    # Manifesto: 3 linhas com Capital em violet
    line_height = 84
    base_y = eyebrow_y + 60
    draw.text((text_x, base_y), "Construção.", font=font_manifesto, fill=DARK["primary"])
    draw.text((text_x, base_y + line_height), "Conteúdo.", font=font_manifesto, fill=DARK["primary"])
    draw.text((text_x, base_y + line_height * 2), "Capital.", font=font_manifesto, fill=DARK["signal"])

    # Tagline italic na base
    tagline_y = height - margin - 60
    draw.text(
        (text_x, tagline_y),
        "Venture studio brasileiro AI-native.",
        font=font_tagline, fill=DARK["secondary"]
    )
    draw.text(
        (text_x, tagline_y + 34),
        "capitalpulse.com.br",
        font=font_tagline, fill=DARK["secondary"]
    )

    return canvas


def make_svg_embed_png(png_path, width, height, output_path):
    """
    Cria um SVG válido que embed o PNG como base64.
    Permite usar como .svg em contextos web sem perder fidelidade do raster.
    """
    with open(png_path, "rb") as f:
        png_b64 = base64.b64encode(f.read()).decode("ascii")

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>Capital Pulse — Logomarca</title>
  <desc>Capital Pulse · venture studio brasileiro AI-native. Wordmark cream sobre fundo ink (#0B0D12).</desc>
  <image href="data:image/png;base64,{png_b64}" x="0" y="0" width="{width}" height="{height}"/>
</svg>
'''
    output_path.write_text(svg, encoding="utf-8")
    return output_path


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"Output dir: {OUT}")

    # === A — Square 1080x1080 dark ===
    img = make_square_logo(1080, DARK["bg"], DARK["primary"])
    path_a = OUT / "logo-square-dark-1080x1080.png"
    img.save(path_a, "PNG", optimize=True)
    print(f"✓ A: {path_a.name}")

    # === B1 — Square 800x800 dark ===
    img = make_square_logo(800, DARK["bg"], DARK["primary"])
    img.save(OUT / "logo-square-dark-800x800.png", "PNG", optimize=True)
    print(f"✓ B1: logo-square-dark-800x800.png")

    # === B2 — Square 400x400 dark ===
    img = make_square_logo(400, DARK["bg"], DARK["primary"])
    img.save(OUT / "logo-square-dark-400x400.png", "PNG", optimize=True)
    print(f"✓ B2: logo-square-dark-400x400.png")

    # === C — Monograma 1080x1080 dark ===
    img = make_monogram(1080, DARK["bg"], DARK["primary"])
    img.save(OUT / "logo-monograma-dark-1080x1080.png", "PNG", optimize=True)
    print(f"✓ C: logo-monograma-dark-1080x1080.png")

    # === D — OG image 1200x630 ===
    img = make_og_image(1200, 630)
    path_d = OUT / "logo-og-1200x630.png"
    img.save(path_d, "PNG", optimize=True)
    print(f"✓ D: {path_d.name}")

    # === E — Square 1080x1080 paper (violet wordmark sobre cream) ===
    img = make_square_logo(1080, PAPER["bg"], PAPER["signal"])
    img.save(OUT / "logo-square-paper-1080x1080.png", "PNG", optimize=True)
    print(f"✓ E: logo-square-paper-1080x1080.png")

    # === F — Stacked layout 1080x1080 dark (símbolo grande + wordmark 2 linhas) ===
    img = make_stacked_logo(1080, DARK["bg"], DARK["primary"])
    img.save(OUT / "logo-stack-dark-1080x1080.png", "PNG", optimize=True)
    print(f"✓ F: logo-stack-dark-1080x1080.png")

    # === F-paper — Stacked paper variant ===
    img = make_stacked_logo(1080, PAPER["bg"], PAPER["signal"])
    img.save(OUT / "logo-stack-paper-1080x1080.png", "PNG", optimize=True)
    print(f"✓ F-paper: logo-stack-paper-1080x1080.png")

    # === F-400 — Stacked 400x400 dark (versão pequena para avatar LinkedIn) ===
    img = make_stacked_logo(400, DARK["bg"], DARK["primary"])
    img.save(OUT / "logo-stack-dark-400x400.png", "PNG", optimize=True)
    print(f"✓ F-400: logo-stack-dark-400x400.png")

    # === Avatar Variants — monograma "punch" para escala pequena ===
    # G-A: Cream sobre dark, C bem maior (75% do canvas)
    img = make_monogram_punch(1080, DARK["bg"], DARK["primary"], c_ratio=0.75)
    img.save(OUT / "avatar-A-cream-on-dark-1080x1080.png", "PNG", optimize=True)
    img.resize((400, 400), Image.LANCZOS).save(OUT / "avatar-A-cream-on-dark-400x400.png", "PNG", optimize=True)
    print(f"✓ G-A: avatar-A-cream-on-dark (cream / dark)")

    # G-B: Cream sobre violet — punch máximo
    img = make_monogram_punch(1080, DARK["signal"], DARK["primary"], c_ratio=0.75)
    img.save(OUT / "avatar-B-cream-on-violet-1080x1080.png", "PNG", optimize=True)
    img.resize((400, 400), Image.LANCZOS).save(OUT / "avatar-B-cream-on-violet-400x400.png", "PNG", optimize=True)
    print(f"✓ G-B: avatar-B-cream-on-violet (cream / violet)")

    # G-C: Violet sobre dark — accent invertido
    img = make_monogram_punch(1080, DARK["bg"], DARK["signal"], c_ratio=0.75)
    img.save(OUT / "avatar-C-violet-on-dark-1080x1080.png", "PNG", optimize=True)
    img.resize((400, 400), Image.LANCZOS).save(OUT / "avatar-C-violet-on-dark-400x400.png", "PNG", optimize=True)
    print(f"✓ G-C: avatar-C-violet-on-dark (violet / dark)")

    # === SVG: variante A em formato vetorial via embed PNG ===
    make_svg_embed_png(path_a, 1080, 1080, OUT / "logo-square-dark-1080x1080.svg")
    print(f"✓ SVG: logo-square-dark-1080x1080.svg")

    # === SVG paper ===
    make_svg_embed_png(
        OUT / "logo-square-paper-1080x1080.png",
        1080, 1080,
        OUT / "logo-square-paper-1080x1080.svg"
    )
    print(f"✓ SVG: logo-square-paper-1080x1080.svg")

    # === SVG stack dark ===
    make_svg_embed_png(
        OUT / "logo-stack-dark-1080x1080.png",
        1080, 1080,
        OUT / "logo-stack-dark-1080x1080.svg"
    )
    print(f"✓ SVG: logo-stack-dark-1080x1080.svg")

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
