Welcome to the world of web application hacking! Before our session on SQL Injection (SQLi), it's important to build a solid foundation. This guide will walk you through the core concepts of how databases interact with web applications and how attackers can exploit this relationship.

### Reminder: The Language of Databases - SQL

As we've previously learned, applications use a **database** to store, manage, and retrieve data. The language they use to "talk" to the database is **Structured Query Language (SQL)**.

The most common SQL command you'll encounter is the `SELECT` statement, which is used to retrieve data. It has a clear structure:

- `SELECT [columns]`: Specifies which columns of data you want.
- `FROM [table]`: Specifies which table to get the data from.
- `WHERE [condition]`: Filters the data, returning only the rows that meet a certain condition.

A typical query to fetch a user's data looks like this:

```
SELECT user_id, username, password_hash FROM users WHERE username = 'alice';
```

This command tells the database: "From the `users` table, find the row where the `username` column contains the text 'alice', and give me the `user_id`, `username`, and `password_hash` from that specific row."

While `SELECT` is for reading data, SQL can also modify it:

- `INSERT INTO ...`: Adds new rows of data.
- `UPDATE ... SET ...`: Changes existing data.
- `DELETE FROM ...`: Removes rows of data.

Understanding that SQL can read, create, update, and delete data is key to realizing why an attacker who can control these queries has so much power.

### How Web Applications Use Databases

Web applications are dynamic. Instead of having a static page for every item in an online store, they have a single template. When you click on a product, the application fetches that specific product's details from a database and populates the template.

Consider a typical login page. The process looks something like this:

1. **User Input:** You enter your username and password into a form on a website.
2. **HTTP Request:** Your browser sends this information to the web server.
3. **Application Logic:** The application code on the server (e.g., a Python Flask app) receives your input. It needs to check if your credentials are valid.
4. **SQL Query Construction:** The application dynamically constructs an SQL query using the input you provided.
5. **Database Execution:** The database runs this query. If a matching record is found, it returns the user's data. If not, it returns nothing.
6. **Application Response:** Based on the database result, the application either logs you in or shows an "Invalid credentials" error message.

The critical vulnerability lies in **Step 4**. The application is building a command in one language (SQL) by embedding text from another context (user input) without properly sanitizing it.

Here's a simplified but realistic code snippet showing how this might look in a Python Flask application:

```python
# Insecure code example!
from flask import request
# ... inside a login function ...
username = request.form.get('username') # Gets 'alice' from the form
password = request.form.get('password') # Gets 'password123' from the form

# The developer dangerously mixes code (SQL) and user data (variables)
# by just pasting strings together.
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"

# The application then sends this 'query' string to the database
```

This practice of simple string concatenation is the root cause of SQL injection.

### What is SQL Injection (SQLi)?

**SQL Injection (SQLi)** is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. By inserting their own SQL code into the user input, an attacker can change the query's logic to their own advantage.

This allows an attacker to view data they are not normally able to retrieve, such as other users' private information, company secrets, or password hashes.

### Anatomy of an Attack: Authentication Bypass

![image.png](attachment:ee796435-cbc2-45aa-a292-81e0498fa8f9:image.png)

Let's dissect the most classic SQLi payload. An attacker wants to log in without a password.

The backend query is expecting a username and password, like so: `SELECT * FROM users WHERE username = '[USERNAME]' AND password = '[PASSWORD]';`

The attacker provides the following input in the `username` field: `' OR '1'='1' --` They can leave the password field blank.

The application takes this input and builds the following query string: `SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = '';`

Let's break this down from the database's perspective:

1. `'` : The first single quote provided by the attacker closes the string for the `username` value. The query now looks like `... WHERE username = ''`. The database is now expecting a keyword like `AND` or `OR`.
2. `OR '1'='1'` : The attacker provides this. The `OR` is a logical operator. The condition `'1'='1'` is universally, undeniably **true**. The `WHERE` clause now evaluates to `(username = '') OR (true)`. Since anything `OR true` is `true`, the `WHERE` clause will be true for **every single row** in the table.
3. `-` : This is a comment operator in most SQL dialects. It tells the database to completely ignore everything that follows on the same line.

So, the database effectively executes this: `SELECT * FROM users WHERE username = '' OR '1'='1'`

The original `AND password = ...` part of the query is ignored as a comment. The query finds all users, the application receives a list of users instead of an empty result, and it often logs the attacker in as the first user in that list—frequently, the administrator.

### Think about it

Why might a developer write code that is vulnerable to SQLi? What are the pressures or common mistakes that could lead to this, even when developers know it's a risk?

### Types of SQL Injection

1. **In-Band SQLi (Classic SQLi)** The attacker uses the same channel to launch the attack and see the results.
    
    - **Error-Based SQLi:** The attacker sends a malicious query designed to fail. The goal is to make the detailed error message from the database appear on the web page, which might reveal table names, column names, or other internal details.
    - **UNION-Based SQLi:** This powerful technique uses the `UNION` operator, which combines the results of two `SELECT` statements into a single result. An attacker can use this to stitch their malicious query's output onto the legitimate query's output.
    
    ![image.png](attachment:f1afa456-c636-4935-8f52-7fc4c2451c48:image.png)
    
    For example, if a page displays product names (`SELECT name FROM products WHERE id=...`), an attacker could try to extract user data:
    
    1. **Find column count:** The attacker must first match the number of columns in their `UNION` query to the original query. They can do this by injecting `ORDER BY 1--`, `ORDER BY 2--`, etc., until the page errors. If `ORDER BY 3--` errors, they know the original query selects 2 columns.
    2. **Extract data:** Knowing there are two columns, the attacker can now inject a payload like `' UNION SELECT username, password FROM users--`. The application will run `SELECT name, price FROM products WHERE id='' UNION SELECT username, password FROM users--`. The page will now display all the usernames and passwords from the `users` table.
2. **Inferential SQLi (Blind SQLi)** This is used when the application doesn't show any data or errors on the page. The attacker must infer information by observing the application's behavior.
    
    - **Boolean-Based Blind SQLi:** The attacker asks the database a series of true/false questions. The page might load differently or show a "Welcome back!" message for a true result and a "Login failed" message for a false result. The attacker can use this to extract data one character at a time.
        - Is the first letter of the admin password 'a'? -> `... AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'a'` -> (Page shows "Login failed") -> False.
        - Is the first letter of the admin password 'b'? -> `... AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'b'` -> (Page shows "Login failed") -> False.
        - ...
        - Is the first letter of the admin password 'p'? -> `... AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'p'` -> (Page shows "Welcome back!") -> True! The first letter is 'p'.
    - **Time-Based Blind SQLi:** If the page looks identical for true and false results, the attacker can ask the database to pause. For example: "If the first letter of the admin password is 'a', then sleep for 5 seconds." If the website takes 5 seconds longer to load, the attacker knows the answer was true.
3. **Out-of-Band SQLi** A rare technique where the attacker forces the database to make an external network connection (e.g., an HTTP or DNS request) to a server they control, sending the stolen data through that channel.
    

### The Real-World Impact of SQLi

SQLi is not just a theoretical problem. It has been the cause of some of the largest data breaches in history. In 2008, Heartland Payment Systems was breached via SQL injection, leading to the theft of over 130 million credit card records. In 2015, UK telecom company TalkTalk was breached, exposing the data of thousands of customers, due to an SQLi vulnerability on their website. These incidents resulted in massive financial losses, regulatory fines, and severe reputational damage.

### Why is SQLi So Dangerous?

- **Confidentiality:** Attackers can read sensitive data like personal user information, credit card details, or trade secrets.
- **Integrity:** Attackers can modify or delete data, corrupting backups and disrupting business operations.
- **Availability:** Attackers can delete entire tables or databases, making the application unavailable.
- **Authentication Bypass:** Attackers can gain access to any user's account, including administrators.
- **Complete Takeover:** On misconfigured systems, SQLi can be used to run commands on the underlying server, giving the attacker total control.

Understanding SQL injection is a critical first step in learning how to defend against it. In our upcoming lesson, we will explore these concepts with hands-on demonstrations.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-2-Session-2-SQL-Injection-6xuwr9a0qrxukvz?mode=doc](https://gamma.app/docs/Module-2-Week-2-Session-2-SQL-Injection-6xuwr9a0qrxukvz?mode=doc)

Try not to peek before class - spoilers inside!

</aside>