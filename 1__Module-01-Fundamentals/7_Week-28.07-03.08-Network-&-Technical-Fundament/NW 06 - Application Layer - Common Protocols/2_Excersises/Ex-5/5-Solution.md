Analysis (RFC 3207)  
Purpose of STARTTLS according to RFC 3207:

STARTTLS is used in the SMTP protocol to upgrade an existing unencrypted connection to a TLS-secured connection.  
The connection starts in plain text so that the client can see the server capabilities (e.g. authentication methods).  
If the server supports STARTTLS, the client sends STARTTLS.  
If the server responds with 220 Ready to start TLS, the client must immediately start a TLS handshake.  
From this point onwards, communication is encrypted, including user names, passwords and emails.

Why is this important for port 587?  
Port 587 is intended for submission - i.e. for sending emails from authenticated users to a mail server.  
Without TLS, user data and passwords would be transmitted in plain text - extremely insecure!  
STARTTLS ensures that this data is confidential and protected against man-in-the-middle attacks.

What needs to happen immediately?  
Immediately after the successful STARTTLS handshake:

The client performs the TLS handshake.

A new EHLO is then sent, as the previous capabilities are invalid (RFC 3207 §4.2).

Only now may the client send authentication data.