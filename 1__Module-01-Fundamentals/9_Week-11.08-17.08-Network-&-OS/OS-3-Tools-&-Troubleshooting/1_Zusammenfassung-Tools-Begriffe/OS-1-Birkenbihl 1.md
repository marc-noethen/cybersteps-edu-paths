Welcome to your pre-class preparation for Operating Systems 2! Willkommen zu deiner Vorbereitung vor dem Unterricht für Betriebssysteme 2!

In this module, and indeed for much of our Operating Systems learning, our primary focus will be on the Microsoft Windows operating system. In diesem Modul, und tatsächlich für einen Großteil unseres Betriebssystem-Lernens, wird unser Hauptfokus auf dem Microsoft Windows Betriebssystem liegen.

It's dominant on desktops worldwide and forms the backbone of countless corporate environments, making it a critical area of study for any cybersecurity professional. Es ist weltweit auf Desktops dominant und bildet das Rückgrat unzähliger Unternehmensumgebungen, was es zu einem kritischen Studienbereich für jeden Cybersecurity-Experten macht.

But if you're using a Mac, how will you get hands-on experience with Windows? Aber wenn du einen Mac verwendest, wie wirst du praktische Erfahrung mit Windows sammeln?

The solution is virtualization. Die Lösung ist Virtualisierung.

This document will guide you through the following: Understanding Virtualization. Dieses Dokument wird dich durch Folgendes führen: Virtualisierung verstehen.

We'll explore what virtualization is, how it allows you to run Windows on your Mac, and why it's an indispensable tool in cybersecurity. Wir werden erkunden, was Virtualisierung ist, wie sie dir ermöglicht, Windows auf deinem Mac auszuführen, und warum sie ein unverzichtbares Werkzeug in der Cybersecurity ist.

Introduction to Windows. Einführung in Windows.

A brief overview of the Windows operating system, highlighting key features and components that will be relevant to our cybersecurity studies. Ein kurzer Überblick über das Windows Betriebssystem, der wichtige Funktionen und Komponenten hervorhebt, die für unsere Cybersecurity-Studien relevant sein werden.

Overview of Virtual Machine Setup. Überblick über das Einrichten der virtuellen Maschine.

We'll outline the main steps for setting up your Windows Virtual Machine. Wir werden die Hauptschritte zum Einrichten deiner virtuellen Windows-Maschine skizzieren.

For detailed, step-by-step instructions, please refer to the provided setup video. Für detaillierte Schritt-für-Schritt-Anleitungen beziehe dich bitte auf das bereitgestellte Setup-Video.

Getting Started with Your Windows Virtual Machine. Erste Schritte mit deiner virtuellen Windows-Maschine.

A few initial tasks to help you become familiar with your new Windows environment once it's up and running. Ein paar erste Aufgaben, die dir helfen, dich mit deiner neuen Windows-Umgebung vertraut zu machen, sobald sie läuft.

Let's begin by understanding virtualization. Lass uns damit beginnen, Virtualisierung zu verstehen.

What is Virtualization? Was ist Virtualisierung?

Virtualization allows you to run multiple operating systems simultaneously on a single physical computer. Virtualisierung ermöglicht es dir, mehrere Betriebssysteme gleichzeitig auf einem einzigen physischen Computer auszuführen.

We do this using a Virtual Machine, which is essentially a computer emulated in software. Wir tun dies mithilfe einer virtuellen Maschine, die im Wesentlichen ein in Software emulierter Computer ist.

This Virtual Machine acts like a separate, independent computer, running its own operating system, in our case Windows, and applications, all isolated from your Mac's main operating system, the host. Diese virtuelle Maschine verhält sich wie ein separater, unabhängiger Computer, der sein eigenes Betriebssystem, in unserem Fall Windows, und Anwendungen ausführt, alles isoliert vom Hauptbetriebssystem deines Macs, dem Host.

This magic is orchestrated by a piece of software called a hypervisor. Dieser Zauber wird von einer Software namens Hypervisor orchestriert.

The hypervisor, like VMware Fusion Pro, which we'll use, manages your Mac's physical resources, CPU, memory, storage, and allocates a portion of them to each Virtual Machine. Der Hypervisor, wie VMware Fusion Pro, das wir verwenden werden, verwaltet die physischen Ressourcen deines Macs, CPU, Speicher, Storage, und weist jeder virtuellen Maschine einen Teil davon zu.

Think about it. Denk darüber nach.

Why might it be useful to run a completely separate operating system like Windows on your Mac without needing to buy a new physical computer or alter your Mac's primary setup? Warum könnte es nützlich sein, ein völlig separates Betriebssystem wie Windows auf deinem Mac auszuführen, ohne einen neuen physischen Computer kaufen oder die primäre Einrichtung deines Macs ändern zu müssen?

Why Use Virtual Machines in Cybersecurity? Warum virtuelle Maschinen in der Cybersecurity verwenden?

Virtual machines are indispensable tools in the cybersecurity field for several reasons. Virtuelle Maschinen sind aus mehreren Gründen unverzichtbare Werkzeuge im Cybersecurity-Bereich.

Isolated Environments for Analysis. Isolierte Umgebungen für die Analyse.

When analyzing malware, viruses, ransomware, etc., you need a safe space. Wenn du Malware, Viren, Ransomware usw. analysierst, brauchst du einen sicheren Ort.

Running malware on your primary machine could be disastrous. Malware auf deinem Hauptrechner auszuführen könnte katastrophal sein.

A Virtual Machine provides an isolated sandbox where you can execute and study malicious software without risking your host system. Eine virtuelle Maschine bietet eine isolierte Sandbox, in der du bösartige Software ausführen und untersuchen kannst, ohne dein Host-System zu gefährden.

If the Virtual Machine gets infected, you can often revert it to a clean state using snapshots or simply delete it and start over. Wenn die virtuelle Maschine infiziert wird, kannst du sie oft in einen sauberen Zustand zurückversetzen mithilfe von Snapshots oder sie einfach löschen und von vorne beginnen.

Testing and Experimentation. Testen und Experimentieren.

Cybersecurity professionals often need to test security tools, configurations, or exploits. Cybersecurity-Experten müssen oft Sicherheitstools, Konfigurationen oder Exploits testen.

Virtual Machines allow you to create various environments, different operating systems, patch levels, software installations, to test how things work or how vulnerabilities can be exploited, all without impacting your daily-use computer. Virtuelle Maschinen ermöglichen es dir, verschiedene Umgebungen, unterschiedliche Betriebssysteme, Patch-Level, Software-Installationen, zu erstellen, um zu testen, wie Dinge funktionieren oder wie Schwachstellen ausgenutzt werden können, alles ohne deinen täglich genutzten Computer zu beeinträchtigen.

Penetration Testing Labs. Penetrationstest-Labore.

Ethical hackers, penetration testers, often build virtual labs consisting of multiple Virtual Machines networked together. Ethische Hacker, Penetrationstester, bauen oft virtuelle Labore auf, die aus mehreren vernetzten virtuellen Maschinen bestehen.

This allows them to simulate real-world network environments and practice attacking and defending different systems. Dies ermöglicht es ihnen, reale Netzwerkumgebungen zu simulieren und das Angreifen und Verteidigen verschiedener Systeme zu üben.

Forensic Investigations. Forensische Untersuchungen.

Virtual Machines can be used to examine disk images from compromised systems. Virtuelle Maschinen können verwendet werden, um Festplatten-Images von kompromittierten Systemen zu untersuchen.

This allows investigators to boot up a copy of the suspect system in an isolated environment to look for evidence. Dies ermöglicht es Ermittlern, eine Kopie des verdächtigen Systems in einer isolierten Umgebung hochzufahren, um nach Beweisen zu suchen.

Running Different Operating Systems. Verschiedene Betriebssysteme ausführen.

As we're about to do, Virtual Machines let you run an operating system like Windows that's different from your host operating system, macOS, when needed for specific tools or learning objectives. Wie wir es gleich tun werden, ermöglichen dir virtuelle Maschinen, ein Betriebssystem wie Windows auszuführen, das sich von deinem Host-Betriebssystem, macOS, unterscheidet, wenn es für bestimmte Tools oder Lernziele benötigt wird.

Introduction to the Windows Operating System. Einführung in das Windows-Betriebssystem.

Microsoft Windows, as mentioned, is a cornerstone of modern computing and a central focus for this course. Microsoft Windows ist, wie erwähnt, ein Eckpfeiler der modernen Datenverarbeitung und ein zentraler Fokus für diesen Kurs.

As you progress in cybersecurity, you'll encounter it constantly. Während du in der Cybersecurity vorankommst, wirst du ständig darauf stoßen.

Here are some key aspects we'll explore. Hier sind einige Schlüsselaspekte, die wir erkunden werden.

Graphical User Interface. Grafische Benutzeroberfläche.

Windows is known for its user-friendly graphical interface, which includes the desktop, Start Menu, File Explorer, and Taskbar. Windows ist bekannt für seine benutzerfreundliche grafische Oberfläche, die den Desktop, das Startmenü, den Datei-Explorer und die Taskleiste umfasst.

File System, NTFS. Dateisystem, NTFS.

Windows primarily uses the NTFS, New Technology File System, to organize and store files on disk. Windows verwendet hauptsächlich das NTFS, New Technology File System, um Dateien auf der Festplatte zu organisieren und zu speichern.

Understanding NTFS is important for digital forensics. Das Verständnis von NTFS ist wichtig für digitale Forensik.

Registry. Registrierung.

The Windows Registry is a hierarchical database that stores low-level settings for the operating system and for applications. Die Windows-Registrierung ist eine hierarchische Datenbank, die Low-Level-Einstellungen für das Betriebssystem und Anwendungen speichert.

It's a critical component for system configuration and a common place for malware to maintain persistence. Sie ist eine kritische Komponente für die Systemkonfiguration und ein häufiger Ort für Malware, um Persistenz aufrechtzuerhalten.

Command Line Interfaces. Befehlszeilenschnittstellen.

While the Graphical User Interface is prominent, Windows also has powerful command-line interfaces. Während die grafische Benutzeroberfläche prominent ist, hat Windows auch leistungsstarke Befehlszeilenschnittstellen.

Command Prompt. Eingabeaufforderung.

The traditional command-line interpreter. Der traditionelle Befehlszeileninterpreter.

PowerShell. PowerShell.

A more advanced command-line shell and scripting language built on the .NET framework. Eine fortschrittlichere Befehlszeilen-Shell und Skriptsprache, die auf dem .NET Framework aufbaut.

PowerShell is extensively used for system administration and, increasingly, in cybersecurity for both offensive and defensive tasks. PowerShell wird ausgiebig für die Systemadministration und zunehmend in der Cybersecurity sowohl für offensive als auch defensive Aufgaben verwendet.

User Account Control. Benutzerkontensteuerung.

A security feature that helps prevent unauthorized changes to your computer. Eine Sicherheitsfunktion, die hilft, unbefugte Änderungen an deinem Computer zu verhindern.

Windows Defender / Microsoft Defender Antivirus. Windows Defender / Microsoft Defender Antivirus.

Built-in anti-malware software. Integrierte Anti-Malware-Software.

Event Logs. Ereignisprotokolle.

Windows records significant events that occur on the system, which are invaluable for troubleshooting and security incident investigation. Windows zeichnet bedeutende Ereignisse auf, die im System auftreten und die von unschätzbarem Wert für die Fehlerbehebung und Untersuchung von Sicherheitsvorfällen sind.

Becoming comfortable navigating Windows, understanding its core components, and knowing how to use its tools are key goals. Sich mit der Navigation in Windows vertraut zu machen, seine Kernkomponenten zu verstehen und zu wissen, wie man seine Tools verwendet, sind wichtige Ziele.

Setup: Installing Your Windows Virtual Machine. Einrichtung: Installation deiner virtuellen Windows-Maschine.

This section provides a high-level overview of the steps to get your Windows virtual machine running using VMware Fusion Pro on your Mac. Dieser Abschnitt bietet einen Überblick über die Schritte, um deine virtuelle Windows-Maschine mit VMware Fusion Pro auf deinem Mac zum Laufen zu bringen.

For detailed, step-by-step instructions on downloading, installing, and configuring VMware Fusion Pro and your Windows Virtual Machine, please watch the provided setup video. Für detaillierte Schritt-für-Schritt-Anleitungen zum Herunterladen, Installieren und Konfigurieren von VMware Fusion Pro und deiner virtuellen Windows-Maschine schaue bitte das bereitgestellte Setup-Video an.

Run Windows 11 on Mac with free VMware Fusion Pro license. Führe Windows 11 auf dem Mac mit einer kostenlosen VMware Fusion Pro Lizenz aus.

Important Notes Before You Begin, covered in detail in the video. Wichtige Hinweise, bevor du beginnst, im Video ausführlich behandelt.

Time. Zeit.

The entire process can take 30 minutes to over an hour. Der gesamte Prozess kann 30 Minuten bis über eine Stunde dauern.

Disk Space. Festplattenspeicher.

Ensure at least 40 gigabytes of free disk space. Stelle sicher, dass du mindestens 40 Gigabyte freien Festplattenspeicher hast.

Internet Connection. Internetverbindung.

A stable connection is needed for downloads. Eine stabile Verbindung ist für Downloads erforderlich.

Administrator Privileges. Administratorrechte.

Required for installing VMware Fusion Pro. Erforderlich für die Installation von VMware Fusion Pro.

Brief Outline of the Installation Process. Kurze Übersicht über den Installationsprozess.

The video will guide you through these main stages. Das Video wird dich durch diese Hauptphasen führen.

Get VMware Fusion Pro. Besorge VMware Fusion Pro.

Download VMware Fusion Pro. Lade VMware Fusion Pro herunter.

Follow the guide, create a Broadcom account, download link should be under free downloads, search for vmware fusion. Folge dem Leitfaden, erstelle ein Broadcom-Konto, der Download-Link sollte unter kostenlose Downloads zu finden sein, suche nach vmware fusion.

Create Your Windows Virtual Machine in VMware Fusion Pro. Erstelle deine virtuelle Windows-Maschine in VMware Fusion Pro.

Open VMware Fusion Pro and start the new virtual machine creation process. Öffne VMware Fusion Pro und starte den Prozess zur Erstellung einer neuen virtuellen Maschine.

Utilize the built-in feature to Get Windows from Microsoft. Nutze die integrierte Funktion, um Windows von Microsoft zu bekommen.

VMware Fusion Pro will help you download the necessary Windows installation files, ISO. VMware Fusion Pro wird dir helfen, die notwendigen Windows-Installationsdateien, ISO, herunterzuladen.

Install the Windows Operating System. Installiere das Windows-Betriebssystem.

Start the Virtual Machine. Starte die virtuelle Maschine.

It will boot from the downloaded Windows installation media. Sie wird von den heruntergeladenen Windows-Installationsmedien booten.

Follow the on-screen prompts of the Windows Setup wizard, selecting language, edition, accepting terms, choosing Custom install, and creating your user account and password. Folge den Bildschirmaufforderungen des Windows-Setup-Assistenten, Auswahl der Sprache, Edition, Akzeptieren der Bedingungen, Auswahl der benutzerdefinierten Installation und Erstellen deines Benutzerkontos und Passworts.

Install VMware Tools. Installiere VMware Tools.

After the Virtual Machine is installed and running, from the top menu select Virtual Machine, Install VMware Tools. Nachdem die virtuelle Maschine installiert ist und läuft, wähle im oberen Menü Virtuelle Maschine, VMware Tools installieren.

This will allow you to copy and paste text into the Virtual Machine, move files and other useful features. Dies ermöglicht es dir, Text in die virtuelle Maschine zu kopieren und einzufügen, Dateien zu verschieben und andere nützliche Funktionen zu nutzen.

Again, please refer to the provided video for the complete, step-by-step walkthrough of this setup process. Nochmals, beziehe dich bitte auf das bereitgestellte Video für die vollständige Schritt-für-Schritt-Anleitung dieses Einrichtungsprozesses.

Getting Started with Your Windows Virtual Machine, Post-Installation. Erste Schritte mit deiner virtuellen Windows-Maschine, nach der Installation.

Once you have successfully installed your Windows Virtual Machine by following the video guide, take these first steps to familiarize yourself with the environment. Sobald du deine virtuelle Windows-Maschine erfolgreich installiert hast, indem du dem Video-Leitfaden gefolgt bist, unternimm diese ersten Schritte, um dich mit der Umgebung vertraut zu machen.

Try it yourself. Probiere es selbst aus.

Log In. Melde dich an.

Start your Windows Virtual Machine from VMware Fusion and log in with the username and password you created during the Windows setup. Starte deine virtuelle Windows-Maschine von VMware Fusion und melde dich mit dem Benutzernamen und Passwort an, die du während der Windows-Einrichtung erstellt hast.

Explore the Start Menu. Erkunde das Startmenü.

Click the Start button, usually in the bottom-left corner or centered on Windows 11. Klicke auf die Start-Schaltfläche, normalerweise in der unteren linken Ecke oder zentriert bei Windows 11.

See what applications and settings are available. Schau, welche Anwendungen und Einstellungen verfügbar sind.

File Explorer. Datei-Explorer.

Open File Explorer, the folder icon on the taskbar or find it in the Start Menu. Öffne den Datei-Explorer, das Ordnersymbol auf der Taskleiste oder finde es im Startmenü.

Try creating a new folder on your Desktop, right-click on Desktop, New, Folder. Versuche, einen neuen Ordner auf deinem Desktop zu erstellen, Rechtsklick auf Desktop, Neu, Ordner.

Command Prompt. Eingabeaufforderung.

Search for cmd in the Start Menu and open Command Prompt. Suche nach cmd im Startmenü und öffne die Eingabeaufforderung.

Type the command ipconfig and press Enter. Gib den Befehl ipconfig ein und drücke Enter.

This command shows your Virtual Machine's network configuration. Dieser Befehl zeigt die Netzwerkkonfiguration deiner virtuellen Maschine.

What is the IPv4 Address listed? Welche IPv4-Adresse ist aufgeführt?

PowerShell. PowerShell.

Search for PowerShell in the Start Menu and open Windows PowerShell. Suche nach PowerShell im Startmenü und öffne Windows PowerShell.

Type the command Get-Process and press Enter. Gib den Befehl Get-Process ein und drücke Enter.

This lists all running processes on your Windows Virtual Machine. Dies listet alle laufenden Prozesse auf deiner virtuellen Windows-Maschine auf.

Scroll through the list. Scrolle durch die Liste.

Do you recognize any process names? Erkennst du irgendwelche Prozessnamen?

Shutdown/Restart. Herunterfahren/Neustart.

Practice properly shutting down your Windows Virtual Machine, Start Menu, Power icon, Shut down, and then starting it again from VMware Fusion. Übe das ordnungsgemäße Herunterfahren deiner virtuellen Windows-Maschine, Startmenü, Energie-Symbol, Herunterfahren, und starte sie dann erneut von VMware Fusion.

Avoid just closing the Virtual Machine window without shutting down Windows, as this can sometimes lead to issues like a forced power-off. Vermeide es, einfach das Fenster der virtuellen Maschine zu schließen, ohne Windows herunterzufahren, da dies manchmal zu Problemen führen kann, wie einem erzwungenen Ausschalten.

Congratulations! Herzlichen Glückwunsch!

You've successfully set up your Windows lab environment. Du hast erfolgreich deine Windows-Laborumgebung eingerichtet.

Having this Virtual Machine ready is crucial for the upcoming lessons where we'll dive deeper into the Windows operating system from a cybersecurity perspective. Diese virtuelle Maschine bereit zu haben, ist entscheidend für die kommenden Lektionen, in denen wir tiefer in das Windows-Betriebssystem aus einer Cybersecurity-Perspektive eintauchen werden.