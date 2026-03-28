Welcome to the pre-class preparation for our lesson on Permissions, Authentication, and Users in Windows! Understanding these concepts is fundamental to cybersecurity, as they control who can access what and what they can do with it. This preparation will lay the groundwork for our live session.

## Users and Accounts

In an operating system, a **user** represents an individual who can interact with the system. To manage this interaction, each user is typically assigned a **user account**. This account is a collection of information that tells Windows who you are, what you can do, and what your preferences are.

There are primarily two types of user accounts you'll encounter on a standalone Windows machine:

1. **Administrator Accounts**: These accounts have full control over the computer. They can install software and hardware, access all files on the system, change system settings, and manage other user accounts. It's powerful, and with great power comes great responsibility! Running as an administrator all the time can be risky, as any malicious software that runs under an administrator account will also have full control.
2. **Standard User Accounts**: These accounts have limited privileges. They can run applications and change settings that affect only their own account, but they cannot perform system-wide changes like installing most software, modifying critical system files, or changing settings for other users without providing credentials for an administrator account. This is the recommended account type for daily use.

Windows also has built-in accounts like `SYSTEM`, `Local Service`, and `Network Service` which are used by the operating system and services, but you typically don't log in with these directly. These accounts have specific, often highly privileged, purposes for running background tasks and services.

![image.png](attachment:adca00ad-1ce8-40fe-bae1-fbe968e2a5d7:image.png)

### User Groups

To simplify the management of permissions, Windows uses **user groups**. Instead of assigning permissions to each user individually, you can assign permissions to a group, and then add users to that group. All users in the group inherit the permissions assigned to the group. This makes managing access much more efficient, especially when dealing with many users.

Common default groups in Windows include:

- **Administrators**: Members have full, unrestricted control of the computer.
- **Users**: Members can perform common tasks like running applications and managing their own files, but are prevented from making system-wide changes or modifying files belonging to other users unless explicitly permitted.
- **Guests**: Members have temporary access with very limited rights. This group is often disabled by default for security reasons.
- **Backup Operators**: Members can back up and restore files on the computer, regardless of their individual file permissions. This is necessary for backup software to function correctly.
- **Remote Desktop Users**: Members are permitted to log in to the computer remotely using Remote Desktop.

### Try it yourself

On your Windows VM:

1. Press `Win + R` to open the Run dialog.
2. Type `compmgmt.msc` and press Enter. This opens Computer Management.
3. In the left pane, navigate to `System Tools > Local Users and Groups > Groups`.
4. Observe the list of built-in groups. You can double-click a group to see its members (though some system groups might not show members easily here or might be managed differently). Don't make any changes.

![image.png](attachment:cc930a91-c71d-4115-80e3-fca34802eb63:image.png)

### Think about it

- Why is it generally a bad idea to use an Administrator account for everyday tasks like browsing the internet or checking emails?
- If you needed to install a new trusted application, what would you expect to happen if you were logged in as a Standard User?

## Authentication: Who Are You?

**Authentication** is the process of verifying the identity of a user, process, or device. It's like showing your ID to prove you are who you say you are before you're allowed into a restricted area. Common authentication methods include:

1. **Passwords**: The most common form of authentication. A secret string of characters that only the user should know. Strong passwords are long, complex, and unique.
2. **PINs (Personal Identification Numbers)**: Often used for quick access, especially with Windows Hello. Shorter than passwords but usually tied to a specific device, offering a balance of convenience and security for device login.
3. **Biometrics**: Uses unique physical characteristics. Examples include fingerprint scanners, facial recognition (like Windows Hello), and iris scanners.
4. **Smart Cards or Security Keys**: Physical devices that must be present to authenticate, often used in corporate environments for stronger security.
5. **Multi-Factor Authentication (MFA)**: Enhances security by requiring two or more different authentication factors. For example, something you know (password) AND something you have (a code from an authenticator app on your phone or a security key) AND/OR something you are (biometric).

![image.png](attachment:62b56c7b-47fe-4641-be7c-dcd9720391f4:image.png)

When you log into Windows, you're undergoing an authentication process. The system compares the credentials you provide (e.g., username and password) against its local security database (Security Account Manager - SAM file) or, in a domain environment, against a central directory like Active Directory.

### Try it yourself

- Review your current Windows login method on your VM. Are you using a password, PIN, or is Windows Hello configured (if your VM environment supports it)? (No need to change anything, just observe).
- Think about the websites or apps you use that offer MFA. Why do they offer it, especially for sensitive accounts like banking or email?

![image.png](attachment:4b3b8e34-f76d-4f48-a963-6ecf2828b046:image.png)

## Permissions: What Can You Do?

Once a user is authenticated, **permissions** (also known as **authorizations**) determine what resources the user can access and what actions they can perform on those resources. Resources can include files, folders, printers, registry keys, and other system objects.

Permissions are crucial for protecting data and maintaining system stability. They ensure that users can only access the information they need and cannot accidentally (or intentionally) damage the system or compromise sensitive data.

### The Principle of Least Privilege

This is a core security concept. It states that a user (or process) should only be granted the minimum level of access – or permissions – necessary to perform its legitimate functions. For example, if a user only needs to read documents in a specific folder, they should not be given write or delete permissions for that folder. Adhering to this principle significantly reduces the potential damage from errors, malware, or compromised accounts.

![image.png](attachment:1a0fb455-18c9-4c72-afa2-0a21275a8a41:image.png)

### File and Folder Permissions (NTFS Permissions)

Windows uses the NT File System (NTFS), which supports a rich set of permissions for files and folders. These permissions can be very granular, allowing for precise control over access.

Common NTFS permissions include:

- **Full Control**: Allows users to read, write, modify, execute, change attributes, delete files and subfolders, and take ownership.
- **Modify**: Allows users to read, write, modify, execute, and delete.
- **Read & Execute**: Allows users to display folder contents, read files, and run executable files (applications).
- **List Folder Contents**: (For folders) Allows users to see the names of files and subfolders within a folder. Does not grant access to the files themselves.
- **Read**: Allows users to open and view files and their attributes (like creation date, size).
- **Write**: Allows users to create new files and subfolders within a folder, write data to files, and append to files.

These permissions can be set to **Allow** or **Deny**. Importantly, **Deny** permissions usually override **Allow** permissions. This means if a user is a member of two groups, one that is allowed access and another that is denied access to the same resource, the user will typically be denied. This is a key concept in troubleshooting access issues.

### Try it yourself

On your Windows VM:

1. Open File Explorer and navigate to your Desktop.
2. Right-click in an empty space and select `New > Text Document`. Name it `MyTestFile.txt`.
3. Right-click on `MyTestFile.txt` and select `Properties`.
4. Go to the `Security` tab.
5. Observe the list under "Group or user names". Select different users or groups (e.g., your current user account, the `Administrators` group, the `SYSTEM` account) and see how the permissions listed below (like "Full control", "Read", "Write") change. Notice the checkmarks in the "Allow" or "Deny" columns.
6. (Optional) Click the `Advanced` button for a more detailed view. Here you can see permissions entries, inheritance, and the owner of the file. Do not make any changes, just explore the interface.

### Ownership

In Windows, every file and folder (and other system objects) has an **owner**. The owner is typically the user account that created the object. The owner of an object has a special status: they can always change the permissions for that object, even if they have been denied all other access through permission settings. This ensures that someone always has control over an object to fix permission misconfigurations. "Taking ownership" is an administrative privilege that allows an administrator to seize ownership of a file or folder, often necessary for accessing objects created by other users or by the system.

### User Account Control (UAC)

You've likely encountered User Account Control (UAC) in Windows. It's the feature that dims your screen and asks for confirmation (or administrator credentials) before allowing an application to make changes that could affect your computer's settings or files (e.g., installing software, changing system-wide settings).

UAC helps enforce the principle of least privilege, even for administrator accounts. When an administrator logs in, most of their applications run with standard user privileges by default (a "filtered token"). Only when an action requires administrative privileges does UAC prompt for elevation. This elevation process grants the application the full administrator privileges for that specific task. This helps prevent malicious software from silently gaining administrative control.

### Think about it

- Consider a shared folder in a company. Why would it be important to set different permissions for different groups of users (e.g., "Accountants" vs. "Interns")?
- How does UAC contribute to the security of a Windows system even when you are logged in as an administrator?

That's it for your pre-class preparation! By understanding these core concepts of users, authentication, and permissions, and by familiarizing yourself with where to find these settings in Windows, you'll be well-prepared for our interactive session. We'll explore these topics in more detail and see them in action.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-11-Permissions-Authentication-Users-kpmac66toxoabn0?mode=doc](https://gamma.app/docs/Operating-Systems-11-Permissions-Authentication-Users-kpmac66toxoabn0?mode=doc)

Try not to peek before class - spoilers inside!

</aside>