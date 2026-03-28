# Permissions, Authentication & Users in Windows - Kategorisierung

## Verwendete Tools

|Tool|Bedeutung|
|---|---|
|**Computer Management (compmgmt.msc)**|Zentrale Verwaltungskonsole für lokale Benutzer, Gruppen, Dienste und Systemressourcen|
|**Local Users and Groups**|Verwaltung von Benutzerkonten und Gruppen auf einem lokalen Windows-System|
|**File Explorer Security Tab**|Zeigt und verwaltet NTFS-Berechtigungen für Dateien und Ordner|
|**User Account Control (UAC)**|Sicherheitsfunktion, die administrative Aktionen durch Bestätigung schützt|
|**Windows Hello**|Biometrisches Authentifizierungssystem von Microsoft (Gesichtserkennung, Fingerabdruck)|
|**Security Account Manager (SAM)**|Datenbank, die lokale Benutzerkonten und Passwörter speichert|
|**Active Directory**|Zentrales Verzeichnis zur Verwaltung von Benutzern und Ressourcen in Netzwerkumgebungen|
|**Properties Dialog (Eigenschaften)**|Fenster zur Anzeige und Bearbeitung von Datei-/Ordnerattributen und Berechtigungen|
|**Advanced Security Settings**|Detaillierte Ansicht von Berechtigungen, Vererbung und Besitzverhältnissen|

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|**User Account (Benutzerkonto)**|Sammlung von Informationen, die Identität, Berechtigungen und Einstellungen eines Benutzers definiert|
|**Administrator Account**|Benutzerkonto mit vollständiger Kontrolle über das System und alle Ressourcen|
|**Standard User Account**|Benutzerkonto mit eingeschränkten Rechten, das keine systemweiten Änderungen vornehmen kann|
|**User Groups (Benutzergruppen)**|Sammlung von Benutzerkonten zur vereinfachten Rechteverwaltung|
|**Authentication (Authentifizierung)**|Prozess der Identitätsüberprüfung eines Benutzers, Prozesses oder Geräts|
|**Authorization (Autorisierung)**|Bestimmung, welche Aktionen ein authentifizierter Benutzer ausführen darf|
|**Permissions (Berechtigungen)**|Regeln, die festlegen, welche Aktionen auf Ressourcen erlaubt oder verboten sind|
|**NTFS Permissions**|Dateisystem-Berechtigungen des NT File Systems für granulare Zugriffskontrolle|
|**Allow/Deny (Erlauben/Verweigern)**|Berechtigungstypen, wobei "Deny" normalerweise "Allow" überschreibt|
|**Ownership (Besitz)**|Der Besitzer einer Ressource kann deren Berechtigungen immer ändern|
|**Principle of Least Privilege**|Sicherheitsprinzip: Benutzer erhalten nur minimal notwendige Zugriffsrechte|
|**Multi-Factor Authentication (MFA)**|Authentifizierung mit zwei oder mehr verschiedenen Faktoren (Wissen, Besitz, Biometrie)|
|**Inheritance (Vererbung)**|Weitergabe von Berechtigungen von übergeordneten auf untergeordnete Objekte|
|**Token (Zugriffstoken)**|Datenstruktur mit Benutzeridentität und Berechtigungen für Zugriffsentscheidungen|
|**Elevation (Rechteerweiterung)**|Temporäre Erhöhung von Berechtigungen für administrative Aufgaben|
|**SYSTEM Account**|Internes Windows-Konto mit höchsten Privilegien für Systemdienste|

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|**Full Control (Vollzugriff)**|Höchste Berechtigungsstufe mit allen Rechten inklusive Löschen und Besitzübernahme|
|**Modify (Ändern)**|Berechtigung zum Lesen, Schreiben, Ändern, Ausführen und Löschen|
|**Read & Execute (Lesen & Ausführen)**|Berechtigung zum Anzeigen und Ausführen von Dateien|
|**List Folder Contents**|Berechtigung zum Anzeigen von Datei- und Ordnernamen ohne Zugriff auf Inhalte|
|**Read (Lesen)**|Berechtigung zum Öffnen und Anzeigen von Dateien und Attributen|
|**Write (Schreiben)**|Berechtigung zum Erstellen neuer Dateien und Schreiben in bestehende|
|**Credentials (Anmeldedaten)**|Benutzername und Passwort oder andere Authentifizierungsinformationen|
|**Biometrics (Biometrie)**|Authentifizierung durch einzigartige physische Merkmale (Fingerabdruck, Gesicht)|
|**PIN (Personal Identification Number)**|Kurze numerische Kennung zur gerätegebundenen Authentifizierung|
|**Smart Card (Chipkarte)**|Physisches Gerät zur sicheren Authentifizierung|
|**Taking Ownership (Besitzübernahme)**|Administratives Recht, Besitz einer Ressource zu übernehmen|
|**Filtered Token**|Eingeschränkter Zugriffstoken für Administratoren im Standardmodus|
|**Security Principal**|Entität (Benutzer, Gruppe, Computer), der Berechtigungen zugewiesen werden können|
|**Remote Desktop**|Fernzugriff auf einen Windows-Computer über Netzwerk|
|**Backup Operators**|Gruppe mit Rechten zum Sichern und Wiederherstellen von Dateien|

---

# Zusammenfassung nach dem 80/20-Prinzip

## Die wichtigsten 20% des Wissens für 80% der Anwendungsfälle

### Drei Säulen der Zugriffssicherheit

Die Windows-Sicherheit basiert auf drei grundlegenden Konzepten:

1. **Users (Benutzer)** - Wer bist du?
2. **Authentication (Authentifizierung)** - Kannst du beweisen, wer du bist?
3. **Permissions (Berechtigungen)** - Was darfst du tun?

### Benutzerkonten: Die zwei wichtigsten Typen

**1. Administrator-Konto**

- **Rechte:** Vollständige Kontrolle über das System
- **Kann:** Software installieren, Systemeinstellungen ändern, alle Dateien zugreifen, andere Konten verwalten
- **Risiko:** Malware mit Admin-Rechten hat volle Systemkontrolle
- **Empfehlung:** NICHT für tägliche Aufgaben verwenden

**2. Standard-Benutzerkonto**

- **Rechte:** Eingeschränkte Privilegien
- **Kann:** Programme ausführen, eigene Dateien verwalten, persönliche Einstellungen ändern
- **Kann NICHT:** Systemweite Änderungen vornehmen, Software installieren (ohne Admin-Passwort)
- **Empfehlung:** Für tägliche Nutzung (Internet, E-Mail, Office)

**Wichtige System-Konten:**

- `SYSTEM` - Höchste Privilegien für Windows-Dienste
- `Local Service` / `Network Service` - Für Hintergrunddienste

### Benutzergruppen: Effiziente Rechteverwaltung

**Warum Gruppen?** Statt jedem Benutzer einzeln Rechte zu geben, weisen Sie Rechte einer Gruppe zu und fügen Benutzer hinzu.

**Die 5 wichtigsten Standard-Gruppen:**

|Gruppe|Berechtigungen|Typische Verwendung|
|---|---|---|
|**Administrators**|Vollzugriff auf alles|IT-Administratoren|
|**Users**|Standard-Berechtigungen|Normale Mitarbeiter|
|**Guests**|Sehr eingeschränkt (oft deaktiviert)|Temporäre Besucher|
|**Backup Operators**|Datensicherung trotz fehlender Dateiberechtigungen|Backup-Software|
|**Remote Desktop Users**|Fernzugriff auf Computer|Externe Mitarbeiter|

**Zugriff:** `Win + R` → `compmgmt.msc` → System Tools → Local Users and Groups → Groups

### Authentifizierung: Identität beweisen

**Die 5 Hauptmethoden:**

1. **Passwort** - Etwas, das Sie **wissen**
    
    - Am häufigsten verwendet
    - Sollte lang, komplex und einzigartig sein
2. **PIN** - Etwas, das Sie **wissen** (gerätegebunden)
    
    - Kürzer als Passwort
    - An spezifisches Gerät gebunden
3. **Biometrie** - Etwas, das Sie **sind**
    
    - Fingerabdruck, Gesichtserkennung (Windows Hello)
    - Einzigartige physische Merkmale
4. **Smart Card/Security Key** - Etwas, das Sie **haben**
    
    - Physisches Gerät zur Authentifizierung
    - Oft in Unternehmen
5. **Multi-Faktor-Authentifizierung (MFA)** - Kombination
    
    - Mindestens 2 verschiedene Faktoren
    - Beispiel: Passwort + Code vom Smartphone
    - **Deutlich sicherer** als einzelne Methode

**Technischer Hintergrund:**

- Lokale Anmeldung: Vergleich mit **SAM-Datenbank** (Security Account Manager)
- Netzwerk-Anmeldung: Vergleich mit **Active Directory**

### NTFS-Berechtigungen: Kontrolle über Dateien und Ordner

**Die 6 Standard-Berechtigungen (nach Umfang sortiert):**

|Berechtigung|Was erlaubt ist|
|---|---|
|**Full Control**|Alles: Lesen, Schreiben, Ändern, Löschen, Berechtigungen ändern, Besitz übernehmen|
|**Modify**|Lesen, Schreiben, Ändern, Ausführen, Löschen|
|**Read & Execute**|Anzeigen, Lesen, Ausführen von Programmen|
|**List Folder Contents**|Nur Datei-/Ordnernamen sehen (nicht öffnen)|
|**Read**|Dateien öffnen und Eigenschaften anzeigen|
|**Write**|Neue Dateien erstellen und in bestehende schreiben|

**Berechtigungen überprüfen:**

1. Rechtsklick auf Datei/Ordner → Eigenschaften
2. Tab "Sicherheit"
3. Benutzer/Gruppe auswählen → Berechtigungen anzeigen

**KRITISCHE REGEL: Deny schlägt Allow**

- Wenn ein Benutzer in Gruppe A "Allow" und in Gruppe B "Deny" hat → **Zugriff verweigert**
- Wichtig für Troubleshooting bei Zugriffsproblemen

### Besitz (Ownership): Der ultimative Trumpf

**Was ist Besitz?**

- Jede Datei/Ordner hat einen Besitzer (normalerweise der Ersteller)
- Der Besitzer kann **IMMER** die Berechtigungen ändern
- Selbst wenn alle anderen Rechte verweigert wurden

**Besitzübernahme (Taking Ownership):**

- Administratives Recht
- Ermöglicht Zugriff auf fremde Dateien bei Berechtigungsproblemen
- Findet sich unter: Eigenschaften → Sicherheit → Erweitert → Besitzer

### Das Prinzip der geringsten Rechte (Principle of Least Privilege)

**Kernaussage:** Gewähren Sie nur die **minimal notwendigen** Berechtigungen.

**Beispiele:**

- ❌ FALSCH: Alle Mitarbeiter als Administratoren
    
- ✅ RICHTIG: Standard-Konten + Admin-Passwort bei Bedarf
    
- ❌ FALSCH: Praktikant mit Vollzugriff auf Finanzordner
    
- ✅ RICHTIG: Praktikant mit Lesezugriff auf relevante Dokumente
    

**Vorteile:**

- Weniger Schaden bei kompromittierten Konten
- Schutz vor versehentlichen Änderungen
- Bessere Compliance und Nachvollziehbarkeit

### User Account Control (UAC): Der Schutzengel

**Was macht UAC?**

- Dimmt Bildschirm und fragt nach Bestätigung bei administrativen Aktionen
- Verhindert, dass Programme heimlich Admin-Rechte erhalten
- Gilt auch für Administrator-Konten (!)

**Wie funktioniert es?**

1. Administrator meldet sich an
2. Programme laufen mit **Standard-Rechten** (filtered token)
3. Bei Admin-Aktion → UAC-Prompt
4. Nach Bestätigung → Temporäre **Elevation** (Rechteerweiterung)

**Typische UAC-Trigger:**

- Software-Installation
- Systemeinstellungen ändern
- Treiber installieren
- Dateien in System-Ordnern ändern

### Praktische Anwendungsfälle

**Szenario 1: Software installieren als Standard-User**

1. Installationsdatei doppelklicken
2. UAC fordert Administrator-Passwort
3. Admin-Passwort eingeben
4. Installation läuft mit Admin-Rechten

**Szenario 2: Zugriff auf gemeinsamen Ordner verweigert**

1. Eigenschaften → Sicherheit prüfen
2. Ist der Benutzer/Gruppe aufgelistet?
3. Gibt es ein "Deny"? (überschreibt "Allow"!)
4. Berechtigungen entsprechend anpassen

**Szenario 3: MFA für kritische Systeme einrichten**

1. Passwort (Wissen) allein ist nicht sicher genug
2. Zusätzlich: Authenticator-App (Besitz) oder Biometrie (Sein)
3. Deutlich höherer Schutz gegen Hacking

### Die wichtigsten Takeaways

✅ **Standard-Konten für Alltag, Administrator nur bei Bedarf** ✅ **Gruppen verwenden statt einzelne Benutzer-Berechtigungen** ✅ **MFA aktivieren für sensible Accounts (E-Mail, Banking)** ✅ **Principle of Least Privilege: So wenig Rechte wie möglich** ✅ **Deny überschreibt Allow - wichtig bei Troubleshooting** ✅ **UAC nicht ignorieren - es schützt vor Malware** ✅ **Besitzer kann immer Berechtigungen ändern**

Diese 20% des Wissens decken die wichtigsten Konzepte ab, die für 80% der täglichen Aufgaben und Sicherheitsentscheidungen in Windows benötigt werden.