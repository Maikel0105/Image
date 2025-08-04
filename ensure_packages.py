import importlib
import subprocess
import sys

# Packages grouped by category. Adjust names where import name differs from pip package.
REQUIRED_PACKAGES = [
    # Core
    "Pillow", "opencv-python", "scikit-image", "wand",
    # AI & diffusion
    "diffusers", "transformers", "torch", "tensorflow", "onnxruntime",
    "compel", "accelerate", "xformers",
    # Analysis / enhancement
    "rembg", "opencv-python-headless", "super-image", "realesrgan",
    "facenet-pytorch", "mediapipe", "pytesseract",
    # Visualization
    "matplotlib", "plotly",
    # Format conversion
    "imageio", "pyvips", "pyheif", "ffmpeg-python",
    # Drawing & rendering
    "cairosvg", "svgwrite", "manim", "pygame", "pycairo",
    # Augmentation & utilities
    "imgaug", "albumentations", "PyMuPDF", "moviepy"
]

def ensure_packages(packages):
    for pkg in packages:
        module_name = {
            "opencv-python": "cv2",
            "opencv-python-headless": "cv2",
            "PyMuPDF": "fitz",
            "ffmpeg-python": "ffmpeg"
        }.get(pkg, pkg)  # Import name vs. pip name

        try:
            importlib.import_module(module_name)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

if __name__ == "__main__":
    ensure_packages(REQUIRED_PACKAGES)
