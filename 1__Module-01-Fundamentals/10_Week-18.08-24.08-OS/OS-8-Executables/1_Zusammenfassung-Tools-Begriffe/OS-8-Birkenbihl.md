Welcome to your pre-class preparation for our upcoming lesson on Executables. Willkommen zu deiner Vorbereitung vor dem Unterricht für unsere kommende Lektion über ausführbare Dateien.

This material will give you the basic knowledge to understand what executable files are, how they are created, how they generally work, and why they're important in operating systems and cybersecurity. Dieses Material wird dir das Grundwissen vermitteln, um zu verstehen, was ausführbare Dateien sind, wie sie erstellt werden, wie sie allgemein funktionieren und warum sie in Betriebssystemen und Cybersicherheit wichtig sind.

What is an Executable File? Was ist eine ausführbare Datei?

Think of an executable file as a ready-to-run instruction manual for your computer. Stell dir eine ausführbare Datei als eine einsatzbereite Bedienungsanleitung für deinen Computer vor.

When you want to start a program, like a web browser, a game, or a simple calculator, you're telling the operating system, OS, to open this manual and follow its steps. Wenn du ein Programm starten möchtest, wie einen Webbrowser, ein Spiel oder einen einfachen Taschenrechner, sagst du dem Betriebssystem, OS, es soll diese Anleitung öffnen und ihren Schritten folgen.

The computer's processor, CPU, reads these instructions and carries them out. Der Prozessor des Computers, CPU, liest diese Anweisungen und führt sie aus.

On Windows computers, you'll often see these files with an dot exe extension, short for executable, for example, notepad dot exe, Notepad. Auf Windows-Computern wirst du diese Dateien oft mit einer punkt exe-Erweiterung sehen, kurz für executable, zum Beispiel notepad punkt exe, Notepad.

Another common type you'll encounter is a dot dll, Dynamic Link Library, file, which we'll discuss later. Ein anderer häufiger Typ, auf den du stoßen wirst, ist eine punkt dll-Datei, Dynamic Link Library, über die wir später sprechen werden.

From Human Code to Machine Instructions: A Quick Overview. Von menschlichem Code zu Maschinenanweisungen: Ein kurzer Überblick.

You might wonder how these executable files come into being. Du fragst dich vielleicht, wie diese ausführbaren Dateien entstehen.

Programmers write software using human-readable languages like Python, C plus plus, or Java. Programmierer schreiben Software mit für Menschen lesbaren Sprachen wie Python, C plus plus oder Java.

This is called source code. Dies wird Quellcode genannt.

However, a computer's CPU doesn't understand Python or C plus plus directly. Jedoch versteht die CPU eines Computers Python oder C plus plus nicht direkt.

It only understands very basic instructions called machine code, which are sequences of numbers. Sie versteht nur sehr grundlegende Anweisungen, genannt Maschinencode, die Zahlenfolgen sind.

So, how does source code become machine code? Also, wie wird Quellcode zu Maschinencode?

Compilation: For languages like C plus plus or C sharp, the source code goes through a process called compilation. Kompilierung: Für Sprachen wie C plus plus oder C sharp durchläuft der Quellcode einen Prozess namens Kompilierung.

A special program called a compiler translates the human-readable source code into low-level instructions. Ein spezielles Programm namens Compiler übersetzt den für Menschen lesbaren Quellcode in niedrigstufige Anweisungen.

Sometimes, this intermediate step is assembly language. Manchmal ist dieser Zwischenschritt Assemblersprache.

Assembly language is a bit more human-readable than raw machine code but is very close to what the hardware understands. Assemblersprache ist etwas besser für Menschen lesbar als reiner Maschinencode, liegt aber sehr nahe an dem, was die Hardware versteht.

Assembling: If the compiler produces assembly language, another tool called an assembler then converts the assembly language into actual machine code. Assemblieren: Wenn der Compiler Assemblersprache erzeugt, wandelt ein anderes Werkzeug namens Assembler die Assemblersprache dann in tatsächlichen Maschinencode um.

Linking: Often, a program is made of many different source code files and might use pre-written code from libraries. Linken: Oft besteht ein Programm aus vielen verschiedenen Quellcodedateien und könnte vorgeschriebenen Code aus Bibliotheken verwenden.

A linker takes all these pieces of machine code and combines them into a single executable file, like an dot exe or dot dll. Ein Linker nimmt all diese Stücke Maschinencode und kombiniert sie zu einer einzelnen ausführbaren Datei, wie einer punkt exe oder punkt dll.

It also prepares the file so the operating system knows how to load and run it. Er bereitet auch die Datei so vor, dass das Betriebssystem weiß, wie es sie laden und ausführen kann.

The result of this process is an executable file, packed with machine code instructions that your CPU can execute. Das Ergebnis dieses Prozesses ist eine ausführbare Datei, vollgepackt mit Maschinencode-Anweisungen, die deine CPU ausführen kann.

Think about it. Denk darüber nach.

Why do you think programmers use high-level languages like Python or C plus plus instead of writing machine code or assembly language directly, even though the computer only understands machine code? Warum denkst du, verwenden Programmierer höhere Programmiersprachen wie Python oder C plus plus, anstatt Maschinencode oder Assemblersprache direkt zu schreiben, obwohl der Computer nur Maschinencode versteht?

A Quick Look Inside: How Executables are Organized. Ein kurzer Blick ins Innere: Wie ausführbare Dateien organisiert sind.

Executable files aren't just a jumble of machine code. Ausführbare Dateien sind nicht nur ein Durcheinander von Maschinencode.

They have an internal structure that helps the OS understand and run them efficiently. Sie haben eine interne Struktur, die dem OS hilft, sie effizient zu verstehen und auszuführen.

On Windows, this structure is often referred to as the Portable Executable, PE, format. Unter Windows wird diese Struktur oft als Portable Executable-, PE-, Format bezeichnet.

You don't need to know all the tiny details, but the main idea is that the file is organized into different parts. Du musst nicht alle winzigen Details kennen, aber die Hauptidee ist, dass die Datei in verschiedene Teile organisiert ist.

Headers: These are at the very beginning, like a cover page and table of contents. Header: Diese sind ganz am Anfang, wie eine Titelseite und ein Inhaltsverzeichnis.

They tell the OS essential information: what kind of program it is, where the main instructions start, how much memory it might need, and where other important pieces of information within the file are located. Sie sagen dem OS wesentliche Informationen: was für ein Programm es ist, wo die Hauptanweisungen beginnen, wie viel Speicher es möglicherweise benötigt und wo andere wichtige Informationen innerhalb der Datei zu finden sind.

Sections: Following the headers, the file is divided into various sections. Abschnitte: Nach den Headern ist die Datei in verschiedene Abschnitte unterteilt.

Think of these as chapters, each holding a specific type of content. Denk an diese als Kapitel, von denen jedes einen bestimmten Inhaltstyp enthält.

One section typically holds the actual program instructions, the machine code. Ein Abschnitt enthält typischerweise die tatsächlichen Programmanweisungen, den Maschinencode.

Other sections might hold data the program uses, like text messages it displays or default settings. Andere Abschnitte könnten Daten enthalten, die das Programm verwendet, wie Textnachrichten, die es anzeigt, oder Standardeinstellungen.

Another important section often lists any external functions the program needs to borrow from other files, like DLLs. Ein anderer wichtiger Abschnitt listet oft alle externen Funktionen auf, die das Programm von anderen Dateien ausleihen muss, wie DLLs.

This organization helps the OS load only what's needed into memory and manage the program effectively. Diese Organisation hilft dem OS, nur das Nötige in den Speicher zu laden und das Programm effektiv zu verwalten.

In cybersecurity, analysts often examine these headers and sections to understand a program's purpose, especially if it's suspected malware. In der Cybersicherheit untersuchen Analysten oft diese Header und Abschnitte, um den Zweck eines Programms zu verstehen, besonders wenn es verdächtige Malware ist.

The Loading Process: From Clicking to Running. Der Ladeprozess: Vom Klicken zum Ausführen.

When you double-click an dot exe file, the OS doesn't just instantly run it. Wenn du auf eine punkt exe-Datei doppelklickst, führt das OS sie nicht einfach sofort aus.

A part of the OS called the loader performs several important steps. Ein Teil des OS namens Loader führt mehrere wichtige Schritte aus.

Reads the File: The loader first looks at the executable's headers to understand its structure and requirements. Liest die Datei: Der Loader schaut sich zuerst die Header der ausführbaren Datei an, um ihre Struktur und Anforderungen zu verstehen.

Sets up Memory: It allocates space in the computer's memory for the program. Richtet Speicher ein: Er weist Platz im Speicher des Computers für das Programm zu.

Loads Instructions and Data: It copies the necessary parts of the program, like the machine code and initial data, from your storage, for example hard drive, into the allocated memory. Lädt Anweisungen und Daten: Er kopiert die notwendigen Teile des Programms, wie den Maschinencode und anfängliche Daten, von deinem Speicher, zum Beispiel Festplatte, in den zugewiesenen Speicher.

Handles Dependencies, Dynamic Linking: Many programs need to use functions provided by other files, especially Dynamic Link Libraries, DLLs. Behandelt Abhängigkeiten, dynamisches Linken: Viele Programme müssen Funktionen verwenden, die von anderen Dateien bereitgestellt werden, besonders Dynamic Link Libraries, DLLs.

The loader finds these required DLLs and connects them to the program so it can use their functions. Der Loader findet diese erforderlichen DLLs und verbindet sie mit dem Programm, damit es ihre Funktionen nutzen kann.

Starts the Program: Once everything is prepared, the loader tells the CPU to begin executing the program's instructions from its designated starting point. Startet das Programm: Sobald alles vorbereitet ist, sagt der Loader der CPU, sie soll beginnen, die Anweisungen des Programms von seinem festgelegten Startpunkt aus auszuführen.

Sharing Code: Dynamic Linking and DLLs. Code teilen: Dynamisches Linken und DLLs.

Programs often need to perform common tasks, like opening files, displaying windows, or communicating over the network. Programme müssen oft allgemeine Aufgaben ausführen, wie Dateien öffnen, Fenster anzeigen oder über das Netzwerk kommunizieren.

Instead of every program having its own code for these tasks, they can use shared code from Dynamic Link Libraries, DLLs. Anstatt dass jedes Programm seinen eigenen Code für diese Aufgaben hat, können sie gemeinsamen Code aus Dynamic Link Libraries, DLLs, verwenden.

What are DLLs? Was sind DLLs?

DLLs are collections of pre-compiled code and data that multiple programs can use simultaneously. DLLs sind Sammlungen von vorkompiliertem Code und Daten, die mehrere Programme gleichzeitig verwenden können.

For example, a single DLL might contain functions for drawing windows on the screen, and many different applications can use this DLL to create their user interfaces. Zum Beispiel könnte eine einzelne DLL Funktionen zum Zeichnen von Fenstern auf dem Bildschirm enthalten, und viele verschiedene Anwendungen können diese DLL verwenden, um ihre Benutzeroberflächen zu erstellen.

How does it work? Wie funktioniert es?

When a program needs a function from a DLL, it doesn't include the entire DLL's code within its own dot exe file. Wenn ein Programm eine Funktion aus einer DLL benötigt, enthält es nicht den gesamten Code der DLL in seiner eigenen punkt exe-Datei.

Instead, the dot exe file just contains a reference saying, I need to use function X from Y dot dll. Stattdessen enthält die punkt exe-Datei nur einen Verweis, der besagt: Ich muss Funktion X aus Y punkt dll verwenden.

When you run the program, the OS loader is responsible for finding Y dot dll and making function X available to your program. Wenn du das Programm ausführst, ist der OS-Loader dafür verantwortlich, Y punkt dll zu finden und Funktion X für dein Programm verfügbar zu machen.

This is called dynamic linking. Dies wird dynamisches Linken genannt.

Benefits: Smaller dot exe files. Vorteile: Kleinere punkt exe-Dateien.

Programs are smaller because they don't duplicate common code. Programme sind kleiner, weil sie keinen gemeinsamen Code duplizieren.

Memory saving: If multiple programs use the same DLL, the OS can load a single copy of the DLL into memory and share it. Speichereinsparung: Wenn mehrere Programme dieselbe DLL verwenden, kann das OS eine einzelne Kopie der DLL in den Speicher laden und sie teilen.

Easier updates: If a DLL is updated, for example with a security fix or new features, all programs that use it can benefit from the update without needing to be changed themselves. Einfachere Updates: Wenn eine DLL aktualisiert wird, zum Beispiel mit einem Sicherheitsfix oder neuen Funktionen, können alle Programme, die sie verwenden, von dem Update profitieren, ohne selbst geändert werden zu müssen.

Potential Issues: If a required DLL is missing, corrupted, or the wrong version, the program might not start or work correctly. Potenzielle Probleme: Wenn eine erforderliche DLL fehlt, beschädigt ist oder die falsche Version hat, startet das Programm möglicherweise nicht oder funktioniert nicht richtig.

This is sometimes referred to as DLL Hell. Dies wird manchmal als DLL Hell bezeichnet.

Malicious actors can also try to trick programs into loading fake DLLs, DLL hijacking. Böswillige Akteure können auch versuchen, Programme dazu zu bringen, gefälschte DLLs zu laden, DLL-Hijacking.

You'll find many DLLs in your Windows system, for example in C colon backslash Windows backslash System32. Du wirst viele DLLs in deinem Windows-System finden, zum Beispiel in C Doppelpunkt Backslash Windows Backslash System32.

They are a fundamental part of how Windows and its applications operate. Sie sind ein grundlegender Teil davon, wie Windows und seine Anwendungen funktionieren.

Try it yourself. Probiere es selbst aus.

On your Windows VM, open File Explorer and go to the C colon backslash Windows backslash System32 folder. Öffne auf deiner Windows-VM den Datei-Explorer und gehe zum C Doppelpunkt Backslash Windows Backslash System32-Ordner.

Look at the file types. Schau dir die Dateitypen an.

You'll see a very large number of files with the dot dll extension. Du wirst eine sehr große Anzahl von Dateien mit der punkt dll-Erweiterung sehen.

You don't need to open them, but just notice they are there. Du musst sie nicht öffnen, aber bemerke einfach, dass sie da sind.

These are examples of dynamically linked libraries that many programs on your system share. Dies sind Beispiele für dynamisch gelinkte Bibliotheken, die viele Programme auf deinem System teilen.

Why is Understanding Executables Important in Cybersecurity? Warum ist das Verstehen von ausführbaren Dateien wichtig in der Cybersicherheit?

Even a high-level understanding of executables is very valuable in cybersecurity. Selbst ein grundlegendes Verständnis von ausführbaren Dateien ist sehr wertvoll in der Cybersicherheit.

Malware Analysis: Most malicious software, viruses, ransomware, spyware, is distributed as executable files, dot exe or sometimes dot dll. Malware-Analyse: Die meiste schädliche Software, Viren, Ransomware, Spyware, wird als ausführbare Dateien verteilt, punkt exe oder manchmal punkt dll.

Analysts need to understand how these files work to figure out what damage they can do and how to protect against them. Analysten müssen verstehen, wie diese Dateien funktionieren, um herauszufinden, welchen Schaden sie anrichten können und wie man sich dagegen schützt.

Understanding Attacks: Many cyberattacks involve tricking users into running malicious executables or exploiting how executables and DLLs are loaded by the OS. Angriffe verstehen: Viele Cyberangriffe beinhalten, Benutzer dazu zu bringen, schädliche ausführbare Dateien auszuführen, oder auszunutzen, wie ausführbare Dateien und DLLs vom OS geladen werden.

Digital Forensics: When investigating a security breach, experts often examine executable files found on compromised systems to understand how the attack happened. Digitale Forensik: Bei der Untersuchung eines Sicherheitsvorfalls untersuchen Experten oft ausführbare Dateien, die auf kompromittierten Systemen gefunden wurden, um zu verstehen, wie der Angriff stattgefunden hat.

Setup. Einrichtung.

For our upcoming lesson, we'll use a tool called CFF Explorer to look inside PE files. Für unsere kommende Lektion werden wir ein Werkzeug namens CFF Explorer verwenden, um in PE-Dateien hineinzuschauen.

Please set this up on your Windows Virtual Machine. Bitte richte dies auf deiner virtuellen Windows-Maschine ein.

Download CFF Explorer: Go to the official NTCore website, http colon slash slash www dot ntcore dot com slash exsuite dot php. CFF Explorer herunterladen: Gehe zur offiziellen NTCore-Website, http Doppelpunkt Schrägstrich Schrägstrich www Punkt ntcore Punkt com Schrägstrich exsuite Punkt php.

Download the Explorer Suite, it's a zip file. Lade die Explorer Suite herunter, es ist eine Zip-Datei.

Extract CFF Explorer: Create a folder on your Windows VM, for instance, C colon backslash Tools backslash CFFExplorer. CFF Explorer extrahieren: Erstelle einen Ordner auf deiner Windows-VM, zum Beispiel C Doppelpunkt Backslash Tools Backslash CFFExplorer.

Extract the contents of the downloaded zip file into this new folder. Extrahiere den Inhalt der heruntergeladenen Zip-Datei in diesen neuen Ordner.

Run CFF Explorer: Inside the folder, double-click CFF Explorer dot exe to run it. CFF Explorer ausführen: Doppelklicke im Ordner auf CFF Explorer punkt exe, um es auszuführen.

It doesn't need a separate installation. Es benötigt keine separate Installation.

Sometimes, security software might flag tools like this because they can be used to inspect system files. Manchmal könnte Sicherheitssoftware solche Werkzeuge markieren, weil sie zum Inspizieren von Systemdateien verwendet werden können.

CFF Explorer from the official site is a well-known tool for this purpose. CFF Explorer von der offiziellen Seite ist ein bekanntes Werkzeug für diesen Zweck.

Try opening a common program with it, like C colon backslash Windows backslash System32 backslash notepad dot exe. Versuche, ein gängiges Programm damit zu öffnen, wie C Doppelpunkt Backslash Windows Backslash System32 Backslash notepad Punkt exe.

Just look around the interface a bit. Schau dir einfach die Benutzeroberfläche ein wenig an.

We'll go over how to use it and what to look for in our lesson. Wir werden in unserer Lektion durchgehen, wie man es benutzt und wonach man sucht.

This preparation should give you a good foundation. Diese Vorbereitung sollte dir eine gute Grundlage geben.

Completing the setup will ensure you're ready for our hands-on activities. Das Abschließen der Einrichtung wird sicherstellen, dass du für unsere praktischen Aktivitäten bereit bist.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside. Versuche nicht vor dem Unterricht zu spicken, Spoiler drinnen.