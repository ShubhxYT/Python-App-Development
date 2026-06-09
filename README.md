# Python App Development
> My first attempt at desktop GUI apps with PyQt5 — a calculator, an image editor, and a lesson in what I don't enjoy building

## What I Built It For
I wanted to build something with a real window — buttons you could click, something that felt like an application instead of a terminal. So I tried PyQt5. Built a calculator and an image editor with undo/redo. Dropped it after 4 days. Desktop GUI development wasn't for me — the widget hierarchy and layout managers felt like fighting the framework. Committed the entire venv to the repo by accident (rookie mistake). But it taught me something important: not every technology is for you, and that's okay. I moved on to Streamlit and it felt like breathing by comparison.

## What It Does
- Calculator with grid-based button layout, expression evaluation, dark theme
- Image editor with folder browsing, 8 transformations (rotate, mirror, grayscale, blur, contrast, saturation, sharpness, reset)
- Undo/redo system using a stack pattern — each transform pushes state, undo pops it back
- Random word generator — 3 columns, click to randomize, reset to clear

## Tech Stack
- Python 3
- PyQt5 (widgets, signal-slot event handling, layout management)
- Pillow (image processing: transforms, filters, enhancement)
- Standard library only otherwise

## How to Run
1. Install dependencies:
```
pip install PyQt5 Pillow
```
2. Run any script:
```
python calculator.py
python image_editor_improved.py
python random-word-gen.py
```
3. For the image editor, click "Select Folder" and pick a folder with .png/.jpg/.jpeg images
