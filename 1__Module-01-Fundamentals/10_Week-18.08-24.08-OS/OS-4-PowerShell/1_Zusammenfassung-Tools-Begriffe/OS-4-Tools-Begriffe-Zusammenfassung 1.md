Ich erstelle für Sie eine strukturierte Kategorisierung der PowerShell-Einführung auf Deutsch mit den wichtigsten Informationen für Windows 11.

## Kategorisierung der Themen

|**Kategorie**|**Bedeutung**|
|---|---|
|**Verwendete Tools**||
|PowerShell|Plattformübergreifende Automatisierungslösung mit Befehlszeilen-Shell, Skriptsprache und Konfigurations-Framework von Microsoft|
|PowerShell ISE|Integrierte Skripting-Umgebung für Windows zum Schreiben und Testen von PowerShell-Skripten|
|Visual Studio Code|Moderner Code-Editor mit ausgezeichneter PowerShell-Unterstützung für die Entwicklung|
|Windows PowerShell|Die auf Windows vorinstallierte Version von PowerShell (ab Windows 7 SP1)|
|.NET Framework|Grundlage von PowerShell, ermöglicht die Arbeit mit Objekten statt reinem Text|
|**Technische Fachbegriffe**||
|Cmdlets|Leichtgewichtige Befehle in PowerShell, die eine bestimmte Funktion ausführen (Verb-Nomen-Syntax)|
|Pipeline (`\|`)|Mechanismus zum Weiterleiten der Ausgabe (Objekte) eines Cmdlets als Eingabe für ein anderes|
|Objekte|Strukturierte Dateneinheiten mit Eigenschaften (Properties) und Methoden, nicht nur Text|
|Parameter|Optionen, die das Verhalten von Cmdlets modifizieren (mit `-` Präfix)|
|Variablen|Datenspeicher in PowerShell, beginnen immer mit `$` (z.B. `$myName`)|
|Execution Policy|Sicherheitsfunktion, die steuert, ob und welche Skripte ausgeführt werden können|
|Aliases|Kurzbefehle für häufig verwendete Cmdlets (z.B. `dir` für `Get-ChildItem`)|
|Properties|Eigenschaften/Charakteristika eines Objekts (z.B. ProcessName, CPU, Status)|
|Methods|Aktionen, die ein Objekt ausführen kann|
|`$_`|Spezielle Variable, die auf das aktuelle Objekt in der Pipeline verweist|
|**Wichtige Vokabeln (Verb-Nomen-Cmdlets)**||
|Get-Process|Ruft eine Liste der aktuell laufenden Prozesse ab|
|Get-Service|Ruft Informationen über Windows-Dienste ab|
|Get-Help|Zeigt Hilfeinformationen zu Cmdlets und Konzepten an|
|Get-Command|Listet alle verfügbaren Befehle auf|
|Get-ChildItem|Listet Dateien und Verzeichnisse auf (Alias: `dir`, `ls`)|
|Set-Location|Wechselt das aktuelle Arbeitsverzeichnis (Alias: `cd`)|
|Get-Location|Zeigt den aktuellen Verzeichnispfad an (Alias: `pwd`)|
|Sort-Object|Sortiert Objekte nach einer bestimmten Eigenschaft|
|Where-Object|Filtert Objekte basierend auf Bedingungen|
|Select-Object|Wählt bestimmte Eigenschaften von Objekten aus (Alias: `select`)|
|Start-Service|Startet einen angegebenen Dienst|
|Stop-Process|Beendet einen laufenden Prozess|
|Clear-Host|Löscht den Bildschirminhalt (Alias: `cls`)|
|Update-Help|Aktualisiert die Hilfedateien (benötigt Administrator-Rechte)|
|Get-ExecutionPolicy|Zeigt die aktuelle Ausführungsrichtlinie an|
|Set-ExecutionPolicy|Ändert die Ausführungsrichtlinie für Skripte|
|Get-Alias|Zeigt an, wofür ein Alias steht|

---

## Zusammenfassung nach dem 80/20-Prinzip

**PowerShell: Die essentiellen 20% für 80% des Verständnisses**

### Was ist PowerShell?

PowerShell ist Microsofts moderne Automatisierungslösung für Windows 11 (und andere Plattformen). Der entscheidende Unterschied zu herkömmlichen Shells: **PowerShell arbeitet mit Objekten statt mit reinem Text**. Dies ermöglicht deutlich elegantere und mächtigere Automatisierung.

### Die wichtigsten Konzepte:

**1. Cmdlets (Verb-Nomen-Struktur)**

- Alle Befehle folgen dem Muster: `Verb-Nomen` (z.B. `Get-Process`, `Set-Location`)
- Die häufigsten Verben: `Get` (abrufen), `Set` (setzen), `Start`/`Stop` (starten/stoppen), `New`/`Remove` (erstellen/entfernen)

**2. Pipeline (`|`)**

- Verbindet Befehle und übergibt Objekte (nicht Text!) zwischen ihnen
- Beispiel: `Get-Process | Sort-Object CPU -Descending` sortiert Prozesse nach CPU-Auslastung

**3. Objekte statt Text**

- Jede Ausgabe ist ein strukturiertes Objekt mit Eigenschaften und Methoden
- Dadurch entfällt mühsames Text-Parsing – Sie greifen direkt auf Eigenschaften zu

**4. Variablen**

- Beginnen immer mit `$` (z.B. `$prozesse = Get-Process`)
- Speichern Werte, Objekte oder ganze Sammlungen für die Weiterverwendung

### Die 5 wichtigsten Cmdlets für den Start:

1. **`Get-Help`** – Ihr wichtigstes Werkzeug zum Lernen (Parameter: `-Examples`, `-Detailed`, `-Online`)
2. **`Get-Command`** – Findet verfügbare Befehle
3. **`Get-Process`** – Zeigt laufende Prozesse
4. **`Get-Service`** – Zeigt Windows-Dienste
5. **`Get-ChildItem`** – Listet Dateien/Ordner (wie `dir` oder `ls`)

### Kritisch für Windows 11: Execution Policy

Bevor Sie Skripte (`.ps1`-Dateien) ausführen können, müssen Sie die Ausführungsrichtlinie anpassen:

1. PowerShell **als Administrator** öffnen
2. Befehl ausführen: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Mit `Y` bestätigen

**RemoteSigned** bedeutet: Ihre eigenen Skripte laufen, heruntergeladene Skripte müssen signiert sein – ein guter Sicherheitskompromiss für das Lernen.

### Warum PowerShell in der Cybersecurity wichtig ist:

- **Incident Response**: Schnelle Datenerfassung auf kompromittierten Systemen
- **Forensik**: Zugriff auf Event Logs, Registry, Dienste
- **Penetration Testing**: Angreifer nutzen PowerShell – Sie müssen es verstehen, um zu verteidigen
- **Automatisierung**: Security-Checks, Compliance-Berichte, Remediation-Aufgaben

### Sofort-Einstieg in der Konsole:

```
Get-Location              # Wo bin ich?
Set-Location C:\          # Navigation
Get-ChildItem             # Was ist hier?
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10  # Top 10 Prozesse
Get-Help Get-Process -Examples  # Wie funktioniert ein Befehl?
```

**Merksatz**: PowerShell = Objekte + Pipeline + Verb-Nomen + `Get-Help` ist Ihr Freund!