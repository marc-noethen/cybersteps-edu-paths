# Kategorisierung der Themen

## Verwendete Tools

|Tool/Anwendung|Bedeutung|
|---|---|
|**Datei-Explorer** (File Explorer)|Hauptwerkzeug zum Navigieren, Anzeigen und Verwalten von Dateien und Ordnern in Windows|
|**Datenträgerverwaltung** (diskmgmt.msc)|Windows-Dienstprogramm zum Anzeigen, Erstellen, Löschen, Formatieren und Verwalten von Festplatten und Partitionen|
|**Dateiverlauf** (File History)|Automatisches Backup-Tool für Dateien in Bibliotheken, Desktop, Kontakte und Favoriten auf externe Laufwerke|
|**Sichern und Wiederherstellen**|Traditionelles Windows-Backup-Tool für Systemabbilder und Datei-/Ordnersicherungen|
|**BitLocker Drive Encryption**|Microsofts Vollverschlüsselungslösung für gesamte Laufwerke und Partitionen (nur in Pro/Enterprise-Versionen)|
|**EFS (Encrypting File System)**|NTFS-Funktion zur Verschlüsselung einzelner Dateien oder Ordner, gebunden an Benutzerkonten|
|**Defragmentierung**|Tool zur Reorganisation fragmentierter Dateien auf HDDs für bessere Performance|
|**Eigenschaften-Dialog**|Rechtsklick → Eigenschaften zeigt Metadaten, Berechtigungen und Details zu Dateien/Ordnern|

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|**Dateisystem**|Methode und Datenstruktur zur Organisation, Speicherung und Verwaltung von Dateien auf Speichermedien|
|**NTFS (New Technology File System)**|Primäres modernes Dateisystem für Windows mit Journaling, ACLs, Kompression und Verschlüsselung|
|**FAT32 (File Allocation Table 32)**|Älteres, einfaches Dateisystem mit 4GB Dateigrößenbeschränkung, kompatibel mit vielen Betriebssystemen|
|**exFAT (Extended FAT)**|Modernes FAT32-Nachfolgesystem ohne Größenbeschränkungen, ideal für USB-Laufwerke und SD-Karten|
|**Master File Table (MFT)**|Zentrale Datenstruktur in NTFS, die alle Dateien und Verzeichnisse katalogisiert|
|**Volume (Datenträger)**|Einzelner zugänglicher Speicherbereich mit eigenem Dateisystem, oft als Laufwerksbuchstabe (C:, D:) dargestellt|
|**Partition**|Logische Unterteilung einer physischen Festplatte; jede kann mit eigenem Dateisystem formatiert werden|
|**Formatierung**|Vorbereitung eines Laufwerks durch Löschen von Daten und Einrichtung eines Dateisystems|
|**HDD (Hard Disk Drive)**|Mechanische Festplatte mit rotierenden Magnetplatten, Speicherung in Sektoren und Spuren|
|**SSD (Solid State Drive)**|Flash-basiertes Speichermedium ohne bewegliche Teile, schneller und langlebiger als HDDs|
|**Fragmentierung**|Verteilung von Datei-Teilen über nicht zusammenhängende Blöcke, verlangsamt HDDs|
|**Journaling**|Dateisystem-Technik zur Protokollierung von Änderungen vor deren Ausführung für Crash-Recovery|
|**ACL (Access Control List)**|Liste von Berechtigungen, die festlegt, welche Benutzer/Gruppen welche Zugriffe auf Dateien haben|
|**Full-Disk Encryption (FDE)**|Verschlüsselung eines gesamten Laufwerks/Volumes für automatischen Schutz aller Daten|
|**TPM (Trusted Platform Module)**|Sicherheitschip zur Speicherung kryptografischer Schlüssel, oft für BitLocker verwendet|

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|**Datei**|Benannte Sammlung zusammengehöriger Informationen auf einem Speichermedium|
|**Verzeichnis/Ordner**|Container für Dateien und andere Verzeichnisse, ermöglicht hierarchische Organisation|
|**Pfad**|Zeichenkette zur eindeutigen Angabe des Speicherorts einer Datei im Dateisystem|
|**Absoluter Pfad**|Vollständiger Pfad vom Stamm (Root) des Dateisystems (z.B. C:\Users\Name\Documents\datei.txt)|
|**Relativer Pfad**|Pfad relativ zum aktuellen Arbeitsverzeichnis (z.B. Documents\datei.txt)|
|**Metadaten**|Informationen über Dateien: Name, Größe, Typ, Zeitstempel, Berechtigungen, Eigentümer|
|**Laufwerksbuchstabe**|Windows-Kennzeichnung für Volumes (C: = Systemlaufwerk, D:, E: = weitere Laufwerke)|
|**Backup**|Kopie von Daten an anderem Ort zur Wiederherstellung nach Verlust|
|**Vollständige Sicherung**|Backup aller ausgewählten Daten; einfache Wiederherstellung, hoher Speicherbedarf|
|**Inkrementelle Sicherung**|Backup nur der seit letztem Backup geänderten Daten; platzsparend, komplexe Wiederherstellung|
|**Differenzielle Sicherung**|Backup aller seit letzter Vollsicherung geänderten Daten; Kompromiss zwischen voll und inkrementell|
|**Verschlüsselung**|Umwandlung von Daten in unlesbares Format, nur mit Schlüssel entschlüsselbar|
|**NAS (Network Attached Storage)**|Zentraler Netzwerkspeicher für Backups und gemeinsame Dateinutzung|
|**Cloud-Speicher**|Online-Speicherdienste wie OneDrive, Google Drive für externe Backups|
|**Sektor**|Kleinste physische Speichereinheit auf HDDs (typisch 512 Bytes oder 4KB)|
|**Spur**|Konzentrischer Kreis auf HDD-Platte, auf dem Daten in Sektoren gespeichert werden|
|**NAND-Flash**|Speichertechnologie in SSDs, ermöglicht schnellen, nicht-flüchtigen Datenzugriff|
|**Schnellformat**|Formatierung, die nur Dateisystem-Strukturen erstellt; Daten bleiben wiederherstellbar|
|**Vollformat**|Formatierung mit Überschreiben aller Daten; sicherer, aber langsamer|

---

# Zusammenfassung nach dem 80/20-Prinzip

## Was ist ein Dateisystem?

Ein **Dateisystem** ist die grundlegende Organisationsstruktur, die ein Betriebssystem verwendet, um Daten auf Speichermedien zu verwalten. Es funktioniert wie ein Bibliothekar, der alle Informationen katalogisiert und auffindbar macht.

### Hauptfunktionen:

- **Organisation**: Gruppierung in Dateien und Ordner (hierarchische Struktur)
- **Benennung**: Vergabe aussagekräftiger Namen
- **Metadaten-Verwaltung**: Speicherung von Größe, Datum, Berechtigungen
- **Speicherplatzverwaltung**: Tracking freier und belegter Bereiche
- **Datenabruf**: Effizientes Lokalisieren und Zugreifen auf Daten
- **Integrität**: Schutz vor Datenverlust durch Journaling

## Die 3 wichtigsten Dateisysteme für Windows

|Dateisystem|Verwendung|Hauptmerkmale|
|---|---|---|
|**NTFS**|Windows-Systemlaufwerk (C:)|Journaling, Berechtigungen (ACLs), große Dateien, Verschlüsselung (EFS), MFT|
|**FAT32**|USB-Sticks, SD-Karten|Universelle Kompatibilität, **aber**: max. 4GB Dateigröße|
|**exFAT**|Große USB-Laufwerke, externe HDDs|Keine Größenbeschränkungen, gute Kompatibilität|

## Speichertechnologien

### HDD vs. SSD

|Aspekt|HDD (Hard Disk Drive)|SSD (Solid State Drive)|
|---|---|---|
|**Technologie**|Mechanisch, rotierende Magnetplatten|Elektronisch, Flash-Speicher (NAND)|
|**Geschwindigkeit**|Langsamer (Suchzeit erforderlich)|Sehr schnell (instant access)|
|**Lebensdauer**|Anfällig für mechanische Schäden|Langlebiger, keine beweglichen Teile|
|**Kosten**|Günstiger pro GB|Teurer pro GB|
|**Fragmentierung**|Problem (Defragmentierung nötig)|Kein Problem (nicht defragmentieren!)|

## Windows-Pfade und Struktur

- **Laufwerksbuchstaben**: C: (System), D:, E:, etc.
- **Wichtige Systemordner**:
    - `C:\Windows` - Betriebssystem-Dateien
    - `C:\Programme` - Installierte Anwendungen
    - `C:\Users\[Name]` - Benutzerdaten
    - `C:\Users\[Name]\Documents` - Dokumente
    - `C:\temp` - Temporäre Dateien

### Pfad-Beispiele:

- **Absolut**: `C:\Users\Max\Documents\report.docx`
- **Relativ**: `Documents\report.docx` (wenn in C:\Users\Max)

## Datenschutz: Die 2 Säulen

### 1. Backups - Schutz vor Datenverlust

**Warum wichtig?**

- Hardware-Ausfälle (Festplatten-Crash)
- Versehentliches Löschen
- Ransomware-Angriffe
- Datenbeschädigung

**Backup-Strategien:**

1. **Vollsicherung**
    
    - ✅ Alle Daten, einfache Wiederherstellung
    - ❌ Viel Speicherplatz, zeitaufwendig
2. **Inkrementelle Sicherung**
    
    - ✅ Nur Änderungen seit letztem Backup, platzsparend
    - ❌ Komplexe Wiederherstellung (braucht alle Backups)
3. **Differenzielle Sicherung**
    
    - ✅ Änderungen seit letzter Vollsicherung, schnellere Wiederherstellung
    - ❌ Wachsende Backup-Größe bis zur nächsten Vollsicherung

**Windows-Tools:**

- **Dateiverlauf**: Automatische Versionierung wichtiger Ordner
- **Sichern und Wiederherstellen**: Systemabbilder und Datensicherungen

**Speicherorte:**

- Externe Festplatten/SSDs
- NAS (Network Attached Storage)
- Cloud (OneDrive, Google Drive, Backblaze)

### 2. Verschlüsselung - Schutz vor unbefugtem Zugriff

**Zwei Verschlüsselungstypen:**

#### Full-Disk Encryption (FDE) - BitLocker

- Verschlüsselt **gesamte Laufwerke**
- Automatische Ver-/Entschlüsselung beim Zugriff
- Nutzt oft TPM-Chip für Sicherheit
- Ideal für: Laptops, tragbare Geräte
- ⚠️ Nur in Windows Pro/Enterprise verfügbar

#### Datei-/Ordner-Verschlüsselung - EFS

- Verschlüsselt **einzelne Dateien/Ordner** auf NTFS
- Gebunden an Benutzerkonto
- Ideal für: Spezifische sensible Daten, gemeinsam genutzte Systeme

**Warum Verschlüsselung?**

- ✅ Schutz bei Diebstahl/Verlust
- ✅ Compliance (DSGVO, HIPAA)
- ✅ Minimiert Datenschutzverletzungen

## Formatierung verstehen

**Was passiert beim Formatieren?**

- Dateisystem-Strukturen werden angelegt
- (Optional) Vorhandene Daten gelöscht
- Laufwerk wird nutzbar gemacht

**Formatierungstypen:**

- **Schnellformat**: Nur Dateisystem-Struktur, Daten wiederherstellbar
- **Vollformat**: Überschreibt Daten, sicherer

**Wann formatieren?**

- Neue Laufwerke vorbereiten
- Dateisystem wechseln (z.B. FAT32 → NTFS)
- Laufwerk komplett löschen
- Dateisystem-Fehler beheben

## Praktische Windows-Tools

### Datei-Explorer

- Navigation durch Dateisystem
- Dateieigenschaften anzeigen (Rechtsklick → Eigenschaften)
- Metadaten in Tab "Details"
- Berechtigungen in Tab "Sicherheit" (NTFS)

### Datenträgerverwaltung (diskmgmt.msc)

- Partitionen anzeigen und verwalten
- Laufwerke formatieren
- Laufwerksbuchstaben ändern
- ⚠️ Vorsicht: Falsche Nutzung führt zu Datenverlust!

## Wichtige Sicherheitsempfehlungen

1. **3-2-1-Backup-Regel**:
    
    - 3 Kopien der Daten
    - 2 verschiedene Medientypen
    - 1 Kopie extern (Cloud/anderer Standort)
2. **BitLocker aktivieren** auf Laptops und tragbaren Geräten
    
3. **Regelmäßige Backups** automatisieren
    
4. **Wiederherstellungsschlüssel sichern** bei Verschlüsselung
    
5. **Alte Laufwerke sicher löschen** vor Entsorgung (Vollformat oder Shredder-Software)
    

## Forensik-Relevanz

- **Gelöschte Dateien**: Oft wiederherstellbar, da nur Dateisystem-Einträge entfernt werden
- **Formatierung**: Standardformat löscht Daten nicht sicher
- **Metadaten**: Wichtige Spur für digitale Forensik (Zeitstempel, Besitzer)
- **Fragmentierung**: Kann auf HDD-Nutzungsmuster hinweisen

**Kernbotschaft**: Dateisysteme organisieren Daten strukturiert, Backups schützen vor Verlust, Verschlüsselung schützt vor unbefugtem Zugriff. Das Verständnis von Dateisystemen ist fundamental für Cybersecurity, Forensik und Systemadministration.