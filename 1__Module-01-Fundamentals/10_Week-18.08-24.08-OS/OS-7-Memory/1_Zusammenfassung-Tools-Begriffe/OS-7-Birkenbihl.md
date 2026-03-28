Welcome to the fascinating world of computer memory. Willkommen in der faszinierenden Welt des Computerspeichers.

Before our live session on Operating System Memory, it's important to grasp some fundamental concepts. Vor unserer Live-Sitzung über Betriebssystem-Speicher ist es wichtig, einige grundlegende Konzepte zu erfassen.

This preparation will guide you through what memory is, why it needs managing, and how operating systems begin to tackle this crucial task. Diese Vorbereitung wird dich durch das führen, was Speicher ist, warum er verwaltet werden muss und wie Betriebssysteme beginnen, diese entscheidende Aufgabe anzugehen.

What is Computer Memory? Was ist Computerspeicher?

At its core, computer memory is any physical device capable of storing information temporarily, like Random Access Memory, RAM, or permanently, like your hard drive or Solid State Drive, SSD. Im Kern ist Computerspeicher jedes physische Gerät, das in der Lage ist, Informationen vorübergehend zu speichern, wie Random Access Memory, RAM, oder dauerhaft, wie deine Festplatte oder Solid State Drive, SSD.

For our purposes in discussing operating system memory management, we're primarily interested in Main Memory, RAM. Für unsere Zwecke bei der Diskussion über Betriebssystem-Speicherverwaltung sind wir hauptsächlich an Hauptspeicher, RAM, interessiert.

Random Access Memory, RAM, is the workspace of your computer. Random Access Memory, RAM, ist der Arbeitsbereich deines Computers.

When you run a program, like a web browser or a game, or open a file, the data and instructions the computer needs to work with are loaded from the slower permanent storage, like your SSD or hard drive, into RAM. Wenn du ein Programm ausführst, wie einen Webbrowser oder ein Spiel, oder eine Datei öffnest, werden die Daten und Anweisungen, mit denen der Computer arbeiten muss, vom langsameren permanenten Speicher, wie deiner SSD oder Festplatte, in den RAM geladen.

RAM is much faster than permanent storage, which is why it's used for active tasks. RAM ist viel schneller als permanenter Speicher, weshalb er für aktive Aufgaben verwendet wird.

Think of RAM as your desk: you pull out the papers, data and programs, you're currently working on from your filing cabinet, hard drive, and place them on your desk for quick access. Stell dir RAM als deinen Schreibtisch vor: du holst die Papiere, Daten und Programme, an denen du gerade arbeitest, aus deinem Aktenschrank, der Festplatte, und legst sie für schnellen Zugriff auf deinen Schreibtisch.

RAM is typically volatile memory, meaning its contents are lost when the power is turned off. RAM ist typischerweise flüchtiger Speicher, was bedeutet, dass sein Inhalt verloren geht, wenn die Stromversorgung ausgeschaltet wird.

This is in contrast to non-volatile memory, like SSDs, hard drives, or Read-Only Memory, ROM, which retains information even without power. Dies steht im Gegensatz zu nicht-flüchtigem Speicher, wie SSDs, Festplatten oder Read-Only Memory, ROM, der Informationen auch ohne Strom behält.

Think about it. Denk darüber nach.

Why do you think computers have both fast, volatile memory, RAM, and slower, non-volatile memory, storage drives? Warum denkst du, haben Computer sowohl schnellen, flüchtigen Speicher, RAM, als auch langsameren, nicht-flüchtigen Speicher, Speicherlaufwerke?

What would be the pros and cons of having only one type? Was wären die Vor- und Nachteile, nur einen Typ zu haben?

The Need for Memory Management. Die Notwendigkeit der Speicherverwaltung.

Imagine an office with many workers, processes, all needing desk space, RAM, simultaneously. Stell dir ein Büro mit vielen Arbeitern, Prozessen, vor, die alle gleichzeitig Schreibtischplatz, RAM, benötigen.

If there's no system for allocating and organizing this desk space, chaos would ensue. Wenn es kein System gibt, um diesen Schreibtischplatz zuzuweisen und zu organisieren, würde Chaos ausbrechen.

Workers might try to use the same spot, run out of space, or accidentally interfere with each other's documents. Arbeiter könnten versuchen, denselben Platz zu nutzen, keinen Platz mehr haben oder versehentlich die Dokumente der anderen stören.

An Operating System, OS, acts as the office manager for memory. Ein Betriebssystem, OS, fungiert als Büromanager für Speicher.

Memory management is the process by which the OS controls and coordinates the use of computer memory, allocating portions called blocks to various running programs to optimize overall system performance. Speicherverwaltung ist der Prozess, durch den das OS die Nutzung des Computerspeichers kontrolliert und koordiniert, indem es Teile, genannt Blöcke, verschiedenen laufenden Programmen zuweist, um die Gesamtsystemleistung zu optimieren.

Effective memory management is crucial for several reasons. Effektive Speicherverwaltung ist aus mehreren Gründen entscheidend.

Sharing: It allows multiple processes to share memory securely and efficiently. Teilen: Es ermöglicht mehreren Prozessen, Speicher sicher und effizient zu teilen.

Protection: It prevents one process from interfering with the memory of another process or the OS itself. Schutz: Es verhindert, dass ein Prozess in den Speicher eines anderen Prozesses oder des OS selbst eingreift.

If one program crashes, it shouldn't bring down the entire system or corrupt other programs. Wenn ein Programm abstürzt, sollte es nicht das gesamte System zum Absturz bringen oder andere Programme beschädigen.

Efficiency: It ensures that memory is used efficiently, minimizing wasted space and ensuring that processes have enough memory to run. Effizienz: Es stellt sicher, dass Speicher effizient genutzt wird, verschwendeten Platz minimiert und sicherstellt, dass Prozesse genug Speicher zum Laufen haben.

Relocation: It allows programs to be loaded into different parts of memory each time they run, providing flexibility. Verlagerung: Es ermöglicht, dass Programme bei jedem Lauf in verschiedene Teile des Speichers geladen werden, was Flexibilität bietet.

Memory Addresses: Finding Data. Speicheradressen: Daten finden.

Every byte of memory has a unique address, just like every house on a street has a unique address. Jedes Byte Speicher hat eine eindeutige Adresse, genau wie jedes Haus in einer Straße eine eindeutige Adresse hat.

When a program needs to store or retrieve data, it uses these addresses. Wenn ein Programm Daten speichern oder abrufen muss, verwendet es diese Adressen.

There are two main types of addresses we'll encounter. Es gibt zwei Haupttypen von Adressen, auf die wir stoßen werden.

Logical Address, or Virtual Address: This is the address generated by the CPU as seen by a program. Logische Adresse oder virtuelle Adresse: Dies ist die Adresse, die von der CPU generiert wird, wie sie von einem Programm gesehen wird.

Each process has its own private logical address space, starting from zero up to some maximum. Jeder Prozess hat seinen eigenen privaten logischen Adressraum, der von null bis zu einem Maximum reicht.

This means two different programs could both refer to address one thousand, but they would be referring to different actual memory locations. Das bedeutet, zwei verschiedene Programme könnten beide auf Adresse eintausend verweisen, aber sie würden sich auf verschiedene tatsächliche Speicherorte beziehen.

This simplifies programming, as programmers don't need to know where their program will physically reside in RAM. Dies vereinfacht die Programmierung, da Programmierer nicht wissen müssen, wo ihr Programm physisch im RAM residieren wird.

Physical Address: This is the actual address in the physical RAM chips. Physische Adresse: Dies ist die tatsächliche Adresse in den physischen RAM-Chips.

The OS, with the help of hardware, specifically the Memory Management Unit or MMU, translates logical addresses into physical addresses. Das OS übersetzt mit Hilfe von Hardware, speziell der Memory Management Unit oder MMU, logische Adressen in physische Adressen.

The concept of a separate logical address space for each process is fundamental to modern operating systems. Das Konzept eines separaten logischen Adressraums für jeden Prozess ist grundlegend für moderne Betriebssysteme.

It provides memory protection and allows for more flexible memory management techniques. Es bietet Speicherschutz und ermöglicht flexiblere Speicherverwaltungstechniken.

Try it yourself. Probiere es selbst aus.

Conceptual: Think of a large library. Konzeptionell: Denk an eine große Bibliothek.

Each book has a unique call number, its physical address on the shelf. Jedes Buch hat eine eindeutige Signatur, seine physische Adresse im Regal.

When you look up a book in the catalog using its title, a logical identifier, the catalog tells you its call number so you can find it. Wenn du ein Buch im Katalog anhand seines Titels nachschlägst, ein logischer Identifikator, sagt dir der Katalog seine Signatur, damit du es finden kannst.

How does this analogy relate to logical and physical addresses in a computer? Wie bezieht sich diese Analogie auf logische und physische Adressen in einem Computer?

A Process's View of Memory: The Address Space. Die Sicht eines Prozesses auf Speicher: Der Adressraum.

When a program is run, the OS creates a process and allocates it a process address space. Wenn ein Programm ausgeführt wird, erstellt das OS einen Prozess und weist ihm einen Prozessadressraum zu.

This is the set of logical addresses that the process can see and use. Dies ist die Menge der logischen Adressen, die der Prozess sehen und verwenden kann.

This address space is typically divided into several distinct segments. Dieser Adressraum ist typischerweise in mehrere verschiedene Segmente unterteilt.

Text Segment, or Code Segment: Contains the executable instructions of the program. Text-Segment oder Code-Segment: Enthält die ausführbaren Anweisungen des Programms.

This area is often read-only to prevent a program from accidentally modifying its own instructions. Dieser Bereich ist oft schreibgeschützt, um zu verhindern, dass ein Programm versehentlich seine eigenen Anweisungen ändert.

Data Segment: Stores global and static variables that are initialized before the program starts. Daten-Segment: Speichert globale und statische Variablen, die initialisiert werden, bevor das Programm startet.

BSS Segment, Block Started by Symbol: Stores uninitialized global and static variables. BSS-Segment, Block Started by Symbol: Speichert nicht initialisierte globale und statische Variablen.

These are typically initialized to zero by the OS when the program loads. Diese werden typischerweise auf null vom OS initialisiert, wenn das Programm lädt.

Heap: This is an area of memory used for dynamic memory allocation. Heap: Dies ist ein Speicherbereich, der für dynamische Speicherzuweisung verwendet wird.

When a program needs more memory at runtime, for example to store data whose size is not known at compile time, it can request it from the heap. Wenn ein Programm zur Laufzeit mehr Speicher benötigt, zum Beispiel um Daten zu speichern, deren Größe zur Kompilierzeit nicht bekannt ist, kann es ihn vom Heap anfordern.

The programmer is responsible for managing heap memory, allocating and freeing it. Der Programmierer ist verantwortlich für die Verwaltung des Heap-Speichers, ihn zuzuweisen und freizugeben.

Stack: This area is used for storing temporary data such as local variables within functions, function parameters, and return addresses when functions are called. Stack: Dieser Bereich wird verwendet, um temporäre Daten zu speichern, wie lokale Variablen innerhalb von Funktionen, Funktionsparameter und Rücksprungadressen, wenn Funktionen aufgerufen werden.

The stack operates on a Last-In, First-Out, LIFO, principle. Der Stack arbeitet nach einem Last-In-First-Out-, LIFO-, Prinzip.

Each thread in a process gets its own stack. Jeder Thread in einem Prozess bekommt seinen eigenen Stack.

This segmented view is a logical organization. Diese segmentierte Ansicht ist eine logische Organisation.

The OS and hardware work together to map these logical segments to physical RAM. Das OS und die Hardware arbeiten zusammen, um diese logischen Segmente auf den physischen RAM abzubilden.

Basic Memory Allocation. Grundlegende Speicherzuweisung.

When a new process starts, the OS needs to find a free block of physical memory large enough to hold it, or parts of it. Wenn ein neuer Prozess startet, muss das OS einen freien Block physischen Speichers finden, der groß genug ist, um ihn oder Teile davon aufzunehmen.

This is called memory allocation. Dies wird Speicherzuweisung genannt.

When the process terminates, its memory is deallocated and becomes available for other processes. Wenn der Prozess beendet wird, wird sein Speicher freigegeben und steht anderen Prozessen zur Verfügung.

Operating systems use various strategies to manage free memory and allocate it to processes. Betriebssysteme verwenden verschiedene Strategien, um freien Speicher zu verwalten und ihn Prozessen zuzuweisen.

Some early, simple methods include Fixed Partitioning. Einige frühe, einfache Methoden umfassen Fixed Partitioning.

Memory is divided into fixed-size partitions. Speicher wird in Partitionen fester Größe unterteilt.

Each partition can hold one process. Jede Partition kann einen Prozess aufnehmen.

This is simple but can lead to wasted memory if a process is smaller than its partition, internal fragmentation, or if a process is too large to fit in any available partition. Dies ist einfach, kann aber zu verschwendetem Speicher führen, wenn ein Prozess kleiner als seine Partition ist, interne Fragmentierung, oder wenn ein Prozess zu groß ist, um in eine verfügbare Partition zu passen.

Dynamic Partitioning: Partitions are created dynamically to fit the size of the process. Dynamic Partitioning: Partitionen werden dynamisch erstellt, um zur Größe des Prozesses zu passen.

This reduces internal fragmentation but can lead to small, unusable holes of free memory between allocated blocks, external fragmentation, over time. Dies reduziert interne Fragmentierung, kann aber im Laufe der Zeit zu kleinen, unbrauchbaren Löchern freien Speichers zwischen zugewiesenen Blöcken, externe Fragmentierung, führen.

Modern operating systems use more sophisticated techniques like paging and segmentation, which we will explore in more detail during the live session. Moderne Betriebssysteme verwenden ausgefeiltere Techniken wie Paging und Segmentierung, die wir während der Live-Sitzung ausführlicher erkunden werden.

These techniques allow for virtual memory, where the OS can make the system appear to have more RAM than it physically does by using disk space as an overflow area. Diese Techniken ermöglichen virtuellen Speicher, bei dem das OS dem System den Anschein geben kann, mehr RAM zu haben, als es physisch hat, indem es Festplattenplatz als Überlaufbereich verwendet.

Think about it. Denk darüber nach.

Consider dynamic partitioning. Betrachte Dynamic Partitioning.

If you have a one hundred megabyte block of free memory and a process requests thirty megabytes, you allocate it. Wenn du einen einhundert Megabyte Block freien Speichers hast und ein Prozess dreißig Megabyte anfordert, weist du sie zu.

Then another process requests forty megabytes, you allocate that. Dann fordert ein anderer Prozess vierzig Megabyte an, du weist sie zu.

Now you have a thirty megabyte free block. Jetzt hast du einen dreißig Megabyte freien Block.

If a new process needs fifty megabytes, it can't be satisfied even though there's sixty megabytes free in total, thirty megabytes from the first allocation plus thirty megabytes from the second. Wenn ein neuer Prozess fünfzig Megabyte benötigt, kann er nicht befriedigt werden, obwohl insgesamt sechzig Megabyte frei sind, dreißig Megabyte von der ersten Zuweisung plus dreißig Megabyte von der zweiten.

This is external fragmentation. Dies ist externe Fragmentierung.

Can you think of any ways an OS might try to solve or reduce this problem? Kannst du dir irgendwelche Möglichkeiten vorstellen, wie ein OS versuchen könnte, dieses Problem zu lösen oder zu reduzieren?

This pre-class material should give you a solid foundation for our upcoming lesson on OS Memory. Dieses Vorbereitungsmaterial sollte dir eine solide Grundlage für unsere kommende Lektion über OS-Speicher geben.

We'll build upon these concepts to understand how Windows manages memory in more detail, including virtual memory, paging, and other advanced topics. Wir werden auf diesen Konzepten aufbauen, um zu verstehen, wie Windows Speicher im Detail verwaltet, einschließlich virtuellem Speicher, Paging und anderen fortgeschrittenen Themen.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside. Versuche nicht vor dem Unterricht zu spicken, Spoiler drinnen.