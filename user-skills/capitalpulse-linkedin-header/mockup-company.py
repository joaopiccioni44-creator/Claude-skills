"""
Preview do banner Company Page com avatar logo overlaid.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE = Path(__file__).parent


def overlay_company_avatar(banner_path, output_path, avatar_size=160, avatar_x=24, avatar_y_offset=24):
    """
    Sobrepõe o avatar quadrado da Capital Pulse no bottom-left do banner.
    Avatar de Company Page é tipicamente quadrado com cantos arredondados.
    """
    banner = Image.open(banner_path).convert("RGBA")
    W, H = banner.size

    # Avatar overlap: começa a coberturar a partir de ~y=H-avatar_size+avatar_y_offset
    # e desce além do banner
    avatar_top = H - avatar_size + avatar_y_offset
    avatar_left = avatar_x
    avatar_right = avatar_x + avatar_size
    avatar_bottom = avatar_top + avatar_size

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Quadrado com cantos arredondados representando o logo
    radius = 16
    odraw.rounded_rectangle(
        (avatar_left, avatar_top, avatar_right, avatar_bottom),
        radius=radius,
        fill=(120, 120, 130, 220),
        outline=(255, 255, 255, 240),
        width=4,
    )

    # Texto "LOGO" no centro do avatar
    fonts_dir = BASE / "fonts"
    try:
        font = ImageFont.truetype(str(fonts_dir / "JetBrainsMono-Regular.ttf"), 14)
    except Exception:
        font = ImageFont.load_default()

    cx = (avatar_left + avatar_right) // 2
    cy = (avatar_top + avatar_bottom) // 2
    odraw.text((cx, cy), "LOGO", font=font, fill=(255, 255, 255, 230), anchor="mm")

    composed = Image.alpha_composite(banner, overlay)
    composed.convert("RGB").save(output_path, "PNG", optimize=True)
    return output_path


def main():
    out = overlay_company_avatar(
        str(BASE / "linkedin-company-pt-dark-full-1128x191.png"),
        str(BASE / "preview-company-pt-dark-full-with-avatar.png"),
    )
    print(f"✓ Preview com avatar: {out}")


if __name__ == "__main__":
    main()
