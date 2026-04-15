
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

This project is intended to run from a local virtual environment stored in `.venv/`.

1. Create the virtual environment:

```bash
python -m venv .venv
```

2. Activate it:

```bash
# Windows (Command Prompt)
.venv\Scripts\activate

# Windows (Git Bash)
source .venv/Scripts/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

If `.venv` does not exist, `run_watermark.bat` falls back to the Python interpreter available in your global `PATH`.

## Usage

1. Place images in the `input/` folder
2. Add `logo_transparente.png` and `arial.ttf` to the project root
3. Run the watermark script from the activated `.venv`:

```bash
python main.py
```

On Windows, you can also use:

```bat
run_watermark.bat
```

The batch file will use `.venv\Scripts\python.exe` when `.venv` exists, and only fall back to the global `python` command when `.venv` is missing.

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
├── .venv/               # local virtual environment (created locally)
├── input/
└── output/
```
