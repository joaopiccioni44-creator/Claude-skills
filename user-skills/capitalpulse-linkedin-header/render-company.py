"""
Capital Pulse — Company Page LinkedIn Banner
Renderiza banner para a página da empresa (1128x191).

Diferenças vs banner pessoal:
- Dimensão strip horizontal (5.9:1 em vez de 4:1)
- Manifesto em linha única (formato estreito não comporta 3 linhas)
- SEM wordmark sobreposto — o avatar da página já mostra a logo
- Safe zone bottom-left para a logomarca da empresa que sobrepõe
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE = Path(__file__).parent
FONTS = BASE / "fonts"
OUT = BASE

# === Canvas Company Page ===
WIDTH = 1128
HEIGHT = 191

# === Brand tokens (mesmos do banner pessoal) ===
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

# === Tipografia (calibrada para 1128x191) ===
EYEBROW_SIZE = 17
MANIFESTO_SIZE = 56
TAGLINE_SIZE = 20

# === Layout ===
# Avatar da empresa cobre bottom-left ~190x190px sobreposto
# Por isso SAFE_LEFT é maior aqui que no banner pessoal
SAFE_LEFT = 220


def draw_tracked_text(draw, text, position, font, color, tracking_em=0.0):
    """Texto com tracking manual."""
    x, y = position
    font_size = font.size if hasattr(font, 'size') else EYEBROW_SIZE
    extra = font_size * tracking_em
    for char in text:
        draw.text((x, y), char, font=font, fill=color)
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        x += char_width + extra
    return x


def draw_manifesto(draw, words_with_colors, position, font):
    """Desenha manifesto em linha única com cores diferentes por palavra."""
    x, y = position
    for i, (word, color) in enumerate(words_with_colors):
        draw.text((x, y), word, font=font, fill=color)
        bbox = draw.textbbox((0, 0), word, font=font)
        word_width = bbox[2] - bbox[0]
        if i < len(words_with_colors) - 1:
            space_bbox = draw.textbbox((0, 0), " ", font=font)
            space_width = space_bbox[2] - space_bbox[0]
            x += word_width + space_width
        else:
            x += word_width
    return x


def render_company_banner(theme, eyebrow_text, manifesto_words, tagline_text, output_path):
    """
    Renderiza banner para Company Page.
    manifesto_words: lista de tuples [(palavra, "primary"|"signal"), ...]
    """
    img = Image.new("RGB", (WIDTH, HEIGHT), theme["bg"])
    draw = ImageDraw.Draw(img)

    fonts = {
        "eyebrow": ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), EYEBROW_SIZE),
        "manifesto": ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), MANIFESTO_SIZE),
        "tagline": ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), TAGLINE_SIZE),
    }

    color_map = {
        "primary": theme["primary"],
        "signal": theme["signal"],
    }
    manifesto_resolved = [(w, color_map[c]) for w, c in manifesto_words]

    # === Layout vertical ===
    # eyebrow (17) + gap (14) + manifesto (56) + gap (14) + tagline (20) = 121px
    # Centro vertical em 191 -> top margin ~35px
    if tagline_text:
        eyebrow_y = 26
        manifesto_y = 56
        tagline_y = 138
    else:
        # Sem tagline — centro do manifesto + eyebrow
        eyebrow_y = 50
        manifesto_y = 80
        tagline_y = None

    # === Eyebrow ===
    draw_tracked_text(
        draw, eyebrow_text, (SAFE_LEFT, eyebrow_y),
        fonts["eyebrow"], theme["secondary"], tracking_em=0.14,
    )

    # === Manifesto ===
    draw_manifesto(
        draw, manifesto_resolved, (SAFE_LEFT - 2, manifesto_y),
        fonts["manifesto"],
    )

    # === Tagline opcional ===
    if tagline_text:
        draw.text(
            (SAFE_LEFT, tagline_y), tagline_text,
            font=fonts["tagline"], fill=theme["secondary"],
        )

    img.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    # === DARK PT — versão FULL (com tagline) — recomendada ===
    out = render_company_banner(
        theme=DARK,
        eyebrow_text="RESEARCH · STUDIO · CAPITAL",
        manifesto_words=[
            ("Conteúdo.", "primary"),
            ("Construção.", "primary"),
            ("Capital.", "signal"),
        ],
        tagline_text="Análise editorial, alocação e construção na fronteira entre mercados e IA",
        output_path=str(OUT / "linkedin-company-pt-dark-full-1128x191.png"),
    )
    print(f"✓ Generated: {out}")

    # === DARK PT — versão MINIMAL (sem tagline) ===
    out = render_company_banner(
        theme=DARK,
        eyebrow_text="RESEARCH · STUDIO · CAPITAL",
        manifesto_words=[
            ("Conteúdo.", "primary"),
            ("Construção.", "primary"),
            ("Capital.", "signal"),
        ],
        tagline_text=None,
        output_path=str(OUT / "linkedin-company-pt-dark-minimal-1128x191.png"),
    )
    print(f"✓ Generated: {out}")

    # === DARK EN — versão FULL ===
    out = render_company_banner(
        theme=DARK,
        eyebrow_text="RESEARCH · STUDIO · CAPITAL",
        manifesto_words=[
            ("Content.", "primary"),
            ("Construction.", "primary"),
            ("Capital.", "signal"),
        ],
        tagline_text="Editorial research, allocation and construction at the frontier of markets and AI",
        output_path=str(OUT / "linkedin-company-en-dark-full-1128x191.png"),
    )
    print(f"✓ Generated: {out}")

    # === PAPER PT — versão FULL ===
    out = render_company_banner(
        theme=PAPER,
        eyebrow_text="RESEARCH · STUDIO · CAPITAL",
        manifesto_words=[
            ("Conteúdo.", "primary"),
            ("Construção.", "primary"),
            ("Capital.", "signal"),
        ],
        tagline_text="Análise editorial, alocação e construção na fronteira entre mercados e IA",
        output_path=str(OUT / "linkedin-company-pt-paper-full-1128x191.png"),
    )
    print(f"✓ Generated: {out}")


if __name__ == "__main__":
    main()
