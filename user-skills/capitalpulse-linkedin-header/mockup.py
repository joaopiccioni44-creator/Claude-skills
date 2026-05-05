"""
Mockup do header com profile photo overlay simulado.
Mostra como o banner vai aparecer no LinkedIn real, com a foto cobrindo
o bottom-left.
"""
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE


def overlay_profile_photo(banner_path, output_path, photo_diameter=224, photo_x=88, photo_y_offset=82):
    """
    Pega um banner 1584x396 e desenha um círculo cinza simulando onde
    a profile photo vai cobrir.

    Coordenadas baseadas em LinkedIn 2026 desktop:
    - Banner ocupa fullbleed
    - Profile photo é circular ~224px diameter no perfil real
    - Foto fica posicionada com center_x ~200 e center_y na metade da
      borda inferior do banner (sobe ~50% pra dentro)
    """
    banner = Image.open(banner_path).convert("RGBA")
    W, H = banner.size

    # Photo center: aproximação do perfil LinkedIn
    photo_center_x = photo_x + photo_diameter // 2
    photo_center_y = H - photo_y_offset  # parcialmente dentro do banner, parcialmente fora

    # Cria mockup mostrando a área coberta
    mockup = banner.copy()
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Desenha um círculo cinza semi-transparente representando a foto
    photo_bbox = (
        photo_center_x - photo_diameter // 2,
        photo_center_y - photo_diameter // 2,
        photo_center_x + photo_diameter // 2,
        photo_center_y + photo_diameter // 2,
    )
    # Círculo de borda branca pra demarcar
    odraw.ellipse(photo_bbox, fill=(120, 120, 130, 200), outline=(255, 255, 255, 255), width=4)

    # Texto "PHOTO" no centro do círculo
    from PIL import ImageFont
    fonts_dir = BASE / "fonts"
    try:
        font = ImageFont.truetype(str(fonts_dir / "JetBrainsMono-Regular.ttf"), 18)
    except Exception:
        font = ImageFont.load_default()
    odraw.text(
        (photo_center_x, photo_center_y),
        "PHOTO",
        font=font,
        fill=(255, 255, 255, 230),
        anchor="mm",
    )

    composed = Image.alpha_composite(mockup, overlay)
    composed.convert("RGB").save(output_path, "PNG", optimize=True)
    return output_path


def crop_to_mobile_safe(banner_path, output_path):
    """
    Simula como o banner vai aparecer em mobile (crop ~60% central).
    """
    banner = Image.open(banner_path).convert("RGB")
    W, H = banner.size

    # Mobile crop: ~60% central horizontal
    crop_width = int(W * 0.60)
    left = (W - crop_width) // 2
    right = left + crop_width

    cropped = banner.crop((left, 0, right, H))
    cropped.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    # Mockup com profile photo overlay (versão recomendada)
    out = overlay_profile_photo(
        str(OUT / "linkedin-header-pt-dark-full-1584x396.png"),
        str(OUT / "preview-pt-dark-full-with-photo.png"),
    )
    print(f"✓ Preview com foto: {out}")

    out = overlay_profile_photo(
        str(OUT / "linkedin-header-pt-dark-minimal-1584x396.png"),
        str(OUT / "preview-pt-dark-minimal-with-photo.png"),
    )
    print(f"✓ Preview com foto (minimal): {out}")

    # Mobile crop simulation (versão recomendada)
    out = crop_to_mobile_safe(
        str(OUT / "linkedin-header-pt-dark-full-1584x396.png"),
        str(OUT / "preview-pt-dark-full-mobile-crop.png"),
    )
    print(f"✓ Preview mobile crop: {out}")


if __name__ == "__main__":
    main()
