**Kurs:** Cyber Security Analyst - Project 2| **Datum:** 27.06.2025

## Introduction

**CVE** stands for **Common Vulnerabilities and Exposures**. It's a public system that assigns unique IDs to known cybersecurity vulnerabilities in software and hardware. Each CVE entry includes a short description of the issue, its severity, and details about affected products or vendors. This database is a critical tool for security professionals, software developers, and researchers to stay informed about vulnerabilities and track fixes.

For this project, you aren't just browsing data - you're building the engine that manages it. You will design the database, write the Python logic, and create a tool that a real-world security analyst could actually use.

## **Step 1: Explore the Landscape**

Before you build, you must understand. Explore a few real CVE databases to get a feel for the information they store, how they structure it, and how professionals use them.

- **Official CVE Program:** [https://www.cve.org/](https://www.cve.org/)
- **Detailed Breakdowns:** [](https://www.cvedetails.com/)[https://www.cvedetails.com](https://www.cvedetails.com)
- **National Vulnerability Database (NVD):** [https://nvd.nist.gov/vuln/search](https://nvd.nist.gov/vuln/search)
- **VulDB:** [https://vuldb.com/](https://vuldb.com/)
- **and others…**

Pay attention to the data fields, the relationships between different pieces of information (like a vulnerability and the products it affects), and the search/filter capabilities.

### **Step 2: Build Your CVEDB**

In this project, you’ll build your own version of a CVE database. This is your system to design. You decide how it works, what data it holds, and how users interact with it. The core requirement is that your program stores and interacts with real or realistic CVE-like data using a **relational database** and **SQL**, accessed via **Python**.

We've broken the project into stages so you can get the basics right before adding the complex stuff.

<aside> 💡

**Quick Tip**

You don't have to finish every single stage to be successful. Start with something simple that works, and improve as you go.

</aside>

### Stage 1: The Foundations

Don't just start typing code. You need a solid blueprint first.

- **The Tools:** We suggest using **SQLite**. It comes with Python and doesn't require a complicated server setup. To see what's happening inside your database, use [DB Browser for SQLite](https://sqlitebrowser.org/).
- **Python Basics:** You'll mostly be working with the `sqlite3` module.
- **Schema Design:** Map out your tables. What columns do you need? (Pro tip: use `cve_id` as your Primary Key).
- **Manual Entry:** Build a menu in Python that lets you manually type in a new vulnerability and save it.
- **Query:** Write a simple `SELECT` query so you can find a specific CVE just by entering its ID.

<aside> 💡

### **Pro Tip: Use a Virtual Environment (venv)**

Before you start coding, set up a **virtual environment**.

**Why?** It creates an isolated "container" for your project. This prevents your CVE project's libraries (like `requests` or `openai`) from clashing with other Python projects on your computer. It keeps your setup clean and professional.

**How to use it:**

1. **Create:** Open your terminal in your project folder and run:
    
    `python -m venv venv`
    
2. **Activate:**
    
    - _Windows:_ `.\\venv\\Scripts\\activate`
    - _Mac/Linux:_ `source venv/bin/activate`
3. **Install:** Now, any `pip install` commands will stay inside this folder! </aside>
    

### Stage 2: The Core

Entering bugs one by one is slow. Let's automate it and look at the big picture.

- **Bulk Import:** Read a `.csv` or `.json` file and dump hundreds of real vulnerabilities into your database at once. Use appropriate modules to load the files and parse them. You can use [https://nvd.nist.gov/vuln/data-feeds#divJson20Feeds](https://nvd.nist.gov/vuln/data-feeds#divJson20Feeds)
- **Analyze:** Use SQL functions like `COUNT`, `AVG`, and `GROUP BY` to find trends. Try to answer: "Which company has the most bugs?" or "What's the average risk score in my database?"
- **Smart Filters:** Let users filter results by score (like "everything above a 9.0") or search by specific keywords.

### Stage 3: Live Data

Static files get old fast. Let's pull data directly from the source.

- **Syncing Up:** Use the `requests` module to grab the latest vulnerabilities straight from NVD [https://nvd.nist.gov/developers/vulnerabilities](https://nvd.nist.gov/developers/vulnerabilities)
- **Live Updates:** Set it up so your script can "refresh" your database with fresh data from the web whenever you want.

### Stage 4: Talk to your Data

Writing SQL is great, but wouldn't it be easier to just ask a question?

- **Query Generation:** Set it up so a user can say, "Show me Microsoft bugs from last month," and the AI writes the SQL query for them.
- **The Conversation:** If the user is too vague (like saying "show me the bad ones"), have the AI ask a follow-up question to clarify what they mean.
- **Execution:** Your Python script should take that AI-generated SQL, run it, and show the results.

<aside> 💡

For this stage you would need an AI API, like [https://aistudio.google.com/](https://aistudio.google.com/)

</aside>

### Stage 5: Make it Yours

This is where you add your own features. What would make this tool actually useful for a security team? Visualizations? Export results? Alerts? Complex analysis? You decide!

## Step 3: Show Off Your Work!

You’ll present your CVEDB project to the class. Be prepared to explain how your system works, what kind of queries it supports, and what design decisions you made along the way. Show us your schema, your Python code, and your favorite query in action.

## **What To Submit**

1. **Your Python Project:** Clean, readable code.
2. **SQL Schema:** A `.sql` file with your table structures.
3. **Data Sample:** The file you used to test your bulk import.
4. **Project Summary (PDF):**
    - A quick guide on how to run your tool.
    - Why you chose this specific structure.
    - The most annoying bug you had to fix or the coolest thing you learned.

Think like a designer, stay curious like an analyst, and build something you're proud of!