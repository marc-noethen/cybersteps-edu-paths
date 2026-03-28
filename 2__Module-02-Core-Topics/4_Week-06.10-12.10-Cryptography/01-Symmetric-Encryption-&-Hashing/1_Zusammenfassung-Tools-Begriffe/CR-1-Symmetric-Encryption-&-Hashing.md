Welcome! In Module 1, you were introduced to the fundamentals of encryption and hashing. This week, we will dive deeper into applied cryptography, building from foundational concepts to the complex systems used in the real world. We'll start today with the essential tools—**Symmetric Encryption** for confidentiality and **Hashing** for integrity. Understanding these tools and their limitations, especially the 'key distribution problem,' is the critical first step. The rest of the week will be about solving the problems we uncover in this session.

### Core Principles Refresher

As a quick recap, our goal in cryptography is generally to provide some combination of the following guarantees, often called the **CIA Triad** plus one more crucial concept: **Non-repudiation**.

- **Confidentiality:** Keeping data secret from unauthorized parties. (Achieved via Encryption)
- **Integrity:** Ensuring data has not been altered. (Achieved via Hashing)
- **Availability:** Ensuring data is accessible when needed.
- **Non-repudiation:** Providing proof of an action, so that the entity that performed the action cannot deny it. For example, proving that a specific user sent a message or authorized a transaction. (Achieved via Digital Signatures)

This session will focus primarily on the tools for **Confidentiality** and **Integrity**. We will cover the mechanisms for non-repudiation, like digital signatures, in greater detail when we discuss asymmetric cryptography.

### A Deeper Look at Symmetric Encryption

![image.png](attachment:04c93a25-3399-4a10-bd44-6e1bbf3399b7:image.png)

You'll recall that symmetric encryption uses a **single, shared secret key** for both encryption and decryption. If you have the key, you can both lock and unlock the data. It's fast and efficient, making it the workhorse for encrypting large amounts of data.

**The Simplest Cipher: XOR** At its core, a symmetric cipher is just a reversible mathematical operation that uses a key. The simplest example is the XOR cipher. The XOR (exclusive OR) operation is a basic logical function that takes two inputs. The rule is simple: if the inputs are the same, the output is 0; if they are different, the output is 1.

The magic of XOR is that it's its own inverse: `Plaintext XOR Key = Ciphertext`, `Ciphertext XOR Key = Plaintext`

This is a perfect, simple symmetric cipher. The same key locks and unlocks the data. However, it's very insecure on its own, as we'll discuss in class.

**Better Solutions: Stream and Block Ciphers** To create stronger ciphers, cryptographers developed two main approaches: **stream ciphers** and **block ciphers**.

- **Stream Ciphers:** These operate like a very long, complex XOR key. They generate a continuous stream of pseudo-random bits (the keystream) and XOR it with the plaintext one bit at a time. They are very fast and are often used for real-time communication like video calls.
- **Block Ciphers:** These operate on fixed-size chunks of data, called blocks. The **Advanced Encryption Standard (AES)** is the most famous block cipher. It takes a block of data (16 bytes for AES) and puts it through many rounds of complex mathematical operations—including substitutions (replacing data), permutations (shuffling data), and mixing operations.

Using a strong algorithm like AES is critical, but it's only half the battle. As we'll see in class, the _way_ you apply it (its "mode of operation") is just as important for security.

The persistent challenge with all symmetric systems remains **secure key distribution**. If you and a friend need to communicate, how do you securely share the secret key to begin with? If an attacker intercepts the key, the entire system is compromised.

_For more reading about the history of AES in comic form checkout this [link](https://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html)_

### Try it yourself

Let's see the simple XOR cipher in action using CyberChef.

1. Navigate to [CyberChef](https://gchq.github.io/CyberChef/).
2. In the "Input" box, type a secret message, like `Attack at dawn!`.
3. In the "Recipe" pane, drag the "XOR" operation over.
4. In the "Key" field of the XOR recipe, type a simple secret key, like `secretkey`.
5. For the output format, choose `Hex`. Look at the output. Your message is now scrambled into unreadable hexadecimal characters. This is the ciphertext.
6. Now, to decrypt it, simply add another "XOR" operation to your recipe. Use the exact same key (`secretkey`).
7. The final output is now your original plaintext message, `Attack at dawn!`. You have successfully encrypted and decrypted a message with a symmetric key.

### Hashing for Integrity

![image.png](attachment:ffd2239a-0fec-4fa2-b572-f861930d329b:image.png)

You'll remember that a hash function creates a fixed-length "digital fingerprint" (e.g., `SHA-256`) for a piece of data. This is a **one-way** process; you cannot get the original data back from the hash by reversing the algorithm. Its primary purpose is to verify **integrity**.

A classic example is verifying a file download. After downloading a file, you can calculate its hash. If it matches the hash provided by the source, you can be sure the file is authentic and hasn't been altered.

This same principle is fundamental to how we handle passwords. Storing passwords in plaintext is extremely dangerous. Instead, systems store a hash of the user's password. When you log in, the system hashes the password you just typed and compares this new hash to the stored one. If they match, the system has verified the **integrity** of your password—it knows you provided the correct one—without ever needing to store or see the original secret. The hash acts as a secure, one-way reference to the original password.

A critical property for a secure hash function is **collision resistance**. A "collision" is when two different inputs produce the _exact same_ hash. Finding a collision should be practically impossible. Algorithms like **MD5** and **SHA-1** are considered broken because methods for creating collisions have been found. This is why we now use stronger algorithms from the **SHA-2** family (like `SHA-256`) and **SHA-3**.

**Rainbow Tables and the Power of Salting** While you can't reverse a hash, you can "pre-compute" them. Attackers create massive databases of common passwords and their corresponding hashes. These pre-computed databases are called **rainbow tables**. When an attacker gets a list of password hashes (for example, from a data breach), they don't try to "crack" each one individually. Instead, they just look up the hash in their table to find the original password.

So how do we defend against this? We use a **salt**.

A salt is a unique, random string that is added to a password _before_ it gets hashed. This salt is then stored in the database alongside the username and the final hash.

- **Without Salt:** `hash("password123")` -> `ef92b7...`
- **With Salt:** `hash("password123" + "aJd837bFgx")` -> `a45f01...`

When a user tries to log in, the system retrieves their unique salt from the database, adds it to the password they just entered, hashes the new combined string, and compares it to the stored hash.

This simple step completely defeats rainbow tables. Since every user has a different random salt, the hash for "password123" will be different for every user. An attacker's pre-computed table of hashes is now useless. They are forced back to cracking each password one by one, which is vastly more difficult and time-consuming.

![image.png](attachment:c6458504-300a-482c-877a-fe65840ce53b:image.png)

### Try it yourself

Let's see how salting defeats a hash lookup.

1. Navigate to an online SHA-256 generator, like [this one](https://emn178.github.io/online-tools/sha256.html).
2. In the input box, type `password123`. The generated hash is `ef92b778bafe771e89245b89ec5b8c55ba41af7f6370532d48c6823db9785898`. We know from before that this is easily found in a rainbow table.
3. Now, let's simulate adding a salt. In the input box, type `password123somerandomsalt`.
4. Copy the new hash. It will be completely different.
5. Try looking up this new hash on a site like [CrackStation](https://crackstation.net/). It will not be found. You have successfully defeated the rainbow table lookup!

### Obfuscation: Hiding in Plain Sight

Obfuscation is the process of making something intentionally difficult for humans to understand, usually source code. It is **not encryption**.

- **Encryption** makes data unreadable without a secret key, with the goal of **confidentiality**.
- **Obfuscation** just makes code messy and confusing, with the goal of **discouraging analysis**.

Think of it as taking a clear, simple recipe and rewriting it using bizarrely complex words and sentence structures. You could still figure it out with enough time and effort, but it would be a major headache. No secret key is needed to reverse it, just patience.

Obfuscation is often used on website code (JavaScript) to make it harder for people to copy or reverse-engineer. It offers a small hurdle for an attacker but provides no real security. It is a form of "security through obscurity," which should not be relied upon to protect sensitive information.

In summary, symmetric ciphers are our tool for confidentiality and hashing is our tool for integrity. While powerful, understanding their limitations is the first step toward building robust, secure systems.