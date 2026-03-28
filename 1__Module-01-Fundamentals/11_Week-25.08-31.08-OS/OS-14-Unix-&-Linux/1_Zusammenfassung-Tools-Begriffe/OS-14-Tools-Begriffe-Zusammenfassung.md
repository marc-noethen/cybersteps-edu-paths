# Unix & Linux Grundlagen - Kategorisierung

## Verwendete Tools

|Tool|Bedeutung|
|---|---|
|**Bash (Bourne Again Shell)**|Weit verbreitete Shell und Kommandozeileninterpreter, Standard in vielen Linux-Distributionen|
|**Zsh (Z Shell)**|Moderne, leistungsstarke Shell, Standard in macOS und Kali Linux|
|**Terminal / Terminal Emulator**|Anwendung zur Interaktion mit der Shell über Befehlszeile|
|**APT (Advanced Package Tool)**|Paketverwaltungssystem für Debian-basierte Systeme wie Kali Linux und Ubuntu|
|**systemd**|Modernes Init-System und Service-Manager für Linux-Distributionen|
|**systemctl**|Befehl zur Verwaltung von systemd-Diensten (Start, Stopp, Status, Enable/Disable)|
|**cron**|Zeitbasierter Job-Scheduler für wiederkehrende Aufgaben|
|**SSH (Secure Shell)**|Verschlüsseltes Protokoll für sicheren Remote-Zugriff auf Command-Line|
|**scp (Secure Copy)**|Tool für sichere Dateiübertragung über SSH|
|**sftp (SSH File Transfer Protocol)**|Sicheres Dateiübertragungsprotokoll über SSH|
|**VMware Fusion Player**|Virtualisierungssoftware für macOS (auf Windows: VMware Workstation oder VirtualBox)|
|**chmod**|Befehl zum Ändern von Dateiberechtigungen|
|**chown**|Befehl zum Ändern von Besitzverhältnissen (Owner)|
|**id**|Zeigt Benutzer-ID (UID), Gruppen-ID (GID) und Gruppenmitgliedschaften an|
|**tree**|Zeigt Verzeichnisstrukturen in Baumansicht an|

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|**Unix**|Familie von Multitasking-Betriebssystemen aus den 1960/70er Jahren, Grundlage moderner Systeme|
|**Linux Kernel**|Kern des Betriebssystems, verwaltet Hardware, Prozesse und Systemaufrufe|
|**GNU/Linux**|Korrekte Bezeichnung für "Linux": Linux-Kernel + GNU-Software-Sammlung|
|**Open Source**|Quellcode ist frei verfügbar, kann verwendet, modifiziert und verteilt werden|
|**Distribution (Distro)**|Vollständiges Betriebssystem aus Linux-Kernel plus zusätzlicher Software und Tools|
|**CLI (Command-Line Interface)**|Textbasierte Benutzeroberfläche zur Steuerung des Systems über Befehle|
|**Shell**|Kommandozeileninterpreter, Schnittstelle zwischen Benutzer und Kernel|
|**File System Hierarchy Standard (FHS)**|Standard-Verzeichnisstruktur in Linux-Systemen|
|**Root (/)**|Oberste Ebene des Dateisystems, Ausgangspunkt der Verzeichnishierarchie|
|**Root User (Superuser)**|Administratorkonto mit vollständigen Systemprivilegien|
|**sudo (Superuser Do)**|Befehl zur temporären Ausführung von Kommandos mit Root-Rechten|
|**Package (Paket)**|Archiv mit allen Dateien einer Software plus Metadaten (Version, Abhängigkeiten)|
|**Repository (Repo)**|Server, der Software-Pakete zum Download bereitstellt|
|**Dependencies (Abhängigkeiten)**|Andere Pakete, die für die Funktion einer Software benötigt werden|
|**Daemon**|Hintergrundprozess, der Systemdienste bereitstellt (z.B. Webserver, SSH-Server)|
|**Init System**|Erster gestarteter Prozess, verwaltet alle anderen Prozesse und Dienste|
|**Crontab**|Konfigurationsdatei für zeitgesteuerte, wiederkehrende Aufgaben|
|**UID (User ID)**|Eindeutige numerische Kennung eines Benutzers|
|**GID (Group ID)**|Eindeutige numerische Kennung einer Gruppe|
|**Pipe (|)**|
|**Redirection (>, >>, <)**|Umleitung von Ein-/Ausgabe in/aus Dateien|
|**ISO Image**|Abbild-Datei einer CD/DVD, verwendet zur Installation von Betriebssystemen|

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|**Owner (Besitzer)**|Benutzer, dem eine Datei oder ein Verzeichnis gehört|
|**Group (Gruppe)**|Sammlung von Benutzern zur vereinfachten Rechteverwaltung|
|**Others (Andere)**|Alle Benutzer außer Owner und Gruppenmitglieder|
|**Read (r) - Lesen**|Berechtigung zum Anzeigen von Dateiinhalten oder Verzeichnislisten|
|**Write (w) - Schreiben**|Berechtigung zum Ändern von Dateien oder Erstellen/Löschen in Verzeichnissen|
|**Execute (x) - Ausführen**|Berechtigung zum Ausführen von Dateien oder Betreten von Verzeichnissen|
|**Permissions (Berechtigungen)**|Zugriffsrechte für Dateien und Verzeichnisse (rwx für u/g/o)|
|**Virtual Machine (VM)**|Simulierte Computer-Umgebung innerhalb eines Host-Systems|
|**Hierarchical File System**|Baumstruktur-Dateisystem mit Root (/) als Ausgangspunkt|
|**Portable**|Software, die auf verschiedenen Systemen lauffähig ist|
|**Modular**|Aus unabhängigen, austauschbaren Komponenten aufgebaut|
|**Text Streams**|Textbasierte Datenflüsse zwischen Programmen|
|**Binary Compatible**|Software läuft ohne Änderungen auf verschiedenen Systemen derselben Architektur|
|**Kernel Space / User Space**|Trennung zwischen Kernel-Bereich (privilegiert) und Benutzer-Bereich|
|**Home Directory**|Persönliches Verzeichnis eines Benutzers (z.B. /home/username)|
|**Configuration Files (Configs)**|Einstellungsdateien zur Systemkonfiguration (meist in /etc)|
|**Log Files**|Protokolldateien mit Systemmeldungen und Ereignissen (meist in /var/log)|

---

# Zusammenfassung nach dem 80/20-Prinzip

## Die wichtigsten 20% des Wissens für 80% der Linux-Nutzung

### Was ist Linux?

**Linux** ist ein **Unix-ähnliches, Open-Source-Betriebssystem**, das aus zwei Hauptkomponenten besteht:

1. **Linux-Kernel** (von Linus Torvalds 1991 entwickelt) - Das Herzstück
2. **GNU-Software** + zusätzliche Tools - Die Werkzeuge drumherum

**Richtige Bezeichnung:** GNU/Linux

### Kernmerkmale von Linux

|Merkmal|Bedeutung|Vorteil|
|---|---|---|
|**Open Source**|Quellcode frei verfügbar|Kostenlos, anpassbar, transparent|
|**Stabilität**|Server laufen oft Jahre ohne Neustart|Zuverlässig für kritische Systeme|
|**Sicherheit**|Starkes Berechtigungsmodell|Weniger anfällig für Malware|
|**Flexibilität**|Läuft auf allen Geräten|Smartphones bis Supercomputer|
|**CLI-fokussiert**|Leistungsstarke Kommandozeile|Effiziente Systemverwaltung|

### Die Unix/Linux-Philosophie (3 Grundprinzipien)

1. **Programme tun eine Sache - und das gut**
    
    - Jedes Tool hat einen fokussierten Zweck
    - Beispiel: `ls` listet nur Dateien, `grep` filtert nur Text
2. **Programme arbeiten zusammen**
    
    - Ausgabe eines Programms = Eingabe für ein anderes
    - Über Pipes (`|`) verbunden: `ls | grep dokument`
3. **Text ist die universelle Schnittstelle**
    
    - Programme kommunizieren über Textströme
    - Ermöglicht flexible Kombination verschiedener Tools

### Linux-Distributionen: Die wichtigsten

Eine **Distribution** = Linux-Kernel + vorinstallierte Software + Konfiguration

|Distribution|Zielgruppe|Besonderheit|
|---|---|---|
|**Ubuntu**|Anfänger, Desktop|Benutzerfreundlich, große Community|
|**Debian**|Fortgeschrittene, Server|Sehr stabil, Basis für Ubuntu/Kali|
|**Kali Linux**|Cybersecurity|Vorinstallierte Hacking-Tools|
|**Fedora**|Entwickler|Neueste Software-Versionen|
|**CentOS/Rocky/Alma**|Enterprise-Server|Langzeit-Support, Red Hat-kompatibel|

**Für diesen Kurs:** Kali Linux (Debian-basiert)

### Dateisystem-Hierarchie: Die 10 wichtigsten Verzeichnisse

Linux folgt dem **File System Hierarchy Standard (FHS)** - alles beginnt bei `/` (Root)

|Verzeichnis|Inhalt|Beispiel|
|---|---|---|
|**/**|Root - oberste Ebene|Ausgangspunkt aller Pfade|
|**/home**|Benutzer-Verzeichnisse|`/home/max` (entspricht `C:\Users\Max` in Windows)|
|**/etc**|System-Konfigurationsdateien|Netzwerk-Configs, Service-Einstellungen|
|**/bin**|Essenzielle Benutzer-Programme|`ls`, `cp`, `mv`, `cat`|
|**/usr/bin**|Weitere Benutzer-Programme|Installierte Anwendungen|
|**/var**|Variable Daten|`/var/log` (Protokolle), Mailboxen|
|**/tmp**|Temporäre Dateien|Wird bei Neustart gelöscht|
|**/dev**|Gerätedateien|Hardware-Repräsentationen|
|**/proc**|Virtuelles Prozess-Dateisystem|Laufende Prozesse, Kernel-Infos|
|**/lib**|System-Bibliotheken|Shared Libraries für Programme|

**Navigation:**

- `cd /` → Root-Verzeichnis
- `cd ~` oder `cd` → Eigenes Home-Verzeichnis
- `pwd` → Aktuellen Pfad anzeigen
- `ls /etc` → Inhalt von /etc anzeigen

### Die Shell: Ihre Kommandozentrale

**Was ist eine Shell?**

- Kommandozeileninterpreter zwischen Ihnen und dem Kernel
- Sie tippen Befehle, Shell führt sie aus

**Die zwei wichtigsten Shells:**

- **Bash** - Standard auf vielen Linux-Systemen, Ubuntu (früher)
- **Zsh** - Modern, Standard auf macOS und Kali Linux

**Shell prüfen:** `echo $SHELL` **Version prüfen:** `zsh --version` oder `bash --version`

### Paketverwaltung mit APT (Debian/Kali/Ubuntu)

**Was ist ein Paket?** Software + alle Abhängigkeiten + Metadaten in einem Archiv

**Die 6 wichtigsten APT-Befehle:**

|Befehl|Funktion|Wann verwenden|
|---|---|---|
|`sudo apt update`|Paketlisten aktualisieren|**IMMER vor Installation/Upgrade**|
|`sudo apt upgrade`|Alle Pakete aktualisieren|Regelmäßig für Updates|
|`sudo apt install <paket>`|Software installieren|Neue Programme hinzufügen|
|`sudo apt remove <paket>`|Software deinstallieren|Nicht mehr benötigte Programme|
|`sudo apt autoremove`|Verwaiste Abhängigkeiten entfernen|Nach dem Deinstallieren|
|`apt search <suchbegriff>`|Pakete suchen|Vor Installation recherchieren|

**Typischer Workflow:**

```bash
sudo apt update              # Listen aktualisieren
apt search vim               # Suchen
sudo apt install vim         # Installieren
sudo apt remove vim          # Deinstallieren
sudo apt autoremove          # Aufräumen
```

**Windows-Äquivalent:** Microsoft Store, winget oder manuelle Downloads

### Benutzer, Gruppen und Berechtigungen

**Linux ist Multi-User:**

- Mehrere Benutzer können gleichzeitig angemeldet sein
- Jeder hat eigenen Bereich (`/home/username`)
- Berechtigungen schützen Daten voreinander

**Das Berechtigungs-Schema: rwx für ugo**

|Wer?|Was?|Bedeutung|
|---|---|---|
|**u** (User/Owner)|**r** (Read)|Datei lesen / Verzeichnis auflisten|
|**g** (Group)|**w** (Write)|Datei ändern / in Verzeichnis erstellen/löschen|
|**o** (Others)|**x** (Execute)|Datei ausführen / Verzeichnis betreten|

**Beispiel:** `-rw-r--r--`

- `-` = reguläre Datei (würde `d` für Verzeichnis sein)
- `rw-` = Owner kann lesen und schreiben
- `r--` = Gruppe kann nur lesen
- `r--` = Andere können nur lesen

**Wichtige Befehle:**

- `ls -l` → Berechtigungen anzeigen
- `chmod 755 datei.sh` → Berechtigungen ändern (Owner: rwx, Group: rx, Others: rx)
- `chown benutzer:gruppe datei` → Besitzer ändern

**Der Root-User (Superuser):**

- Hat **alle Rechte** auf dem System
- Entspricht Administrator in Windows
- **NICHT als root anmelden!** Stattdessen: `sudo` verwenden

**`sudo` (Superuser Do):**

- Führt einzelnen Befehl mit Root-Rechten aus
- Sicherer als permanente Root-Anmeldung
- Beispiel: `sudo apt install firefox`

**Wichtige System-Dateien:**

- `/etc/passwd` - Benutzerinformationen (UID, Home, Shell)
- `/etc/group` - Gruppeninformationen
- `/etc/shadow` - Verschlüsselte Passwörter (nur root lesbar)

**Eigene Infos anzeigen:** `id`

### Dienste (Daemons) mit systemd verwalten

**Was ist ein Daemon?** Hintergrundprozess, der Services bereitstellt (Webserver, SSH, Datenbank)

**systemd** ist der moderne Service-Manager in Linux

**Die 5 wichtigsten systemctl-Befehle:**

|Befehl|Funktion|
|---|---|
|`systemctl status <service>`|Status prüfen (läuft es?)|
|`sudo systemctl start <service>`|Service starten|
|`sudo systemctl stop <service>`|Service stoppen|
|`sudo systemctl enable <service>`|Autostart beim Booten aktivieren|
|`sudo systemctl disable <service>`|Autostart deaktivieren|

**Beispiel - SSH-Server:**

```bash
systemctl status ssh         # Läuft SSH?
sudo systemctl start ssh     # SSH starten
sudo systemctl enable ssh    # Bei Boot automatisch starten
```

### Zeitgesteuerte Aufgaben mit cron

**cron** führt Befehle zu festgelegten Zeiten automatisch aus

**Eigene Crontab bearbeiten:** `crontab -e`

**Format:** `Minute Stunde Tag Monat Wochentag Befehl`

**Beispiele:**

```bash
0 2 * * * /home/user/backup.sh          # Täglich um 2:00 Uhr
*/15 * * * * /usr/bin/check-server.sh   # Alle 15 Minuten
0 0 * * 0 /home/user/weekly-report.sh   # Jeden Sonntag um Mitternacht
```

### Remote-Zugriff mit SSH

**SSH (Secure Shell)** = verschlüsselter Remote-Zugriff auf Command-Line

**Warum SSH?**

- Sicher (verschlüsselt)
- Standard für Linux-Server-Verwaltung
- Ermöglicht Fernwartung

**Grundlegende SSH-Befehle:**

```bash
ssh benutzer@192.168.1.100        # Auf Remote-System anmelden
scp datei.txt benutzer@server:~/  # Datei kopieren
sftp benutzer@server              # Interaktiver Dateitransfer
```

**Windows-Äquivalent:** PuTTY, Windows Terminal mit OpenSSH

### Kali Linux Setup (für den Kurs)

**Virtualisierung auf Mac:**

1. **VMware Fusion Player** installieren (kostenlose Personal-Lizenz)
2. **Kali Linux ARM64 ISO** herunterladen ([kali.org](https://cdimage.kali.org/))
3. VM erstellen, als Betriebssystem "Debian 12" auswählen
4. Kali installieren
5. **VMware Tools** installieren:
    
    ```bash
    sudo apt update && sudo apt install open-vm-tools-desktopsudo reboot
    ```
    

**Auf Windows 11:**

- VMware Workstation Player oder VirtualBox verwenden
- Kali Linux x64 ISO herunterladen (nicht ARM)
- Ansonsten identischer Prozess

### Die wichtigsten Basis-Befehle (Kurzübersicht)

|Befehl|Funktion|Beispiel|
|---|---|---|
|`pwd`|Aktuelles Verzeichnis anzeigen|`pwd`|
|`ls`|Dateien auflisten|`ls -la` (alle Details)|
|`cd`|Verzeichnis wechseln|`cd /home/user/Documents`|
|`mkdir`|Verzeichnis erstellen|`mkdir meinordner`|
|`touch`|Leere Datei erstellen|`touch datei.txt`|
|`cp`|Kopieren|`cp quelle.txt ziel.txt`|
|`mv`|Verschieben/Umbenennen|`mv alt.txt neu.txt`|
|`rm`|Löschen (permanent!)|`rm datei.txt`|
|`cat`|Datei-Inhalt anzeigen|`cat config.txt`|
|`less`|Datei seitenweise anzeigen|`less logfile.log`|
|`head`|Erste Zeilen anzeigen|`head -n 10 datei.txt`|
|`tail`|Letzte Zeilen anzeigen|`tail -f /var/log/syslog`|
|`grep`|Text filtern|`ps aux|
|`\|` (Pipe)|Ausgabe weiterleiten|`ls \| grep .txt`|
|`>`|Ausgabe in Datei (überschreiben)|`echo "Test" > datei.txt`|
|`>>`|Ausgabe anhängen|`echo "Mehr" >> datei.txt`|

### Praktische Beispiele für Befehlskombinationen

**1. Alle .txt-Dateien im aktuellen Verzeichnis finden:**

```bash
ls | grep .txt
```

**2. Die 10 größten Dateien anzeigen:**

```bash
ls -lhS | head -n 11
```

**3. Aktive Netzwerkverbindungen anzeigen:**

```bash
ss -tuln
```

**4. Systemlogs in Echtzeit verfolgen:**

```bash
sudo tail -f /var/log/syslog
```

**5. Nach einem laufenden Prozess suchen:**

```bash
ps aux | grep firefox
```

### Die wichtigsten Takeaways

✅ **Linux ist Open Source, stabil, sicher und flexibel** ✅ **Alles ist eine Datei - Hierarchie beginnt bei `/`** ✅ **Die Shell ist mächtig - Unix-Philosophie: kleine Tools kombinieren** ✅ **APT verwaltet Software: update → search → install → remove → autoremove** ✅ **Berechtigungen: rwx für User/Group/Others schützen Daten** ✅ **`sudo` für Admin-Aufgaben statt Root-Anmeldung** ✅ **systemd verwaltet Services (start/stop/enable/disable)** ✅ **SSH für sicheren Remote-Zugriff auf Server** ✅ **Kali Linux für Cybersecurity-Aufgaben in VM installieren** ✅ **Pipe (`|`) und Redirection (`>`, `>>`) sind essentiell für effizientes Arbeiten**

Diese 20% des Wissens ermöglichen Ihnen, 80% der alltäglichen Linux-Aufgaben zu bewältigen und bilden die Grundlage für fortgeschrittene Cybersecurity-Arbeiten mit Kali Linux.