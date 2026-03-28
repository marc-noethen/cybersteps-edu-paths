Welcome to your pre-class preparation for our upcoming session on Windows Services and the System Startup process. Understanding these concepts is crucial for managing and securing an operating system. We'll explore what services are, how they function, and how Windows manages applications and processes that start automatically.

## What are Windows Services?

In Windows, a **service** is a special type of application that runs in the background, without a direct user interface. Think of them as the unsung heroes of the operating system, performing essential tasks that keep your system running smoothly. They can start when the computer boots up, even before you log in, and can continue to run as long as the computer is on.

Services handle a wide variety of functions, such as:

- Managing network connections (e.g., DHCP Client, DNS Client).
- Enabling printing (Print Spooler).
- Keeping your system updated (Windows Update).
- Providing security features (Windows Defender Antivirus Service).
- Running web servers or database engines.

Unlike regular desktop applications (like a web browser or a word processor) that you actively open and interact with, services operate behind the scenes. You typically don't "launch" a service in the same way; the operating system manages their lifecycle.

![image.png](attachment:8994eb9e-36f8-42b2-843c-7d350cb9b1ba:image.png)

### Key Characteristics of Services

- **No User Interface (Typically):** Most services don't have a graphical user interface (GUI). Their operations are logged or managed through administrative tools.
- **Run in their Own Security Context:** Services run under specific user accounts, which might be predefined system accounts (like Local System, Local Service, Network Service) or dedicated user accounts. This determines what resources the service can access.
- **Automatic or Manual Startup:** Services can be configured to start automatically when Windows boots, or they can be set to manual start, requiring a user or another process to initiate them. They can also be disabled entirely.
- **Dependencies:** Some services depend on other services to function correctly. If a required service isn't running, the dependent service might fail to start or operate properly. The timing of when services start is critical, and this is managed during the overall system startup sequence.

### Think about it

- Why is it beneficial for essential tasks like network management or system updates to run as services rather than regular applications that a user has to start manually?
- Can you think of a scenario where a service _not_ running could cause significant problems for a user?

## The Windows Startup Process: An Overview

So, how and when do these vital services actually get started? They are an integral part of the Windows startup process. When you press the power button, a complex sequence of events unfolds to bring your system to life, including the initiation of these background tasks. Here’s a simplified look at this process:

1. **Power On and Hardware Check (Firmware Stage)**
    - When you turn on your PC, the system’s built-in software (called firmware, either BIOS or UEFI) wakes up.
    - It quickly checks your main hardware components (like memory and hard drives) to make sure they're working. This is often called the Power-On Self Test (POST).
    - If everything is okay, the firmware looks for the operating system on your storage device (usually your main hard drive or SSD).
2. **Loading Windows (Bootloader Stage)**
    - The firmware hands over control to a small program called the Windows Boot Manager.
    - The Boot Manager's job is to find and start loading the main parts of the Windows operating system.
    - It reads some configuration files to know where Windows is installed and if there are any special startup options (like starting in Safe Mode).
3. **Starting the Core of Windows (Kernel Initialization)**
    - The Boot Manager loads the Windows kernel, which is the heart of the operating system, into the computer's memory.
    - The kernel then starts to initialize itself. It begins by loading essential drivers – small pieces of software that let Windows talk to your hardware (like your graphics card, keyboard, and mouse).
    - It also loads important system settings from the Windows Registry.
4. **Getting System Ready (Session Manager)**
    - Once the kernel is running, it starts a key process called the Session Manager.
    - The Session Manager sets up the basic environment for Windows to run, including preparing for user logins and starting critical system processes.
5. **Starting Services and Preparing for Logon (Logon Phase)**
    - The Session Manager starts the Service Control Manager (SCM). The SCM is in charge of all the Windows services we discussed earlier.
    - The SCM looks at its list of services and starts all those that are set to "Automatic" startup. These are often crucial for things like networking, sound, and security.
    - At the same time, the system prepares for you to log in by starting the logon process, which eventually shows you the login screen.
6. **User Login and Desktop (User Environment)**
    - When you enter your username and password, Windows verifies your credentials.
    - If successful, it loads your personal settings, desktop background, and icons.
    - Finally, any applications that are set to run automatically when you log in (your "startup programs") will begin to launch. Your Windows desktop appears, and your computer is ready to use.

This entire process, from pressing the power button to seeing your desktop, involves many intricate steps, but this overview covers the main stages. Understanding this flow helps in diagnosing startup problems and appreciating how services fit into the overall operation of your system.

### Try it yourself

- What happens if a critical hardware component fails the POST?
    - The system usually emits a series of beeps (a "beep code") or displays an error message on the screen, and the boot process halts. The specific code can help diagnose which component failed.
- How is this different from a software application failing to start after you've logged in?
    - A POST failure is a hardware-level issue preventing the OS from even beginning to load. A software application failing after login is an issue within the loaded OS environment, often due to software bugs, missing dependencies, or configuration errors, but the underlying system is generally functional.

## Managing Services and Startup Items

Windows provides tools to view and manage services and startup applications.

### Services Management Console (`services.msc`)

This is the primary tool for managing services. You can use it to:

- View a list of all services on your system.
- See the status of each service (Running, Stopped, Paused).
- View the startup type (Automatic, Automatic (Delayed Start), Manual, Disabled).
- Start, stop, pause, resume, or restart services.
- Configure service properties, such as the logon account and recovery options.

![image.png](attachment:693a3269-608b-47f7-8d38-7c2662f29bfd:image.png)

### Task Manager

The Task Manager, particularly its "Startup" tab, allows you to see and manage applications that are configured to run when you log in. These are different from system services but also impact system performance and startup time. You can enable or disable these startup applications.

![image.png](attachment:10f86910-70d0-4ba4-a362-e291e8d638b6:image.png)

### System Configuration Utility (`msconfig`)

Historically, `msconfig` was a common tool for managing startup items and services. While still available, for startup applications, it now often redirects you to the Task Manager. It can still be used to manage some boot options and services for diagnostic purposes.

### Try it yourself

- Explore the properties of a few services. Notice their dependencies and the account they log on as.
- Compare the items listed in Task Manager's "Startup" tab with the services listed in `services.msc`. Are they the same things? Why or why not?
    - They are not the same. `services.msc` lists system services that often run in the background regardless of who is logged in (or even if no one is logged in). Task Manager's "Startup" tab lists applications and scripts that are configured to run specifically when a user logs into their session. While some services might be user-specific, the primary distinction is that services are background processes providing core OS or application functionalities, whereas startup items are typically user-facing applications or utilities.

## Why Care About Services and Startup?

From a cybersecurity perspective, understanding and managing services and startup processes is vital:

- **Attack Surface Reduction:** Every running service or startup application potentially increases the system's attack surface. Disabling unnecessary services and startup items can reduce vulnerabilities.
- **Malware Persistence:** Malware often tries to install itself as a service or a startup application to ensure it runs automatically and remains active even after a reboot. Monitoring and scrutinizing services and startup entries are key to detecting and removing malware.
- **Performance:** Too many unnecessary services or startup applications can slow down your computer's boot time and overall performance.
- **Resource Management:** Services consume system resources (CPU, memory). Efficient management ensures resources are available for essential tasks.

### Think about it

- If you discovered an unknown service running on your system, what steps would you take to investigate it?
    - Check the service name, display name, and description for clues.
    - Look at its properties: What is the path to the executable? What account does it run under? Does it have dependencies? Are other services dependent on it?
    - Search online for the executable name or service name to see if it's a legitimate Windows component, part of a known application, or potentially malware.
    - Check the digital signature of the executable file.
    - Use tools like Autoruns from Sysinternals to get more detailed information.
    - If suspicious, consider stopping and disabling it (after assessing potential impact) and scanning the system with security software.
- Why might an attacker prefer to install malware as a service rather than just a regular startup application?
    - Services can run with higher privileges (e.g., Local System), giving malware more control over the system.
    - Services can start automatically at boot, even before a user logs in, allowing malware to be active earlier.
    - Services often run hidden in the background without a user interface, making them less noticeable to the average user compared to an application that might appear in the taskbar or system tray.
    - Services can be configured with recovery options, automatically restarting if they are stopped, making them more resilient.

## Exploration: Tools for Managing Services and Startup

Before our class, take some time to familiarize yourself with the tools Windows provides for inspecting and managing services and startup items. Ensure your Windows Virtual Machine (VM) is fully updated and operational. You will need administrative privileges within your VM for full access to these tools.

The goal here is to get comfortable navigating these utilities and observing the information they present. **Do not change any settings unless you are very sure of what you are doing.**

1. **Services Management Console (`services.msc`)**
    - Press `Win + R` to open the Run dialog.
    - Type `services.msc` and press Enter.
    - **Explore:** Browse the list of services. Click on a few services to see their properties (right-click > Properties). Note their "Startup type" (Automatic, Manual, Disabled), current "Status" (Running, Stopped), and the "Log On As" account. Check the "Dependencies" tab for a service or two.
2. **Task Manager**
    - Press `Ctrl + Shift + Esc`.
    - Alternatively, right-click the Taskbar and select "Task Manager".
    - **Explore:**
        - Go to the "Services" tab. You'll see a list similar to `services.msc`, but with a slightly different interface. You can right-click services here to start/stop them or open the full Services console.
        - Go to the "Startup" tab (or "Startup apps" in newer Windows versions). This lists applications configured to launch when you log in. Note the "Status" (Enabled/Disabled) and the "Startup impact" if shown.
3. **System Configuration Utility (`msconfig`)**
    - Press `Win + R` to open the Run dialog.
    - Type `msconfig` and press Enter.
    - **Explore:**
        - Look at the "Services" tab. Notice the option to "Hide all Microsoft services," which can be useful for identifying third-party services.
        - The "Startup" tab here usually just redirects you to Task Manager in modern Windows versions.
4. **Autoruns (from Sysinternals)**
    - Open a web browser in your VM and search for "Autoruns Sysinternals" or go directly to the Sysinternals page on the Microsoft website.
    - Download Autoruns (it usually comes as a ZIP file).
    - Extract the contents of the ZIP file to a folder (e.g., on your Desktop or in Documents).
    - Run `Autoruns.exe` (or `Autoruns64.exe` if you have a 64-bit system). You may need to agree to a license term on the first run.
    - **Explore:** This tool is very powerful and shows many more auto-starting locations than Task Manager.
        - Click through the different tabs like "Logon" (shows startup programs, Run keys, etc.), "Services" (shows services, including third-party ones), "Scheduled Tasks", "Drivers", and "KnownDLLs".
        - Notice the wealth of information: the entry, description, publisher, image path (the location of the file), and timestamp.
        - **Again, do not uncheck or delete anything in Autoruns during this pre-class exploration.** The goal is to see the breadth of items that can automatically start on a Windows system.

Spending some time with these tools will give you a much better understanding of what's running on your system and how applications achieve persistence.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-12-Services-System-Startup-0j55hdszl6lelao?mode=doc](https://gamma.app/docs/Operating-Systems-12-Services-System-Startup-0j55hdszl6lelao?mode=doc)

Try not to peek before class - spoilers inside!

</aside>