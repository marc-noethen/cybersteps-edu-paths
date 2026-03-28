# Kategorisierung der Themen

## Tabelle: Tools, Fachbegriffe und Vokabeln

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Local Security Policy (secpol.msc)|Windows-Tool zur Konfiguration von Sicherheitsrichtlinien auf lokalem Computer|
||Event Viewer (eventvwr.msc)|Anzeige und Analyse von System-, Sicherheits- und Anwendungsprotokollen|
||Services (services.msc)|Verwaltungskonsole für Windows-Hintergrunddienste|
||Windows Defender Firewall|Integrierte Host-basierte Firewall zur Netzwerkverkehrskontrolle|
||BitLocker Drive Encryption|Vollständige Festplattenverschlüsselung für Windows|
||EFS (Encrypting File System)|Dateisystem-Verschlüsselung auf Datei- und Ordnerebene|
||Programs and Features|Windows-Tool zur Deinstallation von Software|
||WSUS (Windows Server Update Services)|Zentrale Update-Verteilung in Unternehmensumgebungen|
||Microsoft Endpoint Configuration Manager|Enterprise-Tool für Patch-Verwaltung und Systemkonfiguration|
||Group Policy Editor|Zentrale Verwaltung von Sicherheitskonfigurationen in Domains|
||PowerShell|Automatisierung von Härtungsaufgaben und Security-Audits|
|**Technische Fachbegriffe**|OS Hardening (Systemhärtung)|Prozess der sicheren Konfiguration eines OS zur Reduzierung von Schwachstellen|
||Attack Surface (Angriffsfläche)|Summe aller potentiellen Schwachstellen, die Angreifer ausnutzen können|
||Principle of Least Privilege|Minimalprinzip: Nur notwendige Zugriffsrechte gewähren|
||Defense in Depth|Mehrschichtige Sicherheitsarchitektur mit redundanten Kontrollen|
||Patch Management|Systematischer Prozess für Identifikation, Test und Installation von Updates|
||Patch Tuesday|Zweiter Dienstag im Monat, an dem Microsoft regulär Updates veröffentlicht|
||Out-of-Band Patch|Außerplanmäßiges kritisches Sicherheitsupdate außerhalb des regulären Zyklus|
||UAC (User Account Control)|Sicherheitsfunktion zur Bestätigung administrativer Änderungen|
||NTFS Permissions|Dateisystem-Berechtigungen zur Zugriffskontrolle auf Dateien/Ordner|
||Host-Based Firewall|Firewall auf dem einzelnen System (nicht Netzwerk-Firewall)|
||Security Baseline|Dokumentierte Empfehlungen für sichere Systemkonfigurationen|
||CIS Benchmarks|Konsensbasierte Härtungsrichtlinien des Center for Internet Security|
||Microsoft Security Baselines|Offizielle Microsoft-Empfehlungen für sichere Konfigurationen|
||Whitelisting|Nur explizit erlaubte Anwendungen dürfen ausgeführt werden|
||Blacklisting|Explizit verbotene Anwendungen werden blockiert|
||Account Lockout|Kontosperrung nach mehreren fehlgeschlagenen Login-Versuchen|
||Audit Policy|Richtlinie zur Festlegung, welche Ereignisse protokolliert werden|
||Event ID|Eindeutige Kennzeichnung für spezifische Systemereignisse in Logs|
||Reverse Engineering|Analyse von Patches zur Identifikation der behobenen Schwachstelle|
|**Wichtige Vokabeln**|Vulnerability (Schwachstelle)|Sicherheitslücke, die von Angreifern ausgenutzt werden kann|
||Exploit|Ausnutzung einer Schwachstelle für Angriffe|
||Default Configuration|Standardkonfiguration, oft nicht sicherheitsoptimiert|
||Secure Configuration|Sicherheitsorientierte Anpassung von Systemeinstellungen|
||Service Dependencies|Abhängigkeiten zwischen Windows-Diensten|
||Password Complexity|Anforderungen an Passwortstruktur (Länge, Zeichen, Komplexität)|
||Password Reuse Prevention|Verhinderung der Wiederverwendung alter Passwörter|
||Default Account|Vorkonfigurierte Systemkonten wie Administrator oder Guest|
||Elevated Privileges|Erhöhte Berechtigungen für administrative Aufgaben|
||Brute-Force Attack|Angriff durch systematisches Durchprobieren von Passwörtern|
||Security Log|Protokolldatei für sicherheitsrelevante Ereignisse|
||System Log|Protokolldatei für Betriebssystem-Ereignisse|
||Application Log|Protokolldatei für Anwendungsereignisse|
||Event ID 4624|Ereignis-Code für erfolgreichen Login|
||Event ID 4625|Ereignis-Code für fehlgeschlagenen Login|
||Logging Noise|Übermäßige Protokollierung unwichtiger Ereignisse|
||Attack Vector|Weg oder Methode, über den ein Angriff erfolgt|
||Proactive Security|Vorbeugende Sicherheitsmaßnahmen vor einem Angriff|
||Reactive Security|Reaktive Maßnahmen nach erkannten Angriffen|
||Compliance|Einhaltung von Sicherheitsrichtlinien und Standards|
||Network Protocol|Kommunikationsstandard für Netzwerkverbindungen|
||Firewall Rules|Regelwerk zur Steuerung von ein- und ausgehendem Netzwerkverkehr|
||Port|Netzwerk-Endpunkt für spezifische Dienste (z.B. Port 80 für HTTP)|

---

## Zusammenfassung nach dem 80/20-Prinzip

**Kernaussage:** OS-Härtung ist die proaktive, systematische Reduzierung der Angriffsfläche durch sichere Konfiguration, minimale Berechtigungen und kontinuierliches Patch-Management.

**Die wichtigsten 20% der Informationen:**

### 1. Was ist OS-Härtung?

**Definition:** Prozess der sicheren Konfiguration eines Betriebssystems zur Minimierung von Schwachstellen und Angriffspunkten.

**Kernkonzept:** Wie eine Festung befestigen – Eingangspunkte reduzieren, Verteidigungen stärken, Angriffsversuche erkennbar machen.

**Philosophie:**

- **Proaktiv** statt reaktiv: System vor Angriffen schwer kompromittierbar machen
- **Defense in Depth**: Mehrere Sicherheitsschichten implementieren
- **Attack Surface Reduction**: Alles Unnötige entfernen oder deaktivieren

### 2. Die 5 Kernprinzipien der Härtung

**1. Principle of Least Privilege (Minimalprinzip):**

- Benutzer/Prozesse erhalten nur minimal notwendige Rechte
- Kompromittierte Accounts mit wenigen Rechten = geringer Schaden
- Beispiel: Normaler Benutzer-Account für Alltag, Admin nur wenn nötig

**2. Attack Surface Reduction:**

- Unnötige Software, Dienste, Accounts, Netzwerk-Ports entfernen
- Jede aktive Komponente = potentieller Angriffspunkt
- Wenn nicht benötigt → deaktivieren oder löschen

**3. Secure Configuration:**

- Standard-Einstellungen sind oft unsicher
- Konfigurationen nach Best Practices anpassen
- Security Baselines nutzen (CIS Benchmarks, Microsoft Security Baselines)

**4. Patch Management:**

- Systematisches Identifizieren, Testen und Installieren von Updates
- Schließt bekannte Sicherheitslücken
- Zeitnahe Installation kritisch (Angreifer analysieren Patches)

**5. Logging und Monitoring:**

- Umfassende Protokollierung von Systemereignissen
- Ermöglicht Erkennung verdächtiger Aktivitäten
- Basis für Incident Investigation

### 3. Praktische Härtungsbereiche in Windows 11

**User Account Management:**

- **Starke Passwortrichtlinien**: Komplexität, Länge, regelmäßiger Wechsel
- **Default-Accounts sichern**: Administrator umbenennen, Guest deaktivieren
- **UAC aktiviert lassen**: Verhindert unberechtigte administrative Änderungen
- **Account Lockout Policy**: Schutz vor Brute-Force-Angriffen

**Software Management:**

- Unnötige Anwendungen deinstallieren
- Alle Software aktuell halten (nicht nur OS)
- Application Control: Whitelisting von erlaubten Programmen

**Service Management:**

- Unnötige Hintergrunddienste deaktivieren
- Beispiel: Print Spooler auf Nicht-Druckserver
- **Vorsicht**: Service-Abhängigkeiten beachten

**Patch Management - Der kritische Prozess:**

1. **Identification**: Welche Systeme/Software sind betroffen?
2. **Acquisition**: Patches von Hersteller herunterladen
3. **Testing**: Erst auf Test-Systemen prüfen
4. **Deployment**: Ausrollen (manuell oder automatisiert via WSUS)
5. **Verification**: Installation bestätigen

**Patch Tuesday**: Zweiter Dienstag im Monat = regulärer Microsoft-Update-Tag

### 4. Netzwerk- und Dateisystem-Sicherheit

**Network Security:**

- **Windows Defender Firewall**: Nur notwendige Verbindungen erlauben
- Firewall-Regeln konfigurieren (z.B. Webserver: Port 80/443 offen)
- Veraltete Netzwerkprotokolle deaktivieren

**File System Security:**

- **NTFS-Berechtigungen**: Least Privilege auf Datei-/Ordnerebene
- **BitLocker**: Vollverschlüsselung der Festplatte (Schutz bei Diebstahl)
- **EFS**: Verschlüsselung einzelner Dateien/Ordner pro Benutzer

### 5. Security Policies & Logging (Windows 11)

**Local Security Policy (secpol.msc):**

- Password Policy: Passwortanforderungen definieren
- Account Lockout Policy: z.B. nach 5 Fehlversuchen sperren
- Audit Policy: Welche Ereignisse werden protokolliert?

**Event Viewer (eventvwr.msc) - Drei kritische Logs:**

- **Security Log**: Login-Versuche, Datei-Zugriffe, Audit-Events
- **System Log**: OS-Ereignisse, Dienste, Treiber
- **Application Log**: Anwendungsereignisse

**Wichtige Event IDs:**

- **4624**: Erfolgreicher Login
- **4625**: Fehlgeschlagener Login (möglicher Angriff)

### 6. Tools und Standards

**Eingebaute Windows-Tools:**

- Local Security Policy, Services, Event Viewer
- Windows Defender Firewall, BitLocker
- Programs and Features (Software-Deinstallation)

**Security Baselines:**

- **Microsoft Security Baselines**: Offizielle Empfehlungen
- **CIS Benchmarks**: Industrie-Standard, konsensbasiert, detailliert

**Warum Baselines nutzen?**

- Bewährte Konfigurationen
- Expertenwissen gebündelt
- Compliance-Anforderungen erfüllen

### Kritische Erfolgsfaktoren

**Testing vor Deployment:**

- Patches können Probleme verursachen
- Erst auf nicht-kritischen Systemen testen
- Dann produktiv ausrollen

**Balance finden:**

- Zu wenig Härtung = Angreifbar
- Zu viel Härtung = System unbenutzbar
- Ziel: Maximum an Sicherheit bei akzeptabler Usability

**Zeitkritische Patching:**

- Angreifer reverse-engineeren Patches → finden Schwachstelle
- Exploit ungepatschter Systeme
- Schnelles Patching = weniger Zeitfenster für Angreifer