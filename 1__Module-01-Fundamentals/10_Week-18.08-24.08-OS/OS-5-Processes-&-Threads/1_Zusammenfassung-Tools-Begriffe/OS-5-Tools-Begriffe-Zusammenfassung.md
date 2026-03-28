# Kategorisierung der Themen

## Verwendete Tools

|Tool/Anwendung|Bedeutung|
|---|---|
|**Task Manager** (Aufgabe-Manager)|Zeigt alle laufenden Prozesse, deren Ressourcennutzung und ermöglicht das Beenden von Prozessen (Strg+Shift+Esc)|
|**PowerShell**|Befehlszeilenschnittstelle für erweiterte Systemverwaltung und Prozessanalyse|
|**Get-Process** (PowerShell-Befehl)|Listet alle aktuell laufenden Prozesse mit Details wie Name, ID, CPU- und Speichernutzung auf|
|**Details Tab** (Task Manager)|Detaillierte Ansicht aller Prozesse mit technischen Informationen wie Prozess-ID (PID) und Speicherverbrauch|
|**Processes Tab** (Task Manager)|Vereinfachte Übersicht der laufenden Anwendungen und Hintergrundprozesse mit Ressourcennutzung|

## Technische Fachbegriffe

|Begriff|Bedeutung|
|---|---|
|**Programm**|Passive Einheit - eine ausführbare Datei auf der Festplatte (z.B. notepad.exe), die Anweisungen und Daten enthält|
|**Prozess**|Aktive Ausführung eines Programms im Speicher mit eigenen Ressourcen und eigenem Speicherbereich|
|**Thread**|Kleinste Ausführungseinheit innerhalb eines Prozesses; mehrere Threads können innerhalb eines Prozesses parallel arbeiten|
|**Scheduler**|OS-Komponente, die entscheidet, welcher Prozess/Thread als nächstes CPU-Zeit erhält|
|**Multitasking**|Fähigkeit des OS, mehrere Prozesse scheinbar gleichzeitig auszuführen durch schnelles Umschalten|
|**Concurrency (Nebenläufigkeit)**|Mehrere Aufgaben machen Fortschritte im gleichen Zeitraum, aber nicht unbedingt gleichzeitig|
|**Program Counter**|Register, das die Adresse der nächsten auszuführenden Instruktion speichert|
|**Register Set**|Kleine, schnelle Speicherbereiche in der CPU für temporäre Daten während der Ausführung|
|**Address Space (Adressraum)**|Der dem Prozess zugewiesene Speicherbereich, in dem Code und Daten liegen|
|**Multi-core Processor**|Prozessor mit mehreren Rechenkernen, die echte parallele Ausführung ermöglichen|
|**Single-threaded**|Prozess mit nur einem Ausführungsstrang, der Aufgaben nacheinander abarbeitet|
|**Multi-threaded**|Prozess mit mehreren Ausführungssträngen, die parallel arbeiten können|
|**Context Switch**|Wechsel der CPU von einem Prozess/Thread zu einem anderen durch Speichern/Laden des Zustands|

## Wichtige Vokabeln

|Vokabel|Bedeutung|
|---|---|
|**Process States (Prozesszustände)**|Die verschiedenen Zustände, die ein Prozess durchläuft (New, Ready, Running, Waiting, Terminated)|
|**New (Neu)**|Prozess wird gerade erstellt, Ressourcen werden zugewiesen|
|**Ready (Bereit)**|Prozess hat alle Ressourcen und wartet auf CPU-Zuteilung|
|**Running (Laufend)**|Prozess wird aktuell von der CPU ausgeführt|
|**Waiting/Blocked (Wartend/Blockiert)**|Prozess wartet auf externes Ereignis (I/O, Benutzereingabe) und kann nicht fortfahren|
|**Terminated (Beendet)**|Prozess hat Ausführung abgeschlossen, Ressourcen werden freigegeben|
|**Responsiveness (Reaktionsfähigkeit)**|Fähigkeit einer Anwendung, schnell auf Benutzereingaben zu reagieren|
|**Resource Sharing (Ressourcenteilung)**|Threads innerhalb eines Prozesses teilen Speicher und andere Ressourcen|
|**Scalability (Skalierbarkeit)**|Fähigkeit, Leistung durch Nutzung mehrerer CPU-Kerne zu steigern|
|**Lightweight (Leichtgewichtig)**|Threads sind ressourcenschonender zu erstellen und verwalten als Prozesse|
|**Independent Execution (Unabhängige Ausführung)**|Jeder Thread kann eigenständig Aufgaben ausführen|
|**Memory Space (Speicherbereich)**|Der einem Prozess zugewiesene RAM-Bereich für Code, Daten und Stack|
|**Overhead**|Zusätzlicher Ressourcenaufwand für Verwaltungsaufgaben des Betriebssystems|
|**Synchronization (Synchronisierung)**|Koordination zwischen Threads, um Konflikte beim Zugriff auf gemeinsame Ressourcen zu vermeiden|
|**I/O Completion (E/A-Abschluss)**|Beendigung einer Ein-/Ausgabeoperation (z.B. Datei gelesen, Download beendet)|

---

# Zusammenfassung nach dem 80/20-Prinzip

## Grundkonzepte

### Programm vs. Prozess

- **Programm**: Eine passive Datei auf der Festplatte (z.B. `chrome.exe`) - wie ein Rezept in einem Kochbuch
- **Prozess**: Ein aktiv laufendes Programm im Speicher - wie ein Koch, der das Rezept tatsächlich kocht
- Jeder Prozess hat eigenen Speicherbereich, eigene Ressourcen und läuft unabhängig von anderen Prozessen

### Die 5 Prozesszustände

Ein Prozess durchläuft folgende Zustände:

1. **New**: Wird gerade erstellt
2. **Ready**: Wartet auf CPU-Zeit (in der Warteschlange)
3. **Running**: Wird aktuell ausgeführt
4. **Waiting**: Wartet auf Ereignis (z.B. Datei-Download, Benutzereingabe)
5. **Terminated**: Beendet, Ressourcen werden freigegeben

Der **Scheduler** des OS entscheidet, welcher "Ready"-Prozess als nächstes läuft. Durch schnelles Umschalten entsteht der Eindruck von **Multitasking**.

## Was sind Threads?

**Threads** sind die kleinste Ausführungseinheit innerhalb eines Prozesses:

- **Ein Prozess** = Eine Küche (Container mit Ressourcen)
- **Threads** = Mehrere Köche in derselben Küche (Arbeiter, die parallel arbeiten)

### Hauptmerkmale von Threads

1. **Leichtgewichtig**: Schneller zu erstellen als neue Prozesse
2. **Ressourcenteilung**: Teilen sich Speicher, Code und Dateien des Prozesses
3. **Unabhängige Ausführung**: Jeder Thread hat eigenen Programmzähler und Register

### Warum Threads verwenden?

1. **Reaktionsfähigkeit**: UI bleibt responsiv, während im Hintergrund Aufgaben laufen
    
    - Beispiel: Webbrowser lädt Seite, während du weiter scrollen/klicken kannst
2. **Effizienz**: Keine Prozess-Overhead, da Ressourcen geteilt werden
    
3. **Skalierbarkeit**: Auf Multi-Core-CPUs können Threads echt parallel laufen
    

## Praktisches Beispiel: Webbrowser

Ein Browser-Prozess könnte folgende Threads haben:

- **Thread 1**: Rendert die Webseite
- **Thread 2**: Lädt Bilder herunter
- **Thread 3**: Reagiert auf Mausbewegungen/Klicks
- **Thread 4**: Führt JavaScript aus

Alle arbeiten parallel innerhalb desselben Browser-Prozesses!

## Prozesse vs. Threads im Vergleich

|Aspekt|Prozess|Thread|
|---|---|---|
|**Speicher**|Eigener, isolierter Speicherbereich|Teilt Speicher mit anderen Threads im Prozess|
|**Erstellung**|Ressourcenintensiv, langsam|Leichtgewichtig, schnell|
|**Kommunikation**|Aufwendig (Inter-Process Communication)|Einfach (gemeinsamer Speicher)|
|**Isolation**|Stark isoliert (Absturz betrifft nicht andere)|Schwach (Absturz kann alle Threads betreffen)|
|**Unabhängigkeit**|Komplett unabhängig|Abhängig vom Hauptprozess|

## Windows 11 Tools zur Beobachtung

### Task Manager (Strg+Shift+Esc)

- **Prozesse-Tab**: Übersicht aller laufenden Anwendungen
- **Details-Tab**: Detaillierte technische Informationen (PID, Speicher, CPU)
- Zum Beenden: Rechtsklick → "Task beenden"

### PowerShell

```powershell
Get-Process  # Alle Prozesse anzeigen
Get-Process -Name chrome  # Nur Chrome-Prozesse
Get-Process | Sort-Object CPU -Descending  # Nach CPU-Nutzung sortiert
```

## Potenzielle Probleme

**Bei Threads**: Wenn mehrere Threads gleichzeitig auf denselben Speicher zugreifen, können **Race Conditions** entstehen (wie zwei Köche, die gleichzeitig dasselbe Messer benutzen wollen). Daher ist **Synchronisierung** wichtig.

**Kernbotschaft**: Prozesse sind isolierte Programminstanzen, Threads sind leichtgewichtige Arbeiter innerhalb eines Prozesses. Das OS verwaltet beide durch Scheduling, um effizientes Multitasking zu ermöglichen. Moderne Anwendungen nutzen Threads intensiv für parallele Aufgaben und bessere Performance.