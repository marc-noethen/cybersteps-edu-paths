## 📊 Zusammenfassung nach dem 80/20-Prinzip

**Kernaussage:** Virtualisierung ermöglicht das sichere Ausführen von Windows auf einem Mac für Cybersecurity-Training, ohne das Host-System zu gefährden.

**Die wichtigsten 20% der Informationen:**

**1. Warum Virtualisierung?**

- Windows ist dominant in Unternehmensumgebungen und essenziell für Cybersecurity-Profis
- Virtuelle Maschinen (VMs) erlauben das Ausführen von Windows auf einem Mac ohne separate Hardware
- Ein Hypervisor (VMware Fusion Pro) verwaltet die Ressourcenzuteilung

**2. Hauptnutzen für Cybersecurity:**

- **Sicheres Malware-Testing:** Schadsoftware kann in isolierter Umgebung analysiert werden, ohne das Host-System zu infizieren
- **Snapshots ermöglichen Zurücksetzen** auf sauberen Zustand nach Experimenten
- **Praxislabore** für Penetrationstests und Forensik können aufgebaut werden

**3. Wichtige Windows-Komponenten:**

- **NTFS-Dateisystem** und **Registry** sind kritisch für Forensik und Malware-Analyse
- **PowerShell** ist das mächtigste Tool für Systemadministration und Cybersecurity-Aufgaben
- **Event Logs** dokumentieren alle wichtigen Systemereignisse für Incident-Investigation

**4. Setup-Essentials:**

- Mindestens 40 GB freier Speicherplatz erforderlich
- Prozess dauert 30-60 Minuten
- Nach Installation: VMware Tools installieren für Copy-Paste und Dateiübertragung
- Immer ordnungsgemäß herunterfahren, nicht einfach Fenster schließen

**Praktischer Einstieg:** Nach der Installation sollten Sie sich mit Start-Menü, File Explorer, Command Prompt `ipconfig`) und PowerShell `Get-Process`) vertraut machen, um die Grundlagen für weiterführende Cybersecurity-Analysen zu schaffen.

---

## Verwendete Tools

|Begriff|Bedeutung|
|---|---|
|VMware Fusion Pro|Hypervisor-Software für Mac, um virtuelle Maschinen zu erstellen und zu verwalten|
|Windows 11|Aktuelles Microsoft-Betriebssystem für die VM-Installation|
|Command Prompt (cmd)|Traditionelle Befehlszeilenschnittstelle in Windows|
|PowerShell|Fortgeschrittene Skript- und Befehlszeilen-Shell basierend auf .NET|
|File Explorer|Dateimanager-Tool zur Navigation im Windows-Dateisystem|
|VMware Tools|Erweiterungssoftware für bessere Integration zwischen Host und VM|

---

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|Virtualisierung|Technologie zum gleichzeitigen Ausführen mehrerer Betriebssysteme auf einem Computer|
|Virtual Machine (VM)|In Software emulierter Computer mit eigenem Betriebssystem|
|Hypervisor|Software zur Verwaltung und Zuteilung physischer Ressourcen an VMs|
|Host-System|Das primäre Betriebssystem des physischen Computers|
|Sandbox|Isolierte Umgebung zum sicheren Testen von Software/Malware|
|Snapshot|Momentaufnahme eines VM-Zustands zur späteren Wiederherstellung|
|NTFS|New Technology File System - Standard-Dateisystem von Windows|
|Registry|Hierarchische Datenbank für Windows-Systemeinstellungen|
|ISO|Abbild-Datei mit vollständigem Installationsmedium|
|Malware|Schadsoftware wie Viren, Ransomware, Trojaner|
|Penetration Testing|Ethisches Hacken zur Sicherheitsprüfung von Systemen|
|Forensische Untersuchung|Digitale Spurensuche auf kompromittierten Systemen|

---

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|Isolierte Umgebung|Abgetrennter Bereich ohne Zugriff auf das Hauptsystem|
|Persistenz|Fähigkeit von Malware, nach Neustart weiter aktiv zu bleiben|
|Patch-Level|Aktualisierungsstand des Systems bezüglich Sicherheitsupdates|
|Event Logs|Protokolldateien über Systemereignisse für Fehleranalyse|
|User Account Control (UAC)|Sicherheitsfunktion gegen unbefugte Systemänderungen|
|IPv4-Adresse|Numerische Netzwerkadresse zur Identifikation im Netzwerk|
|Disk Image|Vollständige Kopie einer Festplatte oder Partition|
|Exploit|Ausnutzung einer Sicherheitslücke|
|Administrator-Rechte|Erhöhte Berechtigungen für Systemänderungen|