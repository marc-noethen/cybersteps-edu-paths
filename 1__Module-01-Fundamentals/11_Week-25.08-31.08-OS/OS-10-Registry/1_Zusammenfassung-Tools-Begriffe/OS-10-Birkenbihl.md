Welcome to your introduction to the Windows Registry! It is an important component of the Windows operating system, and understanding its structure and purpose is crucial for many tasks in the field of cybersecurity, from digital forensics to system hardening. Willkommen zu Ihrer Einführung in die Windows-Registrierung! Sie ist eine wichtige Komponente des Windows-Betriebssystems, und das Verständnis ihrer Struktur und ihres Zwecks ist für viele Aufgaben im Bereich der Cybersicherheit von entscheidender Bedeutung, von der digitalen Forensik bis zur Systemhärtung.

What is the Windows Registry? Was ist die Windows-Registrierung?

Imagine the Windows Registry as the central nervous system or as a vast, hierarchical database for your Windows operating system. Stellen Sie sich die Windows-Registrierung als das zentrale Nervensystem oder als eine riesige, hierarchische Datenbank für Ihr Windows-Betriebssystem vor.

It stores a large amount of configuration settings and options for the operating system itself, for hardware devices, software applications, user settings and system policies. Sie speichert eine große Menge an Konfigurationseinstellungen und Optionen für das Betriebssystem selbst, für Hardwaregeräte, Softwareanwendungen, Benutzereinstellungen und Systemrichtlinien.

Every time you install a new program, change the desktop background or connect a new USB drive, the registry is likely updated with new information. Jedes Mal, wenn Sie ein neues Programm installieren, den Desktophintergrund ändern oder ein neues USB-Laufwerk anschließen, wird die Registrierung wahrscheinlich mit neuen Informationen aktualisiert.

The registry was first introduced with Windows 3.1 and has been a central component of every Windows version since then. Die Registrierung wurde erstmals mit Windows 3.1 eingeführt und ist seither ein zentraler Bestandteil jeder Windows-Version.

It replaced the older, less centralized system that used numerous INI files, or initialization files, to store settings. Sie ersetzte das ältere, weniger zentralisierte System, bei dem zahlreiche INI-Dateien, also Initialisierungsdateien, zum Speichern von Einstellungen verwendet wurden.

The main functions of the registry include: storing hardware configuration, such as which drivers should be loaded for which devices. Zu den wichtigsten Funktionen der Registrierung gehören: Speichern der Hardwarekonfiguration, zum Beispiel welche Treiber für welche Geräte geladen werden sollen.

Managing software settings, such as installation paths and user settings for applications. Verwaltung von Softwareeinstellungen, wie Installationspfade und Benutzereinstellungen für Anwendungen.

Controlling user profiles and settings, such as desktop appearance and language settings. Steuerung von Benutzerprofilen und Einstellungen, wie Aussehen des Desktops und Spracheinstellungen.

Maintaining system-level settings, such as boot parameters and security policies. Pflege von Einstellungen auf Systemebene, wie Boot-Parameter und Sicherheitsrichtlinien.

Because it contains such important information, the registry is a common target for malware and a treasure trove for forensic investigators. Da sie so wichtige Informationen enthält, ist die Registrierung ein häufiges Ziel für Malware und eine Fundgrube für forensische Ermittler.

Structure of the Registry Struktur der Registrierung

The registry is not just one huge file, but a complex structure of multiple files called hives that are loaded into memory when the system starts up or a user logs in. Die Registrierung ist nicht nur eine riesige Datei, sondern eine komplexe Struktur aus mehreren Dateien, die Hives genannt werden und in den Speicher geladen werden, wenn das System hochfährt oder sich ein Benutzer anmeldet.

The structure you interact with, for example via the registry editor, is a logical, hierarchical view of these hives. Die Struktur, mit der Sie interagieren, zum Beispiel über den Registrierungseditor, ist eine logische, hierarchische Ansicht dieser Hives.

This hierarchy consists of: Root Keys, or predefined keys or handles. These are the top-level containers in the registry. Diese Hierarchie besteht aus: Root Keys, oder vordefinierte Schlüssel oder Handles. Dies sind die obersten Container in der Registrierung.

There are five main root keys, often abbreviated with HK. Es gibt fünf Haupt-Root-Keys, die oft mit HK abgekürzt werden.

HKEY_CLASSES_ROOT, or HKCR, contains information about file associations, such as which program opens a text file, OLE data, or Object Linking and Embedding, and COM object registrations. HKEY_CLASSES_ROOT, oder HKCR, enthält Informationen über Dateiverknüpfungen, zum Beispiel welches Programm eine Textdatei öffnet, OLE-Daten, also Object Linking and Embedding, und COM-Objektregistrierungen.

This key is actually a combined view of HKEY_LOCAL_MACHINE backslash Software backslash Classes and HKEY_CURRENT_USER backslash Software backslash Classes. Dieser Schlüssel ist eigentlich eine kombinierte Ansicht von HKEY_LOCAL_MACHINE Backslash Software Backslash Classes und HKEY_CURRENT_USER Backslash Software Backslash Classes.

HKEY_CURRENT_USER, or HKCU, stores settings that are specific to the currently logged-in user. HKEY_CURRENT_USER, oder HKCU, speichert Einstellungen, die für den aktuell angemeldeten Benutzer spezifisch sind.

This includes things like the desktop background, screensaver, application settings and folder view settings. Dazu gehören Dinge wie der Desktophintergrund, der Bildschirmschoner, die Anwendungseinstellungen und die Einstellungen für die Ordneransicht.

This is a pointer to a subkey within HKEY_USERS that corresponds to the security identifier, or SID, of the current user. Dies ist ein Zeiger auf einen Unterschlüssel innerhalb von HKEY_USERS, der der Sicherheitskennung, oder SID, des aktuellen Benutzers entspricht.

HKEY_LOCAL_MACHINE, or HKLM, contains configuration information for the local computer, regardless of who is logged in. HKEY_LOCAL_MACHINE, oder HKLM, enthält Konfigurationsinformationen für den lokalen Computer, unabhängig davon, wer angemeldet ist.

This includes hardware settings, such as drivers and devices, system-wide software settings and operating system configurations. This is one of the most critical hives. Dazu gehören Hardwareeinstellungen, wie Treiber und Geräte, systemweite Softwareeinstellungen und Betriebssystemkonfigurationen. Dies ist eine der kritischsten Hives.

HKEY_USERS, or HKU, contains user profiles for all users who have logged on to the computer, as well as a default profile. HKEY_USERS, oder HKU, enthält Benutzerprofile für alle Benutzer, die sich auf dem Computer angemeldet haben, sowie ein Standardprofil.

Each user's profile is stored under their SID. HKEY_CURRENT_USER is a link here to the current user's specific SID subkey. Das Profil eines jeden Benutzers wird unter seiner SID gespeichert. HKEY_CURRENT_USER ist hier ein Link zum spezifischen SID-Unterschlüssel des aktuellen Benutzers.

HKEY_CURRENT_CONFIG, or HKCC, stores information about the hardware profile that the local computer uses at startup. HKEY_CURRENT_CONFIG, oder HKCC, speichert Informationen über das Hardwareprofil, das der lokale Computer beim Start verwendet.

This is generally a pointer to a subkey within HKEY_LOCAL_MACHINE backslash System backslash CurrentControlSet backslash Hardware Profiles backslash Current. Dies ist im Allgemeinen ein Zeiger auf einen Unterschlüssel innerhalb von HKEY_LOCAL_MACHINE Backslash System Backslash CurrentControlSet Backslash Hardware Profiles Backslash Current.

Keys and Subkeys: Within each root key, there are keys, which are comparable to folders in a file system. Schlüssel und Unterschlüssel: Innerhalb jedes Stammschlüssels gibt es Schlüssel, die mit Ordnern in einem Dateisystem vergleichbar sind.

Keys can contain other keys, called subkeys, creating a tree-like structure. Schlüssel können andere Schlüssel enthalten, sogenannte Unterschlüssel, wodurch eine baumartige Struktur entsteht.

This organization helps to logically group related settings. For example, you can find a key for a specific software application and within this key, subkeys for the various components or settings. Diese Organisation hilft dabei, zusammengehörige Einstellungen logisch zu gruppieren. Sie können zum Beispiel einen Schlüssel für eine bestimmte Softwareanwendung finden und innerhalb dieses Schlüssels Unterschlüssel für die verschiedenen Komponenten oder Einstellungen.

Values: In the keys and subkeys, the actual configuration data is stored in values. Each value consists of three parts. Werte: In den Schlüsseln und Unterschlüsseln werden die eigentlichen Konfigurationsdaten in Werten gespeichert. Jeder Wert besteht aus drei Teilen.

Name: A descriptive name for the value, for example ScreenSaveTimeOut. A key can have a default value that often has no explicit name. Name: Ein beschreibender Name für den Wert, zum Beispiel ScreenSaveTimeOut. Ein Schlüssel kann einen Standardwert haben, der oft keinen expliziten Namen hat.

Type: The data type of the stored information. Common types are: REG_SZ, a fixed-length text string. Typ: Der Datentyp der gespeicherten Information. Übliche Typen sind: REG_SZ, eine Textzeichenkette mit fester Länge.

REG_EXPAND_SZ, an expandable string that can contain environment variables, for example percent SystemRoot percent. REG_EXPAND_SZ, ein erweiterbarer String, der Umgebungsvariablen enthalten kann, zum Beispiel Prozent SystemRoot Prozent.

REG_BINARY, raw binary data. REG_BINARY, rohe Binärdaten.

REG_DWORD, a 32-bit number. REG_DWORD, eine 32-Bit-Zahl.

REG_QWORD, a 64-bit number. REG_QWORD, eine 64-Bit-Zahl.

REG_MULTI_SZ, a multi-string value that allows multiple text entries to be stored in a single value. REG_MULTI_SZ, ein Multi-String-Wert, mit dem mehrere Texteinträge in einem einzigen Wert gespeichert werden können.

Data: The actual content of the setting, for example 600 for a 10-minute screensaver timeout or C colon backslash Program Files backslash MyApp backslash app dot exe for an application path. Daten: Der tatsächliche Inhalt der Einstellung, zum Beispiel 600 für ein 10-minütiges Bildschirmschoner-Timeout oder C Doppelpunkt Backslash Program Files Backslash MyApp Backslash app Punkt exe für einen Anwendungspfad.

Registry in Cybersecurity Registrierung in der Cybersicherheit

Understanding the registry is crucial for cybersecurity for several reasons. Das Verständnis der Registrierung ist für die Cybersicherheit aus mehreren Gründen entscheidend.

Digital Forensics: The registry is a treasure trove of evidence. Investigators can find: timestamps for key changes, lists of recently executed programs, such as RunMRU. Digitale Forensik: Die Registrierung ist eine Fundgrube für Beweise. Ermittler können finden: Zeitstempel für Schlüsseländerungen, Listen kürzlich ausgeführter Programme, wie RunMRU.

Connected USB devices, network connection history, user activities and account information. Angeschlossene USB-Geräte, Verlauf der Netzwerkverbindungen, Benutzeraktivitäten und Kontoinformationen.

Malware Analysis and Persistence: Malware frequently uses the registry to: achieve persistence. Malware-Analyse und Persistenz: Malware nutzt die Registrierung häufig, um: Persistenz zu erreichen.

By adding entries to Run keys, for example HKLM backslash Software backslash Microsoft backslash Windows backslash CurrentVersion backslash Run or HKCU backslash Software backslash Microsoft backslash Windows backslash CurrentVersion backslash Run, malware can ensure that it is automatically started every time the system starts or a user logs in. Durch Hinzufügen von Einträgen zu Run-Schlüsseln, zum Beispiel HKLM Backslash Software Backslash Microsoft Backslash Windows Backslash CurrentVersion Backslash Run oder HKCU Backslash Software Backslash Microsoft Backslash Windows Backslash CurrentVersion Backslash Run, kann Malware sicherstellen, dass sie bei jedem Systemstart oder bei der Anmeldung eines Benutzers automatisch gestartet wird.

Store its own configuration data, disable security software or change system behavior, hide its presence. Eigene Konfigurationsdaten speichern, Sicherheitssoftware deaktivieren oder das Systemverhalten ändern, seine Anwesenheit verbergen.

System Hardening and Configuration Management: Security professionals modify registry settings to: improve security by disabling unnecessary services or features. Systemhärtung und Konfigurationsmanagement: Sicherheitsexperten ändern die Einstellungen der Registrierung, um: Sicherheit zu verbessern, indem unnötige Dienste oder Funktionen deaktiviert werden.

Enforce security policies, configure logging and auditing. Sicherheitsrichtlinien durchzusetzen, Protokollierung und Prüfung zu konfigurieren.

Incident Response: During an incident, staff examine the registry to understand the extent of a compromise, identify the attackers' TTPs, or tactics, techniques and procedures, and find indicators of compromise, or IOCs. Reaktion auf einen Vorfall: Während eines Vorfalls untersuchen die Mitarbeiter die Registrierung, um das Ausmaß einer Kompromittierung zu verstehen, die TTPs der Angreifer, also Taktiken, Techniken und Verfahren, zu identifizieren und Indikatoren für eine Kompromittierung, oder IOCs, zu finden.

Vulnerability Assessment: Some vulnerabilities may be related to improper registry permissions or configurations. Schwachstellenbewertung: Einige Schwachstellen können mit unzulässigen Registrierungsberechtigungen oder Konfigurationen zusammenhängen.

Accessing the Registry: The Registry Editor, or Regedit Zugriff auf die Registrierung: Der Registrierungseditor, oder Regedit

Windows provides a built-in tool, the Registry Editor, regedit dot exe, to view and modify the registry. Windows bietet ein eingebautes Werkzeug, den Registrierungseditor, regedit Punkt exe, um die Registrierung anzuzeigen und zu ändern.

Important Caution: The registry contains important system settings. Incorrect modification of the registry can lead to severe system instability or even prevent your system from starting up. Wichtige Vorsicht: Die Registrierung enthält wichtige Systemeinstellungen. Eine falsche Änderung der Registrierung kann zu einer schweren Instabilität des Systems führen oder sogar verhindern, dass Ihr System hochfährt.

In this preparation, you will only view the registry, but not change anything. Bei dieser Vorbereitung werden Sie nur die Registrierung einsehen, aber nichts ändern.

Always be extremely careful when you need to make changes, and make sure you have a backup or know how to restore the settings if something goes wrong. Seien Sie immer äußerst vorsichtig, wenn Sie Änderungen vornehmen müssen, und stellen Sie sicher, dass Sie ein Backup haben oder wissen, wie Sie die Einstellungen wiederherstellen können, falls etwas schief geht.

Try it yourself: Exploring with Regedit Versuchen Sie es selbst: Erkundung mit Regedit

On your virtual Windows machine, press the Windows key plus R combination to open the Run dialog box. Drücken Sie auf Ihrer virtuellen Windows-Maschine die Tastenkombination Windows-Taste plus R, um das Dialogfeld Ausführen zu öffnen.

Type regedit and press Enter or click OK. Geben Sie regedit ein und drücken Sie Enter oder klicken Sie auf OK.

If a User Account Control, or UAC, prompt appears, click Yes. Wenn eine Aufforderung zur Benutzerkontensteuerung, oder UAC, erscheint, klicken Sie auf Ja.

The Registry Editor window will open. The left pane lists the root keys, like the folders in File Explorer. Das Fenster des Registrierungseditors wird geöffnet. Im linken Bereich werden die Stammschlüssel aufgelistet, wie die Ordner im Datei-Explorer.

Try navigating to the following key: HKEY_CURRENT_USER backslash Software backslash Microsoft backslash Windows backslash CurrentVersion backslash Explorer backslash TypedPaths. Versuchen Sie, zum folgenden Schlüssel zu navigieren: HKEY_CURRENT_USER Backslash Software Backslash Microsoft Backslash Windows Backslash CurrentVersion Backslash Explorer Backslash TypedPaths.

Click the arrow next to HKEY_CURRENT_USER to expand it. Klicken Sie auf den Pfeil neben HKEY_CURRENT_USER, um ihn zu erweitern.

Then expand Software, then Microsoft, then Windows, then CurrentVersion, then Explorer. Erweitern Sie dann Software, dann Microsoft, dann Windows, dann CurrentVersion, dann Explorer.

Finally, click on the TypedPaths key. Klicken Sie schließlich auf den Schlüssel TypedPaths.

Observe the values in the right pane. What do you see? These are paths that you recently entered into the File Explorer address bar or the Run dialog box. Beobachten Sie die Werte im rechten Fenster. Was sehen Sie? Dies sind Pfade, die Sie kürzlich in die Adressleiste des Datei-Explorers oder in das Dialogfeld Ausführen eingegeben haben.

Do not change any values. Just observe. Close the Registry Editor when you are finished. Ändern Sie keine Werte. Beobachten Sie einfach. Schließen Sie den Registrierungseditor, wenn Sie fertig sind.

Think about it Denken Sie darüber nach

Consider the previously mentioned Run keys, for example HKEY_LOCAL_MACHINE backslash Software backslash Microsoft backslash Windows backslash CurrentVersion backslash Run. Betrachten Sie die bereits erwähnten Run-Schlüssel, zum Beispiel HKEY_LOCAL_MACHINE Backslash Software Backslash Microsoft Backslash Windows Backslash CurrentVersion Backslash Run.

If you were a malware author who wanted your program to automatically start every time a user logs on to the computer, which Run key would you target and why? Wenn Sie ein Malware-Autor wären, der möchte, dass sein Programm jedes Mal automatisch gestartet wird, wenn sich ein Benutzer am Computer anmeldet, welchen Run-Schlüssel würden Sie anvisieren und warum?

What if you only wanted to start it for the currently infected user? Was wäre, wenn Sie es nur für den aktuell infizierten Benutzer starten wollten?

This preparation will provide you with a solid foundation for our live session, where we will delve deeper into how the registry works, its use and misuse, and its analysis from a cybersecurity perspective. Diese Vorbereitung wird Ihnen eine solide Grundlage für unsere Live-Sitzung bieten, in der wir uns eingehender mit der Funktionsweise der Registrierung, ihrer Verwendung und ihrem Missbrauch sowie ihrer Analyse aus der Perspektive der Cybersicherheit befassen werden.

The slides for the live session can be viewed here at this link. Try not to peek before class, spoilers inside! Die Folien für die Live-Sitzung können hier unter diesem Link angesehen werden. Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!