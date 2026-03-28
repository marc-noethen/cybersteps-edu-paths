# Mission: SMTP

_Wow mail over the internet! So innovative!_

**Goal**

Write a short Python script using `smtplib` to connect to Google's public SMTP server (port 587), initiate the conversation (`EHLO`), examine the server's capabilities (especially `STARTTLS`), and understand the significance of this command in securing the session.

**Instructions**

1. **Your Task:** Write a Python script using `smtplib` that:
    - Connects to `smtp.googlemail.com:587`.
    - Issues the `EHLO` command.
    - Parses the server's multi-line response to find and print all advertised capabilities (each line starting with `250-` or `250` after the initial code).
    - Specifically checks for and prints whether `STARTTLS` is supported.
    - Closes the connection (`quit()`).
    - Includes basic error handling.
2. **Capture & Verify:** Run your script while capturing traffic (filter `tcp.port == 587`) with Wireshark. Confirm the `EHLO` command and response are clear text and that `STARTTLS` is advertised by the server.
3. **Analyze:** According to RFC 3207, what is the exact purpose of the `STARTTLS` command in SMTP? Why is it crucial for security when connecting on port 587, and what should happen _immediately_ after a client issues `STARTTLS` and the server responds positively (e.g., `220 Ready to start TLS`)?

**Submission**

Submit:

1. Your Python script.
2. A screenshot from Wireshark showing the server's multi-line response to the `EHLO` command, highlighting the line containing `STARTTLS`.
3. A text answer explaining the purpose of `STARTTLS` and what happens next in the protocol flow after it's successfully initiated (based on RFC 3207 or other reliable sources).