# Kategorisierung der Themen

## Tabelle: Tools, Fachbegriffe und Vokabeln

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Registry Editor (regedit.exe)|Eingebautes Windows-Tool zum Anzeigen und Bearbeiten der Registrierung|
||Windows + R|Tastenkombination zum Öffnen des "Ausführen"-Dialogs|
||PowerShell|Skripterstellung für Registry-Abfragen und -Änderungen|
||RegEdit Command Line|Befehlszeilenzugriff auf Registry für automatisierte Aufgaben|
||Registry Backup Tools|Tools zur Sicherung von Registry-Hives vor Änderungen|
||Forensic Registry Tools|Spezialisierte Software zur Analyse von Registry-Daten bei Ermittlungen|
|**Technische Fachbegriffe**|Registry (Registrierung)|Zentrale hierarchische Datenbank für Windows-Konfigurationen|
||Hives|Dateien, die Registry-Daten enthalten und beim Boot in den Speicher geladen werden|
||Root Keys (Stammschlüssel)|Oberste Container der Registry-Hierarchie (HKEY_*)|
||HKEY_CLASSES_ROOT (HKCR)|Dateiverknüpfungen, OLE-Daten und COM-Objektregistrierungen|
||HKEY_CURRENT_USER (HKCU)|Einstellungen des aktuell angemeldeten Benutzers|
||HKEY_LOCAL_MACHINE (HKLM)|Computerspezifische Konfiguration unabhängig vom Benutzer|
||HKEY_USERS (HKU)|Profile aller Benutzer mit ihren jeweiligen SIDs|
||HKEY_CURRENT_CONFIG (HKCC)|Aktuelles Hardware-Profil beim Systemstart|
||Keys (Schlüssel)|Containerelemente in der Registry, vergleichbar mit Ordnern|
||Subkeys (Unterschlüssel)|Verschachtelte Schlüssel innerhalb eines übergeordneten Schlüssels|
||Values (Werte)|Eigentliche Konfigurationsdaten innerhalb von Schlüsseln|
||REG_SZ|Registry-Datentyp: Textzeichenkette mit fester Länge|
||REG_EXPAND_SZ|Registry-Datentyp: Erweiterbarer String mit Umgebungsvariablen|
||REG_BINARY|Registry-Datentyp: Rohe Binärdaten|
||REG_DWORD|Registry-Datentyp: 32-Bit-Ganzzahl|
||REG_QWORD|Registry-Datentyp: 64-Bit-Ganzzahl|
||REG_MULTI_SZ|Registry-Datentyp: Mehrere Texteinträge in einem Wert|
||SID (Security Identifier)|Eindeutige Sicherheitskennung für Benutzerkonten|
||Run Keys|Registry-Schlüssel für automatischen Programmstart beim Boot/Login|
||Persistence|Fähigkeit von Malware, Neustarts zu überleben (via Registry)|
||INI-Dateien|Veraltetes Konfigurationssystem vor Einführung der Registry|
|**Wichtige Vokabeln**|Hierarchische Struktur|Baumförmige Organisation von Schlüsseln und Unterschlüsseln|
||OLE (Object Linking and Embedding)|Technologie zum Einbetten von Objekten in Dokumenten|
||COM (Component Object Model)|Microsoft-Standard für Softwarekomponenten|
||Dateiverknüpfung|Zuordnung von Dateitypen zu Anwendungen|
||Systemhärtung|Sicherheitsmaßnahmen zur Reduzierung von Angriffsflächen|
||Malware-Persistenz|Mechanismen, mit denen Malware dauerhaft aktiv bleibt|
||Forensische Artefakte|Spuren in der Registry, die bei Ermittlungen relevant sind|
||RunMRU|Registry-Eintrag mit Liste zuletzt ausgeführter Programme|
||TypedPaths|Registry-Speicherort für eingegebene Dateipfade im Explorer|
||IOC (Indicators of Compromise)|Anzeichen für Systemkompromittierung in der Registry|
||TTPs (Tactics, Techniques, Procedures)|Verhaltensweisen und Methoden von Angreifern|
||UAC (User Account Control)|Sicherheitsabfrage bei administrativen Änderungen|
||Timestamp|Zeitstempel von Registry-Änderungen für forensische Analyse|
||USB-Gerätehistorie|In Registry gespeicherte Informationen über angeschlossene Geräte|
||Netzwerkverbindungshistorie|Registry-Einträge über frühere Netzwerkverbindungen|
||Autostart-Einträge|Registry-Werte für automatisch startende Programme|
||Registry-Berechtigungen|Zugriffsrechte auf Registry-Schlüssel und -Werte|

---

## Zusammenfassung nach dem 80/20-Prinzip

**Kernaussage:** Die Windows-Registrierung ist die zentrale Konfigurationsdatenbank des Systems und ein kritisches Element für Forensik, Malware-Analyse und Systemsicherheit.

**Die wichtigsten 20% der Informationen:**

### 1. Was ist die Registry?

**Definition:** Hierarchische Datenbank, die alle Konfigurationseinstellungen für Windows speichert – vom Betriebssystem über Hardware-Treiber bis zu Anwendungseinstellungen.

**Historischer Kontext:**

- Eingeführt mit Windows 3.1 als Ersatz für zahlreiche INI-Dateien
- Zentralisiert alle Systemkonfigurationen an einem Ort

**Speicherstruktur:**

- Besteht aus mehreren "Hives" (Dateien auf der Festplatte)
- Wird beim Systemstart in den Speicher geladen
- Präsentiert sich als logische, hierarchische Baumstruktur

### 2. Die 5 Root Keys (Stammschlüssel)

**HKEY_LOCAL_MACHINE (HKLM):**

- Computerspezifische Konfiguration
- Hardware, Treiber, systemweite Software
- **Wichtigster Schlüssel für Systemadministration**

**HKEY_CURRENT_USER (HKCU):**

- Einstellungen des angemeldeten Benutzers
- Desktop, Bildschirmschoner, persönliche App-Einstellungen
- Zeiger auf entsprechende SID in HKEY_USERS

**HKEY_USERS (HKU):**

- Enthält alle Benutzerprofile nach SID organisiert
- HKCU verlinkt hierauf

**HKEY_CLASSES_ROOT (HKCR):**

- Dateiverknüpfungen (.txt → Notepad)
- COM-Objekte und OLE-Daten

**HKEY_CURRENT_CONFIG (HKCC):**

- Aktuelles Hardware-Profil beim Start

### 3. Registry-Struktur: Schlüssel und Werte

**Keys/Subkeys:** Container wie Ordner, bilden Baumstruktur

**Values (Werte):** Eigentliche Konfigurationsdaten mit drei Komponenten:

1. **Name:** z.B. "ScreenSaveTimeOut"
2. **Typ:** REG_SZ (Text), REG_DWORD (32-Bit-Zahl), REG_BINARY (Binärdaten)
3. **Data:** z.B. "600" (Sekunden), "C:\Program Files\App\app.exe"

### 4. Cybersecurity-Relevanz der Registry

**Forensische Untersuchungen:**

- **Zeitstempel:** Wann wurden Schlüssel geändert?
- **RunMRU:** Liste zuletzt ausgeführter Programme
- **USB-Historie:** Alle jemals angeschlossenen USB-Geräte
- **Netzwerkverbindungen:** Frühere WLAN- und VPN-Verbindungen
- **Benutzeraktivitäten:** TypedPaths zeigt eingegebene Pfade

**Malware-Persistenz:**

- **Run Keys:** Klassischer Persistenzmechanismus
    - `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` → Alle Benutzer
    - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` → Nur aktueller Benutzer
- Malware trägt sich hier ein für Autostart bei jedem Boot/Login

**Incident Response:**

- Identifikation von IOCs (Indicators of Compromise)
- Analyse von Angreifer-TTPs
- Ermittlung des Kompromittierungsumfangs

### 5. Praktischer Zugriff: Registry Editor

**Öffnen:**

- Windows + R → `regedit` eingeben → Enter
- UAC-Abfrage mit "Ja" bestätigen

**Navigation:**

- Linker Bereich: Baumstruktur der Keys
- Rechter Bereich: Values des ausgewählten Keys
- Beispielpfad: `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`

**KRITISCHE WARNUNG:**

- Falsche Registry-Änderungen können System unbrauchbar machen
- Nur anschauen, nicht ändern (außer mit Backup und genauem Wissen)
- Bei Fehlern kann Windows nicht mehr booten

### Praktische Anwendung in Windows 11

**Für Forensik:** Registry ist erste Anlaufstelle bei Untersuchungen – enthält umfassende Spuren von Benutzeraktivitäten und Systemereignissen.

**Für Malware-Analyse:** Überprüfung der Run Keys ist Standard-Check zur Identifikation von Persistenzmechanismen.

**Für Systemhärtung:** Gezielte Registry-Änderungen deaktivieren unsichere Features und erzwingen Sicherheitsrichtlinien.