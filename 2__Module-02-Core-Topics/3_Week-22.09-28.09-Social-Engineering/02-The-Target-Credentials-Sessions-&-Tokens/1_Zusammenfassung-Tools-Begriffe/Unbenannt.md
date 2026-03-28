Welcome to your pre-class preparation. This week is all about social engineering—the art of manipulating people to give up confidential information or perform actions. But what is the social engineer actually trying to _get_? While their methods are psychological, their goal is almost always technical: to acquire a key that unlocks a digital door.

This material explores the evolution of these "keys." We'll examine the three primary targets a social engineer seeks: **credentials** (like passwords), **session identifiers** (which prove an active login), and **authentication tokens** (which act as digital passports). We'll follow the logical progression from early, insecure methods to the modern standards used today, giving you a clear picture of what you're trying to protect as a defender, and what an attacker is desperate to steal.

### The Fundamental Problem: Statelessness

At its core, the web runs on HTTP, which is a **stateless** protocol. This means each request you send to a web server is treated as an independent event. The server has no built-in memory of your previous interactions. If you logged in on one page, the server would forget who you are by the time you clicked on the next link. This would require you to enter your username and password for every single action, which is clearly unworkable.

Let's explore the solutions that were developed to overcome this.

### The First (Insecure) Solution: Credentials with Every Request

![image (10).png](attachment:41f5287e-6e6d-44b7-878d-8e9bd5e02894:image_\(10\).png)

One of the earliest methods was **HTTP Basic Authentication**. The process was simple:

1. You try to access a protected page.
2. The server responds with a "401 Unauthorized" status and a `WWW-Authenticate: Basic` header.
3. Your browser displays a generic pop-up box asking for your username and password.
4. Once you enter your credentials, the browser combines them into a `username:password` string, encodes it using Base64, and sends it back in an `Authorization` header with _every subsequent request_ to that server.

Base64 is an encoding scheme, not encryption. It's trivially reversible. While this method was simple, it meant the user's actual password was transmitted across the network with every click, making it highly vulnerable to interception. It is rarely used on the public internet today for this reason.

### A Better Way: Stateful Sessions

![image (11).png](attachment:82a44dc6-b5ec-4a20-b87b-43e81f547757:image_\(11\).png)

To avoid re-sending passwords, developers created **sessions**. This is the classic model for traditional web applications and is still widely used. The key idea is to have the server "remember" the user after a single, successful login.

Here's the flow:

1. **Login:** You submit your username and password to the server, typically through a login form. This is (ideally) a one-time event.
2. **Verification & Session Creation:** The server verifies your credentials. If they are correct, it creates a unique session for you on the server. This session is a data structure stored on the server that contains information about your authenticated state (e.g., your user ID, permissions). The server generates a long, random, and unpredictable **Session Identifier (Session ID)** to act as a key for this data.
3. **Cookie Delivery:** The server sends this unique Session ID back to your browser, almost always in a **cookie**. A cookie is just a small piece of data that a website asks your browser to store.
4. **Authenticated Requests:** For every subsequent request you make to that website, your browser automatically includes the cookie containing the Session ID. The server receives the ID, looks up the corresponding session in its storage, confirms you are authenticated, and processes your request.

This is a **stateful** system because the server must maintain the state (the session data) for every single active user. An attacker who steals a valid Session ID from a cookie can add it to their own browser and send it to the server. The server, seeing a valid ID, will grant the attacker full access to the original user's account without ever needing a password. This is called **session hijacking**.

### Try it yourself

Let's see a session cookie in action.

1. Open your web browser (Chrome or Firefox is recommended).
2. Open the Developer Tools. You can usually do this by right-clicking anywhere on a page and selecting "Inspect" or by pressing `F12`.
3. Go to the "Application" tab in Chrome or the "Storage" tab in Firefox.
4. In the left-hand menu, find the "Cookies" section and select the website you're on.
5. Moodle should have a session cookie set. You can also explore other websites that have a traditional login form.
6. Watch the list of cookies. You will likely see a new cookie appear after you log in. Look for names like `sessionid`, `sid`, `PHPSESSID`, or something similar. The long, random-looking value of that cookie is your active session identifier. That's the key the server uses to remember you.

### The Modern, Stateless Solution: Tokens

![image (12).png](attachment:b9afefc8-9aea-446e-bb47-b198d2233250:image_\(12\).png)

The session-based approach works well for traditional websites, but the modern web is dominated by APIs, Single-Page Applications (SPAs), and mobile apps. In this world, a stateless approach is often better for performance and scalability. This is where tokens come in.

A token is a piece of data, generated by the server, that contains all the necessary information about a user's identity and permissions. Unlike a Session ID, which is just a pointer to data on the server, the token itself _is_ the data.

The most common format is the **JSON Web Token (JWT)**.

1. **Login:** You send your credentials to an authentication endpoint.
2. **Verification & Token Creation:** The server validates your credentials. Instead of creating a session on the server, it creates a JWT. This token is a carefully structured string containing a header (metadata), a payload (user data like user ID, roles, expiration time), and a cryptographic signature.
3. **Token Delivery:** The server sends this JWT back to you (the client).
4. **Authenticated Requests:** It's now your responsibility to store this token securely and include it with every request to a protected API endpoint, typically in the `Authorization: Bearer <token>` header.
5. **Verification:** The API server receives the token. It doesn't need to look up a session. It simply checks the token's signature using a secret key that only it knows. If the signature is valid, the server trusts the information in the payload and processes the request.

Because the server doesn't have to store any session data, this approach is **stateless**. This makes it easy to scale applications across many servers. Anyone can read the data inside a JWT, but the signature guarantees that it hasn't been tampered with. Stealing a valid token gives an attacker immediate access until that token expires.

### Try it yourself

Go to [https://www.jwt.io/](https://www.jwt.io/) and explore the demo token and it’s various fields.

- Try to modify the encoded JWT.
- Try to modify the secret used for signature [validation.Is](http://validation.Is) the signature still valid?

### Think about it

Access tokens are often short-lived, expiring after 15-60 minutes, while session cookies might be valid for days. From a security perspective, what is the advantage of a short-lived token? What happens if an attacker steals one?

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-3-Session-2-Credentials-Sessions-Tokens-23z5qyy220yw2ma?mode=doc](https://gamma.app/docs/Module-2-Week-3-Session-2-Credentials-Sessions-Tokens-23z5qyy220yw2ma?mode=doc)

Try not to peek before class - spoilers inside!

</aside>