import os
import glob
from PIL import Image, ImageDraw, ImageFont


def add_logo_watermark(base_image, logo_path, logo_opacity=100, position=(10, 10)):
    logo = Image.open(logo_path).convert("RGBA")
    width, height = base_image.size
    position = (position[0], position[1] + height - 100)
    logo_height = int(height * 0.08)
    logo_width = int(logo.width * logo_height / logo.height)
    logo = logo.resize((logo_width, logo_height))

    if logo_opacity < 255:
        alpha = logo.split()[3]
        alpha = alpha.point(lambda p: p * logo_opacity // 255)
        logo.putalpha(alpha)

    base_image.paste(logo, position, logo)
    return base_image


if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    logo_path = "logo_transparente.png"
    font_path = "arial.ttf"
    text = "Imagem meramente ilustrativa"
    opacity = 120
    angle = 40
    logo_opacity = 170

    os.makedirs(output_folder, exist_ok=True)
    image_extensions = ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.tiff", "*.gif")
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(input_folder, ext)))

    for image_path in image_files:
        filename = os.path.basename(image_path)
        output_path = os.path.join(output_folder, filename)
        base = Image.open(image_path).convert("RGBA")
        # Add logo
        base_with_logo = add_logo_watermark(base, logo_path, logo_opacity)
        # Add diagonal text
        final_image = base_with_logo
        final_image.convert("RGB").save(output_path)
        print(f"✅ Marca d'água salva: {output_path}")
