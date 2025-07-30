# Image Modification Instructions

This repository contains `Devil's Numbers background.png` which should be edited
according to the instructions below. The root `AGENTS.md` summarizes these goals
for automated agents.

## Goal
1. Separate all visible components of the PNG into individual layers so that
each element (background, numbers, figure, text, etc.) can be manipulated
separately.
2. Modify the central figure by adding glowing red eyes.
3. Draw or generate arms for the figure that match the existing art style.
4. Provide the final layered image file (e.g. `.psd` or `.xcf`) alongside the
updated flattened PNG.

## Suggested Workflow
1. Install image editing tools such as **GIMP** or **Krita**. These allow you to
   manually create and manage layers. You may also install `pillow` and `rembg`
   via `pip` to help isolate elements programmatically:
   ```bash
   pip install pillow rembg
   ```
2. Open the PNG and, using selection tools or `rembg`, cut out each component to
   its own layer (background, text, figure, etc.).
3. Add a new layer for the figure's glowing eyes. Paint the eyes red and apply a
   soft glow or blur effect.
4. Create additional layers for the figure's arms. Use colors and shading that
   match the original drawing.
5. Export the layered file (`.psd`/`.xcf`) and a final composed PNG. Commit both
   files to the repository.

## Reference Links
- Original image: `Devil's Numbers background.png` in this repository.
- Backup download: <https://drive.google.com/file/d/1_3hZCH-gxQAdvN2Iy6iFdsXA6TgwzGfB/view?usp=drivesdk>

