# Image Modification Guide

This repository contains the base image `Devil's Numbers background.png`. The goal is to split its contents into individual layers and apply modifications that add glowing red eyes and arms to the central figure.

## Detailed Steps

1. Install any tools you might need for viewing or editing images. Common choices include **GIMP**, **Krita**, **ImageMagick**, and **Photoshop** (if you have a license). For automation you can install Python packages such as `pillow` and `rembg`, and optionally generative AI frameworks like Stable Diffusion.

   ```bash
   sudo apt-get update
   sudo apt-get install -y gimp krita imagemagick
   # Install Python helpers
   pip install pillow rembg
   ```
2. Open the PNG in GIMP or process it with a Python script and move each visible element to its own layer:
   - The starry background
   - Number groups
   - The central figure
   - Title text
   - Any other distinct objects
3. Create a layer named "Eyes" with glowing red pupils for the figure. Apply a blur or glow effect so they shine.
4. Draw matching arms on new layers, keeping the style consistent with the existing art.
5. Save the layered image as `Devils_Numbers_layers.xcf` (or `.psd`) and export a flattened version named `Devils_Numbers_modified.png`.
6. Commit both the layered file and the final PNG.
7. If any of these steps fail, debug the issue and try again until the image looks correct and all files save without errors.

## Reference

The source image resides in this repository, and a backup is hosted at <https://drive.google.com/file/d/1_3hZCH-gxQAdvN2Iy6iFdsXA6TgwzGfB/view?usp=drivesdk>.
