Welcome to the pre-class preparation for our session on OS Hardening & Security! The goal of this preparation is to introduce you to the fundamental concepts of securing an operating system. By understanding these principles, you'll be better equipped for our live session, where we'll dive deeper into practical applications and demonstrations.

## What is OS Hardening?

Operating System (OS) hardening is the process of configuring an OS securely to reduce its vulnerability to cyberattacks. Think of it like fortifying a castle: you want to minimize the number of entry points for attackers, strengthen the existing defenses, and ensure you can detect any attempts to breach them. By systematically reducing the "attack surface" – the sum of all potential vulnerabilities an attacker could exploit – we make the system more resilient.

Hardening an OS is a crucial proactive security measure. It's not about waiting for an attack to happen and then reacting; it's about making the system as difficult as possible to compromise in the first place. This aligns with the cybersecurity principle of "defense in depth," where multiple layers of security controls are implemented.

![image.png](attachment:6711e368-a554-4579-a5f2-113b20c54364:image.png)

## Key Principles of OS Hardening

Several core principles guide the process of OS hardening:

1. **Principle of Least Privilege:** This is one of the most fundamental concepts in security. It dictates that users, applications, and system processes should only be granted the minimum levels of access (or "privileges") necessary to perform their intended functions. If an account or process with excessive privileges is compromised, the attacker gains those same excessive privileges.
2. **Attack Surface Reduction:** This involves identifying and eliminating or disabling unnecessary software, services, user accounts, and network ports. Every active component is a potential entry point for an attacker; if it's not needed, it should be removed or turned off.
3. **Secure Configuration:** Operating systems and applications often come with default configurations that are not optimized for security. Secure configuration involves reviewing and adjusting settings to their most secure state, following best practices and established security guidelines (like CIS Benchmarks or Microsoft Security Baselines).
4. **Patch Management:** Software is rarely perfect and vulnerabilities are discovered over time. Patch management is the process of identifying, acquiring, testing, and installing software updates (patches) to fix these security flaws and other bugs. A robust patch management process is essential for closing known security holes before attackers can exploit them.
5. **Logging and Monitoring:** Comprehensive logging of system events (like user logons, administrative actions, errors, and security events) is vital. Regularly monitoring these logs helps in detecting suspicious activities, investigating security incidents, and ensuring compliance with security policies.

### Think about it

- If a user needs to run a specific application that requires administrator rights, but their daily tasks (like email and web browsing) do not, what would be a more secure approach than giving their main user account permanent administrator rights?

## Common Areas of OS Hardening (Windows Focus)

While the principles are universal, their implementation can vary between operating systems. Since this module focuses on Windows, we'll primarily discuss Windows-specific examples.

### User Account Management

Properly managing user accounts is critical.

- **Strong Password Policies:** Enforce rules for password complexity (e.g., length, use of uppercase, lowercase, numbers, symbols), how often passwords must be changed, and preventing the reuse of old passwords.
    
- **Default Accounts:** Be cautious with default accounts like "Administrator" or "Guest." It's good practice to rename the built-in administrator account (making it harder for attackers to guess) and ensure the guest account is disabled if not explicitly needed.
    
- **User Account Control (UAC):** UAC in Windows helps prevent unauthorized changes by prompting for confirmation or administrator credentials when an action requires elevated privileges. This acts as a safety check, limiting what malware can do silently.
    
- **Account Review:** Regularly review all user accounts. Ensure that only necessary accounts exist and that they have the minimum permissions required for their roles. Disable or remove accounts for users who no longer need access.
    
    ![image.png](attachment:75a7bcd4-09f6-4072-b7c5-4be339c33f60:image.png)
    

### Software Management

Unnecessary or outdated software can introduce vulnerabilities.

- **Uninstall Unnecessary Applications:** If software isn't needed for work or system operations, it shouldn't be on the system. Each program is a potential source of vulnerabilities.
- **Keep Software Updated:** This is a key part of patch management, applying not just to the OS, but to all installed applications (web browsers, office suites, PDF readers, etc.).
- **Application Control:** In some environments, organizations might implement policies to control which applications are allowed to run (whitelisting) or which are explicitly forbidden (blacklisting).

### Service Management

Operating systems run many background processes called "services." Not all of them are required for every system's specific role.

- **Disable Unnecessary Services:** Identify services that are not essential for the system's function and disable them. For example, if a computer isn't sharing printers, the "Print Spooler" service might be a candidate for disabling.
- **Understand Dependencies:** Be careful, as some services rely on others to work correctly. Disabling a service might unintentionally affect another needed function.

### Patch Management in Detail

As mentioned, patch management is critical. Software vendors like Microsoft regularly release patches to address security vulnerabilities, bugs, and sometimes to provide new features.

- **Vulnerability Discovery:** Security researchers, software vendors, and even malicious actors continuously find new flaws in software.
- **Patch Release:** Once a vendor develops a fix, they release it as a patch or update. For Microsoft Windows and other Microsoft products, these are often released on a well-known schedule.
- **"Patch Tuesday":** This is an unofficial term for the second Tuesday of each month, when Microsoft typically releases its security updates. System administrators worldwide anticipate this day to begin their patching cycles. While Microsoft can release "out-of-band" patches for critical vulnerabilities at any time, Patch Tuesday is the most consistent update release day.
- **Patching Process:** A good patching process involves:
    1. **Identification:** Knowing what systems and software you have and what patches are available.
    2. **Acquisition:** Downloading the correct patches from the vendor.
    3. **Testing:** Before deploying patches widely, especially in critical environments, they should be tested on a small group of non-critical systems. This is to ensure the patch doesn't cause unexpected problems with other software or system functions.
    4. **Deployment:** Rolling out the patches to all relevant systems. This can be done manually on individual machines or, more commonly in organizations, using automated tools like Windows Server Update Services (WSUS) or Microsoft Endpoint Configuration Manager.
    5. **Verification:** Confirming that patches have been successfully installed and systems are protected.

![image.png](attachment:c99a3817-b62f-4972-af4a-472499f54e6d:64708204-c778-4f99-a6ee-7065fffbdd66.png)

- **Importance of Timeliness:** Attackers often "reverse engineer" patches to understand the vulnerability they fix. They then try to exploit that vulnerability on systems that haven't been patched yet. This makes timely patching extremely important.

### Think about it

- Why is testing patches before widespread deployment a crucial step, even if the patch is from a trusted vendor like Microsoft?
- What could be the consequences of _not_ having a regular patch management process?

### Network Security

Protecting the system from network-based attacks is essential.

- **Host-Based Firewalls:** Windows includes Windows Defender Firewall, which acts like a guard, controlling network traffic entering and leaving the computer.
- **Firewall Rules:** Configure the firewall to allow only necessary network connections. For example, a web server needs to allow incoming web traffic (typically on ports 80 and 443), but might block other types of connections.
- **Disable Unused Network Protocols:** If older or less secure network communication methods (protocols) aren't needed, they should be disabled.

### File System Security

Controlling who can access files and folders is crucial.

- **NTFS Permissions (Windows):** Use file system permissions to control what users and groups can do with files and folders (e.g., read, write, delete, modify). Always apply the principle of least privilege.
- **Encryption:**
    - **BitLocker Drive Encryption:** This can encrypt the entire hard drive. If the computer or drive is lost or stolen, the data remains unreadable without the decryption key or password.
    - **Encrypting File System (EFS):** Allows individual files and folders to be encrypted, typically tied to a specific user's account.

### Security Policies

Windows uses security policies to define and enforce specific security settings.

- **Local Security Policy:** This tool (`secpol.msc`) allows administrators to configure many security settings on a single computer, such as password requirements, account lockout rules (e.g., locking an account after too many failed login attempts), and what actions are audited.
- **Group Policy:** In larger networks with a Windows domain, Group Policy is a powerful tool for centrally managing and enforcing security configurations across many computers.
- **Examples of Policies:**
    - **Audit Policy:** Determines which events are recorded in the security logs (e.g., successful and failed logon attempts).
    - **Password Policy:** Enforces rules for creating strong passwords.
    - **Account Lockout Policy:** Helps prevent brute-force password attacks by temporarily locking an account after a set number of incorrect password attempts.

### Logging and Auditing

Without a record of what's happening on a system, it's very difficult to detect or investigate security incidents.

- **Event Viewer (`eventvwr.msc`):** This Windows tool is used to view event logs. Key logs include:
    - **Security Log:** Records security-related events, such as logon attempts (successful and failed), and access to files or other resources, based on the audit policies configured. This log is critical for security monitoring.
    - **System Log:** Records events related to the Windows operating system itself, like services starting or stopping, or driver issues.
    - **Application Log:** Records events from installed applications.
- **What to Log:** Audit policies determine what gets recorded. It's a balance: logging too little means missing important events, but logging too much can create excessive "noise" and consume storage. Focus on logging events that are meaningful for security.
- **Key Event IDs:** Certain Event IDs in the Security log are particularly important. For example, Event ID 4624 indicates a successful logon, while Event ID 4625 indicates a failed logon. Knowing common, critical Event IDs helps in quickly identifying important security events.

![image.png](attachment:138d1f68-7e87-4b28-b16f-a0428fc25eef:image.png)

### Try it yourself

- On your Windows VM, open the **Local Security Policy** editor (type `secpol.msc` in the Start Menu search). Look at `Account Policies` -> `Password Policy`. What are the current settings? (Don't change anything yet!)
- Open **Event Viewer** (`eventvwr.msc`). Expand "Windows Logs" and click on the "Security" log. Can you find any recent logon events? Look for Event ID 4624 (successful logon) or 4625 (failed logon).

## Tools for OS Hardening

Many tools for OS hardening are built into Windows:

- **Windows Defender Firewall with Advanced Security**
- **Local Security Policy (`secpol.msc`)**
- **Services (`services.msc`)**
- **Event Viewer (`eventvwr.msc`)**
- **Programs and Features (for uninstalling software)**
- **BitLocker Drive Encryption**

Beyond built-in tools, organizations often use **security baselines** as guides. These are documented sets of recommended configuration settings. Examples include:

- **Microsoft Security Baselines:** Microsoft provides its own recommended security configurations.
- **CIS Benchmarks:** The Center for Internet Security (CIS) publishes detailed, consensus-based hardening guides that are highly respected in the industry.

### Think about it

- Why is it generally more secure to follow a well-known security baseline (like CIS Benchmarks) rather than just trying to figure out all the settings on your own?
- What are the potential downsides of making an OS _too_ hardened, to the point where it impacts usability for legitimate users?

This preparation will give you a solid foundation for our upcoming lesson. We'll be building on these concepts with practical demonstrations and discussions.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-13-OS-Hardening-Security-jmtdpkkimwx7xi5?mode=doc](https://gamma.app/docs/Operating-Systems-13-OS-Hardening-Security-jmtdpkkimwx7xi5?mode=doc)

Try not to peek before class - spoilers inside!

</aside>