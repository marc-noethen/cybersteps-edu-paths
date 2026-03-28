import os
from PIL import Image
import requests
from io import BytesIO

# to work in colab:
# from IPython.display import display

def display_image(image, scale=1):
    height = len(image)
    width = len(image[0]) if height > 0 else 0

    img = Image.new("RGB", (width, height))
    pixels = []
    for row in image:
        for value in row:
            hex_str = f"{value:06x}"
            r, g, b = (int(hex_str[i:i+2], 16) for i in (0, 2, 4))
            pixels.append((r, g, b))
    img.putdata(pixels)
    if scale > 1:
        img = img.resize((width * scale, height * scale), Image.NEAREST)
    if scale == 0:
        img = img.resize((int(width / 2), int(height / 2)), Image.NEAREST)

    img.show()
    #display(img)  Use display() to show the image in Colab

def save_image(grid, path):
    h, w = len(grid), len(grid[0])
    img = Image.new("RGB", (w, h))
    pixels = []

    for row in grid:
        for val in row:
            r = (val >> 16) & 0xFF
            g = (val >> 8) & 0xFF
            b = val & 0xFF
            pixels.append((r, g, b))

    img.putdata(pixels)
    img.save(path)
    print(f"✅ Image saved to: {path}")

def image_to_hex_grid(image_data, resize_to=None):
    img = Image.open(BytesIO(image_data)).convert("RGB")
    if resize_to:
        img = img.resize(resize_to, Image.LANCZOS)
    w, h = img.size
    data = list(img.getdata())
    grid, idx = [], 0
    for _ in range(h):
        row = []
        for _ in range(w):
            r, g, b = data[idx]
            row.append((r << 16) | (g << 8) | b)
            idx += 1
        grid.append(row)
    return grid

# ___________ FILTERS ________________________________

def grayscale(img):
    result = []
    for row in img:
        new_row = []
        for px in row:
            r = (px >> 16) & 0xFF
            g = (px >> 8) & 0xFF
            b = px & 0xFF
            gray = (r + g + b) // 3
            new_px = (gray << 16) | (gray << 8) | gray
            new_row.append(new_px)
        result.append(new_row)
    return result

def sepia(img):
    result = []
    for row in img:
        new_row = []
        for px in row:
            r = (px >> 16) & 0xFF
            g = (px >> 8) & 0xFF
            b = px & 0xFF
            # Sepia anwenden
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            new_px = (min(tr, 255) << 16) | (min(tg, 255) << 8) | min(tb, 255)
            new_row.append(new_px)
        result.append(new_row)
    return result

def no_filter(image):
 return image


def negative(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            neg_r = 255 - r
            neg_g = 255 - g
            neg_b = 255 - b
            new_px = (neg_r << 16) | (neg_g << 8) | neg_b
            new_row.append(new_px)
        result.append(new_row)
    return result

def swap_red_blue(img):
    result = []
    for row in img:
        new_row = []
        for px in row:
            r = (px >> 16) & 0xFF
            g = (px >> 8) & 0xFF
            b = px & 0xFF
            # Swap red and blue channels
            new_px = (b << 16) | (g << 8) | r
            new_row.append(new_px)
        result.append(new_row)
    return result

def redder(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            #
            red_r = min(255, r + 50)
            red_g = g
            red_b = b
            new_px = (red_r << 16) | (red_g << 8) | red_b
            new_row.append(new_px)
        result.append(new_row)
    return result

def pinker(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            #
            red_r = min(255, r + 50)
            red_g = g
            red_b = min(255, r + 50)
            new_px = (red_r << 16) | (red_g << 8) | red_b
            new_row.append(new_px)
        result.append(new_row)
    return result
def brighter(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            #
            bri_r = min(255, r + 50)
            bri_g = min(255, g + 50)
            bri_b = min(255, b + 50)
            new_px = (bri_r << 16) | (bri_g << 8) | bri_b
            new_row.append(new_px)
        result.append(new_row)
    return result

def darker(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            #
            bri_r = max(0, r - 50)
            bri_g = max(0, g - 50)
            bri_b = max(0, b - 50)
            new_px = (bri_r << 16) | (bri_g << 8) | bri_b
            new_row.append(new_px)
        result.append(new_row)
    return result

def crop(image, pHeight, pWidth):
    height = len(image)
    width = len(image[0]) if height > 0 else 0

    new_height = int(len(image) * (1-10/pHeight))
    new_width = int(len(image[0]) * (1-10/pWidth)) if height > 0 else 0
    cropped_pixels = []
    for y in range(new_height):
        row = []
        for x in range(new_width):
            row.append(image[y][x])
        cropped_pixels.append(row)
    return cropped_pixels

# ── RANDOM CAT MODE OR PIC URL ─────────────────────────────────────────────

# ← Set to True for a random cat pic
USE_CAT = True

# Set to False ^^^ and enter your own URL of the image:
image_url = "https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg"
cat_api_url = "https://cataas.com/cat"

# ─────────────────────────────────────────────────────────────

img_data = None # Initialize img_data to None

try:
    if USE_CAT:
        print("🐱 Using cat image from API:", cat_api_url)
        img_data = requests.get(cat_api_url, timeout=10).content
    else:
        print("🌐 Using image URL:", image_url)
        img_data = requests.get(image_url, timeout=10).content
except Exception as e:
    print("❌ Error fetching image:", e)

    pass

# ── PROCESSING ─────────────────────────────────────────────

if img_data is not None:
    scale = 1
    img = image_to_hex_grid(img_data, resize_to=(640, 640))
    selected_filter = input("Enter filter name: ")

    if selected_filter == 'grayscale':
        img = grayscale(img)
    elif selected_filter == 'sepia':
        img = sepia(img)
    elif selected_filter == 'negative':
        img = negative(img)
    elif selected_filter == 'swap_red_blue':
        img = swap_red_blue(img)
    elif selected_filter == 'redder':
        img = redder(img)
    elif selected_filter == 'pinker':
        img = pinker(img)
    elif selected_filter == 'nofilter':
        img = no_filter(img)
    elif selected_filter == 'brighter':
        img = brighter(img)
    elif selected_filter == 'darker':
        img = darker(img)
    elif selected_filter == 'maximize':
        img = no_filter(img)
        scale = 2
    elif selected_filter == 'minimize':
        img = no_filter(img)
        scale = 0
    elif selected_filter == 'crop':
      cropH = int(input("Height percentage to crop (0-99): "))
      cropW = int(input("Width percentage to crop (0-99): "))
      img = crop(img, cropH, cropW)
      display_image(img)

    if selected_filter != "crop":
      display_image(img, scale)
    savingDecision = input("Do you want to save your file? (y/n)")
    if savingDecision == "y":
        saveDir = input("Please input the path to save the img. \n A new folder will be created there to contain the new images: ")
        filename= "output.png"
        filedir= saveDir
        os.makedirs(filedir+"/Modified_" + filename)
        save_image(img, filename)
else:
    print("No image data to process.")