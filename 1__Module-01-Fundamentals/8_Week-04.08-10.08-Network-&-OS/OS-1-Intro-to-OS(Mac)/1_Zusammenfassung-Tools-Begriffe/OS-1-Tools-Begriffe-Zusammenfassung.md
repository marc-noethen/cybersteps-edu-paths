## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Was ist ein Betriebssystem?

Ein **Betriebssystem** ist die zentrale Software, die alle Hardware- und Softwareressourcen eines Computers koordiniert. Es dient zwei Hauptzielen: **Benutzerfreundlichkeit** durch Vereinfachung komplexer Hardware-Operationen und **effiziente Ressourcenverwaltung** von CPU, Speicher und Geräten.

### Kernkomponenten

Die wichtigsten Komponenten sind:

1. **Kernel** - Das "Herz" des OS, verwaltet CPU, Speicher und Hardware direkt
2. **Shell/Terminal** - Befehlszeilenschnittstelle für fortgeschrittene Steuerung
3. **GUI** - Grafische Oberfläche mit Fenstern und Icons (bei Windows: Datei-Explorer statt Finder)
4. **Dateisystem** - Organisiert Daten auf Festplatten (Windows verwendet NTFS statt APFS)

### Windows 11 Besonderheiten

- **Kernel**: NT-Kernel (statt XNU)
- **Shell**: PowerShell und Eingabeaufforderung (statt Zsh)
- **Dateimanager**: Datei-Explorer (statt Finder)
- **Einstellungen**: Windows-Einstellungen (statt Systemeinstellungen)
- **Verschlüsselung**: BitLocker (statt FileVault)
- **Sicherheit**: Windows Defender, SmartScreen (statt Gatekeeper/XProtect)

### Warum Betriebssysteme für Cybersicherheit wichtig sind

Betriebssysteme sind das **Hauptziel von Angriffen**, da Schwachstellen im OS vollständige Systemkontrolle ermöglichen können. Wichtige Aspekte:

- **Angriffsziel**: Schwachstellen in Kernel, Systemdiensten und Treibern
- **Sicherheitstools**: Antivirensoftware, Firewalls, EDR-Lösungen arbeiten auf OS-Ebene
- **Forensik**: Analyse von Logs, Prozessen und Dateisystem-Artefakten nach Vorfällen
- **Systemhärtung**: Deaktivieren unnötiger Dienste, Patches einspielen, starke Berechtigungen

### Wichtigste Sicherheitsmaßnahmen (Windows 11)

1. **BitLocker** aktivieren für Festplattenverschlüsselung
2. **Windows Defender Firewall** eingeschaltet lassen
3. **Updates** regelmäßig installieren
4. **SmartScreen** für Download-Schutz nutzen
5. **Benutzerkonten** mit eingeschränkten Rechten arbeiten
6. **Datenschutzeinstellungen** in den Windows-Einstellungen überprüfen

### Praktische Werkzeuge (Windows 11)

- **Task-Manager** (Strg+Shift+Esc): Prozesse und Ressourcennutzung überwachen
- **PowerShell**: Befehle wie `Get-Process`, `Get-Service` für Systemanalyse
- **Datenträgerverwaltung**: Festplatten formatieren und partitionieren
- **Ereignisanzeige**: System-Logs für Fehlersuche und Sicherheitsanalyse

**Kernbotschaft**: Das Betriebssystem ist die fundamentale Sicherheitsebene - wer das OS kontrolliert, kontrolliert das gesamte System. Daher ist tiefes OS-Verständnis für Cybersicherheit unverzichtbar.

---

## Verwendete Tools

|Tool/Anwendung|Bedeutung|
|---|---|
|**Activity Monitor** (Win: Task-Manager)|Zeigt laufende Prozesse und Systemressourcennutzung (CPU, RAM, Festplatte, Netzwerk) an|
|**Terminal** (Win: Eingabeaufforderung/PowerShell)|Befehlszeilenschnittstelle für textbasierte Systembefehle|
|**Finder** (Win: Datei-Explorer)|Grafischer Dateimanager zum Durchsuchen und Verwalten von Dateien und Ordnern|
|**System Preferences** (Win: Einstellungen)|Zentrale Anwendung zur Konfiguration von Systemeinstellungen|
|**Disk Utility** (Win: Datenträgerverwaltung)|Werkzeug zum Formatieren, Partitionieren und Reparieren von Festplatten|
|**Spotlight** (Win: Windows-Suche)|Systemweite Suchfunktion für Dateien, Programme und Inhalte|
|**Gatekeeper** (Win: SmartScreen)|Sicherheitsmechanismus, der Downloads von nicht vertrauenswürdigen Quellen blockiert|
|**FileVault** (Win: BitLocker)|Vollständige Festplattenverschlüsselung zum Schutz von Daten|

---

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|**Kernel**|Kern des Betriebssystems, der grundlegende Systemoperationen verwaltet und privilegierten Hardwarezugriff hat|
|**XNU** (Win: NT-Kernel)|Hybrid-Kernel von macOS, kombiniert Mach-Mikrokernel und BSD-Unix-Komponenten|
|**Shell**|Befehlszeilenschnittstelle zur Interaktion mit dem Betriebssystem (z.B. Zsh bei macOS, PowerShell bei Windows)|
|**GUI (Grafische Benutzeroberfläche)**|Visuelle Schnittstelle mit Fenstern, Icons und Menüs zur Computersteuerung|
|**CLI (Command-Line Interface)**|Textbasierte Schnittstelle zur Eingabe von Befehlen|
|**Gerätetreiber**|Spezialisierte Software zur Kommunikation zwischen Betriebssystem und Hardware|
|**Systemaufruf (System Call)**|Schnittstelle, über die Programme Dienste vom Kernel anfordern|
|**APFS** (Win: NTFS)|Apple File System - modernes Dateisystem für SSDs mit Verschlüsselung und Snapshots|
|**Prozess**|Ein Programm in Ausführung, das vom Betriebssystem verwaltet wird|
|**Multitasking**|Gleichzeitige Ausführung mehrerer Programme durch schnelles Umschalten der CPU|
|**SIP (System Integrity Protection)** (Win: ähnlich: geschützte Systemdateien)|Schutzmechanismus, der kritische Systemdateien vor Änderungen schützt|
|**Sandboxing**|Ausführung von Programmen in isolierter Umgebung mit eingeschränktem Zugriff|
|**Root/Administrator**|Benutzer mit vollständigen Systemrechten|
|**Virtueller Speicher**|Verwendung von Festplattenspeicher als Erweiterung des RAM|

---

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|**Betriebssystem (OS)**|Zentrale Software, die Hardware- und Softwareressourcen koordiniert und verwaltet|
|**Abstraktion**|Vereinfachung komplexer Vorgänge durch Verbergen technischer Details|
|**Ressourcenverwaltung**|Zuteilung und Kontrolle von CPU, Speicher, Festplatte und E/A-Geräten|
|**Dateisystem**|Strukturierte Organisation und Verwaltung von Daten auf Speichergeräten|
|**Berechtigungen**|Zugriffsrechte, die festlegen, wer was mit Dateien und Ordnern tun darf|
|**Verschlüsselung**|Umwandlung von Daten in unlesbares Format zum Schutz vor unbefugtem Zugriff|
|**Malware**|Schadsoftware wie Viren, Würmer, Trojaner, Ransomware|
|**Schwachstelle (Vulnerability)**|Sicherheitslücke in Software, die von Angreifern ausgenutzt werden kann|
|**Systemhärtung (Hardening)**|Sicherheitsmaßnahmen zur Reduzierung der Angriffsfläche eines Systems|
|**Angriffsfläche**|Summe aller Punkte, an denen ein System angegriffen werden kann|
|**Privilegienerweiterung**|Erlangen höherer Zugriffsrechte durch Ausnutzen von Schwachstellen|
|**Forensische Analyse**|Untersuchung von Systemen nach Sicherheitsvorfällen zur Spurensicherung|
|**Patch**|Software-Update zur Behebung von Sicherheitslücken oder Fehlern|
|**Firewall**|Sicherheitssystem zur Kontrolle des Netzwerkverkehrs|