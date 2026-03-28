# Jinja Ninja

_Without a sound_

**Goal**

Build a Flask application that serves HTML pages using templates and passes dynamic data from your Python code to these templates.

**Instructions**

1. Set up a Flask application and create a `templates` folder.
2. Create an HTML template named `profile.html` in your `templates` folder. This template should be designed to display:
    - A page title: "User Profile - [User's Name]".
    - A main heading: "Welcome, [User's Name]!".
    - A paragraph: "Your favorite language is: [Language]."
    - An unordered list of the user's hobbies.
3. Create a Flask route, `/user/<username>`.
4. The view function for this route should:
    - Accept the `username` from the URL.
    - Define Python variables for a favorite programming language (e.g., "Python") and a list of hobbies (e.g., `["Reading", "Gaming", "Traveling"]`).
    - Render the `profile.html` template, passing the username, language, and hobbies list to it so they appear in the correct places.
5. Test by navigating to `/user/YourName` (replace `YourName` with any name) in your browser.

**Submission**

Submit your Python script (`.py` file) and your `profile.html` template file.