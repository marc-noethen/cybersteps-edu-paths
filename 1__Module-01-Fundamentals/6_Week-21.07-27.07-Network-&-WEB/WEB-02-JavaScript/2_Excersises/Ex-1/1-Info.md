# Time Lord's Greeting (PR)

_Bow ties are cool, and so is knowing when to say "Good Evening!"_

**Goal**

Create a short JavaScript script **directly inside your HTML page** that greets the user in the browser console with a message that changes depending on the time of day, and simultaneously updates the `<h1>` heading on your webpage with the same message.

**Instructions**

1. Use your existing `index.html` page from Day 1.
2. At the bottom of your HTML file, right before the closing `</body>` tag, add a `<script>` block that will contain your JavaScript code.
3. Inside the `<script>` block:
    - Retrieve the current hour of the day using `new Date().getHours()`.
    - Determine which greeting to use:
        - Before 12 → `"Good Morning, Cyber Explorer!"`
        - Between 12 and 17 (inclusive) → `"Good Afternoon, Cyber Defender!"`
        - After 17 → `"Good Evening, Night Watcher!"`
    - Log the same greeting to the browser console using `console.log()`.
    - Find the `<h1>` element in your HTML (`document.querySelector("h1")`) and change its text content to display the same greeting.

Create a single file named `index.html` with the following structure:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Dynamic Greeting</title>
</head>
<body>
  <h1>Welcome!</h1>

  <script>
    const hour = new Date().getHours();
    let message = "";

    if (hour < 12) {
      message = "Good Morning, Cyber Explorer!";
    } else if (hour < 18) {
      message = "Good Afternoon, Cyber Defender!";
    } else {
      message = "Good Evening, Night Watcher!";
    }

    console.log(message);
    document.querySelector("h1").textContent = message;
  </script>
</body>
</html>

```

**What this does**

When you open the page in your browser, the `<h1>` text will automatically change to a greeting based on the current time, and the same message will also appear in the browser console (`Ctrl + Shift + J` or `F12` → Console tab).

**Submission**

Submit a screenshot of your webpage displaying the correct greeting based on the time you run the script. Include your full HTML code with the embedded `<script>` block.