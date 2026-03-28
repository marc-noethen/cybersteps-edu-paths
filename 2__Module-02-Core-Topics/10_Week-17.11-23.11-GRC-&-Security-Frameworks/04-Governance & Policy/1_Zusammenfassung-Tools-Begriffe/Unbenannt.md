Welcome to the pre-class preparation for our session on Governance and Policy. In our previous sessions, we've introduced the concepts of Governance, Risk, and Compliance (GRC). We've explored risk management and the legal/regulatory side of compliance.

This session focuses on the "G" (Governance) and the policy that brings governance to life. We will specifically look at one of the most influential frameworks used to structure cybersecurity governance: the **NIST Cybersecurity Framework (CSF)**.

## What is Governance?

In our GRC introduction, we defined governance as the set of rules, policies, and processes that direct and control an organization. Think of it as the "board of directors" or the "government" for an organization's cybersecurity program.

Governance answers the big questions:

- **Who is in charge?** (Establishes authority and accountability)
- **What is our goal?** (Sets the high-level strategy, e.g., "We must protect customer privacy above all else.")
- **How do we ensure we're on track?** (Defines oversight and measurement).

Governance isn't about configuring a firewall; it's about _deciding_ that firewalls are necessary, who is responsible for them, and how their effectiveness will be measured, all in alignment with the company's business goals.

## From Governance to Action: The Policy Hierarchy

![image.png](attachment:79c91f86-7ec2-45b6-8bf1-952f61645c6d:image.png)

A governance body (like a board or a security committee) doesn't write step-by-step instructions. They create high-level **Policies** to state their intent. But how does that intent turn into an actual action by an IT administrator? Through a policy hierarchy.

Understanding this hierarchy is one of the most critical parts of this topic.

### 1. **Policy**

**Purpose:** Defines **Why we must do this**

**What it is:** A high-level, mandatory statement from management that identifies the issue, scope, and intent. It does not give technical details or steps.

**Example:**

"All company data stored on mobile devices must be protected from unauthorized access."

### 2. **Standard**

**Purpose:** Defines **What is required**

**What it is:** A mandatory set of specific, measurable requirements that support the policy. Unlike policy, standards describe what must be enforced at a technical level.

**Example (supporting the policy):** "All company-issued smartphones must use a minimum 6-digit PIN and have remote wipe enabled."

### 3. **Procedure**

**Purpose:** Explains **How do I do it**

**What it is:** A step-by-step, detailed instruction set that operational staff follow. This is the “do X, then click Y” part.

**Example:** "To configure an iPhone: 1. Open Settings. 2. Tap Face ID & Passcode. 3. Select ‘Turn Passcode On’. 4. Choose ‘6-Digit Numeric Code’. 5. Enter the code..."

### 4. **Guideline**

**Purpose:** Provides additional recommended guidance

**What it is:** A non-mandatory best practice. It helps people meet the standard or improve security beyond the minimum.

**Example:** "It is recommended that users set a complex alphanumeric passcode instead of only a 6-digit PIN for stronger protection."

## Think about it

Think about your home Wi-Fi network. Can you apply this hierarchy?

- **Policy:** "My home network must be secure from neighbors and attackers."
- **Standard:** "The Wi-Fi network must use WPA3 encryption and have a strong, non-default password."
- **Guideline:** "It's recommended to hide the network SSID to make it harder to find."
- **Procedure:** "1. Open a browser and navigate to 192.168.1.1. 2. Log in with the admin credentials. 3. Go to the 'Wireless Security' page. 4. Select 'WPA3-Personal'. 5. Enter the new password in the 'Passphrase' box. 6. Click 'Save'."

## The NIST Cybersecurity Framework (CSF)

Now that we understand governance and policy, we need a way to _organize_ it all. It would be chaotic if every company just made up its own security rules from scratch. This is where **frameworks** come in.

You've already been introduced to the idea of frameworks. The **NIST Cybersecurity Framework (CSF)** is one of the most respected and widely adopted frameworks in the world.

- **Who is NIST?** The U.S. National Institute of Standards and Technology. They are a non-regulatory government agency that creates standards and best practices for many industries, including cybersecurity.
- **What is the CSF?** It is a _voluntary_ set of standards, guidelines, and best practices to help organizations manage their cybersecurity risks.
    - Being "voluntary" means it's not a law like GDPR. No one is _forced_ to use it. Organizations _choose_ to use it because it's so effective.
- **What is its goal?** To provide a common, understandable language and a structured approach for managing cybersecurity. It helps everyone—from a technical engineer to the CEO—get on the same page.

<aside> 📖

Read more: [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)

</aside>

## Closer Look: The 6 Functions

The CSF is built around **six functions**. These are the 6 highest-level activities in any security program.

![image.png](attachment:f0733c9c-af1b-4c7b-8edf-3f1326e3c2df:image.png)

### The 6 Functions of the NIST CSF

1. **Govern (GV)**
    - **The Goal:** To establish the overall security strategy, direction, and accountability for the organization.
    - **The Question it Answers:** "Who is in charge, what are the rules, and are we aligned with the business?"
    - **Core Activities:** Establishing the cybersecurity strategy, creating policies, defining roles and responsibilities, and managing risk from a high level. It's the "brain" of the operation.
2. **Identify (ID)**
    - **The Goal:** Understand your organization, your assets, and your risks.
    - **The Question it Answers:** "What do I have, and what are my biggest problems?"
    - **Core Activities:** Asset Management (building an inventory of your data, hardware, and software), Risk Assessment (analyzing threats and vulnerabilities), and establishing a Governance strategy. You can't protect what you don't know you have.
3. **Protect (PR)**
    - **The Goal:** Implement safeguards to prevent or reduce the impact of a cybersecurity event.
    - **The Question it Answers:** "How can I stop an attack from succeeding?"
    - **Core Activities:** Access Control (who can access what?), Data Security (encryption, data integrity), Protective Technology (firewalls, antivirus, endpoint protection), and Security Awareness Training for employees.
4. **Detect (DE)**
    - **The Goal:** Discover the presence of an attacker or a security incident _as it happens_ or as quickly as possible.
    - **The Question it Answers:** "How do I know if I'm being attacked?"
    - **Core Activities:** Anomalies and Events (collecting logs from all your systems), Security Continuous Monitoring, and setting up detection processes (e.g., alerts from a SIEM).
5. **Respond (RS)**
    - **The Goal:** Take action once a security incident has been detected.
    - **The Question itAnswers:** "What do I do when I find an attacker?"
    - **Core Activities:** Response Planning (having an Incident Response plan _before_ you need it), Communications (who do you tell, when?), Analysis (figuring out what happened), Mitigation (stopping the bleeding), and Improvements.
6. **Recover (RC)**
    - **The Goal:** Restore normal operations and services that were impaired during an incident.
    - **The Question it Answers:** "How do we get back to business?"
    - **Core Activities:** Recovery Planning (having a Disaster Recovery plan), Improvements (learning from the incident to get better), and Communications (telling stakeholders you are back online).

## Tying It All Together

Let's see how Governance, Policy, and the NIST CSF work together.

- **Governance Goal:** The Board of Directors says, "Our company's reputation depends on our systems being available. We cannot afford a long outage."
- **NIST CSF Function:** This goal maps directly to the **Recover (RC)** function.
- **CSF Category/Subcategory:** The security team looks at the **Recover (RC)** function and finds the Category "Recovery Planning (RC.RP)".
- **Organizational Policy:** Based on this, management writes a high-level **Policy**: "The company must maintain a Disaster Recovery (DR) capability to restore critical systems within 24 hours of a declared disaster."
- **Organizational Standard:** The IT team then creates a **Standard**: "All critical systems must be backed up nightly to an off-site location. Full DR tests must be performed twice per year."
- **Organizational Procedure:** An engineer writes a **Procedure**: "How to conduct the semi-annual DR test: 1. Notify all stakeholders... 2. Log into the backup vault... 3. Begin restoration of servers A, B, and C..."

The NIST CSF provides the "shopping list" of best practices (the Core), and governance/policy is the process of deciding _which_ items on the list are most important for _your_ organization and _how_ you will implement them.

## Try it yourself

The best way to understand the CSF is to look at it.

1. Go to the official NIST CSF website: [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
2. Open the latest CSF 2.0 document
3. Review the document, see how the different parts of CSF we covered in this pre-class show in the document