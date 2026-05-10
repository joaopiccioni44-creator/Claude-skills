"""
Capital Pulse — LinkedIn Header Renderer
Renderiza o banner do LinkedIn em 1584x396 usando os tokens do site (globals.css).

Tokens reusados:
- Background dark: #0B0D12 (--ink-bg)
- Texto primário dark: #F2F1EB (--text-primary cream)
- Texto secundário dark: #A8AAB4 (--text-secondary)
- Signal accent: #5B3BFF (--signal violet)
- Background paper: #FAFAF7 (--paper)
- Texto primário light: #0B0D12 (--text-primary ink)
- Texto secundário light: #4A4E5A

Tipografia:
- Geist Sans SemiBold — masthead (manifesto)
- Instrument Serif Italic — tagline (tese)
- JetBrains Mono Regular — eyebrow label
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# === Paths ===
BASE = Path(__file__).parent
FONTS = BASE / "fonts"
LOGO = BASE / "logo"
OUT = BASE

# === Canvas ===
WIDTH = 1584
HEIGHT = 396

# === Brand tokens (Capital Pulse Sistema "Signal" v1) ===
DARK = {
    "bg": "#0B0D12",
    "primary": "#F2F1EB",
    "secondary": "#A8AAB4",
    "signal": "#5B3BFF",
    "hairline": "#2A2E38",
}

PAPER = {
    "bg": "#FAFAF7",
    "primary": "#0B0D12",
    "secondary": "#4A4E5A",
    "signal": "#5B3BFF",
    "hairline": "#E8E7E1",
}

# === Typography sizes (calibrated for 1584x396 at LinkedIn display) ===
EYEBROW_SIZE = 26
MASTHEAD_SIZE_MINIMAL = 92   # 3 linhas empilhadas, cabe mobile safe zone
MASTHEAD_SIZE_FULL = 76      # versão com tagline — 3 linhas + tagline
TAGLINE_SIZE = 28

# === Layout ===
SAFE_LEFT = 380   # x onde texto começa (dentro da safe zone mobile 317-1267)
SAFE_RIGHT = 1530


def load_fonts(masthead_size):
    """Carrega as três fontes nos tamanhos definidos."""
    return {
        "eyebrow": ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), EYEBROW_SIZE),
        "masthead": ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), masthead_size),
        "tagline": ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), TAGLINE_SIZE),
        "tagline_regular": ImageFont.truetype(str(FONTS / "InstrumentSerif-Regular.ttf"), TAGLINE_SIZE),
    }


def draw_tracked_text(draw, text, position, font, color, tracking_em=0.0):
    """
    Desenha texto com tracking (letter-spacing) manual.
    tracking_em é a fração do tamanho da fonte para adicionar entre cada caractere.
    """
    x, y = position
    # Estimar tamanho da fonte para tracking
    font_size = font.size if hasattr(font, 'size') else EYEBROW_SIZE
    extra = font_size * tracking_em

    for char in text:
        draw.text((x, y), char, font=font, fill=color)
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        x += char_width + extra
    return x  # retorna o x final


def draw_masthead_with_accent(draw, words_with_colors, position, font, gap_extra=0):
    """
    Desenha o masthead com diferentes cores por palavra.
    words_with_colors: [(palavra, cor), ...]
    """
    x, y = position
    for i, (word, color) in enumerate(words_with_colors):
        draw.text((x, y), word, font=font, fill=color)
        bbox = draw.textbbox((0, 0), word, font=font)
        word_width = bbox[2] - bbox[0]
        # Espaço normal entre palavras
        if i < len(words_with_colors) - 1:
            space_bbox = draw.textbbox((0, 0), " ", font=font)
            space_width = (space_bbox[2] - space_bbox[0]) + gap_extra
            x += word_width + space_width
        else:
            x += word_width
    return x


def tint_logo(logo_img, target_hex):
    """
    Tonaliza a logomarca para uma cor alvo, preservando alpha.
    Usado para gerar a versão violet (paper) a partir da cream (dark).
    """
    # Hex -> RGB
    target = tuple(int(target_hex[i:i+2], 16) for i in (1, 3, 5))
    rgba = logo_img.convert("RGBA")
    pixels = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a > 0:
                # Aplica a cor alvo preservando alpha original
                pixels[x, y] = (target[0], target[1], target[2], a)
    return rgba


def composite_logo(canvas, theme, logo_height=82, margin_right=64, margin_bottom=64):
    """
    Coloca a logomarca no canto inferior direito.
    """
    # Carrega logo cream (versão para fundo dark)
    logo_path = LOGO / "wordmark-cream.png"
    logo = Image.open(logo_path).convert("RGBA")

    # Tonaliza se for paper (precisa virar violet pra contraste em fundo claro)
    if theme["bg"] == PAPER["bg"]:
        logo = tint_logo(logo, theme["signal"])

    # Redimensiona mantendo aspect ratio
    aspect = logo.width / logo.height
    new_h = logo_height
    new_w = int(new_h * aspect)
    logo = logo.resize((new_w, new_h), Image.LANCZOS)

    # Posiciona no canto inferior direito
    x = canvas.width - new_w - margin_right
    y = canvas.height - new_h - margin_bottom

    # Cola com alpha compositing
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(logo, (x, y), logo)
    return canvas_rgba.convert("RGB")


def render_header(theme, eyebrow_text, manifesto_lines, tagline_text, output_path):
    """
    Renderiza um banner.
    theme: dict com cores (DARK ou PAPER)
    eyebrow_text: string maiúscula para o label superior
    manifesto_lines: lista de listas — cada linha é [(palavra, "primary"|"signal"), ...]
    tagline_text: string da tese em italic (None pra omitir)
    output_path: caminho do PNG final
    """
    img = Image.new("RGB", (WIDTH, HEIGHT), theme["bg"])
    draw = ImageDraw.Draw(img)

    # Escolher tamanho do masthead baseado em ter ou não tagline
    masthead_size = MASTHEAD_SIZE_FULL if tagline_text else MASTHEAD_SIZE_MINIMAL
    fonts = load_fonts(masthead_size)

    # Resolver cores
    color_map = {
        "primary": theme["primary"],
        "signal": theme["signal"],
        "secondary": theme["secondary"],
    }

    # === Layout vertical ===
    # 3 linhas empilhadas (Conteúdo. / Construção. / Capital.)
    if tagline_text:
        # FULL: eyebrow + 3 linhas masthead 76px + tagline 28px
        eyebrow_y = 32
        masthead_y_line1 = 76
        masthead_line_gap = -10  # apertar linhas (overshoot natural do font para baixo)
        tagline_y = 348
    else:
        # MINIMAL: eyebrow + 3 linhas masthead 92px (centro vertical)
        # 3 × 92 = 276 + eyebrow stack ~50 + gaps = ~340; centra em 396
        eyebrow_y = 32
        masthead_y_line1 = 76
        masthead_line_gap = -8
        tagline_y = None

    # === Eyebrow label (mono uppercase, tracked) ===
    draw_tracked_text(
        draw,
        eyebrow_text,
        (SAFE_LEFT, eyebrow_y),
        fonts["eyebrow"],
        theme["secondary"],
        tracking_em=0.14,
    )

    # === Masthead em múltiplas linhas ===
    line_height = masthead_size + masthead_line_gap
    for i, line_words in enumerate(manifesto_lines):
        resolved = [(w, color_map[c]) for w, c in line_words]
        y = masthead_y_line1 + i * line_height
        draw_masthead_with_accent(
            draw,
            resolved,
            (SAFE_LEFT - 4, y),
            fonts["masthead"],
            gap_extra=0,
        )

    # === Tagline opcional ===
    if tagline_text:
        draw.text(
            (SAFE_LEFT, tagline_y),
            tagline_text,
            font=fonts["tagline"],
            fill=theme["secondary"],
        )

    # === Logomarca no canto inferior direito ===
    img = composite_logo(img, theme, logo_height=82, margin_right=64, margin_bottom=64)

    img.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    # === DARK PT — versão MINIMAL (sem tagline, masthead grande) ===
    out = render_header(
        theme=DARK,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construção.", "primary")],
            [("Conteúdo.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text=None,
        output_path=str(OUT / "linkedin-header-pt-dark-minimal-1584x396.png"),
    )
    print(f"✓ Generated: {out}")

    # === DARK PT — versão FULL (com tagline) ===
    out = render_header(
        theme=DARK,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construção.", "primary")],
            [("Conteúdo.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text="Construímos, escrevemos e alocamos na fronteira entre mercado e IA",
        output_path=str(OUT / "linkedin-header-pt-dark-full-1584x396.png"),
    )
    print(f"✓ Generated: {out}")

    # === PAPER PT — versão MINIMAL ===
    out = render_header(
        theme=PAPER,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construção.", "primary")],
            [("Conteúdo.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text=None,
        output_path=str(OUT / "linkedin-header-pt-paper-minimal-1584x396.png"),
    )
    print(f"✓ Generated: {out}")

    # === PAPER PT — versão FULL ===
    out = render_header(
        theme=PAPER,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construção.", "primary")],
            [("Conteúdo.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text="Construímos, escrevemos e alocamos na fronteira entre mercado e IA",
        output_path=str(OUT / "linkedin-header-pt-paper-full-1584x396.png"),
    )
    print(f"✓ Generated: {out}")

    # === DARK EN — versão MINIMAL ===
    out = render_header(
        theme=DARK,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construction.", "primary")],
            [("Content.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text=None,
        output_path=str(OUT / "linkedin-header-en-dark-minimal-1584x396.png"),
    )
    print(f"✓ Generated: {out}")

    # === DARK EN — versão FULL ===
    out = render_header(
        theme=DARK,
        eyebrow_text="STUDIO · EDITORIAL · CAPITAL",
        manifesto_lines=[
            [("Construction.", "primary")],
            [("Content.", "primary")],
            [("Capital.", "signal")],
        ],
        tagline_text="We build, write and allocate at the frontier between markets and AI",
        output_path=str(OUT / "linkedin-header-en-dark-full-1584x396.png"),
    )
    print(f"✓ Generated: {out}")


if __name__ == "__main__":
    main()
