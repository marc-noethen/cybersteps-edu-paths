Welcome to your pre-class preparation. In this session, we will build upon our understanding of social engineering to focus on one of its most common and impactful forms: phishing. We will dissect how these attacks work on a technical level and explore the fundamental defense mechanisms that organizations use to protect themselves and their employees.

### The Anatomy of a Phishing Email

![image.png](attachment:e6675a26-e196-42c4-a370-38f5671ede39:696393a3-a9a3-429d-b059-0d62891bdb2b.png)

At its core, a phishing email is a form of deception. The attacker's goal is to make a fraudulent email look as if it came from a legitimate, trustworthy source, like a bank, a popular online service, or even a colleague. The primary technical trick behind this is **email spoofing**, which is forging the "From" address of an email.

Imagine sending a letter through the postal service. You can write any return address you want on the envelope. The postal service's main job is to deliver the letter to the destination, not to verify that the return address is legitimate. The internet's email system, by its original design, worked similarly. This trust-based design is what attackers exploit.

To make the deception convincing, attackers focus on several key components:

- **Sender Address ("From" field):** This is the most commonly spoofed part. An attacker might make an email _appear_ to come from `security@yourbank.com` when it actually originated from a completely different, malicious server.
- **Subject Line:** Usually crafted to create a sense of urgency, curiosity, or fear (e.g., "Action Required: Your Account Has Been Suspended," "Urgent: Invoice Overdue").
- **Content:** The body of the email is designed to mimic the branding, tone, and formatting of the impersonated organization. This includes logos, standard email footers, and official-sounding language.
- **The Malicious Payload:** This is the part that does the damage. It typically comes in one of two forms:
    - **Malicious Link:** A hyperlink that directs the victim to a fraudulent website. This is often a **credential harvesting page**—a pixel-perfect copy of a real login page (e.g., for Microsoft 365, Google, or a bank) designed to steal the user's username and password.
    - **Malicious Attachment:** A file attached to the email that contains malware. Common examples include infected documents (.docm, .xlsm), compressed files (.zip, .rar), or disk images (.iso) that, when opened, execute malicious code to compromise the victim's computer.

### Common Phishing Variations

While "phishing" is a general term, attackers often use more targeted techniques:

- **Spear Phishing:** This is a highly targeted attack aimed at a specific individual or a small group within an organization. The attacker first conducts reconnaissance to gather personal information about the target (e.g., their name, job title, colleagues, recent projects). The email is then crafted to be extremely personal and believable, perhaps appearing to come from the target's direct manager or a trusted vendor. Because of this personalization, spear phishing attacks are much more difficult to detect and have a higher success rate.
- **Whaling:** This is a specific type of spear phishing that targets high-profile, senior executives (the "big fish" or "whales") such as CEOs, CFOs, or other C-level staff. The goal is often to trick the executive into making a high-value wire transfer or revealing sensitive corporate strategy. The pretext might be a confidential business deal or an urgent request from a lawyer.

### Spotting the Phish: Common Red Flags

Before diving into the technical headers, you can often identify a phishing attempt by looking for common warning signs.

- **Mismatched Link URL:** This is the most reliable indicator. Hover your mouse cursor over a link in the email _without clicking it_. Your email client or browser will show the actual destination URL. If the email says it's from `paypal.com`, but the link points to `secure-login-pp-81.xyz`, it's a phish.
- **Sense of Urgency or Threats:** Attackers try to make you panic and act without thinking. Be suspicious of language like "Your account will be suspended in 24 hours" or "Immediate action required."
- **Poor Spelling and Grammar:** While some phishing attacks are sophisticated, many are not. Legitimate corporations typically have teams of editors who review communications. Obvious spelling or grammar mistakes are a major red flag.
- **Generic Greetings:** An email from your bank that starts with "Dear Valued Customer" instead of your name is suspicious. Legitimate services you have an account with will almost always address you by name.
- **Unexpected Attachments:** Be extremely wary of attachments you weren't expecting, especially if they are `.zip`, `.exe`, or office documents that ask you to "Enable Macros" or "Enable Content."
- **Spoofed but "Slightly Off" Domain:** Attackers often register domains that look very similar to legitimate ones, a technique known as typosquatting. For example, `Lufthansa.com` vs. `Lufthansа.com` (with a Cyrillic 'a'). At a quick glance, they look identical.

### Under the Hood: Email Headers

![image.png](attachment:1a157eef-e759-45ad-89d7-2b4cc071c6b3:image.png)

Every email carries a set of hidden metadata called **headers**. These headers are like a digital passport, containing information about the email's journey from the sender to the recipient. While the "From" address you see in your email client can be easily faked, the headers provide a more detailed and harder-to-forge record of its origins.

One of the most important fields in the headers for security analysis is the **`Return-Path`** (sometimes called the "envelope sender"). This header specifies where bounce messages should be sent if the email can't be delivered. Often, the `Return-Path` address will reveal the true, underlying domain from which the email was sent, even if the "From" address is spoofed.

Another key header is **`Received`**. There are often multiple `Received` headers, and they form a chain of custody. Each time the email is passed to a new server on its way to you, that server adds a `Received` header to the top of the list. By reading these from bottom to top, you can trace the email's path back from your server to its origin. If an email _claims_to be from your company but the `Received` headers show it originated from a random server in another country, that's a major red flag.

### Try it yourself

Find a non-sensitive email in your inbox (like a marketing newsletter). Find the option to view the original message or its headers. In Gmail, you can click the three dots next to the reply button and select "Show original." In Outlook, you can open the email and go to `File > Properties`.

Look through the headers. Can you find the `Return-Path`? Can you identify the `Received` headers and see the names of the servers it passed through? Don't worry about understanding everything, just get comfortable with the idea that this data exists beneath the surface of every email.

### The Defenders: SPF, DKIM, and DMARC

Because the basic email system is so easy to abuse, a suite of security protocols has been developed to help verify a sender's identity and prevent spoofing. These are **SPF**, **DKIM**, and **DMARC**. They work together to build a chain of trust.

### Sender Policy Framework (SPF)

![image.png](attachment:38f410f5-e11c-4f15-a67d-5152e51ebed9:0a9dbc18-b7db-4655-8078-7d399a9945df.png)

- **What it is:** SPF is a way for a domain owner (e.g., `yourbank.com`) to publicly state which mail servers are allowed to send emails on its behalf.
- **How it works:** The domain owner publishes a special text (TXT) record in their Domain Name System (DNS) configuration. This record is a list of authorized IP addresses of mail servers. When your email server receives a message claiming to be from `yourbank.com`, it checks the DNS for the SPF record. It then compares the IP address of the server that sent the email to the list of authorized IP addresses in the SPF record.
- **Analogy:** SPF is like a bouncer at a club who has a guest list. If your name (the sending server's IP address) is on the list for a specific party (`yourbank.com`), you're allowed in. If not, you're rejected.
- **Limitation:** SPF on its own only validates the `Return-Path` domain, not the "From" address that the user sees. An attacker could pass an SPF check for their own malicious domain while still showing a spoofed "From" address to the victim.

### DomainKeys Identified Mail (DKIM)

![image.png](attachment:659bef93-543a-4327-afe6-2f9a0cc953a7:6d6a62a3-6975-4ffc-a5a6-99b853d0ff80.png)

- **What it is:** DKIM provides a way to "sign" an email, proving that it hasn't been tampered with in transit and that it genuinely came from the claimed domain.
- **How it works:** The sending mail server uses a private key to create a unique digital signature, which is then added as a header in the email. The corresponding public key is published in the domain's DNS records. When the receiving email server gets the message, it fetches the public key from the DNS and uses it to verify the signature. If the signature is valid, it proves two things: 1) The email came from a server with access to the private key, and 2) The signed parts of the email (like the body and key headers) haven't been altered.
- **Analogy:** DKIM is like a tamper-proof wax seal on a letter. The seal (the signature) proves that the letter came from the person with the unique signet ring (the private key) and that the envelope hasn't been opened and its contents changed.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

![image.png](attachment:a819deca-70c7-4a00-885b-c5d070d9e1f6:4cd98e5f-d1b4-4cd4-9df5-e7a3fe2a63a1.png)

- **What it is:** DMARC is the policy layer that ties SPF and DKIM together. It tells receiving email servers what to do if an email fails SPF or DKIM checks.
- **How it works:** Like SPF and DKIM, DMARC is a TXT record in a domain's DNS. This record tells receivers:
    1. **Alignment:** It requires that the domain in the user-visible "From" address aligns with (matches) the domain verified by SPF and/or DKIM. This is crucial for preventing spoofing.
    2. **Policy:** It specifies whether the receiver should `reject` the email, send it to `quarantine` (e.g., the spam folder), or do `none` (just monitor it).
    3. **Reporting:** It provides an address where receiving servers can send reports about which emails are passing and failing these checks. These reports are invaluable for an organization to monitor its email security and identify abuse of its domain.
- **Analogy:** DMARC is the manager of the club. It tells the bouncer (the receiving server) not just to check the guest list (SPF) and look for a proper invitation (DKIM), but also what to do with people who fail those checks—kick them out (`reject`) or move them to a waiting area (`quarantine`). It also asks the bouncer to send a daily report on who tried to get in.

Together, these three protocols create a powerful defense-in-depth system against email spoofing and are a cornerstone of modern email security.

### The Silent Guardian: Email Gateways and Filters

![image.png](attachment:84945027-8ad0-4633-b9a6-5748fe720fbc:image.png)

If billions of phishing emails are sent every day, why aren't our inboxes completely overwhelmed? The answer is a critical layer of defense called a **secure email gateway (SEG)** or, more simply, an email filter. Your personal email provider (like Gmail or Outlook) and virtually every corporation places a powerful filtering system in front of its mail servers.

These gateways act as a checkpoint for all incoming email, subjecting each message to intense scrutiny before it's ever delivered to your inbox. They use a wide array of techniques:

- **Reputation Filtering:** They check the IP address of the sending server against massive, constantly updated blacklists of known spam and malware sources. If the sender has a bad reputation, the email is blocked outright.
- **Signature-Based Filtering:** They scan attachments for signatures of known malware, much like traditional antivirus software.
- **Content Analysis:** The filters analyze the text of the email for suspicious phrases, links to known malicious domains, and other patterns commonly associated with phishing.
- **Heuristic and Behavioral Analysis:** Modern filters use machine learning to detect anomalies. They might flag an email for using unusual language, having a sense of urgency, or asking for credentials—even if it comes from a "clean" IP address and has no known malware.
- **Sandboxing:** For suspicious but not definitively malicious attachments, the gateway can open the file in a safe, isolated virtual environment (a "sandbox") to see what it does. If the file attempts to perform malicious actions (like encrypting files or contacting a command-and-control server), the gateway deletes the email.
- **Authentication Checks:** Crucially, these gateways are what perform the SPF, DKIM, and DMARC checks we discussed. A failed check is a strong signal that the email is fraudulent, and the gateway will act according to the DMARC policy.

Only after an email passes this gauntlet of tests is it delivered to the user. This is why your Spam or Junk folder exists—it's where the gateway puts emails that it deems suspicious but isn't 100% certain are malicious. The emails that are clearly bad are simply dropped and never seen at all.

### Try it yourself

Let's see these records in the wild. You can use online tools or your own terminal to look up the DNS records for a domain.

**Using the terminal:**

Open your terminal and use the `dig` command to look up the TXT records for a domain. These records are where SPF, DKIM, and DMARC policies are stored.

1. **Check for an SPF record:**
    
    ```
    dig txt google.com
    ```
    
    Look for a line in the output that starts with `"v=spf1..."`. This is Google's SPF record, defining which servers are authorized to send email for them.
    
2. **Check for a DMARC record:** DMARC records are stored under a specific name: `_dmarc.domain.com`.
    
    ```
    dig txt _dmarc.google.com
    ```
    
    You'll see a record starting with `"v=DMARC1..."`. Look at the policy tag (`p=`). What policy has Google set (`none`, `quarantine`, or `reject`)?
    
3. **Check for a DKIM record:** DKIM is a bit different. The record isn't just on the domain, but on a specific "selector" which is named in the email header. However, you can see an _example_ of a DKIM public key by looking up a selector for a domain. For Google, a one selector is `20230601`.
    
    ```
    dig txt 20230601._domainkey.google.com
    ```
    
    The long string of text you see after `"p="` is the public key used to verify DKIM signatures from Google's emails.
    

Pick another major domain (like `github.com` or `microsoft.com`) and try looking up its SPF and DMARC records. Do their policies differ from Google's?

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Module-2-Week-3-Session-3-Phishing-Attacks-Email-Defenses-q5lixlg5mwb2ea1?mode=doc](https://gamma.app/docs/Module-2-Week-3-Session-3-Phishing-Attacks-Email-Defenses-q5lixlg5mwb2ea1?mode=doc)

Try not to peek before class - spoilers inside!

</aside>