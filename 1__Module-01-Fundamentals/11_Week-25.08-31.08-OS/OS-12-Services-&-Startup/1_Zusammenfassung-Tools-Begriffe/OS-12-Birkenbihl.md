Welcome to your pre-class preparation for our upcoming session on Windows Services and the System Startup process. Willkommen zur Vorbereitung vor dem Unterricht für unsere kommende Sitzung über Windows-Dienste und den Systemstartprozess.

Understanding these concepts is crucial for managing and securing an operating system. Das Verständnis dieser Konzepte ist entscheidend für die Verwaltung und Sicherung eines Betriebssystems.

We'll explore what services are, how they function, and how Windows manages applications and processes that start automatically. Wir werden untersuchen, was Dienste sind, wie sie funktionieren und wie Windows Anwendungen und Prozesse verwaltet, die automatisch starten.

What are Windows Services? Was sind Windows-Dienste?

In Windows, a service is a special type of application that runs in the background, without a direct user interface. In Windows ist ein Dienst eine spezielle Art von Anwendung, die im Hintergrund läuft, ohne eine direkte Benutzeroberfläche.

Think of them as the unsung heroes of the operating system, performing essential tasks that keep your system running smoothly. Denken Sie an sie als die unbesungenen Helden des Betriebssystems, die wesentliche Aufgaben ausführen, die Ihr System reibungslos am Laufen halten.

They can start when the computer boots up, even before you log in, and can continue to run as long as the computer is on. Sie können starten, wenn der Computer hochfährt, sogar bevor Sie sich anmelden, und können weiterlaufen, solange der Computer eingeschaltet ist.

Services handle a wide variety of functions, such as: managing network connections, for example DHCP Client and DNS Client. Dienste übernehmen eine Vielzahl von Funktionen, wie zum Beispiel: Verwaltung von Netzwerkverbindungen, beispielsweise DHCP-Client und DNS-Client.

Enabling printing, the Print Spooler. Drucken ermöglichen, die Druckerwarteschlange.

Keeping your system updated, Windows Update. Ihr System auf dem neuesten Stand halten, Windows Update.

Providing security features, Windows Defender Antivirus Service. Sicherheitsfunktionen bereitstellen, Windows Defender Antivirus-Dienst.

Running web servers or database engines. Webserver oder Datenbank-Engines ausführen.

Unlike regular desktop applications, like a web browser or a word processor, that you actively open and interact with, services operate behind the scenes. Im Gegensatz zu regulären Desktop-Anwendungen, wie einem Webbrowser oder einem Textverarbeitungsprogramm, die Sie aktiv öffnen und mit denen Sie interagieren, arbeiten Dienste hinter den Kulissen.

You typically don't launch a service in the same way; the operating system manages their lifecycle. Sie starten einen Dienst normalerweise nicht auf die gleiche Weise; das Betriebssystem verwaltet ihren Lebenszyklus.

Key Characteristics of Services Hauptmerkmale von Diensten

No User Interface, typically. Most services don't have a graphical user interface, or GUI. Keine Benutzeroberfläche, typischerweise. Die meisten Dienste haben keine grafische Benutzeroberfläche, oder GUI.

Their operations are logged or managed through administrative tools. Ihre Operationen werden protokolliert oder durch Verwaltungstools verwaltet.

Run in their Own Security Context. Services run under specific user accounts, which might be predefined system accounts, like Local System, Local Service, Network Service, or dedicated user accounts. Laufen in ihrem eigenen Sicherheitskontext. Dienste laufen unter bestimmten Benutzerkonten, die vordefinierte Systemkonten sein können, wie Lokales System, Lokaler Dienst, Netzwerkdienst oder dedizierte Benutzerkonten.

This determines what resources the service can access. Dies bestimmt, auf welche Ressourcen der Dienst zugreifen kann.

Automatic or Manual Startup. Services can be configured to start automatically when Windows boots, or they can be set to manual start, requiring a user or another process to initiate them. Automatischer oder manueller Start. Dienste können so konfiguriert werden, dass sie automatisch starten, wenn Windows hochfährt, oder sie können auf manuellen Start gesetzt werden, was einen Benutzer oder einen anderen Prozess erfordert, um sie zu starten.

They can also be disabled entirely. Sie können auch vollständig deaktiviert werden.

Dependencies. Some services depend on other services to function correctly. Abhängigkeiten. Einige Dienste hängen von anderen Diensten ab, um korrekt zu funktionieren.

If a required service isn't running, the dependent service might fail to start or operate properly. Wenn ein erforderlicher Dienst nicht läuft, kann der abhängige Dienst möglicherweise nicht starten oder ordnungsgemäß arbeiten.

The timing of when services start is critical, and this is managed during the overall system startup sequence. Der Zeitpunkt, wann Dienste starten, ist kritisch, und dies wird während der gesamten Systemstartsequenz verwaltet.

Think about it Denken Sie darüber nach

Why is it beneficial for essential tasks like network management or system updates to run as services rather than regular applications that a user has to start manually? Warum ist es vorteilhaft, dass wesentliche Aufgaben wie Netzwerkverwaltung oder Systemaktualisierungen als Dienste laufen, anstatt als reguläre Anwendungen, die ein Benutzer manuell starten muss?

Can you think of a scenario where a service not running could cause significant problems for a user? Können Sie sich ein Szenario vorstellen, in dem ein nicht laufender Dienst erhebliche Probleme für einen Benutzer verursachen könnte?

The Windows Startup Process: An Overview Der Windows-Startprozess: Ein Überblick

So, how and when do these vital services actually get started? Also, wie und wann werden diese wichtigen Dienste tatsächlich gestartet?

They are an integral part of the Windows startup process. Sie sind ein integraler Bestandteil des Windows-Startprozesses.

When you press the power button, a complex sequence of events unfolds to bring your system to life, including the initiation of these background tasks. Wenn Sie den Netzschalter drücken, entfaltet sich eine komplexe Abfolge von Ereignissen, um Ihr System zum Leben zu erwecken, einschließlich der Initiierung dieser Hintergrundaufgaben.

Here's a simplified look at this process. Hier ist ein vereinfachter Blick auf diesen Prozess.

Power On and Hardware Check, Firmware Stage. Einschalten und Hardware-Überprüfung, Firmware-Phase.

When you turn on your PC, the system's built-in software, called firmware, either BIOS or UEFI, wakes up. Wenn Sie Ihren PC einschalten, wacht die in das System integrierte Software, genannt Firmware, entweder BIOS oder UEFI, auf.

It quickly checks your main hardware components, like memory and hard drives, to make sure they're working. Sie überprüft schnell Ihre Haupthardwarekomponenten, wie Speicher und Festplatten, um sicherzustellen, dass sie funktionieren.

This is often called the Power-On Self Test, or POST. Dies wird oft als Einschalt-Selbsttest, oder POST, bezeichnet.

If everything is okay, the firmware looks for the operating system on your storage device, usually your main hard drive or SSD. Wenn alles in Ordnung ist, sucht die Firmware nach dem Betriebssystem auf Ihrem Speichergerät, normalerweise Ihrer Hauptfestplatte oder SSD.

Loading Windows, Bootloader Stage. Windows laden, Bootloader-Phase.

The firmware hands over control to a small program called the Windows Boot Manager. Die Firmware übergibt die Kontrolle an ein kleines Programm namens Windows Boot Manager.

The Boot Manager's job is to find and start loading the main parts of the Windows operating system. Die Aufgabe des Boot Managers ist es, die Hauptteile des Windows-Betriebssystems zu finden und zu laden.

It reads some configuration files to know where Windows is installed and if there are any special startup options, like starting in Safe Mode. Er liest einige Konfigurationsdateien, um zu wissen, wo Windows installiert ist und ob es spezielle Startoptionen gibt, wie den Start im abgesicherten Modus.

Starting the Core of Windows, Kernel Initialization. Starten des Kerns von Windows, Kernel-Initialisierung.

The Boot Manager loads the Windows kernel, which is the heart of the operating system, into the computer's memory. Der Boot Manager lädt den Windows-Kernel, der das Herz des Betriebssystems ist, in den Speicher des Computers.

The kernel then starts to initialize itself. Der Kernel beginnt dann, sich selbst zu initialisieren.

It begins by loading essential drivers, small pieces of software that let Windows talk to your hardware, like your graphics card, keyboard, and mouse. Er beginnt damit, wesentliche Treiber zu laden, kleine Softwareteile, die Windows ermöglichen, mit Ihrer Hardware zu kommunizieren, wie Ihrer Grafikkarte, Tastatur und Maus.

It also loads important system settings from the Windows Registry. Er lädt auch wichtige Systemeinstellungen aus der Windows-Registrierung.

Getting System Ready, Session Manager. System bereit machen, Sitzungsmanager.

Once the kernel is running, it starts a key process called the Session Manager. Sobald der Kernel läuft, startet er einen Schlüsselprozess namens Sitzungsmanager.

The Session Manager sets up the basic environment for Windows to run, including preparing for user logins and starting critical system processes. Der Sitzungsmanager richtet die grundlegende Umgebung für Windows ein, einschließlich der Vorbereitung für Benutzeranmeldungen und des Startens kritischer Systemprozesse.

Starting Services and Preparing for Logon, Logon Phase. Dienste starten und Vorbereitung für Anmeldung, Anmeldephase.

The Session Manager starts the Service Control Manager, or SCM. Der Sitzungsmanager startet den Dienststeuerungsmanager, oder SCM.

The SCM is in charge of all the Windows services we discussed earlier. Der SCM ist für alle Windows-Dienste verantwortlich, die wir zuvor besprochen haben.

The SCM looks at its list of services and starts all those that are set to Automatic startup. Der SCM schaut auf seine Liste von Diensten und startet alle, die auf automatischen Start eingestellt sind.

These are often crucial for things like networking, sound, and security. Diese sind oft entscheidend für Dinge wie Netzwerk, Ton und Sicherheit.

At the same time, the system prepares for you to log in by starting the logon process, which eventually shows you the login screen. Gleichzeitig bereitet das System Ihre Anmeldung vor, indem es den Anmeldeprozess startet, der Ihnen schließlich den Anmeldebildschirm zeigt.

User Login and Desktop, User Environment. Benutzeranmeldung und Desktop, Benutzerumgebung.

When you enter your username and password, Windows verifies your credentials. Wenn Sie Ihren Benutzernamen und Ihr Passwort eingeben, überprüft Windows Ihre Anmeldeinformationen.

If successful, it loads your personal settings, desktop background, and icons. Wenn erfolgreich, lädt es Ihre persönlichen Einstellungen, den Desktop-Hintergrund und Symbole.

Finally, any applications that are set to run automatically when you log in, your startup programs, will begin to launch. Schließlich werden alle Anwendungen, die so eingestellt sind, dass sie automatisch starten, wenn Sie sich anmelden, Ihre Startprogramme, beginnen zu starten.

Your Windows desktop appears, and your computer is ready to use. Ihr Windows-Desktop erscheint, und Ihr Computer ist einsatzbereit.

This entire process, from pressing the power button to seeing your desktop, involves many intricate steps, but this overview covers the main stages. Dieser gesamte Prozess, vom Drücken des Netzschalters bis zum Sehen Ihres Desktops, beinhaltet viele komplizierte Schritte, aber diese Übersicht deckt die Hauptphasen ab.

Understanding this flow helps in diagnosing startup problems and appreciating how services fit into the overall operation of your system. Das Verständnis dieses Ablaufs hilft bei der Diagnose von Startproblemen und beim Verständnis, wie Dienste in den Gesamtbetrieb Ihres Systems passen.

Try it yourself Versuchen Sie es selbst

What happens if a critical hardware component fails the POST? Was passiert, wenn eine kritische Hardwarekomponente den POST nicht besteht?

The system usually emits a series of beeps, a beep code, or displays an error message on the screen, and the boot process halts. Das System gibt normalerweise eine Reihe von Pieptönen aus, einen Piepcode, oder zeigt eine Fehlermeldung auf dem Bildschirm an, und der Bootvorgang wird angehalten.

The specific code can help diagnose which component failed. Der spezifische Code kann helfen zu diagnostizieren, welche Komponente ausgefallen ist.

How is this different from a software application failing to start after you've logged in? Wie unterscheidet sich dies von einer Softwareanwendung, die nach Ihrer Anmeldung nicht startet?

A POST failure is a hardware-level issue preventing the OS from even beginning to load. Ein POST-Fehler ist ein Problem auf Hardware-Ebene, das verhindert, dass das Betriebssystem überhaupt zu laden beginnt.

A software application failing after login is an issue within the loaded OS environment, often due to software bugs, missing dependencies, or configuration errors, but the underlying system is generally functional. Eine Softwareanwendung, die nach der Anmeldung fehlschlägt, ist ein Problem innerhalb der geladenen Betriebssystemumgebung, oft aufgrund von Softwarefehlern, fehlenden Abhängigkeiten oder Konfigurationsfehlern, aber das zugrunde liegende System ist im Allgemeinen funktionsfähig.

Managing Services and Startup Items Verwaltung von Diensten und Startelementen

Windows provides tools to view and manage services and startup applications. Windows bietet Tools zum Anzeigen und Verwalten von Diensten und Startanwendungen.

Services Management Console, services dot msc. Dienstverwaltungskonsole, services Punkt msc.

This is the primary tool for managing services. You can use it to: view a list of all services on your system. Dies ist das primäre Tool zur Verwaltung von Diensten. Sie können es verwenden, um: eine Liste aller Dienste auf Ihrem System anzuzeigen.

See the status of each service, Running, Stopped, Paused. Den Status jedes Dienstes zu sehen, Läuft, Gestoppt, Pausiert.

View the startup type, Automatic, Automatic with Delayed Start, Manual, Disabled. Den Starttyp anzuzeigen, Automatisch, Automatisch mit verzögertem Start, Manuell, Deaktiviert.

Start, stop, pause, resume, or restart services. Dienste zu starten, zu stoppen, zu pausieren, fortzusetzen oder neu zu starten.

Configure service properties, such as the logon account and recovery options. Diensteigenschaften zu konfigurieren, wie das Anmeldekonto und Wiederherstellungsoptionen.

Task Manager Task-Manager

The Task Manager, particularly its Startup tab, allows you to see and manage applications that are configured to run when you log in. Der Task-Manager, insbesondere seine Startup-Registerkarte, ermöglicht es Ihnen, Anwendungen zu sehen und zu verwalten, die so konfiguriert sind, dass sie beim Anmelden ausgeführt werden.

These are different from system services but also impact system performance and startup time. Diese unterscheiden sich von Systemdiensten, beeinflussen aber auch die Systemleistung und die Startzeit.

You can enable or disable these startup applications. Sie können diese Startanwendungen aktivieren oder deaktivieren.

System Configuration Utility, msconfig. Systemkonfigurationsprogramm, msconfig.

Historically, msconfig was a common tool for managing startup items and services. Historisch gesehen war msconfig ein gängiges Tool zur Verwaltung von Startelementen und Diensten.

While still available, for startup applications, it now often redirects you to the Task Manager. Obwohl noch verfügbar, leitet es Sie für Startanwendungen jetzt oft zum Task-Manager weiter.

It can still be used to manage some boot options and services for diagnostic purposes. Es kann immer noch verwendet werden, um einige Boot-Optionen und Dienste für Diagnosezwecke zu verwalten.

Try it yourself Versuchen Sie es selbst

Explore the properties of a few services. Notice their dependencies and the account they log on as. Erkunden Sie die Eigenschaften einiger Dienste. Beachten Sie ihre Abhängigkeiten und das Konto, unter dem sie sich anmelden.

Compare the items listed in Task Manager's Startup tab with the services listed in services dot msc. Are they the same things? Why or why not? Vergleichen Sie die in der Startup-Registerkarte des Task-Managers aufgeführten Elemente mit den in services Punkt msc aufgeführten Diensten. Sind sie die gleichen Dinge? Warum oder warum nicht?

They are not the same. Services dot msc lists system services that often run in the background regardless of who is logged in, or even if no one is logged in. Sie sind nicht die gleichen. Services Punkt msc listet Systemdienste auf, die oft im Hintergrund laufen, unabhängig davon, wer angemeldet ist, oder sogar wenn niemand angemeldet ist.

Task Manager's Startup tab lists applications and scripts that are configured to run specifically when a user logs into their session. Die Startup-Registerkarte des Task-Managers listet Anwendungen und Skripte auf, die so konfiguriert sind, dass sie speziell ausgeführt werden, wenn sich ein Benutzer in seiner Sitzung anmeldet.

While some services might be user-specific, the primary distinction is that services are background processes providing core OS or application functionalities, whereas startup items are typically user-facing applications or utilities. Während einige Dienste benutzerspezifisch sein können, besteht der primäre Unterschied darin, dass Dienste Hintergrundprozesse sind, die Kern-Betriebssystem- oder Anwendungsfunktionalitäten bereitstellen, während Startelemente typischerweise benutzerseitige Anwendungen oder Dienstprogramme sind.

Why Care About Services and Startup? Warum sich um Dienste und Start kümmern?

From a cybersecurity perspective, understanding and managing services and startup processes is vital. Aus Cybersicherheitsperspektive ist das Verständnis und die Verwaltung von Diensten und Startprozessen von entscheidender Bedeutung.

Attack Surface Reduction. Every running service or startup application potentially increases the system's attack surface. Reduzierung der Angriffsfläche. Jeder laufende Dienst oder jede Startanwendung erhöht potenziell die Angriffsfläche des Systems.

Disabling unnecessary services and startup items can reduce vulnerabilities. Das Deaktivieren unnötiger Dienste und Startelemente kann Schwachstellen reduzieren.

Malware Persistence. Malware often tries to install itself as a service or a startup application to ensure it runs automatically and remains active even after a reboot. Malware-Persistenz. Malware versucht oft, sich als Dienst oder Startanwendung zu installieren, um sicherzustellen, dass sie automatisch läuft und auch nach einem Neustart aktiv bleibt.

Monitoring and scrutinizing services and startup entries are key to detecting and removing malware. Die Überwachung und genaue Prüfung von Diensten und Starteinträgen sind entscheidend für die Erkennung und Entfernung von Malware.

Performance. Too many unnecessary services or startup applications can slow down your computer's boot time and overall performance. Leistung. Zu viele unnötige Dienste oder Startanwendungen können die Bootzeit und die Gesamtleistung Ihres Computers verlangsamen.

Resource Management. Services consume system resources, CPU and memory. Ressourcenverwaltung. Dienste verbrauchen Systemressourcen, CPU und Speicher.

Efficient management ensures resources are available for essential tasks. Effiziente Verwaltung stellt sicher, dass Ressourcen für wesentliche Aufgaben verfügbar sind.

Think about it Denken Sie darüber nach

If you discovered an unknown service running on your system, what steps would you take to investigate it? Wenn Sie einen unbekannten Dienst entdecken würden, der auf Ihrem System läuft, welche Schritte würden Sie unternehmen, um ihn zu untersuchen?

Check the service name, display name, and description for clues. Überprüfen Sie den Dienstnamen, den Anzeigenamen und die Beschreibung auf Hinweise.

Look at its properties. What is the path to the executable? What account does it run under? Does it have dependencies? Are other services dependent on it? Schauen Sie sich seine Eigenschaften an. Was ist der Pfad zur ausführbaren Datei? Unter welchem Konto läuft er? Hat er Abhängigkeiten? Sind andere Dienste von ihm abhängig?

Search online for the executable name or service name to see if it's a legitimate Windows component, part of a known application, or potentially malware. Suchen Sie online nach dem Namen der ausführbaren Datei oder dem Dienstnamen, um zu sehen, ob es eine legitime Windows-Komponente, Teil einer bekannten Anwendung oder potenziell Malware ist.

Check the digital signature of the executable file. Überprüfen Sie die digitale Signatur der ausführbaren Datei.

Use tools like Autoruns from Sysinternals to get more detailed information. Verwenden Sie Tools wie Autoruns von Sysinternals, um detailliertere Informationen zu erhalten.

If suspicious, consider stopping and disabling it, after assessing potential impact, and scanning the system with security software. Wenn verdächtig, erwägen Sie, ihn zu stoppen und zu deaktivieren, nach Bewertung der potenziellen Auswirkungen, und das System mit Sicherheitssoftware zu scannen.

Why might an attacker prefer to install malware as a service rather than just a regular startup application? Warum könnte ein Angreifer es vorziehen, Malware als Dienst zu installieren, anstatt nur als reguläre Startanwendung?

Services can run with higher privileges, for example Local System, giving malware more control over the system. Dienste können mit höheren Privilegien laufen, zum Beispiel Lokales System, was Malware mehr Kontrolle über das System gibt.

Services can start automatically at boot, even before a user logs in, allowing malware to be active earlier. Dienste können beim Booten automatisch starten, sogar bevor sich ein Benutzer anmeldet, was Malware ermöglicht, früher aktiv zu sein.

Services often run hidden in the background without a user interface, making them less noticeable to the average user compared to an application that might appear in the taskbar or system tray. Dienste laufen oft verborgen im Hintergrund ohne Benutzeroberfläche, was sie für den durchschnittlichen Benutzer weniger auffällig macht im Vergleich zu einer Anwendung, die in der Taskleiste oder im Systembereich erscheinen könnte.

Services can be configured with recovery options, automatically restarting if they are stopped, making them more resilient. Dienste können mit Wiederherstellungsoptionen konfiguriert werden, die automatisch neu starten, wenn sie gestoppt werden, was sie widerstandsfähiger macht.

Exploration: Tools for Managing Services and Startup Erkundung: Tools zur Verwaltung von Diensten und Start

Before our class, take some time to familiarize yourself with the tools Windows provides for inspecting and managing services and startup items. Vor unserem Unterricht nehmen Sie sich etwas Zeit, um sich mit den Tools vertraut zu machen, die Windows zum Inspizieren und Verwalten von Diensten und Startelementen bereitstellt.

Ensure your Windows Virtual Machine, or VM, is fully updated and operational. Stellen Sie sicher, dass Ihre virtuelle Windows-Maschine, oder VM, vollständig aktualisiert und betriebsbereit ist.

You will need administrative privileges within your VM for full access to these tools. Sie benötigen administrative Privilegien innerhalb Ihrer VM für vollen Zugriff auf diese Tools.

The goal here is to get comfortable navigating these utilities and observing the information they present. Das Ziel hier ist es, sich mit der Navigation in diesen Dienstprogrammen und der Beobachtung der von ihnen präsentierten Informationen vertraut zu machen.

Do not change any settings unless you are very sure of what you are doing. Ändern Sie keine Einstellungen, es sei denn, Sie sind sich sehr sicher, was Sie tun.

Services Management Console, services dot msc. Dienstverwaltungskonsole, services Punkt msc.

Press Windows key plus R to open the Run dialog. Drücken Sie die Windows-Taste plus R, um das Dialogfeld Ausführen zu öffnen.

Type services dot msc and press Enter. Geben Sie services Punkt msc ein und drücken Sie Enter.

Explore. Browse the list of services. Click on a few services to see their properties, right-click, then Properties. Erkunden. Durchsuchen Sie die Liste der Dienste. Klicken Sie auf einige Dienste, um ihre Eigenschaften zu sehen, Rechtsklick, dann Eigenschaften.

Note their Startup type, Automatic, Manual, Disabled, current Status, Running or Stopped, and the Log On As account. Beachten Sie ihren Starttyp, Automatisch, Manuell, Deaktiviert, aktuellen Status, Läuft oder Gestoppt, und das Anmelden als Konto.

Check the Dependencies tab for a service or two. Überprüfen Sie die Registerkarte Abhängigkeiten für einen oder zwei Dienste.

Task Manager Task-Manager

Press Control plus Shift plus Escape. Drücken Sie Steuerung plus Umschalt plus Escape.

Alternatively, right-click the Taskbar and select Task Manager. Alternativ klicken Sie mit der rechten Maustaste auf die Taskleiste und wählen Sie Task-Manager.

Explore. Go to the Services tab. You'll see a list similar to services dot msc, but with a slightly different interface. Erkunden. Gehen Sie zur Registerkarte Dienste. Sie sehen eine Liste ähnlich wie services Punkt msc, aber mit einer etwas anderen Benutzeroberfläche.

You can right-click services here to start or stop them or open the full Services console. Sie können hier mit der rechten Maustaste auf Dienste klicken, um sie zu starten oder zu stoppen oder die vollständige Dienste-Konsole zu öffnen.

Go to the Startup tab, or Startup apps in newer Windows versions. Gehen Sie zur Registerkarte Startup oder Startup-Apps in neueren Windows-Versionen.

This lists applications configured to launch when you log in. Dies listet Anwendungen auf, die so konfiguriert sind, dass sie beim Anmelden gestartet werden.

Note the Status, Enabled or Disabled, and the Startup impact if shown. Beachten Sie den Status, Aktiviert oder Deaktiviert, und die Auswirkung auf den Start, falls angezeigt.

System Configuration Utility, msconfig. Systemkonfigurationsprogramm, msconfig.

Press Windows key plus R to open the Run dialog. Drücken Sie die Windows-Taste plus R, um das Dialogfeld Ausführen zu öffnen.

Type msconfig and press Enter. Geben Sie msconfig ein und drücken Sie Enter.

Explore. Look at the Services tab. Notice the option to Hide all Microsoft services, which can be useful for identifying third-party services. Erkunden. Schauen Sie sich die Registerkarte Dienste an. Beachten Sie die Option, alle Microsoft-Dienste auszublenden, was nützlich sein kann, um Dienste von Drittanbietern zu identifizieren.

The Startup tab here usually just redirects you to Task Manager in modern Windows versions. Die Registerkarte Startup hier leitet Sie normalerweise nur zum Task-Manager in modernen Windows-Versionen weiter.

Autoruns from Sysinternals. Autoruns von Sysinternals.

Open a web browser in your VM and search for Autoruns Sysinternals or go directly to the Sysinternals page on the Microsoft website. Öffnen Sie einen Webbrowser in Ihrer VM und suchen Sie nach Autoruns Sysinternals oder gehen Sie direkt zur Sysinternals-Seite auf der Microsoft-Website.

Download Autoruns. It usually comes as a ZIP file. Laden Sie Autoruns herunter. Es kommt normalerweise als ZIP-Datei.

Extract the contents of the ZIP file to a folder, for example on your Desktop or in Documents. Extrahieren Sie den Inhalt der ZIP-Datei in einen Ordner, zum Beispiel auf Ihrem Desktop oder in Dokumenten.

Run Autoruns dot exe, or Autoruns64 dot exe if you have a 64-bit system. Führen Sie Autoruns Punkt exe oder Autoruns64 Punkt exe aus, wenn Sie ein 64-Bit-System haben.

You may need to agree to a license term on the first run. Sie müssen möglicherweise beim ersten Ausführen einer Lizenzbedingung zustimmen.

Explore. This tool is very powerful and shows many more auto-starting locations than Task Manager. Erkunden. Dieses Tool ist sehr leistungsfähig und zeigt viel mehr automatisch startende Orte als der Task-Manager.

Click through the different tabs like Logon, shows startup programs, Run keys, etc., Services, shows services including third-party ones, Scheduled Tasks, Drivers, and KnownDLLs. Klicken Sie durch die verschiedenen Registerkarten wie Anmeldung, zeigt Startprogramme, Run-Schlüssel usw., Dienste, zeigt Dienste einschließlich Drittanbieter-Dienste, Geplante Aufgaben, Treiber und KnownDLLs.

Notice the wealth of information: the entry, description, publisher, image path, the location of the file, and timestamp. Beachten Sie die Fülle an Informationen: den Eintrag, die Beschreibung, den Herausgeber, den Bildpfad, den Speicherort der Datei und den Zeitstempel.

Again, do not uncheck or delete anything in Autoruns during this pre-class exploration. Auch hier, deaktivieren oder löschen Sie nichts in Autoruns während dieser Erkundung vor dem Unterricht.

The goal is to see the breadth of items that can automatically start on a Windows system. Das Ziel ist es, die Breite der Elemente zu sehen, die auf einem Windows-System automatisch starten können.

Spending some time with these tools will give you a much better understanding of what's running on your system and how applications achieve persistence. Zeit mit diesen Tools zu verbringen wird Ihnen ein viel besseres Verständnis davon geben, was auf Ihrem System läuft und wie Anwendungen Persistenz erreichen.

The slides for the live session can be viewed here at this link. Try not to peek before class, spoilers inside! Die Folien für die Live-Sitzung können hier unter diesem Link angesehen werden. Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!