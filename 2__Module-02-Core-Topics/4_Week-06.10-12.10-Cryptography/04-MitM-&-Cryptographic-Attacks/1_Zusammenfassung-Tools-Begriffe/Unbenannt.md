Welcome! In our previous sessions, we explored how cryptography builds a shield to protect our data. We learned about powerful tools like AES for symmetric encryption, RSA for asymmetric encryption, and SHA-256 for hashing. These are the building blocks of modern digital security.

However, a shield is only as strong as the person wielding it and the environment it's used in. In cybersecurity, we must not only understand how to build defenses but also how attackers try to tear them down. This lesson focuses on **cryptographic attacks**: the methods adversaries use to bypass, weaken, or break cryptographic protections.

It's important to understand that most successful attacks don't involve "breaking" the core mathematical algorithm (like finding the private key for a modern RSA encryption). That's usually incredibly difficult. Instead, attackers are clever and look for weaker links in the chain: outdated protocols, flawed implementations, or human error.

## The Attacker's Mindset

An attacker's goal is to undermine one or more of the core principles of cryptography:

- **Confidentiality:** To read the secret message.
- **Integrity:** To change the message without detection.
- **Authenticity:** To impersonate one of the parties.
- **Non-repudiation:** To allow a sender to falsely deny they sent a message.

They do this by exploiting vulnerabilities in how cryptography is applied.

### Man-in-the-Middle (MITM) Attacks

![image.png](attachment:68f2f9bb-ee7e-4152-b232-62a3094b98e2:image.png)

A Man-in-the-Middle (MITM) attack is a foundational concept for many other attacks. In a MITM attack, the adversary secretly positions themselves between two parties who believe they are communicating directly with each other. Imagine Alice wants to send a secret message to Bob. An attacker, Mallory, intercepts the communication. Mallory can now read, modify, and relay messages between Alice and Bob without either of them knowing. Alice thinks she's talking only to Bob, and Bob thinks he's talking only to Alice, but Mallory controls the entire conversation.

The attacker needs a way to insert themselves into the communication flow. Common vectors for establishing this position include:

- **Unsecured Public Wi-Fi:** An attacker can set up a malicious Wi-Fi hotspot (e.g., named "Free_Airport_WiFi") and intercept the traffic of everyone who connects.
- **ARP Spoofing:** On a local network, an attacker can send fake ARP (Address Resolution Protocol) messages to associate their MAC address with the IP address of the network's gateway. All traffic from devices on the network to the internet will then flow through the attacker's machine.
- **DNS Spoofing:** An attacker can corrupt a system's DNS cache to redirect traffic. When a user tries to go to `mybank.com`, the attacker's fake DNS response points them to a malicious server's IP address instead of the real one.

The MITM position is the launchpad for many of the attacks we'll discuss below.

### Downgrade Attack

![image.png](attachment:11db1217-faf5-4e96-ab5b-f3bd75f27022:image.png)

A downgrade attack is a clever trick used by an attacker in a Man-in-the-Middle position. Instead of trying to break the strong, modern encryption being used, the attacker forces the two parties to "downgrade" to an older, less secure version of the protocol that the attacker _can_ break.

A common example is an **SSL Stripping Attack**. When you try to connect to a secure website (`https://`), a MITM attacker intercepts your request. They then establish an unencrypted (`http://`) connection with you, while maintaining the secure (`https://`) connection with the website themselves. To you, it might look like the site is just not using HTTPS, but in reality, the attacker is sitting in the middle, reading all your traffic in plain text.

### Real-World Example: The Public Wi-Fi Threat

SSL Stripping is most dangerous on public Wi-Fi networks. An attacker sets up a laptop as a rogue access point with a plausible name like "Cafe_Guest_WiFi". When you connect, all your traffic goes through their machine. You try to visit your bank's website. Your browser sends a request to `http://mybank.com` (which is standard, as the initial request is often unencrypted before being redirected). The attacker intercepts this, forwards it to the bank to establish a fully secure `https` connection for themselves, but sends an unencrypted `http` version back to you. Your browser's lock icon disappears, but many users don't notice, and proceed to log in, sending their credentials in plain text straight to the attacker.

### Think about it

How might your browser warn you that a downgrade attack could be in progress? What visual cues does it provide?

### Hash Collisions and the Birthday Attack

![image.png](attachment:f5e08a03-9c78-41b5-9207-cbd311c8f8d1:image.png)

As we've learned, a hash function takes an input (of any size) and produces a fixed-size string of characters, known as a hash digest. A critical property of a good hash function is **collision resistance**—it should be computationally infeasible to find two different inputs that produce the exact same hash output. A **collision attack** is an attempt to find two such inputs.

This is where the **Birthday Attack** comes in. It's not an attack on birthdays, but a strategy based on a statistical phenomenon called the "Birthday Paradox." The paradox states that in a group of just 23 people, there is a over 50% chance that two of them share a birthday. This same probability principle can be applied to hash functions. It is statistically much easier to find _any two_ inputs that collide than to find an input that collides with a _specific, pre-determined_ hash. This makes finding hash collisions much more practical than you might think, especially for older, weaker hash functions like MD5 and SHA-1.

### Real-World Example: The Flame Malware

A spectacular real-world example of a hash collision attack was used by the **Flame** malware, a highly sophisticated cyber-espionage tool discovered in 2012. The creators of Flame wanted their malware to appear as a legitimate Microsoft software update. To do this, they needed a valid digital certificate from Microsoft.

They found an old Microsoft signing certificate that still used the broken MD5 hash algorithm. Using a powerful "chosen-prefix collision attack," they crafted a fake, malicious certificate that produced the _exact same MD5 hash_ as a legitimate certificate they created. They submitted the legitimate certificate to Microsoft's automated systems, which signed it. Because the hashes matched, this signature was also valid for their malicious certificate. Flame could then use this forged certificate to spread through networks via the Windows Update mechanism, fooling computers into thinking it was a genuine patch from Microsoft.

### Try it yourself

Several websites let you see hash functions in action. Go to an online hash generator, type in some text, and see the MD5 and SHA-256 hashes it produces. Now, try to make a tiny change to your input text (add a space, change a letter). How dramatically does the output hash change? This property is known as the "avalanche effect."

### Replay Attack

A replay attack is deceptively simple. The attacker intercepts a stream of data and then re-transmits it later to impersonate the original sender or to trigger an action again. If a system is not designed to prevent this, it will see a valid (though old) request and grant access or perform an action.

### Real-World Example: Keyless Car Theft

Early remote keyless entry (RKE) systems for cars were vulnerable to simple replay attacks. When a driver pressed the "unlock" button on their key fob, it sent a specific radio signal. An attacker could use a simple radio device to record this signal from a distance. Later, the attacker could return to the car and simply "replay" the captured signal, and the car's doors would unlock.

To prevent this, modern cars use **rolling codes**. Each time the button is pressed, the fob sends a different, new code. The car knows the sequence of expected codes and will not accept an old one. This stops simple replay attacks, but has led to more advanced versions like the **RollJam** attack, where an attacker jams the signal while simultaneously capturing it, tricking the user into pressing the button twice and giving the attacker a fresh, unused code to use later.

To prevent replay attacks in computer systems, we use mechanisms like:

- **Timestamps:** The server rejects messages that are too old.
- **Nonces (Number used once):** A unique, random number is included in each request. The server keeps track of nonces it has seen and rejects any that are repeated.
- **Session IDs:** A unique token is generated upon login that must be used for all subsequent requests.

These defenses ensure that even if an attacker captures the data, it will be invalid for a later transaction.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-2-Session-5-Cryptographic-Attacks-6y4dcfac010webw?mode=doc](https://gamma.app/docs/Module-2-Week-2-Session-5-Cryptographic-Attacks-6y4dcfac010webw?mode=doc)

Try not to peek before class - spoilers inside!

</aside>