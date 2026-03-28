Welcome to your preparation for our session on Broken Authentication and Access Control. In this document, you will learn the fundamental concepts of how websites identify you (authentication) and what they allow you to do (access control). Understanding these mechanisms is crucial because when they fail, it can lead to some of the most common and severe security vulnerabilities on the web.

## What are Authentication and Authorization?

![image.png](attachment:655d6561-4575-4ed7-9d91-daeac42f35cd:image.png)

Though often used interchangeably in casual conversation, authentication and authorization are two distinct and critical concepts in security. They represent sequential steps in a security process: you must first prove who you are before the system can decide what you're allowed to do.

**Authentication: Are You Who You Say You Are?**

Authentication is the process of verifying a user's identity. When you log into a website with a username and password, you are authenticating. The website is checking the credentials you provide against its records to confirm that you are the legitimate owner of that account.

Common methods of authentication, often called "factors," include:

- **Something you know:** A password, a PIN, or the answer to a security question. This is the most common factor.
- **Something you have:** A physical key, a smartphone (for receiving a one-time code via SMS or an authenticator app), or a hardware security token (like a YubiKey).
- **Something you are:** A fingerprint, a facial scan, or another biometric identifier.

**Multi-Factor Authentication (MFA)** significantly strengthens security by requiring verification from two or more of these categories. For example, logging in might require both your password (something you know) and a code from your phone (something you have).

**Authorization: Are You Allowed to Do That?**

Authorization, also known as Access Control, happens _after_ successful authentication. It is the process of determining whether an authenticated user has the permission to access a specific resource or perform a particular action.

Think of it like a concert. Your ticket **authenticates** you as a valid attendee. However, the type of ticket you have (e.g., general admission, VIP, backstage pass) **authorizes** which areas you can access. A general admission ticket holder is not authorized to go backstage. The security guard checking your pass at the backstage entrance is enforcing access control.

In a web application, this means:

- A regular user is not authorized to access the `/admin` panel.
- A user is authorized to view their own profile page at `/profile/user123` but not the profile page of another user at `/profile/user456`.
- A manager might be authorized to approve expense reports, while a standard employee is only authorized to submit them.

A failure in authorization means the application fails to correctly check if the user has the right permissions for a given action, even if they are correctly authenticated.

### Think about it

Think about your online banking application. The login page is for authentication. Once you are logged in, the system enforces authorization everywhere. What stops you from seeing someone else's account balance? What prevents you from transferring more money than you have? These are all authorization checks.

## Managing User Sessions: Cookies and Tokens

![image.png](attachment:2eca17cf-a9f4-407e-9116-03a139e74820:a93c6287-3846-47ad-a484-a3934147dab8.png)

HTTP, the protocol of the web, is "stateless." This means each request you send to a web server is independent and has no memory of previous requests. If you log in, the server would immediately forget who you are on the very next request you make. This would make online shopping or social media impossible.

To solve this, applications use **sessions** to keep track of a user's authenticated state. When you log in, the server creates a session for you and gives your browser a unique identifier to remember it by. This identifier is sent with every subsequent request you make, telling the server, "Hey, it's me again."

This session identifier is most commonly stored in a **cookie** or a **session token**.

**Cookies**

A cookie is a small piece of data that a server sends to a user's web browser. The browser stores it and sends it back with every request to the same server. A common use is to store the session ID. When you log in, the server sets a cookie in your browser like `sessionID=a1b2c3d4e5f67890...`. Your browser then includes this cookie automatically in all future requests to that site.

To be secure, cookies can have special attributes:

- `HttpOnly`: Prevents the cookie from being accessed by client-side scripts (like JavaScript), mitigating cookie theft via Cross-Site Scripting (XSS).
- `Secure`: Ensures the cookie is only sent over HTTPS, protecting it from being intercepted on insecure networks.
- `SameSite`: Controls whether the cookie is sent on requests initiated from other domains, helping to prevent Cross-Site Request Forgery (CSRF).

**Session Tokens (e.g., JSON Web Tokens - JWT)**

Another popular method is using tokens. A JSON Web Token (JWT), for instance, is a self-contained token that can carry information (claims) about the user. When a user logs in, the server generates a JWT and sends it to the client. The client then includes this token in the `Authorization` header of its requests, typically as `Authorization: Bearer <token>`.

A JWT consists of three parts separated by dots: `header.payload.signature`. The header and payload are Base64 encoded (easily readable), while the signature is a cryptographic hash that verifies the token hasn't been tampered with. The server can verify this signature to trust the information within the token without needing to look up session information in a database every time.

Managing these sessions securely is a major part of authentication. If an attacker can steal a user's session cookie or token, they can impersonate that user without needing their password. This is called **Session Hijacking**.

We will dive deeper into JWTs, session tokens, and cookies next week.

### Try it yourself

1. Open your browser's developer tools (usually by pressing F12 or right-clicking and selecting "Inspect").
2. Navigate to the "Application" (in Chrome) or "Storage" (in Firefox) tab.
3. Click on "Cookies" on the left-hand side and select a website you are logged into.
4. Look at the names and values of the cookies. Can you find one that looks like a session identifier (e.g., `sessionid`, `SID`, `auth_token`)? Note its long, random-looking value. This is what keeps you logged in. Check if it has the `HttpOnly` and `Secure` flags set.

## Common Vulnerabilities

When these systems are not implemented correctly, serious vulnerabilities can arise.

**Broken Authentication** This category includes weaknesses in the login and session management processes.

- **Credential Stuffing:** Attackers use lists of usernames and passwords stolen from other data breaches to try and log into an application. This works because many people reuse passwords across different services.

![image.png](attachment:ae144f09-a976-4790-81f0-3621b30cc665:image.png)

- **Brute-Force Attacks:** An attacker systematically tries all possible password combinations for a known username. Defenses include rate limiting (slowing down repeated attempts) and account lockouts.
- **Weak Password Policies:** Allowing users to set simple, easily guessable passwords like "123456" or "password".
- **Unsecured Password Storage:** Storing user passwords in plain text in the database instead of using strong, salted hashing algorithms.

**Broken Access Control** This is one of the most common and critical web application vulnerabilities. It occurs when an attacker can access resources or perform actions they are not supposed to. We can categorize these failures into two main types:

1. **Horizontal Access Control Failure:** A user can access resources belonging to another user at the same privilege level.
2. **Vertical Access Control Failure:** A user can access functionality or resources that should only be available to users with higher privileges (e.g., an administrator).

Here are common examples:

- **Insecure Direct Object References (IDOR):** This is a classic _horizontal_ failure. It happens when an application provides direct access to an object based on user-supplied input. For example, a URL might look like `https://example.com/account?id=123`. An attacker logged in as user `456` could try changing the `id` to `124` to see if they can view another user's account information. A secure application would validate that the currently logged-in user (`456`) is authorized to view account `124` before displaying the information.

![image.png](attachment:8110f7d2-8a4e-4a31-a658-c5dd2c9f06fb:image.png)

- **Missing Function-Level Access Control:** This is a classic _vertical_ failure. The application may hide links or buttons for administrative functions from regular users, but it doesn't actually prevent them from accessing those functions if they know the direct URL. For example, an attacker could navigate directly to `https://example.com/admin/deleteUser?id=5`. Even if the link isn't visible, a secure application must check on the server-side if the user making the request has administrative privileges before executing the deletion.
- **Privilege Escalation:** This is the ultimate goal of many access control attacks. An attacker with a low-privilege user account finds a flaw that allows them to gain the permissions of a higher-privilege user, such as an administrator. This could happen by exploiting a missing function-level access control check or another vulnerability.

These vulnerabilities are dangerous because they are often easy to find and exploit, and they can lead directly to unauthorized data disclosure, modification, or destruction.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-4-Session-4-Broken-Authentication-Access-Control-cc1yk7gvpoaantj?mode=doc](https://gamma.app/docs/Module-2-Week-4-Session-4-Broken-Authentication-Access-Control-cc1yk7gvpoaantj?mode=doc)

Try not to peek before class - spoilers inside!

</aside>