"""
Mockup comparativo das 3 opções de avatar Capital Pulse em contextos reais do LinkedIn.

Estrutura: matriz 3x3
  - Eixo X (colunas): opções A, B, C
  - Eixo Y (linhas): contextos
    1. Mobile feed (post card, avatar ~40px)
    2. Company Page header desktop (avatar ~144px)
    3. Listagem "Empresas para você" (avatar entre peers, ~80px)

Output: PNG horizontal 1800x2200 + PDF compilado para enviar via WhatsApp/email.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

BASE = Path(__file__).parent
FONTS = BASE / "fonts"
MARCA = Path("/sessions/intelligent-bold-allen/mnt/Imagens Capital Pulse/Marca")
OUT = MARCA / "mockup-avatares-decisao"

# === LinkedIn UI tokens ===
LK_BG = "#F4F2EE"  # LinkedIn light theme background
LK_CARD = "#FFFFFF"  # cards
LK_BORDER = "#E0DFDC"  # hairlines
LK_TEXT = "#000000"  # primary text
LK_TEXT_MUTED = "#666666"  # secondary text
LK_BLUE = "#0A66C2"  # LinkedIn blue (botão Seguir)

# === Brand tokens (referencia)
SIGNAL = "#5B3BFF"
INK_BG = "#0B0D12"

# === Layout ===
CANVAS_W = 1800
CANVAS_H = 2400
COL_GAP = 30
ROW_GAP = 50
PADDING = 60
HEADER_H = 220
CELL_W = (CANVAS_W - 2 * PADDING - 2 * COL_GAP) // 3
CELL_H = 580

# === Fonts ===
F_TITLE = lambda sz: ImageFont.truetype(str(FONTS / "Geist-SemiBold.ttf"), sz)
F_BODY = lambda sz: ImageFont.truetype(str(FONTS / "Geist-Regular.ttf"), sz)
F_MED = lambda sz: ImageFont.truetype(str(FONTS / "Geist-Medium.ttf"), sz)
F_MONO = lambda sz: ImageFont.truetype(str(FONTS / "JetBrainsMono-Regular.ttf"), sz)
F_ITALIC = lambda sz: ImageFont.truetype(str(FONTS / "InstrumentSerif-Italic.ttf"), sz)


def circle_crop(img):
    """Recorta imagem em círculo (para avatares circulares do feed mobile)."""
    img = img.convert("RGBA")
    size = min(img.size)
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask


def square_round(img, radius=20):
    """Quadrado com cantos arredondados (avatar de empresa no LinkedIn)."""
    img = img.convert("RGBA")
    size = min(img.size)
    img = img.resize((size, size), Image.LANCZOS)
    mask = rounded_rect_mask((size, size), radius)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def load_avatar(option_letter):
    """Carrega o avatar 400x400 da opção A/B/C."""
    files = {
        "A": "avatar-A-cream-on-dark-400x400.png",
        "B": "avatar-B-cream-on-violet-400x400.png",
        "C": "avatar-C-violet-on-dark-400x400.png",
    }
    return Image.open(MARCA / files[option_letter]).convert("RGBA")


# ============================================================
# Context 1: Mobile feed post card
# ============================================================
def render_mobile_feed(option_letter, cell_size):
    """Card de post do feed mobile com avatar pequeno."""
    w, h = cell_size
    card = Image.new("RGB", (w, h), LK_BG)
    draw = ImageDraw.Draw(card)

    # Card interno (post)
    card_padding = 20
    inner_w = w - 2 * card_padding
    inner_h = h - 2 * card_padding
    card_x = card_padding
    card_y = card_padding

    # Desenha card branco com bordas arredondadas
    card_mask = Image.new("RGBA", (inner_w, inner_h), (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card_mask)
    card_draw.rounded_rectangle(
        (0, 0, inner_w, inner_h),
        radius=12,
        fill=LK_CARD,
        outline=LK_BORDER,
        width=1,
    )
    card.paste(card_mask, (card_x, card_y), card_mask)
    draw = ImageDraw.Draw(card)

    # Avatar (circular em mobile feed) - tamanho realista do LinkedIn mobile: ~48px em 380px viewport
    # Escalar proporcionalmente para a cell
    avatar_size = int(w * 0.13)
    avatar_x = card_x + 30
    avatar_y = card_y + 30

    avatar = load_avatar(option_letter)
    avatar_circle = square_round(avatar, radius=8)  # LinkedIn usa cantos arredondados sutil para empresa
    avatar_circle = avatar_circle.resize((avatar_size, avatar_size), Image.LANCZOS)
    card_rgba = card.convert("RGBA")
    card_rgba.paste(avatar_circle, (avatar_x, avatar_y), avatar_circle)
    card = card_rgba.convert("RGB")
    draw = ImageDraw.Draw(card)

    # Nome + headline ao lado do avatar
    text_x = avatar_x + avatar_size + 16
    draw.text((text_x, avatar_y + 4), "Capital Pulse", font=F_TITLE(20), fill=LK_TEXT)
    draw.text((text_x, avatar_y + 30), "Venture studio AI-native · 1d", font=F_BODY(15), fill=LK_TEXT_MUTED)

    # Conteúdo do post
    body_y = avatar_y + avatar_size + 30
    body_lines = [
        "O ponto cego dos conselhos brasileiros:",
        "a leitura de IA ainda não chegou na sala",
        "onde as decisões nascem.",
        "",
        "Três pesquisas distintas convergem para",
        "a mesma realidade...",
    ]
    line_y = body_y
    for line in body_lines:
        draw.text((avatar_x, line_y), line, font=F_BODY(17), fill=LK_TEXT)
        line_y += 28

    # Footer com stats
    stats_y = h - card_padding - 50
    draw.text((avatar_x, stats_y), "👍 24 · 5 comentários", font=F_BODY(14), fill=LK_TEXT_MUTED)

    return card


# ============================================================
# Context 2: Company Page header desktop
# ============================================================
def render_company_header(option_letter, cell_size):
    """Header de Company Page com banner + avatar quadrado overlapping."""
    w, h = cell_size
    canvas = Image.new("RGB", (w, h), LK_BG)
    draw = ImageDraw.Draw(canvas)

    # Banner no topo (~40% da altura) — versão simplificada para focar no avatar
    banner_h = int(h * 0.42)
    banner = Image.new("RGB", (w, banner_h), INK_BG)
    bdraw = ImageDraw.Draw(banner)

    # Pequenos elementos visuais discretos pra parecer banner real sem competir
    # com o avatar (que é o foco)
    label_y = 30
    draw_tracked(bdraw, "CAPITAL PULSE · STUDIO · EDITORIAL · CAPITAL",
                 (40, label_y), F_MONO(12), "#A8AAB4", 0.14)

    # Linha discreta de manifesto pequeno
    bdraw.text((40, banner_h - 60),
               "Venture studio brasileiro AI-native",
               font=F_ITALIC(16), fill="#A8AAB4")

    canvas.paste(banner, (0, 0))
    draw = ImageDraw.Draw(canvas)

    # Card branco abaixo do banner
    card_top = banner_h
    draw.rectangle((0, card_top, w, h), fill=LK_CARD)
    draw.line((0, h - 1, w, h - 1), fill=LK_BORDER, width=1)

    # Avatar quadrado overlapping (LinkedIn padrão ~144px em desktop)
    avatar_size = int(w * 0.20)
    avatar_x = 40
    avatar_y = banner_h - avatar_size // 2

    # Background branco atrás do avatar (border)
    border = 6
    draw.rounded_rectangle(
        (avatar_x - border, avatar_y - border,
         avatar_x + avatar_size + border, avatar_y + avatar_size + border),
        radius=16, fill=LK_CARD,
    )

    avatar = load_avatar(option_letter)
    avatar_rounded = square_round(avatar, radius=12)
    avatar_rounded = avatar_rounded.resize((avatar_size, avatar_size), Image.LANCZOS)
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(avatar_rounded, (avatar_x, avatar_y), avatar_rounded)
    canvas = canvas_rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # Nome empresa
    name_y = avatar_y + avatar_size + 16
    draw.text((avatar_x, name_y), "Capital Pulse", font=F_TITLE(28), fill=LK_TEXT)
    draw.text((avatar_x, name_y + 40),
              "Venture studio brasileiro AI-native",
              font=F_BODY(15), fill=LK_TEXT_MUTED)
    draw.text((avatar_x, name_y + 62),
              "São Paulo · 482 seguidores",
              font=F_BODY(13), fill=LK_TEXT_MUTED)

    # Botão "Seguir" mock
    btn_x = w - 130
    btn_y = name_y + 30
    draw.rounded_rectangle(
        (btn_x, btn_y, btn_x + 90, btn_y + 32),
        radius=16, fill=LK_BLUE,
    )
    draw.text((btn_x + 28, btn_y + 6), "Seguir", font=F_MED(14), fill="#FFFFFF")

    return canvas


# ============================================================
# Context 3: Lista "Empresas para você" com peers
# ============================================================
def render_peer_list(option_letter, cell_size):
    """Listagem de empresas mostrando Capital Pulse entre peers do nicho."""
    w, h = cell_size
    canvas = Image.new("RGB", (w, h), LK_BG)
    draw = ImageDraw.Draw(canvas)

    # Card branco principal
    card_padding = 20
    inner_w = w - 2 * card_padding
    inner_h = h - 2 * card_padding
    draw.rounded_rectangle(
        (card_padding, card_padding, w - card_padding, h - card_padding),
        radius=12, fill=LK_CARD, outline=LK_BORDER, width=1,
    )

    # Header da listagem
    title_y = card_padding + 20
    draw.text((card_padding + 24, title_y),
              "Empresas que você pode seguir",
              font=F_TITLE(17), fill=LK_TEXT)

    # 4 peers + Capital Pulse no meio
    peers = [
        ("Avenue Securities", "#1B3A57", "AS", "Investimentos internacionais"),
        ("Bossa Invest", "#FF6B35", "BI", "Venture capital · Brasil"),
        ("__CAPITAL_PULSE__", None, None, "Venture studio brasileiro AI-native"),
        ("GV Angels", "#003B71", "GV", "Investidores anjo"),
        ("StartSe", "#FFD500", "SS", "Educação executiva"),
    ]

    row_h = 78
    row_y = title_y + 50
    avatar_size = 56

    for i, (name, color, initials, desc) in enumerate(peers):
        avatar_x = card_padding + 24
        ay = row_y + i * row_h

        if name == "__CAPITAL_PULSE__":
            # Avatar Capital Pulse (a opção sendo testada)
            avatar = load_avatar(option_letter)
            avatar_rounded = square_round(avatar, radius=8)
            avatar_rounded = avatar_rounded.resize((avatar_size, avatar_size), Image.LANCZOS)
            canvas_rgba = canvas.convert("RGBA")
            canvas_rgba.paste(avatar_rounded, (avatar_x, ay), avatar_rounded)
            canvas = canvas_rgba.convert("RGB")
            draw = ImageDraw.Draw(canvas)

            # Destacar essa linha com leve highlight
            highlight_rect = (
                avatar_x - 8, ay - 4,
                w - card_padding - 16, ay + avatar_size + 4,
            )
            # Faz um retângulo translúcido — usa overlay
            overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.rounded_rectangle(
                highlight_rect, radius=8,
                fill=(91, 59, 255, 25),  # signal violet com alpha
            )
            canvas_rgba = canvas.convert("RGBA")
            canvas_rgba = Image.alpha_composite(canvas_rgba, overlay)
            canvas = canvas_rgba.convert("RGB")
            draw = ImageDraw.Draw(canvas)

            # Re-cola o avatar por cima do highlight
            canvas_rgba = canvas.convert("RGBA")
            canvas_rgba.paste(avatar_rounded, (avatar_x, ay), avatar_rounded)
            canvas = canvas_rgba.convert("RGB")
            draw = ImageDraw.Draw(canvas)

            display_name = "Capital Pulse"
            text_color = LK_TEXT
        else:
            # Avatar placeholder colorido com iniciais
            avatar_box = (avatar_x, ay, avatar_x + avatar_size, ay + avatar_size)
            draw.rounded_rectangle(avatar_box, radius=8, fill=color)
            # Iniciais
            text_color_w = "#FFFFFF" if color != "#FFD500" else "#000000"
            bbox = draw.textbbox((0, 0), initials, font=F_TITLE(22))
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            draw.text(
                (avatar_x + (avatar_size - tw) // 2,
                 ay + (avatar_size - th) // 2 - 3),
                initials, font=F_TITLE(22), fill=text_color_w,
            )
            display_name = name
            text_color = LK_TEXT

        # Nome + descrição
        text_x = avatar_x + avatar_size + 16
        draw.text((text_x, ay + 6), display_name, font=F_MED(16), fill=text_color)
        draw.text((text_x, ay + 28), desc, font=F_BODY(13), fill=LK_TEXT_MUTED)

        # Botão Seguir/+ pequeno à direita
        btn_x = w - card_padding - 50
        btn_y = ay + avatar_size // 2 - 14
        draw.rounded_rectangle((btn_x, btn_y, btn_x + 28, btn_y + 28),
                               radius=14, outline=LK_BORDER, width=1)
        draw.text((btn_x + 9, btn_y + 6), "+", font=F_BODY(18), fill=LK_TEXT)

    return canvas


# ============================================================
# Mockup composer — matriz 3x3
# ============================================================
def render_mockup_grid():
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), "#FFFFFF")
    draw = ImageDraw.Draw(canvas)

    # === Header ===
    title_y = 60
    draw.text((PADDING, title_y), "Decisão de avatar — Capital Pulse",
              font=F_TITLE(34), fill=LK_TEXT)
    draw.text((PADDING, title_y + 50),
              "Três opções de logomarca testadas em três contextos reais do LinkedIn.",
              font=F_ITALIC(20), fill=LK_TEXT_MUTED)
    draw.text((PADDING, title_y + 90),
              "Leitura sugerida: comparar cada coluna (A, B, C) verticalmente.",
              font=F_BODY(15), fill=LK_TEXT_MUTED)

    # === Column headers (opções A, B, C) ===
    col_y = HEADER_H - 50
    col_labels = [
        ("A · CREAM / DARK", "Continua a paleta atual"),
        ("B · CREAM / VIOLET", "Punch máximo"),
        ("C · VIOLET / DARK", "Accent invertido (sugestão)"),
    ]
    for i, (label, sub) in enumerate(col_labels):
        x = PADDING + i * (CELL_W + COL_GAP) + 24
        draw_tracked(draw, label, (x, col_y), F_MONO(18),
                     "#5B3BFF" if i == 2 else LK_TEXT, 0.12)
        draw.text((x, col_y + 32), sub, font=F_ITALIC(19), fill=LK_TEXT_MUTED)

    # === Grid 3 contexts x 3 options ===
    contexts = [
        ("01 · Mobile feed (avatar ~40px)", render_mobile_feed),
        ("02 · Company Page header (avatar ~144px)", render_company_header),
        ("03 · Listagem entre peers (avatar ~56px)", render_peer_list),
    ]

    grid_top = HEADER_H + 30
    row_label_h = 36

    for row_idx, (ctx_label, render_fn) in enumerate(contexts):
        row_y = grid_top + row_idx * (CELL_H + ROW_GAP + row_label_h)

        # Row label (mono)
        draw_tracked(draw, ctx_label, (PADDING, row_y),
                     F_MONO(13), LK_TEXT_MUTED, 0.10)

        # 3 cells in this row
        for col_idx, opt in enumerate(["A", "B", "C"]):
            cell_x = PADDING + col_idx * (CELL_W + COL_GAP)
            cell_y = row_y + row_label_h
            cell = render_fn(opt, (CELL_W, CELL_H))
            canvas.paste(cell, (cell_x, cell_y))

    # === Footer ===
    footer_y = CANVAS_H - 80
    draw.line((PADDING, footer_y - 20, CANVAS_W - PADDING, footer_y - 20),
              fill="#E0DFDC", width=1)
    draw.text((PADDING, footer_y),
              "Capital Pulse · Decisão de marca · mai 2026",
              font=F_MONO(13), fill=LK_TEXT_MUTED)

    return canvas


def draw_tracked(draw, text, pos, font, color, tracking_em):
    x, y = pos
    font_size = font.size if hasattr(font, "size") else 13
    extra = font_size * tracking_em
    for ch in text:
        draw.text((x, y), ch, font=font, fill=color)
        bbox = draw.textbbox((0, 0), ch, font=font)
        x += (bbox[2] - bbox[0]) + extra


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    img = render_mockup_grid()
    png_path = OUT / "mockup-avatares-decisao.png"
    img.save(png_path, "PNG", optimize=True)
    print(f"✓ PNG: {png_path}")

    # Também salva como PDF para envio fácil via WhatsApp/email
    pdf_path = OUT / "mockup-avatares-decisao.pdf"
    img.save(pdf_path, "PDF", resolution=144.0)
    print(f"✓ PDF: {pdf_path}")


if __name__ == "__main__":
    main()
