# backend/process.py
import cv2
import numpy as np
from PIL import Image
import os

def process_image_and_generate_art(image_path, style):
    # Load and preprocess image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (500, 500))  # Standardize size
    edges = cv2.Canny(img, 100, 200)   # Detect ridges

    # Extract simple features (fixed contour handling)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    features = [(point[0][0], point[0][1]) for contour in contours for point in contour]

    # Generate art based on style
    output = generate_art(features, style)

    # Save in two resolutions
    low_res = output.resize((1080, 1080), Image.LANCZOS)
    high_res = output.resize((3840, 3840), Image.LANCZOS)

    low_path = f"output_{style}_low.png"
    high_path = f"output_{style}_high.png"
    low_res.save(low_path)
    high_res.save(high_path)

    return {"low": low_path, "high": high_path}

def generate_art(features, style):
    img = Image.new("RGB", (500, 500), "white")
    pixels = img.load()

    for x, y in features:
        if style == "vibrant":
            pixels[x, y] = (np.random.randint(100, 255), 0, np.random.randint(100, 255))
        elif style == "surreal":
            pixels[x, y] = (np.random.randint(0, 255), np.random.randint(0, 255), 255 - x % 255)
        elif style == "geometric":
            pixels[x, y] = (x % 255, y % 255, 150)
        elif style == "lineart":
            pixels[x, y] = (0, 0, 0) if x % 10 < 5 else (255, 255, 255)

    return img