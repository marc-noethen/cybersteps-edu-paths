Welcome to the pre-class preparation for our session on OS Hardening and Security! Willkommen zur Vorbereitung vor dem Unterricht für unsere Sitzung über Betriebssystemhärtung und Sicherheit!

The goal of this preparation is to introduce you to the fundamental concepts of securing an operating system. Das Ziel dieser Vorbereitung ist es, Sie in die grundlegenden Konzepte der Sicherung eines Betriebssystems einzuführen.

By understanding these principles, you'll be better equipped for our live session, where we'll dive deeper into practical applications and demonstrations. Durch das Verständnis dieser Prinzipien werden Sie besser für unsere Live-Sitzung vorbereitet sein, in der wir tiefer in praktische Anwendungen und Demonstrationen eintauchen werden.

What is OS Hardening? Was ist Betriebssystemhärtung?

Operating System, or OS, hardening is the process of configuring an OS securely to reduce its vulnerability to cyberattacks. Betriebssystemhärtung, oder OS-Härtung, ist der Prozess der sicheren Konfiguration eines Betriebssystems, um seine Verwundbarkeit gegenüber Cyberangriffen zu reduzieren.

Think of it like fortifying a castle. You want to minimize the number of entry points for attackers, strengthen the existing defenses, and ensure you can detect any attempts to breach them. Denken Sie daran wie das Befestigen einer Burg. Sie möchten die Anzahl der Eingangspunkte für Angreifer minimieren, die bestehenden Verteidigungen stärken und sicherstellen, dass Sie jeden Versuch, sie zu durchbrechen, erkennen können.

By systematically reducing the attack surface, the sum of all potential vulnerabilities an attacker could exploit, we make the system more resilient. Indem wir systematisch die Angriffsfläche reduzieren, die Summe aller potenziellen Schwachstellen, die ein Angreifer ausnutzen könnte, machen wir das System widerstandsfähiger.

Hardening an OS is a crucial proactive security measure. Die Härtung eines Betriebssystems ist eine entscheidende proaktive Sicherheitsmaßnahme.

It's not about waiting for an attack to happen and then reacting; it's about making the system as difficult as possible to compromise in the first place. Es geht nicht darum, auf einen Angriff zu warten und dann zu reagieren; es geht darum, das System von vornherein so schwer wie möglich kompromittierbar zu machen.

This aligns with the cybersecurity principle of defense in depth, where multiple layers of security controls are implemented. Dies steht im Einklang mit dem Cybersicherheitsprinzip der Verteidigung in der Tiefe, bei dem mehrere Ebenen von Sicherheitskontrollen implementiert werden.

Key Principles of OS Hardening Schlüsselprinzipien der Betriebssystemhärtung

Several core principles guide the process of OS hardening. Mehrere Kernprinzipien leiten den Prozess der Betriebssystemhärtung.

Principle of Least Privilege. This is one of the most fundamental concepts in security. Prinzip der geringsten Privilegien. Dies ist eines der grundlegendsten Konzepte in der Sicherheit.

It dictates that users, applications, and system processes should only be granted the minimum levels of access, or privileges, necessary to perform their intended functions. Es schreibt vor, dass Benutzern, Anwendungen und Systemprozessen nur das Mindestmaß an Zugriff oder Privilegien gewährt werden sollte, das zur Ausführung ihrer beabsichtigten Funktionen erforderlich ist.

If an account or process with excessive privileges is compromised, the attacker gains those same excessive privileges. Wenn ein Konto oder Prozess mit übermäßigen Privilegien kompromittiert wird, erlangt der Angreifer dieselben übermäßigen Privilegien.

Attack Surface Reduction. This involves identifying and eliminating or disabling unnecessary software, services, user accounts, and network ports. Reduzierung der Angriffsfläche. Dies beinhaltet das Identifizieren und Eliminieren oder Deaktivieren unnötiger Software, Dienste, Benutzerkonten und Netzwerkports.

Every active component is a potential entry point for an attacker; if it's not needed, it should be removed or turned off. Jede aktive Komponente ist ein potenzieller Eingangspunkt für einen Angreifer; wenn sie nicht benötigt wird, sollte sie entfernt oder ausgeschaltet werden.

Secure Configuration. Operating systems and applications often come with default configurations that are not optimized for security. Sichere Konfiguration. Betriebssysteme und Anwendungen kommen oft mit Standardkonfigurationen, die nicht für Sicherheit optimiert sind.

Secure configuration involves reviewing and adjusting settings to their most secure state, following best practices and established security guidelines, like CIS Benchmarks or Microsoft Security Baselines. Sichere Konfiguration beinhaltet das Überprüfen und Anpassen von Einstellungen auf ihren sichersten Zustand, unter Befolgung von Best Practices und etablierten Sicherheitsrichtlinien, wie CIS Benchmarks oder Microsoft Security Baselines.

Patch Management. Software is rarely perfect and vulnerabilities are discovered over time. Patch-Management. Software ist selten perfekt und Schwachstellen werden im Laufe der Zeit entdeckt.

Patch management is the process of identifying, acquiring, testing, and installing software updates, or patches, to fix these security flaws and other bugs. Patch-Management ist der Prozess des Identifizierens, Erwerbens, Testens und Installierens von Software-Updates oder Patches, um diese Sicherheitslücken und andere Fehler zu beheben.

A robust patch management process is essential for closing known security holes before attackers can exploit them. Ein robuster Patch-Management-Prozess ist unerlässlich, um bekannte Sicherheitslücken zu schließen, bevor Angreifer sie ausnutzen können.

Logging and Monitoring. Comprehensive logging of system events, like user logons, administrative actions, errors, and security events, is vital. Protokollierung und Überwachung. Eine umfassende Protokollierung von Systemereignissen, wie Benutzeranmeldungen, administrativen Aktionen, Fehlern und Sicherheitsereignissen, ist von entscheidender Bedeutung.

Regularly monitoring these logs helps in detecting suspicious activities, investigating security incidents, and ensuring compliance with security policies. Die regelmäßige Überwachung dieser Protokolle hilft bei der Erkennung verdächtiger Aktivitäten, der Untersuchung von Sicherheitsvorfällen und der Sicherstellung der Einhaltung von Sicherheitsrichtlinien.

Think about it Denken Sie darüber nach

If a user needs to run a specific application that requires administrator rights, but their daily tasks, like email and web browsing, do not, what would be a more secure approach than giving their main user account permanent administrator rights? Wenn ein Benutzer eine bestimmte Anwendung ausführen muss, die Administratorrechte erfordert, seine täglichen Aufgaben, wie E-Mail und Webbrowsing, dies jedoch nicht tun, was wäre ein sichererer Ansatz, als seinem Hauptbenutzerkonto permanente Administratorrechte zu geben?

Common Areas of OS Hardening, Windows Focus Häufige Bereiche der Betriebssystemhärtung, Windows-Fokus

While the principles are universal, their implementation can vary between operating systems. Während die Prinzipien universell sind, kann ihre Implementierung zwischen Betriebssystemen variieren.

Since this module focuses on Windows, we'll primarily discuss Windows-specific examples. Da sich dieses Modul auf Windows konzentriert, werden wir hauptsächlich Windows-spezifische Beispiele besprechen.

User Account Management Benutzerkontenverwaltung

Properly managing user accounts is critical. Die ordnungsgemäße Verwaltung von Benutzerkonten ist entscheidend.

Strong Password Policies. Enforce rules for password complexity, for example length, use of uppercase, lowercase, numbers, symbols, how often passwords must be changed, and preventing the reuse of old passwords. Starke Passwortrichtlinien. Durchsetzen von Regeln für Passwortkomplexität, zum Beispiel Länge, Verwendung von Groß- und Kleinbuchstaben, Zahlen, Symbolen, wie oft Passwörter geändert werden müssen und Verhinderung der Wiederverwendung alter Passwörter.

Default Accounts. Be cautious with default accounts like Administrator or Guest. Standardkonten. Seien Sie vorsichtig mit Standardkonten wie Administrator oder Gast.

It's good practice to rename the built-in administrator account, making it harder for attackers to guess, and ensure the guest account is disabled if not explicitly needed. Es ist gute Praxis, das integrierte Administrator-Konto umzubenennen, was es Angreifern schwerer macht zu erraten, und sicherzustellen, dass das Gastkonto deaktiviert ist, wenn es nicht ausdrücklich benötigt wird.

User Account Control, or UAC. UAC in Windows helps prevent unauthorized changes by prompting for confirmation or administrator credentials when an action requires elevated privileges. Benutzerkontensteuerung, oder UAC. UAC in Windows hilft, unbefugte Änderungen zu verhindern, indem es um Bestätigung oder Administrator-Anmeldeinformationen bittet, wenn eine Aktion erhöhte Privilegien erfordert.

This acts as a safety check, limiting what malware can do silently. Dies fungiert als Sicherheitsprüfung und begrenzt, was Malware stillschweigend tun kann.

Account Review. Regularly review all user accounts. Kontoüberprüfung. Überprüfen Sie regelmäßig alle Benutzerkonten.

Ensure that only necessary accounts exist and that they have the minimum permissions required for their roles. Stellen Sie sicher, dass nur notwendige Konten existieren und dass sie die für ihre Rollen erforderlichen Mindestberechtigungen haben.

Disable or remove accounts for users who no longer need access. Deaktivieren oder entfernen Sie Konten für Benutzer, die keinen Zugriff mehr benötigen.

Software Management Softwareverwaltung

Unnecessary or outdated software can introduce vulnerabilities. Unnötige oder veraltete Software kann Schwachstellen einführen.

Uninstall Unnecessary Applications. If software isn't needed for work or system operations, it shouldn't be on the system. Deinstallieren Sie unnötige Anwendungen. Wenn Software nicht für Arbeit oder Systembetrieb benötigt wird, sollte sie nicht auf dem System sein.

Each program is a potential source of vulnerabilities. Jedes Programm ist eine potenzielle Quelle von Schwachstellen.

Keep Software Updated. This is a key part of patch management, applying not just to the OS, but to all installed applications, web browsers, office suites, PDF readers, etc. Halten Sie Software auf dem neuesten Stand. Dies ist ein wichtiger Teil des Patch-Managements und gilt nicht nur für das Betriebssystem, sondern für alle installierten Anwendungen, Webbrowser, Office-Pakete, PDF-Reader usw.

Application Control. In some environments, organizations might implement policies to control which applications are allowed to run, whitelisting, or which are explicitly forbidden, blacklisting. Anwendungssteuerung. In einigen Umgebungen könnten Organisationen Richtlinien implementieren, um zu kontrollieren, welche Anwendungen ausgeführt werden dürfen, Whitelisting, oder welche ausdrücklich verboten sind, Blacklisting.

Service Management Dienstverwaltung

Operating systems run many background processes called services. Not all of them are required for every system's specific role. Betriebssysteme führen viele Hintergrundprozesse aus, die Dienste genannt werden. Nicht alle von ihnen sind für die spezifische Rolle jedes Systems erforderlich.

Disable Unnecessary Services. Identify services that are not essential for the system's function and disable them. Deaktivieren Sie unnötige Dienste. Identifizieren Sie Dienste, die für die Funktion des Systems nicht wesentlich sind, und deaktivieren Sie sie.

For example, if a computer isn't sharing printers, the Print Spooler service might be a candidate for disabling. Wenn ein Computer beispielsweise keine Drucker freigibt, könnte der Druckerwarteschlangen-Dienst ein Kandidat für die Deaktivierung sein.

Understand Dependencies. Be careful, as some services rely on others to work correctly. Verstehen Sie Abhängigkeiten. Seien Sie vorsichtig, da einige Dienste auf andere angewiesen sind, um korrekt zu funktionieren.

Disabling a service might unintentionally affect another needed function. Das Deaktivieren eines Dienstes könnte unbeabsichtigt eine andere benötigte Funktion beeinträchtigen.

Patch Management in Detail Patch-Management im Detail

As mentioned, patch management is critical. Software vendors like Microsoft regularly release patches to address security vulnerabilities, bugs, and sometimes to provide new features. Wie erwähnt, ist Patch-Management kritisch. Software-Anbieter wie Microsoft veröffentlichen regelmäßig Patches, um Sicherheitsschwachstellen, Fehler zu beheben und manchmal neue Funktionen bereitzustellen.

Vulnerability Discovery. Security researchers, software vendors, and even malicious actors continuously find new flaws in software. Entdeckung von Schwachstellen. Sicherheitsforscher, Software-Anbieter und sogar böswillige Akteure finden kontinuierlich neue Fehler in Software.

Patch Release. Once a vendor develops a fix, they release it as a patch or update. Patch-Veröffentlichung. Sobald ein Anbieter eine Lösung entwickelt hat, veröffentlicht er sie als Patch oder Update.

For Microsoft Windows and other Microsoft products, these are often released on a well-known schedule. Für Microsoft Windows und andere Microsoft-Produkte werden diese oft nach einem bekannten Zeitplan veröffentlicht.

Patch Tuesday. This is an unofficial term for the second Tuesday of each month, when Microsoft typically releases its security updates. Patch Tuesday. Dies ist ein inoffizieller Begriff für den zweiten Dienstag jedes Monats, wenn Microsoft normalerweise seine Sicherheitsupdates veröffentlicht.

System administrators worldwide anticipate this day to begin their patching cycles. Systemadministratoren weltweit erwarten diesen Tag, um ihre Patch-Zyklen zu beginnen.

While Microsoft can release out-of-band patches for critical vulnerabilities at any time, Patch Tuesday is the most consistent update release day. Während Microsoft außerplanmäßige Patches für kritische Schwachstellen jederzeit veröffentlichen kann, ist Patch Tuesday der beständigste Update-Veröffentlichungstag.

Patching Process. A good patching process involves: Identification. Knowing what systems and software you have and what patches are available. Patch-Prozess. Ein guter Patch-Prozess umfasst: Identifizierung. Wissen, welche Systeme und Software Sie haben und welche Patches verfügbar sind.

Acquisition. Downloading the correct patches from the vendor. Erwerb. Herunterladen der richtigen Patches vom Anbieter.

Testing. Before deploying patches widely, especially in critical environments, they should be tested on a small group of non-critical systems. Testen. Bevor Patches weitreichend eingesetzt werden, besonders in kritischen Umgebungen, sollten sie an einer kleinen Gruppe nicht-kritischer Systeme getestet werden.

This is to ensure the patch doesn't cause unexpected problems with other software or system functions. Dies soll sicherstellen, dass der Patch keine unerwarteten Probleme mit anderer Software oder Systemfunktionen verursacht.

Deployment. Rolling out the patches to all relevant systems. Bereitstellung. Ausrollen der Patches auf alle relevanten Systeme.

This can be done manually on individual machines or, more commonly in organizations, using automated tools like Windows Server Update Services, or WSUS, or Microsoft Endpoint Configuration Manager. Dies kann manuell auf einzelnen Maschinen erfolgen oder, häufiger in Organisationen, unter Verwendung automatisierter Tools wie Windows Server Update Services, oder WSUS, oder Microsoft Endpoint Configuration Manager.

Verification. Confirming that patches have been successfully installed and systems are protected. Überprüfung. Bestätigung, dass Patches erfolgreich installiert wurden und Systeme geschützt sind.

Importance of Timeliness. Attackers often reverse engineer patches to understand the vulnerability they fix. Bedeutung der Rechtzeitigkeit. Angreifer führen oft Reverse Engineering von Patches durch, um die Schwachstelle zu verstehen, die sie beheben.

They then try to exploit that vulnerability on systems that haven't been patched yet. Sie versuchen dann, diese Schwachstelle auf Systemen auszunutzen, die noch nicht gepatcht wurden.

This makes timely patching extremely important. Dies macht zeitnahes Patchen extrem wichtig.

Think about it Denken Sie darüber nach

Why is testing patches before widespread deployment a crucial step, even if the patch is from a trusted vendor like Microsoft? Warum ist das Testen von Patches vor der weitreichenden Bereitstellung ein entscheidender Schritt, selbst wenn der Patch von einem vertrauenswürdigen Anbieter wie Microsoft stammt?

What could be the consequences of not having a regular patch management process? Was könnten die Konsequenzen sein, wenn man keinen regelmäßigen Patch-Management-Prozess hat?

Network Security Netzwerksicherheit

Protecting the system from network-based attacks is essential. Der Schutz des Systems vor netzwerkbasierten Angriffen ist unerlässlich.

Host-Based Firewalls. Windows includes Windows Defender Firewall, which acts like a guard, controlling network traffic entering and leaving the computer. Host-basierte Firewalls. Windows enthält die Windows Defender Firewall, die wie ein Wächter fungiert und den Netzwerkverkehr steuert, der in den Computer eintritt und ihn verlässt.

Firewall Rules. Configure the firewall to allow only necessary network connections. Firewall-Regeln. Konfigurieren Sie die Firewall so, dass nur notwendige Netzwerkverbindungen zugelassen werden.

For example, a web server needs to allow incoming web traffic, typically on ports 80 and 443, but might block other types of connections. Zum Beispiel muss ein Webserver eingehenden Webverkehr zulassen, typischerweise auf den Ports 80 und 443, könnte aber andere Arten von Verbindungen blockieren.

Disable Unused Network Protocols. If older or less secure network communication methods, or protocols, aren't needed, they should be disabled. Deaktivieren Sie ungenutzte Netzwerkprotokolle. Wenn ältere oder weniger sichere Netzwerkkommunikationsmethoden oder Protokolle nicht benötigt werden, sollten sie deaktiviert werden.

File System Security Dateisystemsicherheit

Controlling who can access files and folders is crucial. Die Kontrolle darüber, wer auf Dateien und Ordner zugreifen kann, ist entscheidend.

NTFS Permissions for Windows. Use file system permissions to control what users and groups can do with files and folders, for example read, write, delete, modify. NTFS-Berechtigungen für Windows. Verwenden Sie Dateisystemberechtigungen, um zu kontrollieren, was Benutzer und Gruppen mit Dateien und Ordnern tun können, zum Beispiel lesen, schreiben, löschen, ändern.

Always apply the principle of least privilege. Wenden Sie immer das Prinzip der geringsten Privilegien an.

Encryption. BitLocker Drive Encryption. This can encrypt the entire hard drive. Verschlüsselung. BitLocker-Laufwerkverschlüsselung. Dies kann die gesamte Festplatte verschlüsseln.

If the computer or drive is lost or stolen, the data remains unreadable without the decryption key or password. Wenn der Computer oder das Laufwerk verloren geht oder gestohlen wird, bleiben die Daten ohne den Entschlüsselungsschlüssel oder das Passwort unlesbar.

Encrypting File System, or EFS. Allows individual files and folders to be encrypted, typically tied to a specific user's account. Verschlüsselndes Dateisystem, oder EFS. Ermöglicht die Verschlüsselung einzelner Dateien und Ordner, typischerweise an ein bestimmtes Benutzerkonto gebunden.

Security Policies Sicherheitsrichtlinien

Windows uses security policies to define and enforce specific security settings. Windows verwendet Sicherheitsrichtlinien, um spezifische Sicherheitseinstellungen zu definieren und durchzusetzen.

Local Security Policy. This tool, secpol dot msc, allows administrators to configure many security settings on a single computer, such as password requirements, account lockout rules, for example locking an account after too many failed login attempts, and what actions are audited. Lokale Sicherheitsrichtlinie. Dieses Tool, secpol Punkt msc, ermöglicht Administratoren, viele Sicherheitseinstellungen auf einem einzelnen Computer zu konfigurieren, wie Passwortanforderungen, Kontosperrregeln, zum Beispiel das Sperren eines Kontos nach zu vielen fehlgeschlagenen Anmeldeversuchen, und welche Aktionen überwacht werden.

Group Policy. In larger networks with a Windows domain, Group Policy is a powerful tool for centrally managing and enforcing security configurations across many computers. Gruppenrichtlinie. In größeren Netzwerken mit einer Windows-Domäne ist die Gruppenrichtlinie ein leistungsstarkes Tool zur zentralen Verwaltung und Durchsetzung von Sicherheitskonfigurationen über viele Computer hinweg.

Examples of Policies. Audit Policy. Determines which events are recorded in the security logs, for example successful and failed logon attempts. Beispiele für Richtlinien. Überwachungsrichtlinie. Bestimmt, welche Ereignisse in den Sicherheitsprotokollen aufgezeichnet werden, zum Beispiel erfolgreiche und fehlgeschlagene Anmeldeversuche.

Password Policy. Enforces rules for creating strong passwords. Passwortrichtlinie. Erzwingt Regeln für die Erstellung starker Passwörter.

Account Lockout Policy. Helps prevent brute-force password attacks by temporarily locking an account after a set number of incorrect password attempts. Kontosperrrichtlinie. Hilft, Brute-Force-Passwortangriffe zu verhindern, indem ein Konto nach einer festgelegten Anzahl falscher Passwortversuche vorübergehend gesperrt wird.

Logging and Auditing Protokollierung und Überwachung

Without a record of what's happening on a system, it's very difficult to detect or investigate security incidents. Ohne eine Aufzeichnung dessen, was auf einem System passiert, ist es sehr schwierig, Sicherheitsvorfälle zu erkennen oder zu untersuchen.

Event Viewer, eventvwr dot msc. This Windows tool is used to view event logs. Ereignisanzeige, eventvwr Punkt msc. Dieses Windows-Tool wird verwendet, um Ereignisprotokolle anzuzeigen.

Key logs include: Security Log. Records security-related events, such as logon attempts, successful and failed, and access to files or other resources, based on the audit policies configured. Wichtige Protokolle umfassen: Sicherheitsprotokoll. Zeichnet sicherheitsrelevante Ereignisse auf, wie Anmeldeversuche, erfolgreich und fehlgeschlagen, und Zugriff auf Dateien oder andere Ressourcen, basierend auf den konfigurierten Überwachungsrichtlinien.

This log is critical for security monitoring. Dieses Protokoll ist kritisch für die Sicherheitsüberwachung.

System Log. Records events related to the Windows operating system itself, like services starting or stopping, or driver issues. Systemprotokoll. Zeichnet Ereignisse auf, die mit dem Windows-Betriebssystem selbst zusammenhängen, wie das Starten oder Stoppen von Diensten oder Treiberprobleme.

Application Log. Records events from installed applications. Anwendungsprotokoll. Zeichnet Ereignisse von installierten Anwendungen auf.

What to Log. Audit policies determine what gets recorded. Was protokolliert werden soll. Überwachungsrichtlinien bestimmen, was aufgezeichnet wird.

It's a balance. Logging too little means missing important events, but logging too much can create excessive noise and consume storage. Es ist eine Balance. Zu wenig zu protokollieren bedeutet, wichtige Ereignisse zu verpassen, aber zu viel zu protokollieren kann übermäßiges Rauschen erzeugen und Speicher verbrauchen.

Focus on logging events that are meaningful for security. Konzentrieren Sie sich auf die Protokollierung von Ereignissen, die für die Sicherheit bedeutsam sind.

Key Event IDs. Certain Event IDs in the Security log are particularly important. Wichtige Ereignis-IDs. Bestimmte Ereignis-IDs im Sicherheitsprotokoll sind besonders wichtig.

For example, Event ID 4624 indicates a successful logon, while Event ID 4625 indicates a failed logon. Zum Beispiel zeigt Ereignis-ID 4624 eine erfolgreiche Anmeldung an, während Ereignis-ID 4625 eine fehlgeschlagene Anmeldung anzeigt.

Knowing common, critical Event IDs helps in quickly identifying important security events. Das Kennen häufiger, kritischer Ereignis-IDs hilft bei der schnellen Identifizierung wichtiger Sicherheitsereignisse.

Try it yourself Versuchen Sie es selbst

On your Windows VM, open the Local Security Policy editor. Type secpol dot msc in the Start Menu search. Öffnen Sie auf Ihrer Windows-VM den Editor für lokale Sicherheitsrichtlinien. Geben Sie secpol Punkt msc in die Startmenü-Suche ein.

Look at Account Policies, then Password Policy. What are the current settings? Don't change anything yet! Schauen Sie sich Kontorichtlinien an, dann Passwortrichtlinie. Was sind die aktuellen Einstellungen? Ändern Sie noch nichts!

Open Event Viewer, eventvwr dot msc. Expand Windows Logs and click on the Security log. Öffnen Sie die Ereignisanzeige, eventvwr Punkt msc. Erweitern Sie Windows-Protokolle und klicken Sie auf das Sicherheitsprotokoll.

Can you find any recent logon events? Look for Event ID 4624, successful logon, or 4625, failed logon. Können Sie kürzlich erfolgte Anmeldeereignisse finden? Suchen Sie nach Ereignis-ID 4624, erfolgreiche Anmeldung, oder 4625, fehlgeschlagene Anmeldung.

Tools for OS Hardening Werkzeuge für Betriebssystemhärtung

Many tools for OS hardening are built into Windows. Viele Werkzeuge für die Betriebssystemhärtung sind in Windows integriert.

Windows Defender Firewall with Advanced Security. Windows Defender Firewall mit erweiterter Sicherheit.

Local Security Policy, secpol dot msc. Lokale Sicherheitsrichtlinie, secpol Punkt msc.

Services, services dot msc. Dienste, services Punkt msc.

Event Viewer, eventvwr dot msc. Ereignisanzeige, eventvwr Punkt msc.

Programs and Features, for uninstalling software. Programme und Features, zum Deinstallieren von Software.

BitLocker Drive Encryption. BitLocker-Laufwerkverschlüsselung.

Beyond built-in tools, organizations often use security baselines as guides. Über integrierte Tools hinaus verwenden Organisationen oft Sicherheitsbaselines als Leitfäden.

These are documented sets of recommended configuration settings. Dies sind dokumentierte Sätze empfohlener Konfigurationseinstellungen.

Examples include: Microsoft Security Baselines. Microsoft provides its own recommended security configurations. Beispiele umfassen: Microsoft Security Baselines. Microsoft bietet seine eigenen empfohlenen Sicherheitskonfigurationen.

CIS Benchmarks. The Center for Internet Security, or CIS, publishes detailed, consensus-based hardening guides that are highly respected in the industry. CIS Benchmarks. Das Center for Internet Security, oder CIS, veröffentlicht detaillierte, konsensbasierte Härtungsleitfäden, die in der Branche hoch angesehen sind.

Think about it Denken Sie darüber nach

Why is it generally more secure to follow a well-known security baseline, like CIS Benchmarks, rather than just trying to figure out all the settings on your own? Warum ist es im Allgemeinen sicherer, einer bekannten Sicherheitsbaseline zu folgen, wie CIS Benchmarks, anstatt nur zu versuchen, alle Einstellungen selbst herauszufinden?

What are the potential downsides of making an OS too hardened, to the point where it impacts usability for legitimate users? Was sind die potenziellen Nachteile, ein Betriebssystem zu sehr zu härten, bis zu dem Punkt, an dem es die Benutzerfreundlichkeit für legitime Benutzer beeinträchtigt?

This preparation will give you a solid foundation for our upcoming lesson. We'll be building on these concepts with practical demonstrations and discussions. Diese Vorbereitung wird Ihnen eine solide Grundlage für unsere kommende Lektion geben. Wir werden auf diesen Konzepten mit praktischen Demonstrationen und Diskussionen aufbauen.

The slides for the live session can be viewed here at this link. Try not to peek before class, spoilers inside! Die Folien für die Live-Sitzung können hier unter diesem Link angesehen werden. Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!