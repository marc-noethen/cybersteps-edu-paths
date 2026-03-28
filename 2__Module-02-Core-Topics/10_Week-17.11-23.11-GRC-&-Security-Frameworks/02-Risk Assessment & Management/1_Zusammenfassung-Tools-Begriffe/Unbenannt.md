Welcome to your pre-class preparation. In our last session, we introduced the concept of Governance, Risk, and Compliance (GRC). This session, we dive deep into the "R" - **Risk**.

Understanding risk is arguably the central function of any cybersecurity program. We don't implement firewalls, write policies, or hunt for malware just for fun; we do it to **manage risk**. This pre-class material will introduce you to the core concepts of risk management, how to perform a risk assessment, and a formal, widely-used methodology called the Risk Management Framework (RMF).

### What is Risk?

In everyday life, risk is the chance that something bad will happen. In cybersecurity, we have a more formal definition. A **risk** is the potential for loss, damage, or destruction of an asset as a result of a **threat** exploiting a **vulnerability**.

This definition has a few key components:

- **Asset:** Anything of value to the organization. This isn't just physical hardware like a laptop or server. The most important assets are often intangible, such as:
    - **Data:** Customer lists, credit card numbers, intellectual property (e.g., secret source code).
    - **Systems:** A payment processing application, an e-commerce website.
    - **Reputation:** The trust your customers have in you.
- **Vulnerability:** A weakness or gap in a security program that can be exploited by a threat.
    - _Example:_ An unpatched server running an old version of Windows.
    - _Example:_ A poorly trained employee who will click on any email link.
    - _Example:_ A server room without a lock on the door.
- **Threat:** Any person or event that has the potential to cause harm to an asset. Threats can be:
    - **Adversarial:** A hacker, a malicious insider, a script kiddie.
    - **Accidental:** An employee accidentally deleting the wrong database.
    - **Environmental:** A fire, flood, or power outage.

Risk exists at the intersection of these three things. You can have a vulnerability (an unlocked door), but if there is no threat (no one ever walks by), there is no risk. You can have a threat (a skilled hacker), but if you have no vulnerabilities, there is very little risk.

### Think about it

Think about your smartphone. What are the **assets** on it (photos, banking app access, contacts)? What are some **vulnerabilities** (no passcode, old operating system, connecting to untrusted public Wi-Fi)? What are the **threats** (a thief, a hacker on the Wi-Fi)?

### The Risk Management Process

**Risk Management** is the ongoing process of identifying, assessing, responding to, and monitoring risks to an organization's assets. It's a continuous cycle, not a one-time task. The goal is not to _eliminate_ all risk—that's impossible. The goal is to reduce risk to an **acceptable level**.

This process generally follows four phases:

1. **Frame Risk:** Establish the context for risk-based decisions.
2. **Assess Risk:** Identify, analyze, and evaluate risks.
3. **Respond to Risk:** Decide what to do about the identified risks.
4. **Monitor Risk:** Continuously track risks and the effectiveness of controls.

Today, we'll focus on the "Assess" and "Respond" phases.

### Risk Assessment: How to Find and Measure Risk

![image.png](attachment:e6d92b87-d292-4203-b768-2c4d3105d1cb:image.png)

A **Risk Assessment** is the specific procedure used to identify and analyze risks. This is how you find out what you should be most worried about. It helps you prioritize your time, money, and effort.

There are two main ways to analyze risk:

1. **Qualitative Risk Analysis:** This is the most common approach. It's subjective and uses descriptive ratings like **High, Medium, or Low**. You typically determine the rating by using a **risk matrix**, which plots the **Likelihood** of the risk happening against the **Impact** it would have.
    
    - **Impact:** The amount of harm or damage a risk would cause (e.g., Low = minor inconvenience, High = business-ending event).
    - **Likelihood:** The probability or frequency of a threat exploiting a vulnerability (e.g., Low = very unlikely, High = almost certain).
    
    **Example Risk Matrix:**
    
    ![Screenshot 2025-10-31 at 20.23.32.png](attachment:60c932ac-b178-4310-a629-99b97f42ea89:Screenshot_2025-10-31_at_20.23.32.png)
    
2. **Quantitative Risk Analysis:** This approach tries to assign a specific financial value (€) to risk, making it easier to justify security spending. It uses a few key formulas:
    
    - **Single Loss Expectancy (SLE):** How much money you would lose _each time_ a risk occurred.
        - _Formula:_ `SLE = Asset Value (€) * Exposure Factor (%)`
        - (The _Exposure Factor_ is the percentage of the asset's value lost).
    - **Annualized Rate of Occurrence (ARO):** How many times you expect this risk to occur per year.
        - _Example:_ A major data breach might have an ARO of 0.1 (once every 10 years). A phishing attempt might have an ARO of 50.
    - **Annualized Loss Expectancy (ALE):** Your total expected financial loss from this risk per year.
        - _Formula:_ `ALE = SLE * ARO`
    
    If you calculate that the ALE for a specific risk is €200,000, it becomes much easier to justify spending €50,000 on a security control to fix it.
    

### Try it yourself

Consider a small e-commerce website that stores customer names and email addresses (but not credit cards).

1. **Asset:** Customer email list.
2. **Vulnerability:** A SQL Injection (SQLi) vulnerability (which you'll learn about in a few weeks!) allows an attacker to dump the database.
3. **Threat:** An external hacker.
4. **Impact:** What would you rate the impact (Low, Medium, High)? Think about fines (like GDPR), loss of customer trust, and competitors getting the list.
5. **Likelihood:** If the vulnerability is known and easy to find, what is the likelihood (Low, Medium, High)?
6. **Overall Risk:** Using the matrix above, what is the overall risk rating?

### Risk Response: What to Do About Risk

![image.png](attachment:87462bd3-790f-4d7d-9d40-efa69f041927:image.png)

Once your assessment shows you have a "High" or "Critical" risk, you must respond. There are four main ways to respond to a risk:

1. **Mitigate (or Treat):** This is the most common response. You apply a **security control** to reduce the likelihood or impact of the risk.
    - _Risk:_ A hacker can access your server due to an unpatched vulnerability.
    - _Response:_ **Mitigate** the risk by applying the security patch.
2. **Transfer (or Share):** You shift the financial impact of the risk to a third party.
    - _Risk:_ A fire burns down your data center.
    - _Response:_ **Transfer** the risk by buying fire insurance. (Note: You still have to _recover_, but the financial cost is shared). Using a cloud provider (like AWS or Azure) is also a form of risk transfer.
3. **Accept (or Tolerate):** You formally acknowledge the risk and decide to do nothing. This is a valid business decision _if_ the cost of mitigating the risk is far greater than the potential impact, or the risk is already at an acceptable level (e.g., "Low"). This decision must be documented and approved by management.
    - _Risk:_ A meteor could strike your office.
    - _Response:_ **Accept** the risk. The likelihood is so low that it's not worth building a meteor-proof bunker.
4. **Avoid (or Terminate):** You stop performing the activity that causes the risk.
    - _Risk:_ A 15-year-old, unsupported server is constantly getting hacked.
    - _Response:_ **Avoid** the risk by decommissioning the server and shutting it down permanently.

### Think about it

Think about the risk of your personal laptop being stolen. How could you apply each of the four responses?

- **Mitigate:** ?
- **Transfer:** ?
- **Accept:** ?
- **Avoid:** ?

### Third-Party Risk Management (TPRM)

No organization exists in a vacuum. Modern companies rely on a complex network of external vendors, suppliers, and service providers. This is often called the **supply chain**.

- You use a cloud provider (like AWS, Azure, or Google Cloud) to host your servers.
- You use a payment processor (like Stripe) to handle transactions.
- You use a marketing company that has access to your customer list.
- Even the company that cleans your offices has physical access to your building.

**Third-Party Risk Management (TPRM)**, sometimes called Vendor Risk Management, is the process of identifying and reducing the risks associated with these external partners.

Your company's security is only as strong as its weakest link. If you have perfect security, but your marketing vendor (who has all your customer data) gets breached, _your_ data is still leaked.

The TPRM lifecycle involves:

- **Due Diligence:** Before signing a contract, you must vet the vendor's security practices. This often involves sending them a detailed security questionnaire.
- **Contract Management:** Ensuring the legal contract includes specific security requirements, such as the right to audit them or requirements to notify you of a breach.
- **Continuous Monitoring:** Periodically re-assessing the vendor's security to ensure they remain compliant, as their (and your) risk posture can change.

### A Formal System: The Risk Management Framework (RMF)

While the concepts above are universal, large organizations need a structured, repeatable, and documented process. The most famous of these is the **NIST Risk Management Framework (RMF)**, detailed in **NIST Special Publication 800-37**.

<aside> 📖

You can checkout RMF here: [https://csrc.nist.gov/projects/risk-management/about-rmf](https://csrc.nist.gov/projects/risk-management/about-rmf)

</aside>

The RMF is a seven-step process required for all U.S. federal government agencies and is widely adopted by private industry, especially those who work with the government. It provides a comprehensive lifecycle for managing cybersecurity risk.

Here are the 7 steps:

1. **PREPARE:** Get the organization ready to manage risk. This includes assigning roles (like a System Owner), identifying the types of systems you have, and establishing a risk management strategy.
2. **CATEGORIZE:** Formally categorize the system (e.g., a specific application or network) based on the **impact**(High, Medium, or Low) that a loss of **Confidentiality, Integrity, or Availability** would have. This is a crucial step defined in a document called **FIPS 199**, as a High-impact system (like one controlling a power grid) will require many more security controls than a Low-impact system (like a public information website).
3. **SELECT:** Based on the category from Step 2, you select a "baseline" set of security controls from a massive catalog: **NIST SP 800-53**. This catalog lists hundreds of controls, from "AC-1 (Access Control Policy)" to "RA-5 (Vulnerability Scanning)."

<aside> 📖

Read more: [https://csrc.nist.gov/projects/risk-management/sp800-53-controls](https://csrc.nist.gov/projects/risk-management/sp800-53-controls)

</aside>

1. **IMPLEMENT:** You and your teams (IT, developers, etc.) put the selected security controls in place. This is the "doing" phase—installing firewalls, writing policies, configuring systems securely.
2. **ASSESS:** An independent assessor (or a separate internal team) tests the security controls to see if they are implemented correctly and are effective. This is where you might see activities like penetration testing or security audits.
3. **AUTHORIZE:** A senior management official, known as the **Authorizing Official (AO)**, reviews the assessment results and all documentation. If they agree that the remaining risk is acceptable, they will issue an **Authority to Operate (ATO)**. This is a formal declaration that the system is approved to go live.
4. **MONITOR:** This is the continuous, ongoing step. You must continuously monitor the system and its controls, patch vulnerabilities, respond to incidents, and periodically re-assess risk. The RMF is a _cycle_, not a straight line.

We will cover these steps in more detail during the lesson, but for now, understand that the RMF is a formal, in-depth, and documentation-heavy _process_ for applying the risk management concepts we discussed earlier.

That's it for the pre-class reading! You've learned what risk is, how to assess it (qualitatively and quantitatively), how to respond to it, and the structure of a major formal framework (RMF). Please be ready to discuss these concepts in our live session.