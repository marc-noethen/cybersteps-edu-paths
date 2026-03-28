Welcome to your introduction to one of the most persistent and effective threats in cybersecurity: **Social Engineering**. Before our live session, please review the following materials. This will give you the foundational knowledge we'll build upon with practical demonstrations and discussions in class.

## What is Social Engineering?

At its core, **social engineering** is the art of psychological manipulation. Instead of trying to break through complex digital defenses like firewalls or encryption, an attacker targets the weakest link in any security system: **the human being**. The goal is to trick, manipulate, or persuade someone into divulging confidential information or performing an action that compromises security. Think of it as "hacking the human."

An attacker might want several things:

- **Credentials & Access**: Usernames and passwords are the keys to the kingdom. Gaining access to an employee's account is often the first step in a larger attack.
- **Money**: Tricking someone into making a fraudulent wire transfer or paying a fake invoice is a common goal. Ransomware, which encrypts files and demands payment, often starts with a social engineering lure.
- **Information**: This could be Personally Identifiable Information (PII) like social security numbers, valuable intellectual property (e.g., source code, business plans), or even state secrets.
- **Disruption**: Sometimes, the goal is simply to cause chaos, damage a company's reputation, or disrupt their operations.

Why do attackers focus on people? **Because it works**. It's often easier and cheaper to trick a person than to find and exploit a complex software vulnerability. A single mistake by a well-meaning employee can bypass millions of dollars worth of security technology.

## The Psychology of Influence

![Screenshot 2025-09-19 at 20.29.29.png](attachment:fcfab4cf-7572-48f6-b257-337ad64f668c:Screenshot_2025-09-19_at_20.29.29.png)

Social engineers are masters of exploiting predictable human behaviors and psychological triggers. Understanding these principles is the first step to defending against them.

- **Authority**: We are culturally trained to respect and obey authority figures. An attacker might impersonate a CEO, an IT support technician, or a police officer to make their requests seem legitimate and non-negotiable.
- **Urgency**: Attackers create a false sense of a time-sensitive crisis to rush their targets into making mistakes. Phrases like "Your account will be suspended in 24 hours" or "This invoice is overdue" prevent the victim from stopping to think critically.
- **Trust & Familiarity**: An attacker might pretend to be a colleague, mention a mutual acquaintance, or use information gathered from social media to build a false sense of rapport and lower the victim's guard.
- **Consensus (Social Proof)**: People tend to do what they see others doing. An attacker might claim, "Everyone on your team has already updated their credentials on this new portal," making the request seem normal and safe.
- **Scarcity**: This principle creates the illusion that something is in short supply, which increases its perceived value. "This is a limited-time offer!" or "There are only two spots left" are classic examples used to pressure people into immediate action.
- **Intimidation**: Using aggressive language or threats, an attacker can frighten a target into complying with their demands.

## Common Attack Techniques

![image.png](attachment:ad70ab95-a1f3-4159-9b50-c2e430b2e52d:image.png)

These psychological principles are put into action through various techniques:

- **Phishing / Spear Phishing**: Sending emails that appear to be from a legitimate source to trick users into revealing sensitive information or clicking malicious links. Phishing is a broad attack, while Spear Phishing is highly targeted at a specific individual or organization.
- **Vishing / Smishing**: These are variations of phishing that use voice calls (Vishing) or SMS text messages (Smishing) as the delivery method.
- **Baiting**: Luring a victim by offering something enticing. The classic example is leaving a malware-infected USB drive labeled "Salaries" in a public place for a curious employee to find and plug into their computer.
- **Tailgating**: Physically following an authorized person into a restricted area. The attacker might pretend to be on a phone call or carry boxes to seem legitimate and encourage the person in front to hold the door open for them.

### Think about it

Have you ever received a suspicious email, text message, or phone call? What details made it seem "off"? Which of the psychological principles above might the sender have been trying to use on you?

## Passwords: The Ultimate Target

Most social engineering attacks are ultimately aimed at stealing one thing: **your password**. A password is a key that can unlock access to your email, bank accounts, company data, and more. Because people often reuse passwords, stealing one can open the door to many different systems.

## How Passwords Are Stored: Hashing and Salting

When you create a password for a website, they (should) never store it in plain text. If an attacker breached their database, they would instantly have everyone's passwords. Instead, services store a **hash** of your password.

A **hash function** is a one-way mathematical algorithm that takes an input (your password) and produces a fixed-length string of characters, called a hash.

- **It's a one-way street**: It's easy to compute the hash from the password, but it is computationally impossible to go backward and recover the original password from the hash.
- **It's consistent**: The same input will always produce the same output hash.

![image (33).png](attachment:7bec51ff-c2dc-4073-b3be-3c198a76a1b6:4d9c87b5-f444-4f0d-aabb-1a28b5eda764.png)

When you log in, the system takes the password you just typed, hashes it, and compares that new hash to the one stored in its database. If they match, you're in! This way, the service can verify your password without ever knowing what it is.

![image (34).png](attachment:640e9d7d-7bce-4938-8e98-3b582742ea29:image_\(34\).png)

### Think about it

If hashing is a "one-way street," how can attackers possibly crack them after stealing a database? Attackers can't "reverse" the hash. Instead, they use brute force, dictionary attacks, or pre-computed "rainbow tables". They take a common password (like `password123`), hash it themselves, and see if that hash appears anywhere in the stolen database. They repeat this millions of times per second.

This reveals a major flaw with hashing alone. If two users have the same password (`GoBlue!`), it will produce the exact same hash (`a3f8e4d2...`). Once an attacker cracks that hash for one user, they instantly know the password for every other user who has the same hash.

To solve this, we use **salting**. A salt is a unique, random string of characters that is added to each user's password _before_ it gets hashed. The salt is then stored alongside the hashed password in the database.

- `User1's password`: `GoBlue!` + `Salt1`: `abc789` -> **Hash A**
- `User2's password`: `GoBlue!` + `Salt2`: `xyz123` -> **Hash B**

Now, even though both users have the same password, the resulting hashes are completely different. This forces an attacker to crack each password individually, making pre-computed rainbow tables useless and dramatically increasing the time and cost of an attack.

![image (31).png](attachment:98db81b3-1885-46fa-afd1-b271261ba462:image_\(31\).png)

### Try it yourself

Go to an online hash generator like [this one](https://emn178.github.io/online-tools/md5.html).

1. Type a simple password, like `football`, into the input box. Look at the MD5 hash it generates.
2. Now, add a "salt" to it. Type `footballaBc123` into the box. Notice how completely different the hash is.
3. Change the salt slightly to `footballaBc124`. Again, the hash is completely different. This demonstrates how salting ensures that even identical passwords produce unique hashes, providing much stronger security.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-3-Session-1-Social-Engineering-ftyb5dmdhiwa69i?mode=doc](https://gamma.app/docs/Module-2-Week-3-Session-1-Social-Engineering-ftyb5dmdhiwa69i?mode=doc)

Try not to peek before class - spoilers inside!

</aside>