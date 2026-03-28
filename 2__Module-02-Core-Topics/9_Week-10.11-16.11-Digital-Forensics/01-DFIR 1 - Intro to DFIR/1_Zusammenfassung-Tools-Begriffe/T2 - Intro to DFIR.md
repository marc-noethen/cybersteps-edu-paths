Why the focus on Windows? Warum der Fokus auf Windows?

Because the vast majority of corporate and government networks run on Windows. Weil die große Mehrheit der Unternehmens- und Regierungsnetzwerke auf Windows läuft.

From employee workstations to critical servers running Active Directory, Windows is the dominant operating system in the environments that attackers most often target. Von Mitarbeiter-Arbeitsplätzen bis zu kritischen Servern, die Active Directory ausführen, ist Windows das dominierende Betriebssystem in den Umgebungen, die Angreifer am häufigsten ins Visier nehmen.

Understanding how to find evidence on Windows systems is therefore a critical skill for any DFIR professional. Zu verstehen, wie man Beweise auf Windows-Systemen findet, ist daher eine entscheidende Fähigkeit für jeden DFIR-Profi.

Forensic investigators look for artifacts, which are the digital breadcrumbs that attackers leave behind. Forensische Ermittler suchen nach Artefakten, die die digitalen Brotkrumen sind, die Angreifer hinterlassen.

These artifacts can be grouped into several key categories. Diese Artefakte können in mehrere Schlüsselkategorien gruppiert werden.

Filesystem Artifacts. Dateisystem-Artefakte.

These relate to the storage of data on disk. Diese beziehen sich auf die Speicherung von Daten auf der Festplatte.

Analysis can reveal created, modified, and deleted files, and even when they were accessed. Die Analyse kann erstellte, geänderte und gelöschte Dateien offenbaren und sogar wann auf sie zugegriffen wurde.

Examples. The Master File Table, MFT, which acts as a database of all files. Beispiele. Die Master File Table, MFT, die als Datenbank aller Dateien fungiert.

The USN Journal, which tracks changes to files. Das USN Journal, das Änderungen an Dateien verfolgt.

Program Execution Artifacts. Programmausführungs-Artefakte.

These artifacts provide proof that a specific program was run on the system. Diese Artefakte liefern den Beweis, dass ein bestimmtes Programm auf dem System ausgeführt wurde.

Examples. Prefetch files, which Windows creates to speed up application loading. Beispiele. Prefetch-Dateien, die Windows erstellt, um das Laden von Anwendungen zu beschleunigen.

Shimcache, Amcache, which tracks application compatibility information. Shimcache, Amcache, die Informationen zur Anwendungskompatibilität verfolgen.

User Activity Artifacts. Benutzeraktivitäts-Artefakte.

These show what a user has been doing on the system, such as which files they opened or which folders they accessed. Diese zeigen, was ein Benutzer auf dem System gemacht hat, wie welche Dateien er geöffnet oder welche Ordner er aufgerufen hat.

Examples. LNK, shortcut, files. Beispiele. LNK, Verknüpfungs-Dateien.

Shellbags, which store folder viewing preferences. Shellbags, die Ordneransichtspräferenzen speichern.

Browser history. Browserverlauf.

System and Configuration Artifacts. System- und Konfigurations-Artefakte.

These artifacts are part of the operating system's core configuration and logging mechanisms. Diese Artefakte sind Teil der Kernkonfiguration und Protokollierungsmechanismen des Betriebssystems.

They provide a timeline of system level events. Sie bieten eine Zeitleiste von Ereignissen auf Systemebene.

Examples. The Windows Registry, a giant database of system and user settings. Beispiele. Die Windows-Registry, eine riesige Datenbank von System- und Benutzereinstellungen.

Windows Event Logs, which record everything from user logons to application crashes. Windows-Ereignisprotokolle, die alles von Benutzeranmeldungen bis zu Anwendungsabstürzen aufzeichnen.

Volatile Memory Artifacts. Flüchtige Speicher-Artefakte.

Found in RAM, this evidence is lost when the computer is shut down. Im RAM zu finden, gehen diese Beweise verloren, wenn der Computer heruntergefahren wird.

It provides a snapshot of what was happening on the system at a specific moment in time. Sie bieten eine Momentaufnahme dessen, was zu einem bestimmten Zeitpunkt auf dem System passierte.

Examples. A list of running processes, active network connections, command line history, and even encryption keys. Beispiele. Eine Liste laufender Prozesse, aktive Netzwerkverbindungen, Kommandozeilenverlauf und sogar Verschlüsselungsschlüssel.

Try it yourself: Finding Evidence of Program Execution. Probiere es selbst aus: Finden von Beweisen für Programmausführung.

Let's find a real forensic artifact on your own Windows VM. Lass uns ein echtes forensisches Artefakt auf deiner eigenen Windows-VM finden.

We'll look for Prefetch files, which are created by Windows to help speed up the loading of programs you've run. Wir werden nach Prefetch-Dateien suchen, die von Windows erstellt werden, um das Laden von Programmen, die du ausgeführt hast, zu beschleunigen.

In your Windows VM, open the mspaint application. Öffne in deiner Windows-VM die mspaint-Anwendung.

You can find it by searching for Paint in the Start Menu. Du kannst sie finden, indem du im Startmenü nach Paint suchst.

Draw something, then close it. Zeichne etwas und schließe sie dann.

Open File Explorer. Öffne den Datei-Explorer.

Navigate to the Windows Prefetch directory. Navigiere zum Windows Prefetch Verzeichnis.

You will likely see a permissions prompt. Click Continue to grant access. Du wirst wahrscheinlich eine Berechtigungsaufforderung sehen. Klicke auf Fortfahren, um Zugriff zu gewähren.

Look through the list of files. Schaue dir die Liste der Dateien an.

You should see a file with a name like MSPAINT.EXE.pf. Du solltest eine Datei mit einem Namen wie MSPAINT.EXE.pf sehen.

The presence of this file is direct evidence that mspaint.exe was executed on this system. Das Vorhandensein dieser Datei ist ein direkter Beweis dafür, dass mspaint.exe auf diesem System ausgeführt wurde.

Notice the Date modified timestamp for that file. Beachte den Zeitstempel für das Änderungsdatum dieser Datei.

It should correspond to the time you just ran the program. Er sollte dem Zeitpunkt entsprechen, zu dem du das Programm gerade ausgeführt hast.

This is a fundamental technique in forensics: correlating timestamps with known events to build a timeline. Dies ist eine grundlegende Technik in der Forensik: Zeitstempel mit bekannten Ereignissen zu korrelieren, um eine Zeitleiste zu erstellen.

Setup. Einrichtung.

Install Eric Zimmerman's Tools, EZ Tools. Installiere Eric Zimmermans Tools, EZ Tools.

Eric Zimmerman's tools are the industry standard for parsing Windows forensic artifacts from the command line. Eric Zimmermans Tools sind der Industriestandard für das Parsen von Windows-Forensik-Artefakten über die Kommandozeile.

Create a Folder. Erstelle einen Ordner.

In your Windows VM, create a new folder on your C drive called Tools. Erstelle in deiner Windows-VM einen neuen Ordner auf deinem C-Laufwerk namens Tools.

Download the Script. Lade das Skript herunter.

Open a web browser in your VM and go to Eric Zimmerman's website. Öffne einen Webbrowser in deiner VM und gehe zu Eric Zimmermans Website.

Download the Get-ZimmermanTools.ps1 PowerShell script and save it into your Tools folder. Lade das Get-ZimmermanTools.ps1 PowerShell-Skript herunter und speichere es in deinem Tools-Ordner.

Run the Script. Führe das Skript aus.

Open PowerShell as an Administrator. Öffne PowerShell als Administrator.

Search for PowerShell, right click, Run as administrator. Suche nach PowerShell, klicke mit der rechten Maustaste, Als Administrator ausführen.

Navigate to your tools folder by typing: cd Tools. Navigiere zu deinem Tools-Ordner, indem du eingibst: cd Tools.

Run the following command to download all of the tools. Führe den folgenden Befehl aus, um alle Tools herunterzuladen.

This may take a few minutes. Dies kann einige Minuten dauern.

powershell.exe -ExecutionPolicy Bypass -File Get-ZimmermanTools.ps1 powershell.exe -ExecutionPolicy Bypass -File Get-ZimmermanTools.ps1

This will create a new folder, for example, net6, inside Tools containing all the command line executables. Dies erstellt einen neuen Ordner, zum Beispiel net6, innerhalb von Tools, der alle Kommandozeilen-Programme enthält.

Try it yourself: Finding Evidence with EZ Tools. Probiere es selbst aus: Finden von Beweisen mit EZ Tools.

Let's find a real forensic artifact using one of the tools you just installed. Lass uns ein echtes forensisches Artefakt finden, indem wir eines der Tools verwenden, die du gerade installiert hast.

We'll use PECmd.exe to parse Prefetch files, which are created by Windows to help speed up the loading of programs you've run. Wir werden PECmd.exe verwenden, um Prefetch-Dateien zu parsen, die von Windows erstellt werden, um das Laden von Programmen, die du ausgeführt hast, zu beschleunigen.

In your Windows VM, open the mspaint application. Öffne in deiner Windows-VM die mspaint-Anwendung.

You can find it by searching for Paint in the Start Menu. Du kannst sie finden, indem du im Startmenü nach Paint suchst.

Draw something, then close it. Zeichne etwas und schließe sie dann.

This action creates or updates the Prefetch file for Paint. Diese Aktion erstellt oder aktualisiert die Prefetch-Datei für Paint.

Open PowerShell. Öffne PowerShell.

It doesn't need to be as an administrator this time. Es muss diesmal nicht als Administrator sein.

Navigate to the directory where the EZ tools were downloaded. Navigiere zu dem Verzeichnis, in das die EZ-Tools heruntergeladen wurden.

For example, if they are in a net6 folder, you would type: cd Tools net6. Zum Beispiel, wenn sie in einem net6-Ordner sind, würdest du eingeben: cd Tools net6.

Now, run the PECmd.exe tool. Führe jetzt das PECmd.exe-Tool aus.

This command tells it to look in the default Prefetch directory and save the output as a CSV file in your current directory. Dieser Befehl weist es an, im Standard-Prefetch-Verzeichnis zu suchen und die Ausgabe als CSV-Datei in deinem aktuellen Verzeichnis zu speichern.

PECmd.exe -d Windows Prefetch --csv. PECmd.exe -d Windows Prefetch --csv.

After the command finishes, a new CSV file will appear in your Tools net6 folder. Nachdem der Befehl abgeschlossen ist, erscheint eine neue CSV-Datei in deinem Tools net6 Ordner.

The filename will include the current date and time. Der Dateiname enthält das aktuelle Datum und die Uhrzeit.

Open this CSV file with Excel or another spreadsheet viewer. Öffne diese CSV-Datei mit Excel oder einem anderen Tabellenkalkulationsprogramm.

Look through the spreadsheet for the ExecutableName column and find the entry for MSPAINT.EXE. Schaue dir die Tabelle nach der ExecutableName-Spalte an und finde den Eintrag für MSPAINT.EXE.

Look at the RunCount and LastRun columns for that row. Schaue dir die RunCount- und LastRun-Spalten für diese Zeile an.

The timestamp should correspond to when you just ran the program. Der Zeitstempel sollte dem Zeitpunkt entsprechen, zu dem du das Programm gerade ausgeführt hast.

You have just performed a basic forensic analysis of a program execution artifact! Du hast gerade eine grundlegende forensische Analyse eines Programmausführungs-Artefakts durchgeführt!

You are now prepared for our first session on DFIR. Du bist jetzt vorbereitet für unsere erste Sitzung zu DFIR.

Want to learn more? Möchtest du mehr lernen?

This is just the tip of the iceberg. Das ist nur die Spitze des Eisbergs.

The SANS Institute provides an excellent Windows Forensic Analysis poster that is a fantastic reference for these artifacts and many more. Das SANS Institute bietet ein ausgezeichnetes Windows Forensic Analysis Poster, das eine fantastische Referenz für diese Artefakte und viele mehr ist.