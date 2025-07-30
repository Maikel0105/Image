# Task for Code-Mode Agent

1. Install any tools necessary for viewing and editing images. Recommended options include **GIMP**, **Krita**, **ImageMagick**, and, if you have a license, **Photoshop**. You may also install generative AI frameworks such as Stable Diffusion to help create new artwork.
2. Open `Devil's Numbers background.png` in the repository root. A backup of this file is also available at:
   https://drive.google.com/file/d/1_3hZCH-gxQAdvN2Iy6iFdsXA6TgwzGfB/view?usp=drivesdk
3. Separate every visible element of the image onto its own layer using an editor or Python script (`pillow` and `rembg` can help automate masking). Include the background, numbers, central figure, text, and any other distinct pieces.
4. Add a new layer with glowing red eyes for the figure. Use blur or glow effects so the eyes appear bright.
5. Draw arms for the figure on separate layers, matching the colors and shading of the original art.
6. Save the layered project as `Devils_Numbers_layers.xcf` (or `.psd`).
7. Export a flattened version named `Devils_Numbers_modified.png`.
8. Commit both the layered file and the updated PNG to the repository.
9. If any command fails or the result does not look correct, keep troubleshooting and re-running steps until the full image modification succeeds.
