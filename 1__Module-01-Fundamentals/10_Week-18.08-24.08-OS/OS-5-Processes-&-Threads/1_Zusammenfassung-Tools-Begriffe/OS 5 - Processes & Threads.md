Welcome to your pre-class preparation for our upcoming session on Processes and Threads! Understanding these concepts is fundamental to grasping how operating systems manage tasks and enable your computer to do many things seemingly at once. This preparation should take you about 45 minutes.

## What is a Program?

Before we dive into processes, let's clarify what a **program** is. A program is a passive entity, like a file stored on your disk (e.g., `notepad.exe` or `chrome.exe`). It's a set of instructions and data that tells the computer what to do. Think of it as a recipe written down in a cookbook. It's there, ready to be used, but it's not actually doing anything on its own.

## What is a Process?

A **process** is a program in execution. When you double-click an application icon or run a command, the operating system loads the program from the disk into memory and starts executing its instructions. This active instance of a program is what we call a process. Using our recipe analogy, a process is like a chef (the OS) actually cooking the recipe (the program) in the kitchen (the computer).

Each process is an independent entity with its own dedicated resources, managed by the operating system. These resources typically include:

- **The Program's Instructions:** This is the actual code that the computer's processor will execute. It's the step-by-step guide for the task the process needs to perform.
- **Its Current State:** This includes information like which instruction is currently being worked on and any temporary data the processor is using. It's like knowing exactly where the chef is in the recipe.
- **Memory:** Each process gets its own private area of memory. This memory is used to store:
    - Temporary data for active functions or sub-routines (like the chef's quick notes).
    - Data that is accessible throughout the lifetime of the process (like ingredients always available in the kitchen).
    - A flexible area that can grow or shrink as the process needs more or less space (like the chef getting more pantry space if cooking a large meal).

Imagine you open a web browser. That's one process. If you open a word processor, that's another distinct process. Each has its own memory space and operates independently. If one process crashes, it ideally shouldn't affect other processes running on the system.

### Try it yourself: Observing Processes

1. On your Windows Virtual Machine, open the **Task Manager**. You can do this by pressing `Ctrl+Shift+Esc` or by right-clicking the taskbar and selecting "Task Manager".
2. Go to the "Details" tab (or "Processes" tab in older Windows versions). You'll see a list of currently running processes.
3. Notice the names of the processes (e.g., `chrome.exe`, `explorer.exe`, `Taskmgr.exe` itself!). Each of these is an active instance of a program.
4. You can also use PowerShell. Open PowerShell and type the command `Get-Process`. This will list the running processes, similar to Task Manager, but in a command-line interface.

![image.png](attachment:db03f655-8053-431e-aa51-838b4e128f58:image.png)

![image.png](attachment:2cf4b918-f552-4794-8205-e963ff17e350:image.png)

## Process States

A process goes through different states during its lifecycle. While the specifics can vary between operating systems, here's a simplified view of common process states:

1. **New:** The process is being created. The OS is setting up the necessary structures and allocating initial resources.
2. **Ready:** The process has all the resources it needs to run but is waiting for its turn on the CPU. There might be many "ready" processes, forming a queue.
3. **Running:** The process's instructions are currently being executed by the CPU.
4. **Waiting (or Blocked):** The process is waiting for some event to occur, such as I/O completion (e.g., waiting for a file to download, or for user input). It cannot proceed even if the CPU is available.
5. **Terminated:** The process has finished execution or has been explicitly killed. The OS will then reclaim its resources.

![image.png](attachment:e4398efe-4230-4584-b51f-c9b909632e8f:image.png)

The operating system's **scheduler** is responsible for deciding which "ready" process gets to run on the CPU next. This rapid switching between processes gives the illusion that many programs are running simultaneously, a concept known as **multitasking** or **concurrency**.

### Think about it

- Why do you think it's important for an operating system to manage different states for a process, rather than just "running" or "not running"?
- Consider a program downloading a large file. In which state would this process spend a significant amount of time?

## What is a Thread?

Now, let's introduce **threads**. A thread is the smallest unit of execution within a process. Think of a process as a container or a main task, and threads as individual workers or sub-tasks operating within that container. A single process can have multiple threads, all executing concurrently and sharing the process's resources (like its memory space and open files).

If the process is the "chef" (the program in execution), then threads are like the chef's different hands and attention, perhaps one stirring a pot, another chopping vegetables, all part of the same overall cooking task.

Key characteristics of threads:

- **Lightweight:** Creating and managing threads is generally faster and less resource-intensive than creating and managing separate processes.
- **Resource Sharing:** Threads within the same process share the same memory address space, code section, and other OS resources like open files. This makes communication between threads easier and faster than communication between separate processes.
- **Independent Execution:** Each thread has its own program counter, register set, and a small private area for its own temporary working data (like its own mini-scratchpad). This allows each thread to execute independently.

![image.png](attachment:1f52b750-1105-4de8-9a25-417b0321b4f7:image.png)

## Why Use Threads? (Concurrency within a Process)

Threads enable a single process to perform multiple tasks simultaneously, leading to several benefits:

- **Responsiveness:** In an application with a user interface (like a web browser or word processor), threads can keep the UI responsive. For example, one thread can handle user input (typing, clicks) while another thread performs a lengthy operation in the background (like spell-checking or loading a web page). Without threads, the entire application might freeze during the lengthy operation.
- **Efficiency (Resource Sharing):** Since threads within a process share memory and resources, they avoid the overhead associated with creating separate processes for each concurrent task.
- **Scalability:** On multi-core processors, threads can truly run in parallel on different cores, significantly improving performance for CPU-bound tasks.

For example, your web browser might use one thread to render the webpage you're seeing, another to download images for that page, and yet another to respond to your mouse clicks and keyboard input. All these threads belong to the single browser process.

### Think about it

- If you have a web browser open with multiple tabs, and each tab is loading a different website, how do you think processes and threads might be used by the browser to manage this? (Modern browsers often use a multi-process architecture, where each tab _might_ be its own process for stability, and within each of those processes, threads are used for tasks like rendering, network requests, etc.)
- What could be a potential downside of threads within the same process sharing the same memory space?

## Processes vs. Threads: An Analogy

Let's solidify the difference with an analogy:

- **Process:** Imagine a large kitchen (the memory space and resources). It has its own set of ingredients, appliances, and a cookbook (the program code). The kitchen itself is isolated from other kitchens.
- **Single-threaded Process:** There's only one chef in the kitchen. This chef has to do everything one step at a time: read the recipe, chop vegetables, cook on the stove, clean up, etc. If the chef is busy with a long task (like waiting for something to bake), nothing else gets done.
- **Multi-threaded Process:** There are multiple chefs (threads) in the same kitchen. They all share the same ingredients, appliances, and cookbook. One chef might be chopping vegetables, another stirring a pot, and a third washing dishes. They can work on different tasks concurrently, making the overall meal preparation faster and more efficient. They need to coordinate carefully, though, to avoid getting in each other's way (e.g., both trying to use the same knife at the exact same time).

![image.png](attachment:9e9823f7-4988-42ad-b272-c59145164372:55878e4d-5073-4ac9-96fd-8ebc33710f63.png)

## How the OS Manages Them

The Operating System is the ultimate manager. It creates processes, allocates resources to them, and schedules when they (or their threads) get to use the CPU. For threads, the OS (or sometimes a library within the process) manages their creation, scheduling, and synchronization.

You'll learn much more about how the OS juggles all these tasks in our upcoming lessons. For now, focus on understanding what processes and threads are, and the fundamental differences and relationships between them.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-5-Processes-Threads-xom5o8ovuyxmylm?mode=doc](https://gamma.app/docs/Operating-Systems-5-Processes-Threads-xom5o8ovuyxmylm?mode=doc)

Try not to peek before class - spoilers inside!

</aside>