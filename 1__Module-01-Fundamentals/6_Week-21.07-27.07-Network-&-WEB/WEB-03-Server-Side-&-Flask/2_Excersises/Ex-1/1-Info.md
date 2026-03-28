# Path Puzzler (PR)

_Where do all these URLs lead?_

**Goal**

In this exercise, you’ll build the foundation of the entire CyberNews Tracker project – a simple Flask web application that will serve as the core (or engine) for everything we’ll develop throughout the week. This Flask app – for example, a file named web_app.py – will remain your main entry point until the end of the project.

We’ll keep extending it with new routes, features, and authentication logic. You might modify or refactor parts later, but this first version is your base – your application’s backbone.

**Instructions**

1. Create a new Flask application inside a dedicated folder. You can organize your files like this:
    
    ```
    cybernews_tracker/
    ├── web_app.py
    ├── templates/          # (for future HTML files)
    ├── static/             # (for CSS or JS)
    └── data/               # (for mock data or JSON files)
    
    ```
    
    This structure will let you easily expand the project later with new components.
    
2. Implement the following routes:
    
    - `/`: Should return the string "Welcome to the Route Master Home Page!"
    - `/status`: Should return the string "Application is running."
    - `/info`: Should return a string containing the current date (e.g., "Today's date is YYYY-MM-DD"). You can hardcode this or use Python's `datetime` module.
    - `/greet/<name>`: This dynamic route should take a `name` as part of the URL and return a personalized greeting, e.g., if the user visits `/greet/Eliza`, it should return "Hello, Eliza!".
    - `/calculate/add/<int:num1>/<int:num2>`: This dynamic route should take two integers from the URL, add them together, and return a string like "The sum of num1 and num2 is [result]." For example, `/calculate/add/5/3` should return "The sum of 5 and 3 is 8."
3. Run your Flask app with: `flask run` or `python3 web_app.py`(depending on your setup).
    
4. Visit your routes in the browser or with `curl` to verify they work correctly.
    

**Submission**

Submit your Python script (`.py` file) containing the Flask application.