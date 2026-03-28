Welcome to your pre-class reading for our session on Compliance and Regulation. In our last sessions, we explored GRC frameworks and risk management. Now, we shift our focus to the "C" in GRC: Compliance. This area is critically important because it moves from _recommendations_ (like many frameworks) to _requirements_ (like laws and standards).

Understanding compliance is essential for any cybersecurity professional. It is often the primary driver—and budget justification—for many of the security controls you will be hired to implement, manage, and monitor.

## What are Compliance and Regulation?

At first glance, these terms might seem interchangeable, but they have distinct meanings.

- **Regulation:** This is a rule or directive, typically backed by law, issued by a government or a statutory authority. Regulations are **mandatory**. They state _what_ must be done (and what must not be done) and often carry significant penalties for failure, including massive fines or even criminal charges.
- **Standard:** This is a set of specific, established requirements for a product, service, or process. Some standards are voluntary (like ISO 27001, which you can _choose_ to adopt). Others, like the one we'll study, are "quasi-mandatory." This means they aren't technically laws, but if you want to do a certain type of business (like accept credit cards), you are contractually obligated to follow them.
- **Compliance:** This is the act of adhering to, or proving adherence to, a set of rules, such as a regulation or a standard.

A simple way to think about it is:

- **Security** is the _practice_ of defending systems and data.
- **Compliance** is the _proof_ that your security practices meet the specific rules set by a third party.

### Think about it

Can an organization be secure, but not compliant? Can an organization be compliant, but not secure?

(The answer to both is yes. Think about why.)

## Closer Look: GDPR (General Data Protection Regulation)

The GDPR is arguably the most significant and comprehensive data privacy regulation in the world.

- **What is it?** A regulation from the European Union (EU) that went into effect in 2018.
- **Who does it protect?** It protects the personal data and privacy of all EU citizens and residents.
- **Who must comply?** Any organization, _anywhere in the world_, that collects or processes the personal data of EU residents. This "extraterritorial scope" is what makes it so powerful. A US company with EU customers must comply with GDPR.

<aside> 📖

Read more: [https://gdpr-info.eu/](https://gdpr-info.eu/)

</aside>

### Key GDPR Terminology

- **Personal Data:** Any information that can be used to identify a living person. This includes obvious things (name, email address, government ID number) and less obvious ones (IP address, cookie data, location data, biometric data).
- **Data Subject:** The individual person whose data is being collected or processed (e.g., you, the customer, the website visitor).
- **Data Controller:** The organization that determines the "purposes and means" of processing personal data. They decide _why_ and _how_ data is collected (e.g., the airline selling you a ticket).
- **Data Processor:** A separate organization that processes data _on behalf_ of the controller (e.g., the cloud provider that hosts the airline's booking system, or the email marketing company they use).
- **Data Protection Officer (DPO):** A role required in many organizations that acts as an independent advocate for data privacy and compliance.

### Core Principles and Rights

GDPR is built on seven key principles, including lawfulness, purpose limitation (only use data for the reason you stated), data minimization (collect only what is absolutely necessary), and integrity/confidentiality (which is where cybersecurity comes in).

It also grants powerful rights to data subjects, the most famous of which is the **Right to Erasure (Article 17)**, also known as the "Right to be Forgotten." This allows individuals to request that an organization delete all of their personal data in certain circumstances.

### GDPR and Cybersecurity: Article 32

For cybersecurity professionals, **Article 32: Security of Processing** is one of the most important. It doesn't give a simple checklist; instead, it requires the controller and processor to implement "appropriate technical and organisational measures" to ensure a level of security appropriate to the risk.

It specifically suggests:

- The pseudonymisation and encryption of personal data.
- The ability to ensure the ongoing confidentiality, integrity, availability, and resilience of processing systems (sound familiar? This is the CIA triad plus resilience).
- The ability to restore availability and access to data in a timely manner in the event of an incident (backing up your data).
- A process for regularly testing, assessing, and evaluating the effectiveness of security measures (vulnerability scanning, penetration testing).

### Penalties

Penalties for non-compliance are severe: up to **€20 million or 4% of the company's total global annual revenue**, whichever is higher. This is why companies take GDPR very seriously.

Checkout [https://www.enforcementtracker.com/](https://www.enforcementtracker.com/) for some past GDPR fines

### Try it yourself

Check out the following page [https://cloud.google.com/privacy/gdpr](https://cloud.google.com/privacy/gdpr). What GDPR Articles are mentioned?

## Closer Look: PCI-DSS (Payment Card Industry Data Security Standard)

PCI-DSS is a very different beast. It's not a law; it's a security _standard_ created and managed by the PCI Security Standards Council (PCI SSC), which was founded by the major credit card brands (Visa, Mastercard, American Express, etc.).

- **What is it?** A set of security requirements for protecting credit card data.
- **Who must comply?** Any organization that **accepts, processes, stores, or transmits** cardholder data. If your company takes credit card payments, you must comply with PCI-DSS. It is enforced through contracts with the card brands and banks.

<aside> 📖

Read more: [PCI-DSS Quick Reference Guide](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI-DSS-v4_x-QRG.pdf)

</aside>

### Key PCI-DSS Terminology

- **Cardholder Data (CHD):** At its core, this includes the **Primary Account Number (PAN)**—the long number on the front of the card. It also includes the cardholder's name, expiration date, and service code.
- **Sensitive Authentication Data (SAD):** This is even more sensitive data that _must never be stored_ after a transaction is authorized. This includes the full magnetic stripe data, the CVV (the three or four-digit code), and PINs.

### The 6 Goals and 12 Requirements

Unlike GDPR's high-level principles, PCI-DSS is extremely prescriptive. It is organized into 6 goals, which are broken down into 12 specific requirements.

- **Goal 1: Build and Maintain a Secure Network and Systems**
    - Req 1: Install and maintain firewall and router configurations.
    - Req 2: Do not use vendor-supplied defaults for passwords and other security parameters.
- **Goal 2: Protect Cardholder Data**
    - Req 3: Protect stored cardholder data.
    - Req 4: Encrypt transmission of cardholder data across open, public networks.
- **Goal 3: Maintain a Vulnerability Management Program**
    - Req 5: Protect all systems against malware and regularly update anti-virus.
    - Req 6: Develop and maintain secure systems and applications.
- **Goal 4: Implement Strong Access Control Measures**
    - Req 7: Restrict access to cardholder data by business "need to know."
    - Req 8: Identify and authenticate access to system components.
    - Req 9: Restrict physical access to cardholder data.
- **Goal 5: Regularly Monitor and Test Networks**
    - Req 10: Track and monitor all access to network resources and cardholder data.
    - Req 11: Regularly test security systems and processes.
- **Goal 6: Maintain an Information Security Policy**
    - Req 12: Maintain a policy that addresses information security for all personnel.

### PCI-DSS and Cybersecurity: Requirement 3.4

Let's look at a concrete example. **Requirement 3.4** is a classic:

> "Render PAN unreadable anywhere it is stored (including on portable digital media, backup media, and in logs) by using one of the following approaches:
> 
> - One-way hashes based on strong cryptography...
> - Truncation (hashing cannot be used for truncation)...
> - Index tokens and pads...
> - Strong cryptography with associated key-management processes..."

This is a direct instruction to a security or development team. You _must_ encrypt, hash, or truncate (e.t., show only the last 4 digits `************1234`) any stored credit card numbers. As a security analyst, you might be asked to run a scan to _find_ any unprotected card numbers on the network or in databases to ensure the company is compliant with this rule.

### Penalties

Failure to comply with PCI-DSS can result in large fines from the card brands, and in a worst-case scenario, the company's right to accept credit card payments can be revoked, which would be a business-ending event for many.

## Summary

You are now familiar with the two most important compliance regimes for a cybersecurity professional.

- **GDPR** is a broad, principles-based **regulation** (a law) focused on **personal data privacy** for EU citizens.
- **PCI-DSS** is a highly specific, prescriptive **standard** focused on **technical security controls** for **credit card data**.

Both drive a huge amount of cybersecurity work, from implementing encryption and access control to running vulnerability scans and responding to incidents.