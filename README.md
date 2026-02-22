
# Python Watermark

A Python tool to add watermarks to images with both logo and diagonal text overlays.

## Features

- Add transparent logo watermarks to images
- Add diagonal text watermarks with custom opacity and rotation
- Support for multiple image formats (PNG, JPG, JPEG, BMP, TIFF, GIF)
- Batch processing of images from input folder

## Requirements

- Python 3.x
- Pillow 11.3.0

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Place images in the `input/` folder
2. Add `logo_transparente.png` and `arial.ttf` to the project root
3. Run the watermark script:

```bash
python main.py
```

Watermarked images will be saved to the `output/` folder.

## Configuration

Edit `watermark.py` to customize:

- `text`: Watermark text
- `opacity`: Text opacity (0-255)
- `angle`: Text rotation angle
- `logo_opacity`: Logo opacity (0-255)
- `font_path`: Path to TTF font file

## Project Structure

```
python-watermark/
├── main.py
├── watermark.py
├── watermark_logo.py
├── requirements.txt
├── input/
└── output/
```
