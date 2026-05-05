"""
Capital Pulse — Carrossel LinkedIn (6 slides 1080x1350)
Post inauguração sub-thread MasterBoard / Defasagem AI Fluency

Reusa tokens e fontes dos banners (Sistema Signal v1).
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE = Path(__file__).parent
FONTS = BASE / "fonts"
LOGO = BASE / "logo"
OUT = BASE / "carousel"

# === Canvas (LinkedIn document portrait 4:5) ===
WIDTH = 1080
HEIGHT = 1350

# === Brand tokens ===
DARK = {
    "bg": "#0B0D12",
    "primary": "#F2F1EB",
    "secondary": "#A8AAB4",
    "tertiary": "#6B6E78",
    "signal": "#5B3BFF",
    "hairline": "#2A2E38",
}

# === Layout ===
MARGIN_X = 90
MARGIN_TOP = 110
MARGIN_BOTTOM = 110

# === Tipografia base ===
FONT_EYEBROW = lambda: ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), 22)
FONT_MASTHEAD_LG = lambda: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 76)
FONT_MASTHEAD_MD = lambda: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 60)
FONT_MASTHEAD_SM = lambda: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 44)
FONT_NUMBER = lambda: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 124)
FONT_NUMBER_SM = lambda: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), 88)
FONT_BODY = lambda: ImageFont.truetype(str(FONTS / "Geist-Regular.ttf"), 28)
FONT_BODY_LG = lambda: ImageFont.truetype(str(FONTS / "Geist-Medium.ttf"), 36)
FONT_TAGLINE = lambda: ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), 36)
FONT_TAGLINE_SM = lambda: ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), 28)
FONT_SOURCE = lambda: ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), 17)
FONT_PAGE_NUM = lambda: ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), 17)


def draw_tracked_text(draw, text, position, font, color, tracking_em=0.0):
    """Texto com tracking manual."""
    x, y = position
    font_size = font.size if hasattr(font, "size") else 22
    extra = font_size * tracking_em
    for char in text:
        draw.text((x, y), char, font=font, fill=color)
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        x += char_width + extra
    return x


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def draw_multicolor_line(draw, words_with_colors, position, font, gap_extra=0):
    """Desenha uma linha com palavras coloridas distintas."""
    x, y = position
    for i, (word, color) in enumerate(words_with_colors):
        draw.text((x, y), word, font=font, fill=color)
        bbox = draw.textbbox((0, 0), word, font=font)
        word_width = bbox[2] - bbox[0]
        if i < len(words_with_colors) - 1:
            space_width = text_width(draw, " ", font) + gap_extra
            x += word_width + space_width
        else:
            x += word_width
    return x


def composite_logo(canvas, theme, logo_height=44, margin=64):
    """Logo no canto inferior direito — pequeno e discreto."""
    logo_path = LOGO / "wordmark-cream.png"
    logo = Image.open(logo_path).convert("RGBA")
    aspect = logo.width / logo.height
    new_h = logo_height
    new_w = int(new_h * aspect)
    logo = logo.resize((new_w, new_h), Image.LANCZOS)
    x = canvas.width - new_w - margin
    y = canvas.height - new_h - margin
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(logo, (x, y), logo)
    return canvas_rgba.convert("RGB")


def draw_page_indicator(draw, page_num, total, theme):
    """Indicador de página no canto inferior esquerdo."""
    text = f"{page_num:02d} / {total:02d}"
    draw_tracked_text(
        draw, text, (MARGIN_X, HEIGHT - MARGIN_BOTTOM + 30),
        FONT_PAGE_NUM(), theme["tertiary"], tracking_em=0.14,
    )


def draw_eyebrow(draw, text, theme, y=MARGIN_TOP):
    """Eyebrow uppercase tracked no topo."""
    draw_tracked_text(
        draw, text, (MARGIN_X, y),
        FONT_EYEBROW(), theme["secondary"], tracking_em=0.14,
    )


def base_canvas(theme):
    """Cria canvas base com background."""
    return Image.new("RGB", (WIDTH, HEIGHT), theme["bg"])


# ============================================================
# SLIDE 1 — Hook visual
# ============================================================

def render_slide_1(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "CAPITAL PULSE · TESE", theme)

    # Manifesto principal — 3 linhas, com violet em "ponto cego"
    masthead_y = 380
    line_height = 96

    # Linha 1: "O ponto cego" — "ponto cego" em violet
    draw_multicolor_line(
        draw,
        [("O", theme["primary"]), ("ponto", theme["signal"]), ("cego", theme["signal"])],
        (MARGIN_X, masthead_y),
        FONT_MASTHEAD_LG(),
    )
    # Linha 2: "dos conselhos"
    draw.text((MARGIN_X, masthead_y + line_height), "dos conselhos", font=FONT_MASTHEAD_LG(), fill=theme["primary"])
    # Linha 3: "brasileiros."
    draw.text((MARGIN_X, masthead_y + line_height * 2), "brasileiros.", font=FONT_MASTHEAD_LG(), fill=theme["primary"])

    # Tagline
    tagline_y = masthead_y + line_height * 3 + 50
    draw.text(
        (MARGIN_X, tagline_y),
        "Por que a leitura de IA ainda não",
        font=FONT_TAGLINE(), fill=theme["secondary"],
    )
    draw.text(
        (MARGIN_X, tagline_y + 50),
        "chegou na sala onde se decide.",
        font=FONT_TAGLINE(), fill=theme["secondary"],
    )

    draw_page_indicator(draw, 1, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# SLIDE 2 — Três pesquisas convergem
# ============================================================

def render_slide_2(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "EVIDÊNCIA · TRÊS PESQUISAS BRASILEIRAS", theme)

    # Título compacto: uma linha só, violet
    draw.text((MARGIN_X, 175), "Convergem.", font=FONT_MASTHEAD_LG(), fill=theme["signal"])

    # Hairline
    draw.line(
        [(MARGIN_X, 295), (WIDTH - MARGIN_X, 295)],
        fill=theme["hairline"], width=1,
    )

    # Block 1 — Meta + FDC
    block_y = 325
    draw.text((MARGIN_X, block_y), "74%", font=FONT_NUMBER_SM(), fill=theme["signal"])
    draw.text((MARGIN_X, block_y + 95), "sem gestão estruturada", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, block_y + 137), "de risco em IA.", font=FONT_BODY_LG(), fill=theme["primary"])
    draw_tracked_text(
        draw, "META + FUNDAÇÃO DOM CABRAL · 100 PRESIDENTES",
        (MARGIN_X, block_y + 195),
        FONT_SOURCE(), theme["tertiary"], tracking_em=0.10,
    )

    # Hairline
    draw.line(
        [(MARGIN_X, block_y + 240), (WIDTH - MARGIN_X, block_y + 240)],
        fill=theme["hairline"], width=1,
    )

    # Block 2 — ABRASCA
    block_y_2 = block_y + 270
    draw.text((MARGIN_X, block_y_2), "23%", font=FONT_NUMBER_SM(), fill=theme["signal"])
    draw.text((MARGIN_X, block_y_2 + 95), "têm diretrizes formais", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, block_y_2 + 137), "de governança de IA.", font=FONT_BODY_LG(), fill=theme["primary"])
    draw_tracked_text(
        draw, "ABRASCA · COMPANHIAS DE CAPITAL ABERTO",
        (MARGIN_X, block_y_2 + 195),
        FONT_SOURCE(), theme["tertiary"], tracking_em=0.10,
    )

    # Hairline
    draw.line(
        [(MARGIN_X, block_y_2 + 240), (WIDTH - MARGIN_X, block_y_2 + 240)],
        fill=theme["hairline"], width=1,
    )

    # Block 3 — IBGC
    block_y_3 = block_y_2 + 270
    draw.text((MARGIN_X, block_y_3), "3 temas", font=FONT_NUMBER_SM(), fill=theme["signal"])
    draw.text((MARGIN_X, block_y_3 + 95), "em que conselheiros se sentem", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, block_y_3 + 137), "menos preparados — IA é um deles.", font=FONT_BODY_LG(), fill=theme["primary"])
    draw_tracked_text(
        draw, "IBGC · PERSPECTIVAS 2025 · 349 RESPONDENTES",
        (MARGIN_X, block_y_3 + 195),
        FONT_SOURCE(), theme["tertiary"], tracking_em=0.10,
    )

    draw_page_indicator(draw, 2, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# SLIDE 3 — O insight cruzado
# ============================================================

def render_slide_3(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "DIAGNÓSTICO", theme)

    # Estrutura: 3 afirmações em acumulação + 1 conclusão em violet (sem calque do inglês)
    y = 290
    line_h = 96

    draw.text((MARGIN_X, y), "Há capital.", font=FONT_MASTHEAD_LG(), fill=theme["secondary"])
    draw.text((MARGIN_X, y + line_h), "Há ferramenta.", font=FONT_MASTHEAD_LG(), fill=theme["secondary"])
    draw.text((MARGIN_X, y + line_h * 2), "Há mão de obra.", font=FONT_MASTHEAD_LG(), fill=theme["secondary"])

    # Pulo + statement positivo em violet
    y_positive = y + line_h * 3 + 70
    draw.text((MARGIN_X, y_positive), "Falta leitura", font=FONT_MASTHEAD_LG(), fill=theme["signal"])
    draw.text((MARGIN_X, y_positive + line_h), "no nível da decisão.", font=FONT_MASTHEAD_LG(), fill=theme["signal"])

    # Tagline contextual
    tagline_y = y_positive + line_h * 2 + 60
    draw.text(
        (MARGIN_X, tagline_y),
        "Quando a sala do conselho não lê a fronteira,",
        font=FONT_TAGLINE_SM(), fill=theme["secondary"],
    )
    draw.text(
        (MARGIN_X, tagline_y + 38),
        "a empresa fica refém da inércia.",
        font=FONT_TAGLINE_SM(), fill=theme["secondary"],
    )

    draw_page_indicator(draw, 3, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# SLIDE 4 — As três trajetórias
# ============================================================

def render_slide_4(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "TRÊS TRAJETÓRIAS · ACCENTURE", theme)

    draw.text((MARGIN_X, 200), "A escolha nasce", font=FONT_MASTHEAD_MD(), fill=theme["primary"])
    draw.text((MARGIN_X, 268), "na sala do conselho.", font=FONT_MASTHEAD_MD(), fill=theme["primary"])

    # Hairline
    draw.line(
        [(MARGIN_X, 380), (WIDTH - MARGIN_X, 380)],
        fill=theme["hairline"], width=1,
    )

    # Três trajetórias empilhadas
    y_base = 430
    block_h = 230

    # Tradicional
    y1 = y_base
    draw.text((MARGIN_X, y1), "01.", font=FONT_BODY_LG(), fill=theme["tertiary"])
    draw.text((MARGIN_X + 100, y1 - 8), "Tradicional", font=FONT_MASTHEAD_SM(), fill=theme["secondary"])
    draw.text((MARGIN_X + 100, y1 + 56), "IA como ferramenta isolada.", font=FONT_BODY(), fill=theme["tertiary"])

    # Evolução
    y2 = y_base + block_h
    draw.text((MARGIN_X, y2), "02.", font=FONT_BODY_LG(), fill=theme["tertiary"])
    draw.text((MARGIN_X + 100, y2 - 8), "Evolução", font=FONT_MASTHEAD_SM(), fill=theme["primary"])
    draw.text((MARGIN_X + 100, y2 + 56), "Otimização de processo existente.", font=FONT_BODY(), fill=theme["secondary"])

    # Reinvenção (em violet — onde compounding acontece)
    y3 = y_base + block_h * 2
    draw.text((MARGIN_X, y3), "03.", font=FONT_BODY_LG(), fill=theme["signal"])
    draw.text((MARGIN_X + 100, y3 - 8), "Reinvenção", font=FONT_MASTHEAD_SM(), fill=theme["signal"])
    draw.text((MARGIN_X + 100, y3 + 56), "Modelo de negócio reescrito.", font=FONT_BODY(), fill=theme["primary"])

    # Tagline
    tagline_y = y_base + block_h * 3 + 30
    draw.text(
        (MARGIN_X, tagline_y),
        "Sem leitura na sala, a empresa estaciona em Tradicional ou Evolução.",
        font=FONT_TAGLINE_SM(), fill=theme["secondary"],
    )

    draw_page_indicator(draw, 4, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# SLIDE 5 — Fiduciary duty
# ============================================================

def render_slide_5(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "O QUE ESTÁ EM JOGO · DEVER FIDUCIÁRIO EMERGENTE", theme)

    draw.text((MARGIN_X, 200), "Não é mais", font=FONT_MASTHEAD_LG(), fill=theme["primary"])
    draw_multicolor_line(
        draw,
        [("opcional.", theme["signal"])],
        (MARGIN_X, 296),
        FONT_MASTHEAD_LG(),
    )

    # Hairline
    draw.line(
        [(MARGIN_X, 440), (WIDTH - MARGIN_X, 440)],
        fill=theme["hairline"], width=1,
    )

    # Três pontos
    y = 490
    line_gap = 200

    # 1
    draw_tracked_text(draw, "LEI DE IA DA UE · ARTIGO 4", (MARGIN_X, y),
                      FONT_SOURCE(), theme["tertiary"], tracking_em=0.10)
    draw.text((MARGIN_X, y + 30), "Literacia em IA é obrigação", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y + 72), "para diretores, com regimes", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y + 114), "de responsabilização acionados.", font=FONT_BODY_LG(), fill=theme["primary"])

    # 2
    y2 = y + line_gap
    draw_tracked_text(draw, "OXFORD LAW BLOGS · JAN 2026", (MARGIN_X, y2),
                      FONT_SOURCE(), theme["tertiary"], tracking_em=0.10)
    draw.text((MARGIN_X, y2 + 30), "Dois novos deveres fiduciários:", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y2 + 72), "“AI due care” + “AI loyalty oversight”.", font=FONT_BODY_LG(), fill=theme["signal"])

    # 3 — global benchmark
    y3 = y2 + line_gap
    draw_tracked_text(draw, "DELOITTE 2026 · REFERÊNCIA GLOBAL", (MARGIN_X, y3),
                      FONT_SOURCE(), theme["tertiary"], tracking_em=0.10)
    draw.text((MARGIN_X, y3 + 30), "79% dos conselhos globais —", font=FONT_BODY_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y3 + 72), "conhecimento limitado em IA.", font=FONT_BODY_LG(), fill=theme["primary"])

    draw_page_indicator(draw, 5, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# SLIDE 6 — CTA + janela
# ============================================================

def render_slide_6(theme):
    img = base_canvas(theme)
    draw = ImageDraw.Draw(img)

    draw_eyebrow(draw, "JANELA · 12-18 MESES", theme)

    # Manifesto
    y = 240
    line_h = 92
    draw.text((MARGIN_X, y), "Quem se mover", font=FONT_MASTHEAD_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y + line_h), "agora,", font=FONT_MASTHEAD_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y + line_h * 2), "captura", font=FONT_MASTHEAD_LG(), fill=theme["primary"])
    draw.text((MARGIN_X, y + line_h * 3), "Reinvenção.", font=FONT_MASTHEAD_LG(), fill=theme["signal"])

    # Subtext em italic
    sub_y = y + line_h * 4 + 30
    draw.text(
        (MARGIN_X, sub_y),
        "Os que esperarem o consenso vão alcançar",
        font=FONT_TAGLINE_SM(), fill=theme["secondary"],
    )
    draw.text(
        (MARGIN_X, sub_y + 38),
        "Evolução tarde demais para destravar ganho composto.",
        font=FONT_TAGLINE_SM(), fill=theme["secondary"],
    )

    # Hairline
    cta_y_anchor = sub_y + 130
    draw.line(
        [(MARGIN_X, cta_y_anchor), (WIDTH - MARGIN_X, cta_y_anchor)],
        fill=theme["hairline"], width=1,
    )

    # CTA
    cta_y = cta_y_anchor + 35
    draw_tracked_text(
        draw, "FUNDADOR · ALTA LIDERANÇA · CONSELHEIRO",
        (MARGIN_X, cta_y),
        FONT_SOURCE(), theme["tertiary"], tracking_em=0.14,
    )
    draw.text(
        (MARGIN_X, cta_y + 35),
        "Vendo essa defasagem?",
        font=FONT_BODY_LG(), fill=theme["primary"],
    )
    draw.text(
        (MARGIN_X, cta_y + 80),
        "Vamos conversar.",
        font=FONT_BODY_LG(), fill=theme["signal"],
    )

    draw_page_indicator(draw, 6, 6, theme)
    img = composite_logo(img, theme)
    return img


# ============================================================
# Main
# ============================================================

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    slides = [
        ("slide-1-hook", render_slide_1(DARK)),
        ("slide-2-pesquisas", render_slide_2(DARK)),
        ("slide-3-insight", render_slide_3(DARK)),
        ("slide-4-trajetorias", render_slide_4(DARK)),
        ("slide-5-fiduciary", render_slide_5(DARK)),
        ("slide-6-cta", render_slide_6(DARK)),
    ]

    images_for_pdf = []
    for name, img in slides:
        png_path = OUT / f"{name}.png"
        img.save(png_path, "PNG", optimize=True)
        print(f"✓ {png_path}")
        images_for_pdf.append(img)

    # Compilar PDF
    pdf_path = OUT / "carrossel-conselhos-ai-fluency.pdf"
    images_for_pdf[0].save(
        pdf_path,
        save_all=True,
        append_images=images_for_pdf[1:],
        resolution=144.0,
    )
    print(f"\n✓ PDF: {pdf_path}")


if __name__ == "__main__":
    main()
