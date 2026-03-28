Welcome to your introduction to PowerShell! This preparation material will provide you with the foundational knowledge needed for our upcoming lesson. PowerShell is a powerful tool for system administrators and cybersecurity professionals alike. Understanding its basics is a key step in mastering Windows environments.

## What is PowerShell?

PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. It was developed by Microsoft and was first released in 2006 for Windows. Unlike traditional command-line shells that work with text streams (like Command Prompt in Windows or Bash in Linux/macOS), PowerShell is built on the .NET Framework and works with **objects**. This is a fundamental difference and a source of its power and flexibility.

Think of it this way: traditional shells pass around strings of text. If you want to get a list of running processes and then sort them by memory usage, you'd typically get a block of text, then use other text-manipulation tools to parse that text, extract the memory usage, and then sort. PowerShell, on the other hand, gives you a list of "process objects." Each object inherently "knows" its properties (like name, ID, CPU usage, memory usage). You can then directly tell PowerShell to sort these objects by their memory property, without complex text parsing.

PowerShell is designed for:

- **Automation:** Automating repetitive administrative tasks.
- **Configuration Management:** Managing and maintaining the configuration of systems.
- **System Interaction:** Interacting with various components of the operating system and applications.

Initially a Windows-only tool, PowerShell is now open-source and available on macOS and Linux, making it a versatile tool for diverse environments.

![image.png](attachment:d7e4e93f-701e-42dc-bfac-27339a2c5fc9:image.png)

## What is PowerShell Used For?

PowerShell is an indispensable tool for IT professionals, including those in cybersecurity, for several reasons:

- **System Administration & Management:** Many IT tasks involve interacting with and managing Windows systems. PowerShell provides deep access to system internals for configuration, maintenance, and troubleshooting.
- **Incident Response:** During a security incident, PowerShell can be used to quickly gather information about a compromised system, identify malicious processes, check network connections, and collect forensic data.
- **Forensics:** Its ability to access detailed system information (like event logs, registry entries, running services) makes it valuable for digital forensics.
- **Penetration Testing & "Red Teaming":** Attackers (and penetration testers mimicking them) often use PowerShell for reconnaissance, exploitation, and post-exploitation activities due to its power and native presence on Windows systems. Understanding PowerShell helps defenders recognize and counter these techniques.
- **Log Analysis:** PowerShell can parse and analyze various log files, helping to identify suspicious activities or system errors.
- **Active Directory (AD) Management:** AD is a core component of most enterprise networks. PowerShell is the primary tool for managing and querying AD.
- **Automation of Security and IT Tasks:** Security checks, compliance reporting, software deployment, user provisioning, and remediation actions can be scripted and automated.

Because PowerShell is installed by default on all modern Windows operating systems, it's a common tool for both administrators ("blue teams") and attackers ("red teams"). Knowing PowerShell is crucial for both defending systems, managing them efficiently, and understanding potential attack vectors.

![image.png](attachment:e014a69d-603d-4a86-865f-6d0fcbc533d3:image.png)

## Core PowerShell Concepts

Let's dive into some of the fundamental building blocks of PowerShell.

### Cmdlets (Command-lets)

Cmdlets are the heart of PowerShell. They are lightweight commands that implement a specific function. The name "cmdlet" is a contraction of "command-let" (like a small command).

A key feature of cmdlets is their naming convention: **Verb-Noun**.

- The **Verb** part specifies the action the cmdlet performs (e.g., `Get`, `Set`, `Start`, `Stop`, `New`, `Remove`, `Out`).
- The **Noun** part specifies the entity on which the action is performed (e.g., `Process`, `Service`, `Item`, `Content`, `EventLog`).

Examples:

- `Get-Process`: Retrieves a list of currently running processes.
- `Set-Location`: Changes the current working directory (like `cd`).
- `Get-Help`: Provides help about PowerShell cmdlets and concepts.
- `Start-Service`: Starts a specified service.
- `Stop-Process`: Stops a running process.

This consistent naming convention makes it easier to predict and discover commands. If you know you want to retrieve information, you'll likely use a `Get-*` cmdlet. If you want to change something, you'll look for a `Set-*` cmdlet.

### Try it yourself

Once you have PowerShell open (see Setup section below):

1. Type `Get-Date` and press Enter. What does it show you?
2. Type `Get-Process` and press Enter. Observe the list of running processes.
3. Type `Get-Service` and press Enter. Notice the different types of information displayed compared to `Get-Process`.

### Objects

As mentioned earlier, PowerShell cmdlets don't just return text; they return **.NET objects**. Each object is a structured piece of data with properties (characteristics) and methods (actions it can perform).

When you run `Get-Process`, you're not just getting lines of text. You're getting a collection of "process objects." Each of these objects has properties like `ProcessName`, `Id`, `CPU`, `PM` (Paged Memory), `WS` (Working Set memory), and many more.

Because you're dealing with objects, you can:

- Access specific properties: `(Get-Process -Name "explorer").CPU` would attempt to get the CPU usage of the "explorer" process.
- Filter based on properties: Show only processes using more than 100MB of memory.
- Sort based on properties: List processes by their CPU usage.
- Pass these rich objects to other cmdlets for further processing.

### The Pipeline (`|`)

The pipeline is a powerful feature in PowerShell used to send the output (objects) of one cmdlet to be used as input for another cmdlet. The pipe symbol (`|`) is used for this.

![image.png](attachment:0dca6053-a071-41ca-9b68-13436ba0f576:0324ca0e-4e80-4b8a-b641-ba9de2584594.png)

This allows you to chain cmdlets together to perform complex tasks in a concise way.

Example: `Get-Process | Sort-Object -Property CPU -Descending`

1. `Get-Process` runs and outputs a collection of process objects.
2. The `|` symbol takes these process objects and "pipes" them as input to the `Sort-Object` cmdlet.
3. `Sort-Object` then sorts these process objects based on their `CPU` property in `Descending` order.

Another example: `Get-Service | Where-Object {$_.Status -eq "Running"}`

1. `Get-Service` retrieves all service objects.
2. These objects are piped to `Where-Object`.
3. `Where-Object` filters these service objects, only keeping those where the `Status` property is equal (`eq`) to "Running". (`$_.` is a special variable that refers to the current object in the pipeline).

### Think about it

Consider the command `Get-Process | Sort-Object Name`.

- What do you think this command does?
- How is this different from how you might sort a list of processes in a traditional text-based shell?
- Why is the object-oriented nature of PowerShell particularly useful when combined with the pipeline?

### Variables

Like any scripting language, PowerShell allows you to store data in variables. Variable names in PowerShell always start with a dollar sign (`$`).

Examples:

- `$myName = "CyberStudent"` (stores a string)
- `$processCount = (Get-Process).Count` (stores the number of running processes)
- `$runningServices = Get-Service | Where-Object {$_.Status -eq "Running"}` (stores a collection of running service objects)

You can then use these variables in other commands or scripts. To display the value of a variable, just type its name:`$myName` `$processCount`

### Basic Syntax and Parameters

Cmdlets can have **parameters** that modify their behavior. Parameters are typically prefixed with a hyphen (`-`).

Example: `Get-Help Get-Process -Detailed`

- `Get-Help` is the cmdlet.
- `Get-Process` is an argument specifying what to get help for.
- `Detailed` is a parameter that tells `Get-Help` to show detailed information.

Some parameters take values, like `-Name "notepad"` in `Get-Process -Name "notepad"`.

**Aliases:** PowerShell has aliases for common cmdlets to make typing faster, especially for users familiar with other shells.

- `dir` or `ls` (aliases for `Get-ChildItem` - lists files and directories)
- `cd` (alias for `Set-Location` - changes directory)
- `cls` (alias for `Clear-Host` - clears the screen)
- `gps` (alias for `Get-Process`)
- `select` (alias for `Select-Object` - used to pick specific properties of objects)

While aliases are convenient for interactive use, it's generally recommended to use the full cmdlet names in scripts for clarity. You can find out what a command is an alias for using `Get-Alias <alias_name>`, e.g., `Get-Alias dir`.

### The Help System

PowerShell has an excellent built-in help system. The `Get-Help` cmdlet is your best friend when learning PowerShell.

To get help for a specific cmdlet: `Get-Help <Cmdlet-Name>` Example: `Get-Help Get-Process`

Useful parameters for `Get-Help`:

- `Detailed`: Provides detailed information, including parameter descriptions and examples.
- `Examples`: Shows only examples of how to use the cmdlet.
- `Full`: Shows all available help information.
- `Online`: Opens the online version of the help topic in your web browser, which is often the most up-to-date.

PowerShell also has conceptual help topics, often called "about" topics. These explain broader concepts, syntax, and features. To list all "about" topics: `Get-Help about_*` To read a specific "about" topic: `Get-Help about_Objects` or `Get-Help about_Pipelines`

**Updating Help:** The help files on your system can become outdated. You can update them by running: `Update-Help`You'll need to run this in a PowerShell session with Administrator privileges.

### Try it yourself

1. Use `Get-Help` to find out what the `Get-Command` cmdlet does.
2. Explore the parameters of `Get-ChildItem` using `Get-Help Get-ChildItem -Detailed`.
3. Try listing files in your current directory using `Get-ChildItem`. Then try `Get-ChildItem -Path C:\\Windows -File` (this will list only files in C:\Windows).
4. Find an "about" topic that interests you (e.g., `Get-Help about_Variables`) and read through it.
5. If you can, try running `Update-Help` (you might need administrator rights).

## Getting Started with the PowerShell Console

PowerShell can be accessed through its console or through the PowerShell Integrated Scripting Environment (ISE) on Windows, or other editors like Visual Studio Code which has excellent PowerShell support. For now, we'll focus on the console.

**On Windows:** PowerShell is pre-installed on modern Windows versions (Windows 7 SP1 and later, Windows Server 2008 R2 SP1 and later).

1. Click the Start button or press the Windows key.
2. Type "powershell".
3. You should see "Windows PowerShell" in the results. Click it to open the console.
    - You might also see "Windows PowerShell ISE" (a graphical environment for writing and testing scripts) or just "PowerShell" (referring to the newer, cross-platform version if installed). For basic commands, "Windows PowerShell" is fine.

The console window will open, and you'll see a prompt, typically `PS C:\\Users\\YourUserName>`. This indicates PowerShell is ready to accept commands. `C:\\Users\\YourUserName` is your current directory.

**⚠️ IMPORTANT: PowerShell Execution Policy ⚠️**

When you start running PowerShell _scripts_ (files ending in `.ps1`), you will likely encounter the **Execution Policy**. This is a safety feature in PowerShell that controls whether scripts can be run. By default, on Windows client computers (like your VM), this policy is often set to `Restricted`, which **prevents all scripts from running**. You will need to change this to complete many of the exercises in this course.

**Checking Your Current Policy:** Open PowerShell and type: `Get-ExecutionPolicy` If it says `Restricted`, you need to change it.

**Changing the Execution Policy (Recommended for this Course):** To allow locally created scripts to run (which is what you'll be doing), we recommend setting the execution policy to `RemoteSigned` for your user account. This is a good balance between security and usability for learning.

1. **Open PowerShell as Administrator:**
    - Click the Start Menu.
    - Type `powershell`.
    - Right-click on "Windows PowerShell" in the search results.
    - Select "Run as administrator".
    - If a User Account Control (UAC) prompt appears, click "Yes".
2. **Set the Execution Policy:** In the Administrator PowerShell window, type the following command and press Enter: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
    - You might be asked to confirm the change. Type `Y` and press Enter.
    - `Scope CurrentUser`: This applies the policy only to your user account, not system-wide. This is generally safer and doesn't require administrator rights for every PowerShell session _after_ this initial setup.
3. **Verify the Change:** You can close the Administrator PowerShell window. Open a regular PowerShell window (not as administrator) and type: `Get-ExecutionPolicy` It should now show `RemoteSigned`. If it still shows `Restricted`, or if you see `RemoteSigned` for `Process` or `MachinePolicy` but `Undefined` or `Restricted` for `CurrentUser`, ensure you ran the `Set-ExecutionPolicy` command correctly in an _Administrator_ PowerShell window with the `Scope CurrentUser` parameter.

**What does `RemoteSigned` mean?**

- Scripts you write yourself on your computer will run.
- Scripts downloaded from the internet (e.g., from websites) must be digitally signed by a trusted publisher to run. This provides a layer of protection against running potentially malicious scripts from untrusted sources.

**Other Policy Options (For Your Information):**

- `Restricted`: No scripts can be run. Commands in the console work. (Default on Windows clients).
- `AllSigned`: Only scripts signed by a trusted publisher can be run.
- `Unrestricted`: All scripts can run. This is less secure and generally not recommended.
- `Bypass`: Nothing is blocked and there are no warnings or prompts. Useful for specific, temporary situations but should be used with caution.
- `Undefined`: Removes the assigned execution policy for a scope. If all scopes are Undefined, the effective policy is Restricted for Windows clients.

**Security Note:** Changing the execution policy can have security implications. The `RemoteSigned` setting for `CurrentUser` is a reasonable balance for a learning environment. Avoid setting it to `Unrestricted` or `Bypass` globally unless you fully understand the risks. For our course, `RemoteSigned` for `CurrentUser` will be sufficient.

**Basic Navigation Cmdlets:**

- `Get-Location` (alias: `pwd`): Shows your current directory path.
- `Set-Location <Path>` (alias: `cd`): Changes your current directory.
    - `Set-Location C:\\Windows`
    - `Set-Location ..` (moves to the parent directory)
- `Get-ChildItem` (aliases: `dir`, `ls`): Lists the contents of the current directory or a specified path.

## Setup

For this course, you will primarily be using PowerShell within the Windows Virtual Machine (VM) that you should have set up in the "Operating Systems 2: Windows Intro" lesson.

**Accessing PowerShell in your Windows VM:**

1. Start your Windows VM.
2. Once logged into Windows, click the Start Menu.
3. Type `powershell`.
4. Select "Windows PowerShell" from the search results to open the console. This is the environment we will primarily use for PowerShell exercises related to Windows. **Before running any scripts, ensure you have checked and, if necessary, updated your Execution Policy as described in the "IMPORTANT: PowerShell Execution Policy" section above.**

**Important Note for the Course:** Unless specified otherwise, please assume all PowerShell activities and exercises are to be performed within your **Windows VM's PowerShell console**. This ensures a consistent environment and focuses on PowerShell in its native Windows context, which is critical for many cybersecurity roles.

### Try it yourself

1. Open PowerShell in your Windows VM.
2. Use `Get-Location` to see your current directory.
3. Use `Set-Location` to navigate to the `C:\\` directory.
4. Use `Get-ChildItem` to list the contents of the `C:\\` directory.
5. Try using an alias: type `dir` and press Enter. Does it give the same result as `Get-ChildItem`?
6. Clear your screen using `Clear-Host` or its alias `cls`.
7. Check your current execution policy using `Get-ExecutionPolicy`. If it's `Restricted`, follow the steps in the "IMPORTANT: PowerShell Execution Policy" section to change it to `RemoteSigned` for `CurrentUser`.

This pre-class material should give you a solid starting point. Experiment with the cmdlets mentioned, use `Get-Help`extensively, and get comfortable with the PowerShell console. The more you explore now, the more you'll get out of our live session!

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-4-PowerShell-yn7ma0a8f1sx6ak?mode=doc](https://gamma.app/docs/Operating-Systems-4-PowerShell-yn7ma0a8f1sx6ak?mode=doc)

Try not to peek before class - spoilers inside!

</aside>