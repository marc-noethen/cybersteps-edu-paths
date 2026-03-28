# Elementary Fix

_There's a bug in the `<body>` politic! Time to investigate._

**Goal**

You are given an HTML file (`menu.html`) and a CSS file (`menu_style.css`) that are supposed to create a simple horizontal navigation menu. However, the CSS is broken, and the menu looks all wrong. Your task is to debug the CSS to make the menu display correctly as a horizontal bar with styled links.

**The Intended Look:**

- A horizontal navigation bar.
- List items (menu items) should be side-by-side, not stacked vertically.
- No bullet points visible.
- Each menu item should have a light gray background, some padding, and a dark gray text color.
- When a menu item is hovered over, its background should change to a dark gray, and its text color to white. The "Services" item should also have this active state style by default.

**Provided Files:**

**`menu.html` (Do NOT change this file):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Broken Menu</title>
    <link rel="stylesheet" href="menu_style.css">
</head>
<body>
    <nav class="main-navigation">
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li class="active-item"><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
</body>
</html>
```

**`menu_style.css` (This is the file you need to FIX):**

```css
/* Broken CSS for the menu - Please Fix Me! */

.main-navigation ul {
    list-style: circle; /* This should probably be none */
    marginn: 0; /* Typo here? */
    padding: 0px;
}

.main-navigation li {
    display: block; /* How to make them horizontal? */
    margin-right: 5px; /* Add some space between items */
}

.main-navigation a {
    display: inline; /* Or should this be block for padding to work well? */
    padding: 10px 15px; /* Is this padding enough? */
    background-color: #cccccc; /* Too light? */
    color: #eeeeee; /* Too light for the background? */
    text-decoration: underline; /* Should links be underlined? */
}

.main-navigation a:hover,
.main-navigation .active-item a { /* How to target the active item correctly? */
    background-color: #333333;
    color: #ffffff;
}
```

**Instructions**

1. Create a folder named `css_detective`.
2. Save the provided `menu.html` code into a file named `menu.html` inside this folder.
3. Save the provided `menu_style.css` code into a file named `menu_style.css` inside this folder.
4. Open `menu.html` in your browser to see its current broken state.
5. Open `menu_style.css` in VS Code. Your task is to edit **only this CSS file** to achieve the "Intended Look" described above.
    - Use your browser's developer tools (Inspect Element) to help you identify issues and test changes.
    - Look for typos, incorrect property values, and logical errors in how selectors or properties are used.
    - You might need to add, remove, or change CSS properties and selectors.
6. Continuously save `menu_style.css` and refresh `menu.html` in your browser to see your progress.

**Submission**

Submit only your corrected `menu_style.css` file and a screenshot of the fixed horizontal navigation menu as it appears in your browser.