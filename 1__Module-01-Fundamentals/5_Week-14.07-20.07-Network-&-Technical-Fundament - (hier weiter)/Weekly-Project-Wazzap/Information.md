Digital images are grids of tiny colored squares called pixels. In this project, you'll go behind the scenes of applications like Photoshop and Instagram to manipulate these pixels directly. You will build a simple but powerful photo editor from scratch using only Python.

Your core tool won't be a fancy library, but the raw power of **bitwise operations**. You will learn how to pack and unpack color data from single numbers and write functions to create stunning visual effects.

### Core Concepts: Pixels as Numbers

Every color on your screen is a mix of Red, Green, and Blue (RGB). To store this efficiently, we can pack all three values into a single 24-bit integer. The format looks like this: `0xRRGGBB`.

- `0xFF0000` is pure Red (Red=255, Green=0, Blue=0).
- `0x00FF00` is pure Green (Red=0, Green=255, Blue=0).
- `0xFFFFFF` is pure White (Red=255, Green=255, Blue=255).

Our entire project revolves around manipulating these numbers. To do that, we'll use bitwise operators:

- `>>` (Right Shift): Moves bits to the right.
- `<<` (Left Shift): Moves bits to the left.
- `&` (Bitwise AND): Used with a "mask" to extract or remove specific bits.
- `|` (Bitwise OR): Used to combine different bit patterns.

## Project Setup

### Step 1: Install the Pillow Library

We need one external library, Pillow, to handle the complex task of reading, writing, and displaying image files (like `.png`or `.jpg`). You will not be modifying this part of the code, only using it.

Run this command in your terminal: `pip3 install pillow`

### Step 2: Your Image Toolkit

Here are helper functions that will act as your bridge to the outside world. They load, save, display, and scale images. **You do not need to edit this code.**

```python
from PIL import Image

def load_image(filepath):
    """
    Loads an image file and converts it into our project's format
    (a list of lists of pixel integers).
    """
    try:
        with Image.open(filepath) as img:
            img = img.convert("RGB")
            width, height = img.size
            pixels = list(img.getdata())
            image_data = [
                [(r << 16) | (g << 8) | b for r, g, b in pixels[i*width:(i+1)*width]]
                for i in range(height)
            ]
            print(f"Successfully loaded '{filepath}' ({width}x{height})")
            return image_data
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image_data, filepath):
    """
    Takes an image in our format and saves it to a file.
    """
    if not image_data or not image_data[0]:
        print("Error: Image data is empty.")
        return
    height = len(image_data)
    width = len(image_data[0])
    img = Image.new("RGB", (width, height))
    pixels = []
    for row in image_data:
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            pixels.append((r, g, b))
    img.putdata(pixels)
    try:
        img.save(filepath)
        print(f"Successfully saved image to '{filepath}'")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def display_image(image_data):
    """
    Displays an image from our format directly on the screen.
    """
    if not image_data or not image_data[0]:
        print("Error: Image data is empty.")
        return
    height = len(image_data)
    width = len(image_data[0])
    img = Image.new("RGB", (width, height))
    pixels = []
    for row in image_data:
        for value in row:
            r = (value >> 16) & 0xFF
            g = (value >> 8) & 0xFF
            b = value & 0xFF
            pixels.append((r, g, b))
    img.putdata(pixels)
    img.show()

def scale_image(image_data, factor):
    """
    Scales an image by a given integer factor using nearest-neighbor scaling.
    Useful for making small test images easier to see.
    """
    if not image_data or not image_data[0] or factor <= 0:
        return []
    if factor == 1:
        return [row[:] for row in image_data] # Return a copy

    new_height = len(image_data) * factor
    new_width = len(image_data[0]) * factor
    new_image = [[0] * new_width for _ in range(new_height)]

    for y in range(new_height):
        for x in range(new_width):
            orig_y = y // factor
            orig_x = x // factor
            new_image[y][x] = image_data[orig_y][orig_x]

    return new_image
```

### A Sample Image for Testing

Before you use real photos, you can use this simple grid to test your functions. This code can be placed in your main script to see the sample image.

```python
# Define some colors to make creating the image easier
BLACK = 0x000000
YELLOW = 0xFFFF00
BLUE = 0x0000FF

# A smiley face!
smiley_face = [
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, BLACK],
    [BLACK, YELLOW, BLUE, YELLOW, YELLOW, BLUE, YELLOW, BLACK],
    [BLACK, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, BLACK],
    [BLACK, YELLOW, BLUE, YELLOW, YELLOW, BLUE, YELLOW, BLACK],
    [BLACK, YELLOW, YELLOW, BLUE, BLUE, YELLOW, YELLOW, BLACK],
    [BLACK, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
]

# Example of how to use the toolkit functions with the sample image.
# You can run this code once you have the toolkit functions available.
# To see the smiley face, you first need to scale it up.
scaled_smiley = scale_image(smiley_face, 20)
# Then, you can display the scaled version.
display_image(scaled_smiley)
```

## Your Project Roadmap

### Step 1: Build Your Pixel Toolkit

Before you can create filters, you must build the essential tools for working with pixels. Your first task is to write the functions that unpack and pack RGB values from a single integer.

**Complete the following functions:**

1. `get_red(pixel)`: Takes a pixel integer and returns only the red value (0-255).
2. `get_green(pixel)`: Returns the green value (0-255).
3. `get_blue(pixel)`: Returns the blue value (0-255).
4. `create_pixel(r, g, b)`: Takes red, green, and blue values and packs them into a single integer.

### Step 2: Create Your First Filters

Now, use the toolkit you just built to create some classic photo effects. For each function, you should create a _new_ image list; do not modify the original.

1. **Grayscale Filter:** `to_grayscale(image_data)`
2. **Invert Colors Filter:** `invert_colors(image_data)`

### Step 3: Master Pure Bitwise Operations

Some effects are much more elegant to write by manipulating the pixel integer directly. This is where the true power of bitwise operations shines.

1. **Remove a Channel:** `remove_green(image_data)`
2. **Swap Channels:** `swap_red_blue(image_data)`

### Step 4: Get Creative!

Think about ways to make your program better. You might add more filters, make existing ones more flexible, or come up with a brand-new idea. Implement at least one additional filter of your own design, and consider other improvements you could make to enhance your program.

## What To Submit

1. A working Python file (`.py`)
2. A PDF project summary report, that includes:
    - How your editor works at a high level.
    - What effects you implemented.
    - What you learned about bitwise operations and how they can be used for image manipulation.