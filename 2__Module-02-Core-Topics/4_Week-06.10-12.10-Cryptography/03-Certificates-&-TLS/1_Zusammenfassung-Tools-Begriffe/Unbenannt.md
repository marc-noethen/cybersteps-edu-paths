Welcome to your pre-class preparation. Before our live session, please read through this material carefully. The goal is to build a solid foundation so we can dive into practical demonstrations and discussions in class.

### The Problem of Trust Online

In previous lessons, we explored symmetric and asymmetric encryption, including the Diffie-Hellman key exchange. Diffie-Hellman is powerful because it allows two parties to generate an identical shared secret key over an insecure channel. But how do you _really_ know who you are performing the key exchange with?

Imagine you want to connect to `your-bank.com`. Without a way to verify the server's identity, you are vulnerable to a **Man-in-the-Middle (MITM)** attack. An attacker could set up a fraudulent server, intercept your connection attempt to the bank, and position themselves between you and the real bank server.

The attacker would then perform two separate Diffie-Hellman exchanges: one with you, and one with the real bank. To you, it would appear you have a secure connection to your bank. To the bank, it would appear they have a secure connection with you. In reality, the attacker is decrypting every message from you, reading your password, and then re-encrypting the message to send to the bank.

This is the fundamental problem of trust online. How do you verify the identity of the server you're connecting to? This is where digital certificates come in—they are the foundation of trust on the internet, designed specifically to defeat this kind of impersonation attack.

### What is a Digital Certificate?

Think of a digital certificate as a passport or an ID card for a website. It is a small digital file that cryptographically binds an identity (like the domain name `www.google.com`) to a public key. This certificate is issued by a trusted third party called a **Certificate Authority (CA)**.

The primary standard for digital certificates is **X.509**. When we talk about digital certificates, we are almost always referring to X.509 certificates.

A certificate allows a server to prove its identity to you, the client, _before_ the secure channel is established. It answers the question, "Is the public key I am about to use for a key exchange _actually_ owned by who I think it's owned by?"

### The Chain of Trust: Certificate Authorities (CAs)

How do you know you can trust a certificate? You don't have to personally know every website owner. Instead, your computer's operating system and your web browser come with a pre-installed list of globally trusted Certificate Authorities. This is called the **Root Store**.

When a CA issues a certificate, it digitally "signs" it using its own private key. Your browser can then use the CA's public key (which it already has in its root store) to verify this signature. If the signature is valid, your browser trusts that the certificate is authentic and was indeed issued by that CA to the specified domain.

This creates a **chain of trust**:

1. **Root CA Certificate:** A self-signed certificate from a highly-trusted CA (like Let's Encrypt, DigiCert, or GlobalSign) that lives in your browser's root store. The private keys for these are among the most securely guarded secrets in the world.
2. **Intermediate CA Certificate:** For security and administrative reasons, root CAs don't typically sign server certificates directly. They sign certificates for "intermediate" CAs.
3. **Server Certificate:** The intermediate CA then signs the certificate for the end-user's server (e.g., `www.example.com`).

When your browser receives a server certificate, it checks the entire chain. It verifies that the server certificate was signed by the intermediate, and that the intermediate was signed by a root CA it trusts. If this chain is intact and valid, the lock icon appears in your address bar.

![ssl-chain-of-trust-chart-1024x934-1181006810.png](attachment:ce9fc5db-c697-4c82-84a0-30137bc33368:ssl-chain-of-trust-chart-1024x934-1181006810.png)

### What's Inside a Certificate?

An X.509 certificate isn't just a public key. It contains a wealth of information, including:

- **Subject:** The identity the certificate belongs to (e.g., the Common Name, CN, might be `www.google.com`).
- **Issuer:** The entity that signed and issued the certificate (e.g., an Intermediate CA).
- **Public Key:** The public key of the subject. This is the key the client will use to initiate secure communication.
- **Validity Period:** A "Not Before" and "Not After" date, defining the period during which the certificate is considered valid.
- **Serial Number:** A unique identifier for this specific certificate, assigned by the issuer.
- **Signature Algorithm:** The algorithm used by the CA to sign the certificate.
- **Digital Signature:** This is the most critical part for verification. The CA creates a hash of the certificate's contents and then encrypts that hash with its own private key. This is the digital signature.

### Try it yourself

You can inspect the certificate of any HTTPS website right from your browser.

1. Navigate to a secure website like `https://www.google.com`.
2. Click the padlock icon in the address bar.
3. Look for an option like "Connection is secure," which should open a small dialog.
4. Find and click on "Certificate is valid" (or a similar option).
5. A new window will appear, allowing you to view the certificate details. Click through the "Details" and "Certification Path" tabs to see the fields discussed above and the chain of trust.

### Introduction to TLS (Transport Layer Security)

Establishing trust with a certificate is only the first step. Once you've verified the server's identity, you need to secure the actual communication channel. This is the job of **Transport Layer Security (TLS)**, the protocol that uses certificates to build a secure connection. You may have heard of its predecessor, **SSL (Secure Sockets Layer)**, but SSL is now obsolete and should not be used.

TLS is a **hybrid encryption system**. It intelligently combines the strengths of both asymmetric and symmetric cryptography to provide security and performance.

- **Asymmetric Cryptography** is used at the beginning of the connection (the "handshake"). Its main roles are to **authenticate** the server using its certificate and to securely **negotiate** a shared secret key. Because asymmetric encryption is computationally slow, it is not used for the bulk data transfer.
- **Symmetric Cryptography** is used for the actual communication after the handshake is complete. The shared secret key negotiated during the handshake becomes the session key for a fast, efficient symmetric algorithm (like AES). All application data is encrypted with this key.

This hybrid approach gives us the best of both worlds: the trust and key-exchange capabilities of asymmetric cryptography, and the speed of symmetric cryptography.

TLS provides three main security guarantees:

1. **Authentication:** The server certificate proves the server's identity to the client. (Client certificates also exist but are less common).
2. **Confidentiality:** All data exchanged between the client and server is encrypted, preventing eavesdroppers from reading it.
3. **Integrity:** Data cannot be secretly modified in transit. TLS uses a mechanism called a Message Authentication Code (MAC) to ensure that the data you receive is exactly the data that was sent.

### The TLS Handshake: A Simplified Look

Before any application data (like an HTTP GET request) is sent, the client and server must perform a **TLS Handshake**. This is a negotiation to establish a secure session. Here's a simplified version of the process:

1. **ClientHello:** The client sends the first message. It says, "Hello, I'd like to connect securely. Here are the TLS versions and cipher suites (encryption/hashing algorithms) I support."
2. **ServerHello:** The server responds. It says, "Great. From the options you gave me, let's use this specific TLS version and this specific cipher suite. Here is my digital certificate."
3. **Client-Side Verification & Key Exchange:**
    - The client examines the server's certificate: Is it expired? Does the subject name match the website address? Is the signature from a trusted CA? This step prevents the MITM attack.
    - If the certificate is valid, the client and server perform a key exchange (often using the Diffie-Hellman algorithm). They use the server's authenticated public key to securely negotiate a brand new, temporary **symmetric session key** that only they will know.
4. **Finished:** Both client and server send a "Finished" message, which is encrypted with the newly created session key. This confirms that the handshake was successful and not tampered with.

From this point on, all application data between the client and server is encrypted using the symmetric session key.

### Think about it

Why do the client and server go through the trouble of negotiating a new symmetric session key? Why not just encrypt all the data with the server's public key? (This question should be easier to answer now!).

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-2-Session-3-Digital-Certificates-TLS-bb1gflv3stq8yg5?mode=doc](https://gamma.app/docs/Module-2-Week-2-Session-3-Digital-Certificates-TLS-bb1gflv3stq8yg5?mode=doc)

Try not to peek before class - spoilers inside!

</aside>