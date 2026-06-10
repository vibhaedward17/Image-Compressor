Image Compressor

A simple image compression tool built with Python and Pillow.

Requirements

->Python 3.x

->Pillow

Install Pillow with:

-> pip install pillow

How to Run

-> python image_compressor.py

Usage

-> A file dialog opens → select an image file

-> The image is resized and converted to RGB

-> A save dialog opens → choose where to save

-> Compressed image is saved as compressed.jpg


Features

→ Supports images with transparency (converts RGBA to RGB)

→ Saves output as JPEG format

→ Uses high-quality LANCZOS resampling


Limitations

✗ Output is always saved as .jpg

✗ No custom resize dimensions — keeps original size

✗ No GUI window — runs through file dialogs only
