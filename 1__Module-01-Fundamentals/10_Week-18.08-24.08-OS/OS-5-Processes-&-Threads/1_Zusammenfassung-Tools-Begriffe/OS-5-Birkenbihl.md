Welcome to your pre-class preparation for our upcoming session on Processes and Threads. Willkommen zu deiner Vorbereitung vor dem Unterricht für unsere kommende Sitzung über Prozesse und Threads.

Understanding these concepts is fundamental to grasping how operating systems manage tasks and enable your computer to do many things seemingly at once. Das Verständnis dieser Konzepte ist grundlegend, um zu begreifen, wie Betriebssysteme Aufgaben verwalten und es deinem Computer ermöglichen, scheinbar viele Dinge gleichzeitig zu tun.

This preparation should take you about forty-five minutes. Diese Vorbereitung sollte etwa fünfundvierzig Minuten dauern.

What is a Program? Was ist ein Programm?

Before we dive into processes, let's clarify what a program is. Bevor wir in Prozesse eintauchen, lass uns klären, was ein Programm ist.

A program is a passive entity, like a file stored on your disk, for example notepad dot exe or chrome dot exe. Ein Programm ist eine passive Einheit, wie eine Datei, die auf deiner Festplatte gespeichert ist, zum Beispiel notepad punkt exe oder chrome punkt exe.

It's a set of instructions and data that tells the computer what to do. Es ist eine Sammlung von Anweisungen und Daten, die dem Computer sagen, was er tun soll.

Think of it as a recipe written down in a cookbook. Stell es dir als ein Rezept vor, das in einem Kochbuch aufgeschrieben ist.

It's there, ready to be used, but it's not actually doing anything on its own. Es ist da, bereit verwendet zu werden, aber es tut eigentlich nichts von alleine.

What is a Process? Was ist ein Prozess?

A process is a program in execution. Ein Prozess ist ein Programm in Ausführung.

When you double-click an application icon or run a command, the operating system loads the program from the disk into memory and starts executing its instructions. Wenn du auf ein Anwendungssymbol doppelklickst oder einen Befehl ausführst, lädt das Betriebssystem das Programm von der Festplatte in den Speicher und beginnt, seine Anweisungen auszuführen.

This active instance of a program is what we call a process. Diese aktive Instanz eines Programms ist das, was wir einen Prozess nennen.

Using our recipe analogy, a process is like a chef, the OS, actually cooking the recipe, the program, in the kitchen, the computer. Mit unserer Rezeptanalogie ist ein Prozess wie ein Koch, das OS, der tatsächlich das Rezept, das Programm, in der Küche, dem Computer, kocht.

Each process is an independent entity with its own dedicated resources, managed by the operating system. Jeder Prozess ist eine unabhängige Einheit mit seinen eigenen dedizierten Ressourcen, die vom Betriebssystem verwaltet werden.

These resources typically include the program's instructions. Diese Ressourcen umfassen typischerweise die Anweisungen des Programms.

This is the actual code that the computer's processor will execute. Dies ist der tatsächliche Code, den der Prozessor des Computers ausführen wird.

It's the step-by-step guide for the task the process needs to perform. Es ist die Schritt-für-Schritt-Anleitung für die Aufgabe, die der Prozess ausführen muss.

Its current state. Sein aktueller Zustand.

This includes information like which instruction is currently being worked on and any temporary data the processor is using. Dies umfasst Informationen wie welche Anweisung gerade bearbeitet wird und alle temporären Daten, die der Prozessor verwendet.

It's like knowing exactly where the chef is in the recipe. Es ist wie zu wissen, wo genau der Koch im Rezept ist.

Memory. Speicher.

Each process gets its own private area of memory. Jeder Prozess erhält seinen eigenen privaten Speicherbereich.

This memory is used to store temporary data for active functions or sub-routines, like the chef's quick notes. Dieser Speicher wird verwendet, um temporäre Daten für aktive Funktionen oder Unterroutinen zu speichern, wie die schnellen Notizen des Kochs.

Data that is accessible throughout the lifetime of the process, like ingredients always available in the kitchen. Daten, die während der gesamten Lebensdauer des Prozesses zugänglich sind, wie Zutaten, die immer in der Küche verfügbar sind.

A flexible area that can grow or shrink as the process needs more or less space, like the chef getting more pantry space if cooking a large meal. Ein flexibler Bereich, der wachsen oder schrumpfen kann, wenn der Prozess mehr oder weniger Platz benötigt, wie wenn der Koch mehr Vorratsraum bekommt, wenn er ein großes Essen kocht.

Imagine you open a web browser, that's one process. Stell dir vor, du öffnest einen Webbrowser, das ist ein Prozess.

If you open a word processor, that's another distinct process. Wenn du ein Textverarbeitungsprogramm öffnest, ist das ein anderer, eigenständiger Prozess.

Each has its own memory space and operates independently. Jeder hat seinen eigenen Speicherbereich und arbeitet unabhängig.

If one process crashes, it ideally shouldn't affect other processes running on the system. Wenn ein Prozess abstürzt, sollte dies idealerweise keine anderen Prozesse beeinflussen, die auf dem System laufen.

Try it yourself: Observing Processes. Probiere es selbst aus: Prozesse beobachten.

On your Windows Virtual Machine, open the Task Manager. Öffne auf deiner virtuellen Windows-Maschine den Task-Manager.

You can do this by pressing Control plus Shift plus Escape or by right-clicking the taskbar and selecting Task Manager. Du kannst dies tun, indem du Steuerung plus Umschalt plus Escape drückst oder indem du mit der rechten Maustaste auf die Taskleiste klickst und Task-Manager auswählst.

Go to the Details tab, or Processes tab in older Windows versions. Gehe zum Tab Details, oder zum Tab Prozesse in älteren Windows-Versionen.

You'll see a list of currently running processes. Du wirst eine Liste der aktuell laufenden Prozesse sehen.

Notice the names of the processes, for example chrome dot exe, explorer dot exe, Taskmgr dot exe itself. Beachte die Namen der Prozesse, zum Beispiel chrome punkt exe, explorer punkt exe, Taskmgr punkt exe selbst.

Each of these is an active instance of a program. Jeder davon ist eine aktive Instanz eines Programms.

You can also use PowerShell. Du kannst auch PowerShell verwenden.

Open PowerShell and type the command Get-Process. Öffne PowerShell und tippe den Befehl Get-Process.

This will list the running processes, similar to Task Manager, but in a command-line interface. Dies wird die laufenden Prozesse auflisten, ähnlich wie der Task-Manager, aber in einer Befehlszeilenschnittstelle.

Process States. Prozesszustände.

A process goes through different states during its lifecycle. Ein Prozess durchläuft während seines Lebenszyklus verschiedene Zustände.

While the specifics can vary between operating systems, here's a simplified view of common process states. Während die Details zwischen Betriebssystemen variieren können, hier ist eine vereinfachte Ansicht der üblichen Prozesszustände.

New: The process is being created. Neu: Der Prozess wird erstellt.

The OS is setting up the necessary structures and allocating initial resources. Das OS richtet die notwendigen Strukturen ein und weist anfängliche Ressourcen zu.

Ready: The process has all the resources it needs to run but is waiting for its turn on the CPU. Bereit: Der Prozess hat alle Ressourcen, die er zum Laufen benötigt, wartet aber auf seinen Durchgang auf der CPU.

There might be many ready processes, forming a queue. Es könnte viele bereite Prozesse geben, die eine Warteschlange bilden.

Running: The process's instructions are currently being executed by the CPU. Laufend: Die Anweisungen des Prozesses werden gerade von der CPU ausgeführt.

Waiting, or Blocked: The process is waiting for some event to occur, such as I/O completion, for example waiting for a file to download, or for user input. Wartend oder Blockiert: Der Prozess wartet darauf, dass ein Ereignis eintritt, wie der Abschluss von Ein-Ausgabe-Operationen, zum Beispiel das Warten auf den Download einer Datei oder auf Benutzereingaben.

It cannot proceed even if the CPU is available. Er kann nicht fortfahren, selbst wenn die CPU verfügbar ist.

Terminated: The process has finished execution or has been explicitly killed. Beendet: Der Prozess hat die Ausführung beendet oder wurde explizit beendet.

The OS will then reclaim its resources. Das OS wird dann seine Ressourcen zurückfordern.

The operating system's scheduler is responsible for deciding which ready process gets to run on the CPU next. Der Scheduler des Betriebssystems ist dafür verantwortlich zu entscheiden, welcher bereite Prozess als Nächstes auf der CPU laufen darf.

This rapid switching between processes gives the illusion that many programs are running simultaneously, a concept known as multitasking or concurrency. Dieses schnelle Wechseln zwischen Prozessen erzeugt die Illusion, dass viele Programme gleichzeitig laufen, ein Konzept, das als Multitasking oder Nebenläufigkeit bekannt ist.

Think about it. Denk darüber nach.

Why do you think it's important for an operating system to manage different states for a process, rather than just running or not running? Warum denkst du, ist es wichtig für ein Betriebssystem, verschiedene Zustände für einen Prozess zu verwalten, anstatt nur laufend oder nicht laufend?

Consider a program downloading a large file, in which state would this process spend a significant amount of time? Betrachte ein Programm, das eine große Datei herunterlädt, in welchem Zustand würde dieser Prozess eine erhebliche Menge Zeit verbringen?

What is a Thread? Was ist ein Thread?

Now, let's introduce threads. Jetzt lass uns Threads einführen.

A thread is the smallest unit of execution within a process. Ein Thread ist die kleinste Ausführungseinheit innerhalb eines Prozesses.

Think of a process as a container or a main task, and threads as individual workers or sub-tasks operating within that container. Denk an einen Prozess als einen Container oder eine Hauptaufgabe, und Threads als einzelne Arbeiter oder Unteraufgaben, die innerhalb dieses Containers arbeiten.

A single process can have multiple threads, all executing concurrently and sharing the process's resources, like its memory space and open files. Ein einzelner Prozess kann mehrere Threads haben, die alle nebenläufig ausgeführt werden und die Ressourcen des Prozesses teilen, wie seinen Speicherbereich und offene Dateien.

If the process is the chef, the program in execution, then threads are like the chef's different hands and attention, perhaps one stirring a pot, another chopping vegetables, all part of the same overall cooking task. Wenn der Prozess der Koch ist, das Programm in Ausführung, dann sind Threads wie die verschiedenen Hände und Aufmerksamkeit des Kochs, vielleicht eine, die einen Topf umrührt, eine andere, die Gemüse schneidet, alles Teil derselben gesamten Kochaufgabe.

Key characteristics of threads. Hauptmerkmale von Threads.

Lightweight: Creating and managing threads is generally faster and less resource-intensive than creating and managing separate processes. Leichtgewichtig: Das Erstellen und Verwalten von Threads ist im Allgemeinen schneller und weniger ressourcenintensiv als das Erstellen und Verwalten separater Prozesse.

Resource Sharing: Threads within the same process share the same memory address space, code section, and other OS resources like open files. Ressourcenteilung: Threads innerhalb desselben Prozesses teilen denselben Speicheradressraum, Code-Abschnitt und andere OS-Ressourcen wie offene Dateien.

This makes communication between threads easier and faster than communication between separate processes. Dies macht die Kommunikation zwischen Threads einfacher und schneller als die Kommunikation zwischen separaten Prozessen.

Independent Execution: Each thread has its own program counter, register set, and a small private area for its own temporary working data, like its own mini-scratchpad. Unabhängige Ausführung: Jeder Thread hat seinen eigenen Programmzähler, Registersatz und einen kleinen privaten Bereich für seine eigenen temporären Arbeitsdaten, wie sein eigenes Mini-Notizbuch.

This allows each thread to execute independently. Dies ermöglicht es jedem Thread, unabhängig auszuführen.

Why Use Threads? Concurrency within a Process. Warum Threads verwenden? Nebenläufigkeit innerhalb eines Prozesses.

Threads enable a single process to perform multiple tasks simultaneously, leading to several benefits. Threads ermöglichen es einem einzelnen Prozess, mehrere Aufgaben gleichzeitig auszuführen, was zu mehreren Vorteilen führt.

Responsiveness: In an application with a user interface, like a web browser or word processor, threads can keep the UI responsive. Reaktionsfähigkeit: In einer Anwendung mit einer Benutzeroberfläche, wie einem Webbrowser oder Textverarbeitungsprogramm, können Threads die Benutzeroberfläche reaktionsfähig halten.

For example, one thread can handle user input, typing, clicks, while another thread performs a lengthy operation in the background, like spell-checking or loading a web page. Zum Beispiel kann ein Thread Benutzereingaben verarbeiten, Tippen, Klicks, während ein anderer Thread eine langwierige Operation im Hintergrund ausführt, wie Rechtschreibprüfung oder das Laden einer Webseite.

Without threads, the entire application might freeze during the lengthy operation. Ohne Threads könnte die gesamte Anwendung während der langwierigen Operation einfrieren.

Efficiency, Resource Sharing: Since threads within a process share memory and resources, they avoid the overhead associated with creating separate processes for each concurrent task. Effizienz, Ressourcenteilung: Da Threads innerhalb eines Prozesses Speicher und Ressourcen teilen, vermeiden sie den Mehraufwand, der mit dem Erstellen separater Prozesse für jede nebenläufige Aufgabe verbunden ist.

Scalability: On multi-core processors, threads can truly run in parallel on different cores, significantly improving performance for CPU-bound tasks. Skalierbarkeit: Auf Mehrkernprozessoren können Threads wirklich parallel auf verschiedenen Kernen laufen, was die Leistung für CPU-gebundene Aufgaben erheblich verbessert.

For example, your web browser might use one thread to render the webpage you're seeing, another to download images for that page, and yet another to respond to your mouse clicks and keyboard input. Zum Beispiel könnte dein Webbrowser einen Thread verwenden, um die Webseite zu rendern, die du siehst, einen anderen, um Bilder für diese Seite herunterzuladen, und noch einen anderen, um auf deine Mausklicks und Tastatureingaben zu reagieren.

All these threads belong to the single browser process. All diese Threads gehören zu dem einzelnen Browserprozess.

Think about it. Denk darüber nach.

If you have a web browser open with multiple tabs, and each tab is loading a different website, how do you think processes and threads might be used by the browser to manage this? Wenn du einen Webbrowser mit mehreren Tabs geöffnet hast und jeder Tab eine andere Website lädt, wie denkst du, könnten Prozesse und Threads vom Browser verwendet werden, um dies zu verwalten?

Modern browsers often use a multi-process architecture, where each tab might be its own process for stability, and within each of those processes, threads are used for tasks like rendering, network requests, etc. Moderne Browser verwenden oft eine Mehrprozess-Architektur, bei der jeder Tab sein eigener Prozess für Stabilität sein könnte, und innerhalb jedes dieser Prozesse werden Threads für Aufgaben wie Rendering, Netzwerkanfragen usw. verwendet.

What could be a potential downside of threads within the same process sharing the same memory space? Was könnte ein potenzieller Nachteil davon sein, dass Threads innerhalb desselben Prozesses denselben Speicherbereich teilen?

Processes versus Threads: An Analogy. Prozesse versus Threads: Eine Analogie.

Let's solidify the difference with an analogy. Lass uns den Unterschied mit einer Analogie verdeutlichen.

Process: Imagine a large kitchen, the memory space and resources. Prozess: Stell dir eine große Küche vor, den Speicherbereich und die Ressourcen.

It has its own set of ingredients, appliances, and a cookbook, the program code. Sie hat ihre eigene Sammlung von Zutaten, Geräten und ein Kochbuch, den Programmcode.

The kitchen itself is isolated from other kitchens. Die Küche selbst ist von anderen Küchen isoliert.

Single-threaded Process: There's only one chef in the kitchen. Einzelthread-Prozess: Es gibt nur einen Koch in der Küche.

This chef has to do everything one step at a time: read the recipe, chop vegetables, cook on the stove, clean up, etc. Dieser Koch muss alles Schritt für Schritt tun: das Rezept lesen, Gemüse schneiden, auf dem Herd kochen, aufräumen usw.

If the chef is busy with a long task, like waiting for something to bake, nothing else gets done. Wenn der Koch mit einer langen Aufgabe beschäftigt ist, wie dem Warten darauf, dass etwas backt, wird nichts anderes erledigt.

Multi-threaded Process: There are multiple chefs, threads, in the same kitchen. Multithread-Prozess: Es gibt mehrere Köche, Threads, in derselben Küche.

They all share the same ingredients, appliances, and cookbook. Sie alle teilen dieselben Zutaten, Geräte und das Kochbuch.

One chef might be chopping vegetables, another stirring a pot, and a third washing dishes. Ein Koch könnte Gemüse schneiden, ein anderer einen Topf umrühren und ein dritter Geschirr waschen.

They can work on different tasks concurrently, making the overall meal preparation faster and more efficient. Sie können an verschiedenen Aufgaben nebenläufig arbeiten, wodurch die gesamte Essenszubereitung schneller und effizienter wird.

They need to coordinate carefully, though, to avoid getting in each other's way, for example both trying to use the same knife at the exact same time. Sie müssen sich jedoch sorgfältig koordinieren, um sich nicht gegenseitig im Weg zu stehen, zum Beispiel wenn beide versuchen, zur exakt gleichen Zeit dasselbe Messer zu benutzen.

How the OS Manages Them. Wie das OS sie verwaltet.

The Operating System is the ultimate manager. Das Betriebssystem ist der ultimative Manager.

It creates processes, allocates resources to them, and schedules when they, or their threads, get to use the CPU. Es erstellt Prozesse, weist ihnen Ressourcen zu und plant, wann sie oder ihre Threads die CPU nutzen dürfen.

For threads, the OS, or sometimes a library within the process, manages their creation, scheduling, and synchronization. Für Threads verwaltet das OS, oder manchmal eine Bibliothek innerhalb des Prozesses, ihre Erstellung, Planung und Synchronisation.

You'll learn much more about how the OS juggles all these tasks in our upcoming lessons. Du wirst in unseren kommenden Lektionen viel mehr darüber lernen, wie das OS all diese Aufgaben jongliert.

For now, focus on understanding what processes and threads are, and the fundamental differences and relationships between them. Konzentriere dich vorerst darauf zu verstehen, was Prozesse und Threads sind und die grundlegenden Unterschiede und Beziehungen zwischen ihnen.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside. Versuche nicht vor dem Unterricht zu spicken, Spoiler drinnen.