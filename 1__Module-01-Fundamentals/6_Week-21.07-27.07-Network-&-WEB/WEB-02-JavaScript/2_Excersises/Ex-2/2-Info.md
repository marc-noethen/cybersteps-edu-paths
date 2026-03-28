# Headline Listener (PR)

_There is always someone listening…_

**Goal**

Create an interactive section on your webpage where you can dynamically refresh a main headline and add new fake news items. This teaches basic event handling, DOM manipulation, and prepares the page structure for future API integration.

**Instructions**

1. Use your existing `index.html` page from previous exercises.
2. Add a new `<button>` below your main title (`<h1>`), for example:

```html
<button id="refreshButton">Refresh Headlines</button>
```

1. Create a new section below the button to hold your fake headlines:

```html
<section id="headlinesContainer"></section>
```

1. Inside a `<script>` tag at the end of the `<body>`, write JavaScript that:
    
    - Selects the button using `document.getElementById`.
    - Adds a `click` event listener to the button.
    - When clicked:
        - Updates the `<h1>` text with a new headline message.
        - Creates a new headline item (e.g., `<h3>` for the title and `<p>` for the description).
        - Appends the new headline item to the `headlinesContainer` section.
    - Uses arrays of sample headlines and text for random selection.
    
    💡 _You can make up your own fake headlines — or use the examples below:_
    
    ```jsx
    const headlines = [
      "Breaking: Cyber Attack Hits Major Company!",
      "New Security Patch Released Today",
      "AI Tool Detects Malware Faster Than Ever",
      "Phishing Scam Targets Online Users"
    ];
    
    const descriptions = [
      "Experts are analyzing the incident to prevent future breaches.",
      "Make sure to update your systems to stay safe.",
      "AI algorithms are now capable of spotting threats automatically.",
      "Users are advised to verify all emails before clicking links."
    ];
    
    ```
    
2. Ensure each click adds **one new headline** without removing previous ones.
    

**Learning Points**

- Event listeners (`addEventListener`)
- DOM creation (`document.createElement`) and manipulation (`appendChild`)
- Basic interactivity: the page changes dynamically based on user actions
- Preparing page structure for later API data injection

**Submission**

Submit your HTML and JavaScript code. Include a screenshot of the page after clicking the button at least 5 times.