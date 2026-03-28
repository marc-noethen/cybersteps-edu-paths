Welcome to your pre-class preparation for our upcoming lesson on Executables! This material will give you the basic knowledge to understand what executable files are, how they are created, how they generally work, and why they're important in operating systems and cybersecurity.

## What is an Executable File?

Think of an **executable file** as a ready-to-run instruction manual for your computer. When you want to start a program—like a web browser, a game, or a simple calculator—you're telling the operating system (OS) to open this manual and follow its steps. The computer's processor (CPU) reads these instructions and carries them out.

On Windows computers, you'll often see these files with an `.exe` extension (short for "executable"), for example, `notepad.exe` (Notepad). Another common type you'll encounter is a `.dll` (Dynamic Link Library) file, which we'll discuss later.

![image.png](attachment:61a03b19-0cf4-401f-9457-cedc98489014:c10e09fd-6b17-4d9c-9c6c-2f716dbdb580.png)

## From Human Code to Machine Instructions: A Quick Overview

You might wonder how these executable files come into being. Programmers write software using human-readable languages like Python, C++, or Java. This is called **source code**. However, a computer's CPU doesn't understand Python or C++ directly. It only understands very basic instructions called **machine code**, which are sequences of numbers.

So, how does source code become machine code?

1. **Compilation:** For languages like C++ or C#, the source code goes through a process called **compilation**. A special program called a **compiler** translates the human-readable source code into low-level instructions. Sometimes, this intermediate step is **assembly language**. Assembly language is a bit more human-readable than raw machine code but is very close to what the hardware understands.
2. **Assembling:** If the compiler produces assembly language, another tool called an **assembler** then converts the assembly language into actual machine code.
3. **Linking:** Often, a program is made of many different source code files and might use pre-written code from libraries. A **linker** takes all these pieces of machine code and combines them into a single executable file (like an `.exe` or `.dll`). It also prepares the file so the operating system knows how to load and run it.

The result of this process is an executable file, packed with machine code instructions that your CPU can execute.

![image.png](attachment:9367f23f-27b0-4499-822b-f0e51d6357ef:image.png)

### Think about it

Why do you think programmers use high-level languages like Python or C++ instead of writing machine code or assembly language directly, even though the computer only understands machine code?

## A Quick Look Inside: How Executables are Organized

Executable files aren't just a jumble of machine code. They have an internal structure that helps the OS understand and run them efficiently. On Windows, this structure is often referred to as the **Portable Executable (PE)** format.

You don't need to know all the tiny details, but the main idea is that the file is organized into different parts:

- **Headers:** These are at the very beginning, like a cover page and table of contents. They tell the OS essential information: what kind of program it is, where the main instructions start, how much memory it might need, and where other important pieces of information within the file are located.
- **Sections:** Following the headers, the file is divided into various sections. Think of these as chapters, each holding a specific type of content:
    - One section typically holds the actual **program instructions** (the machine code).
    - Other sections might hold **data** the program uses, like text messages it displays or default settings.
    - Another important section often lists any **external functions** the program needs to borrow from other files (like DLLs).

This organization helps the OS load only what's needed into memory and manage the program effectively. In cybersecurity, analysts often examine these headers and sections to understand a program's purpose, especially if it's suspected malware.

![image.png](attachment:d0624187-de6c-4d8d-a888-801165326900:image.png)

## The Loading Process: From Clicking to Running

When you double-click an `.exe` file, the OS doesn't just instantly run it. A part of the OS called the **loader** performs several important steps:

1. **Reads the File:** The loader first looks at the executable's headers to understand its structure and requirements.
2. **Sets up Memory:** It allocates space in the computer's memory for the program.
3. **Loads Instructions and Data:** It copies the necessary parts of the program (like the machine code and initial data) from your storage (e.g., hard drive) into the allocated memory.
4. **Handles Dependencies (Dynamic Linking):** Many programs need to use functions provided by other files, especially Dynamic Link Libraries (DLLs). The loader finds these required DLLs and connects them to the program so it can use their functions.
5. **Starts the Program:** Once everything is prepared, the loader tells the CPU to begin executing the program's instructions from its designated starting point.

## Sharing Code: Dynamic Linking and DLLs

Programs often need to perform common tasks, like opening files, displaying windows, or communicating over the network. Instead of every program having its own code for these tasks, they can use shared code from **Dynamic Link Libraries (DLLs)**.

- **What are DLLs?** DLLs are collections of pre-compiled code and data that multiple programs can use simultaneously. For example, a single DLL might contain functions for drawing windows on the screen, and many different applications can use this DLL to create their user interfaces.
    
- **How does it work?** When a program needs a function from a DLL, it doesn't include the entire DLL's code within its own `.exe` file. Instead, the `.exe` file just contains a reference saying, "I need to use function X from Y.dll." When you run the program, the OS loader is responsible for finding `Y.dll` and making function X available to your program. This is called **dynamic linking**.
    
- **Benefits:**
    
    - **Smaller `.exe` files:** Programs are smaller because they don't duplicate common code.
    - **Memory saving:** If multiple programs use the same DLL, the OS can load a single copy of the DLL into memory and share it.
    - **Easier updates:** If a DLL is updated (e.g., with a security fix or new features), all programs that use it can benefit from the update without needing to be changed themselves.
- **Potential Issues:** If a required DLL is missing, corrupted, or the wrong version, the program might not start or work correctly. This is sometimes referred to as "DLL Hell." Malicious actors can also try to trick programs into loading fake DLLs (DLL hijacking).
    
    ![1_5rr0KW9eNhdrioB_f07k-Q.webp](attachment:d763d182-a14d-4ae1-8e86-c63335f7879d:1_5rr0KW9eNhdrioB_f07k-Q.webp)
    

You'll find many DLLs in your Windows system (e.g., in `C:\\Windows\\System32`). They are a fundamental part of how Windows and its applications operate.

### Try it yourself

1. On your Windows VM, open File Explorer and go to the `C:\\Windows\\System32` folder.
2. Look at the file types. You'll see a very large number of files with the `.dll` extension.
3. You don't need to open them, but just notice they are there. These are examples of dynamically linked libraries that many programs on your system share.

![image.png](attachment:6889330d-5760-481c-bfee-6043c6a4159d:image.png)

## Why is Understanding Executables Important in Cybersecurity?

Even a high-level understanding of executables is very valuable in cybersecurity:

- **Malware Analysis:** Most malicious software (viruses, ransomware, spyware) is distributed as executable files (`.exe` or sometimes `.dll`). Analysts need to understand how these files work to figure out what damage they can do and how to protect against them.
- **Understanding Attacks:** Many cyberattacks involve tricking users into running malicious executables or exploiting how executables and DLLs are loaded by the OS.
- **Digital Forensics:** When investigating a security breach, experts often examine executable files found on compromised systems to understand how the attack happened.

## Setup

For our upcoming lesson, we'll use a tool called **CFF Explorer** to look inside PE files. Please set this up on your Windows Virtual Machine:

1. **Download CFF Explorer:**
    - Go to the official NTCore website: [http://www.ntcore.com/exsuite.php](http://www.ntcore.com/exsuite.php)
    - Download the "Explorer Suite" (it's a zip file).
2. **Extract CFF Explorer:**
    - Create a folder on your Windows VM, for instance, `C:\\Tools\\CFFExplorer`.
    - Extract the contents of the downloaded zip file into this new folder.
3. **Run CFF Explorer:**
    - Inside the folder, double-click `CFF Explorer.exe` to run it. It doesn't need a separate installation.
    - (Sometimes, security software might flag tools like this because they can be used to inspect system files. CFF Explorer from the official site is a well-known tool for this purpose.)

Try opening a common program with it, like `C:\\Windows\\System32\\notepad.exe`. Just look around the interface a bit. We'll go over how to use it and what to look for in our lesson.

This preparation should give you a good foundation. Completing the setup will ensure you're ready for our hands-on activities!

![cerbero_suite.png](attachment:f6878a28-bdb6-474d-ab11-3c5c9c47e570:cerbero_suite.png)

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-8-Executables-qt9j1698gdl9gc7?mode=doc](https://gamma.app/docs/Operating-Systems-8-Executables-qt9j1698gdl9gc7?mode=doc)

Try not to peek before class - spoilers inside!

</aside>