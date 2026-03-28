Welcome to your preparation for our session on Scheduling and Synchronization in Operating Systems! In our last lesson, we explored processes and threads, the fundamental units of execution. Now, we'll delve into how an operating system juggles these tasks—deciding which process or thread gets to use the CPU and when—and how it ensures they can work together harmoniously without tripping over each other. These are crucial concepts for understanding how operating systems efficiently manage resources and prevent chaos in our digital world.

## CPU Scheduling: Who Gets the CPU Next?

Imagine a very popular food truck (your computer) with only one chef (the CPU) and many hungry customers (processes and threads) all wanting their orders (tasks) processed. The chef can only work on one order at a time. Someone needs to decide which customer gets served next, and for how long the chef works on their order before possibly switching to another. This is essentially what CPU scheduling is all about.

The operating system (OS) acts as the manager of this food truck, deciding which process or thread gets the CPU's attention. This is vital because, on a modern computer, there are often dozens, if not hundreds, of active processes and threads, all vying for CPU time—from your web browser and music player to background system tasks. Without scheduling, some tasks might never get to run, or your system could become sluggish and unresponsive.

![image.png](attachment:ca6b9b78-b38a-429a-9b47-8364ac9284bd:image.png)

**Why Does the OS Bother Scheduling?**

Operating systems schedule tasks to achieve several important goals:

- **Keeping the CPU Busy:** An idle CPU is a wasted resource. The OS tries to ensure the CPU is always doing useful work.
- **Responsiveness:** When you click a button or type something, you want a quick reaction. The OS tries to make interactive programs feel responsive.
- **Fairness:** The OS attempts to give each process a fair chance to run, preventing any single power-hungry application from hogging all the CPU time.
- **Efficiency:** Completing as many tasks as possible in a given amount of time.

Achieving all these goals perfectly at the same time can be tricky, so operating systems use smart strategies to find a good balance.

**How Does the OS Manage Running Tasks?**

- **Taking Turns (Preemption):** Most modern operating systems use **preemptive scheduling**. This means the OS can interrupt a running task after a short period (a "time slice") to give another task a turn on the CPU. This is like the food truck manager telling the chef to pause one order to quickly handle a small, urgent one, ensuring everyone gets served eventually and the system feels responsive. Older or simpler systems might use **non-preemptive scheduling**, where a task runs until it's completely finished or voluntarily gives up the CPU, which can sometimes lead to one task making everyone else wait too long.
- **Keeping Track (Context Switching):** When the OS switches from one task to another, it needs to save the current progress of the outgoing task (its "context," like all the ingredients and steps for an order) and then load the saved progress of the incoming task. This process is called a **context switch**. It happens very fast, but it's a bit of overhead for the OS.

![image.png](attachment:a9af0cd8-0f5a-477d-8846-c68fc2243cbb:image.png)

### Think about it

Imagine you're juggling multiple homework assignments: math, history, and programming. How do you decide which one to work on, and for how long, before switching? What factors influence your "scheduling" decisions to try and get everything done effectively?

## Process and Thread Synchronization: Working Together Without Chaos

Often, different processes or threads need to work together or share information. For example:

- One part of a program might be downloading a file (Thread A), while another part updates a progress bar on your screen (Thread B) based on how much of the file is downloaded.
- Multiple users in a collaborative document editor might be trying to make changes to the same paragraph simultaneously.

When multiple threads or processes access and try to modify the same piece of data or resource (like a file, a variable in memory, or a shared document) at the _exact same time_, things can go very wrong if their actions aren't carefully coordinated. This coordination is called **synchronization**.

Synchronization mechanisms are rules and tools that ensure processes and threads play nicely together, accessing shared resources in an orderly way to prevent errors and maintain data consistency.

### The Problem: Race Conditions

A **race condition** occurs when the outcome of a computation depends on the unpredictable order in which multiple processes or threads access and modify shared data. It's like two people trying to update the same cell in a spreadsheet simultaneously – the final value might be the one from the person who saved last, or worse, a garbled mix.

**A Simple Race Condition Example:**

Let's say we have a shared counter, `BankAccountBalance`, which is initially $100.

- **Thread 1 (Deposit):** Wants to add $50.
    1. Reads `BankAccountBalance` (gets $100).
    2. Calculates $100 + $50 = $150.
    3. _Oops! Before Thread 1 can save the new balance, the OS switches to Thread 2!_
- **Thread 2 (Withdraw):** Wants to withdraw $30.
    1. Reads `BankAccountBalance` (still $100, because Thread 1 hasn't saved its update).
    2. Calculates $100 - $30 = $70.
    3. Writes $70 to `BankAccountBalance`. So, `BankAccountBalance` is now $70.
- _Now the OS switches back to Thread 1._ 4. Thread 1 (remember, it calculated $150 way back) writes $150 to `BankAccountBalance`. So, `BankAccountBalance` is now $150.

The final balance is $150. But it _should_ be $100 + $50 - $30 = $120. The $30 withdrawal was effectively lost because of the unlucky timing of the context switch. This is a race condition! These bugs can be incredibly tricky to find because they might only happen occasionally, depending on the exact timing of operations.

![image.png](attachment:b4b6b1dc-bbe2-46aa-a436-d4e5a09bfbcd:2e4db3aa-4e2d-4665-b383-dade2d899b2e.png)

The image humorously illustrates a CPU race condition by showing actions happening out of order - like a response ("Race Condition") arriving before the prompt ("Who's there?"), just as unsynchronized threads can produce unpredictable results.

### Critical Sections: The Danger Zone

The part of a program where shared data is accessed and modified is called a **critical section**. To prevent race conditions, we need to ensure that only one thread or process can be executing in its critical section (for a particular piece of shared data) at any given time. This principle is called **mutual exclusion**.

### Tools for Synchronization: Locks

To enforce mutual exclusion and protect critical sections, operating systems and programming languages provide synchronization tools. One of the most common is a **lock** (often called a **mutex**, short for MUTual EXclusion).

- **Mutexes (Locks):** A mutex is like a key to a restricted area (the critical section).
    1. Before a thread enters a critical section, it must try to "acquire" or "lock" the mutex.
    2. If the mutex is available (no other thread has it), the thread acquires the lock, enters the critical section, and does its work.
    3. While one thread "holds" the lock, any other thread that tries to acquire the same lock will be made to wait (it "blocks") until the lock is released.
    4. When the thread that holds the lock finishes its work in the critical section, it "releases" or "unlocks" the mutex, allowing one of the waiting threads (if any) to acquire it and proceed.

Using our bank account example: Both the deposit and withdrawal operations would need to acquire the _same_ lock before reading or writing the `BankAccountBalance`. This way, Thread 1 would complete its deposit (read, calculate, write) before Thread 2 could even start its withdrawal, or vice-versa, ensuring the balance is always correct.

![image.png](attachment:5659ded7-23d9-45ef-b2e3-9ad01c4d21e5:image.png)

### Try it yourself

Think about a single-lane bridge. Only one car can be on the bridge at a time going in a particular direction.

1. How is this similar to a critical section and a mutex?
2. What acts as the "lock"?
3. What happens if cars from both directions try to enter the bridge at the same time without any signaling system?

### Potential Problems Even With Synchronization

While locks help, improper use or complex interactions can lead to other problems:

- **Deadlock:** This is a situation where two or more threads are stuck waiting for each other, and neither can proceed.
    - Imagine Thread A has locked Resource X and is waiting for Resource Y.
    - At the same time, Thread B has locked Resource Y and is waiting for Resource X.
    - They are now in a deadlock: Thread A won't release X until it gets Y, and Thread B won't release Y until it gets X. Both are stuck indefinitely.
- **Starvation (Indefinite Blocking):** A thread might be repeatedly prevented from acquiring a lock or resource, even though the lock becomes available, because other threads always manage to get it first. The thread "starves" because it never gets its turn.

![image.png](attachment:f8785db0-170b-4ea9-abf3-4ecf68dc2b41:image.png)

### Think about it

Consider two programs, Program A and Program B, that both need to write messages to the _same_ log file.

1. Program A opens the log file and starts writing "Program A activity: Started..."
2. Before Program A finishes its line, Program B also opens the log file and writes "Program B report: Initializing..."
3. Program A then tries to write "...data processing complete." What might the log file look like? How could using a lock associated with the log file prevent this jumbled output?

Understanding these concepts of scheduling (who runs when) and synchronization (how they run together safely) is fundamental to grasping how operating systems create a stable, efficient, and seemingly simultaneous multitasking environment on our computers. In our upcoming session, we'll look at how Windows manages these challenges and explore some tools to observe them in action.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-6-Scheduling-Synchronization-g4w9ht3wmy5j0eh?mode=doc](https://gamma.app/docs/Operating-Systems-6-Scheduling-Synchronization-g4w9ht3wmy5j0eh?mode=doc)

</aside>