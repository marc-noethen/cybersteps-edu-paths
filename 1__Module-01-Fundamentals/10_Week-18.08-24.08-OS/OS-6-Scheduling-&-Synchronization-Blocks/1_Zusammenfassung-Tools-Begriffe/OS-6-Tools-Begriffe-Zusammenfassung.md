# Kategorisierung der Themen

## Tabelle: Tools, Fachbegriffe und Vokabeln

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Task Manager (Windows 11)|Systemtool zur Überwachung von Prozessen, CPU-Auslastung und Threads|
||Resource Monitor|Erweiterte Ansicht für CPU-, Speicher- und Thread-Aktivitäten in Windows|
||Performance Monitor|Windows-Tool für detaillierte Leistungsanalyse und Scheduling-Metriken|
||Process Explorer (Sysinternals)|Fortgeschrittenes Tool zur Analyse von Prozessen und Threads|
||PowerShell|Skripterstellung für Prozess- und Thread-Management|
|**Technische Fachbegriffe**|CPU Scheduling|Mechanismus des OS zur Entscheidung, welcher Prozess/Thread CPU-Zeit erhält|
||Preemptive Scheduling|Unterbrechbares Scheduling, bei dem OS Tasks nach Zeitscheibe unterbrechen kann|
||Non-Preemptive Scheduling|Kooperatives Scheduling, bei dem Tasks selbst CPU freigeben müssen|
||Context Switch|Wechsel zwischen Tasks durch Speichern/Laden des Ausführungszustands|
||Time Slice (Quantum)|Festgelegte CPU-Zeit, die ein Prozess/Thread am Stück erhält|
||Race Condition|Fehler durch unkontrollierte gleichzeitige Zugriffe auf geteilte Daten|
||Critical Section|Codebereich mit Zugriff auf geteilte Ressourcen, der Schutz benötigt|
||Mutual Exclusion|Prinzip, dass nur ein Thread gleichzeitig in kritischem Bereich sein darf|
||Mutex (Lock)|Synchronisationsmechanismus zur Sicherung kritischer Bereiche|
||Deadlock|Blockierung mehrerer Threads, die gegenseitig auf Ressourcen warten|
||Starvation|Dauerhafte Verweigerung von Ressourcenzugang für einen Thread|
||Thread Synchronization|Koordination von Threads beim Zugriff auf geteilte Ressourcen|
||Context (Kontext)|Vollständiger Ausführungszustand eines Prozesses/Threads|
||Blocking|Wartezustand eines Threads beim Versuch, gesperrte Ressource zu erlangen|
|**Wichtige Vokabeln**|Responsiveness (Reaktionsfähigkeit)|Schnelle Antwortzeit des Systems auf Benutzereingaben|
||Fairness|Gleichmäßige Verteilung von CPU-Zeit auf alle Prozesse|
||Throughput (Durchsatz)|Anzahl abgeschlossener Aufgaben pro Zeiteinheit|
||CPU-Auslastung|Prozentsatz der Zeit, in der CPU aktiv arbeitet|
||Overhead|Zusätzlicher Ressourcenaufwand für Systemoperationen|
||Shared Resource|Ressource (Speicher, Datei), auf die mehrere Threads zugreifen|
||Data Consistency|Korrektheit und Integrität von Daten bei parallelem Zugriff|
||Acquire Lock|Sperrmechanismus erwerben vor Betreten kritischer Sektion|
||Release Lock|Sperrmechanismus freigeben nach Verlassen kritischer Sektion|
||Indefinite Blocking|Unbegrenzte Wartezeit eines Threads auf Ressource|
||Preemption|Unterbrechung eines laufenden Prozesses durch das OS|
||Concurrent Access|Gleichzeitiger Zugriff mehrerer Threads auf dieselbe Ressource|
||Thread-safe|Code, der bei paralleler Ausführung keine Race Conditions verursacht|

---

## Zusammenfassung nach dem 80/20-Prinzip

**Kernaussage:** CPU-Scheduling entscheidet über Prozessausführung, während Synchronisation Race Conditions durch kontrollierte Ressourcenzugriffe verhindert.

**Die wichtigsten 20% der Informationen:**

### 1. CPU-Scheduling: Die Grundlagen

**Problem:** Ein Computer hat eine CPU, aber Dutzende bis Hunderte aktive Prozesse/Threads, die alle CPU-Zeit benötigen.

**Lösung durch Scheduling:**

- **Preemptive Scheduling** (modernes Windows): OS unterbricht Tasks nach kurzer Zeitscheibe und wechselt zu anderen
- **Context Switch:** OS speichert aktuellen Task-Zustand und lädt den nächsten Task
- **Ziele:** CPU-Auslastung maximieren, Reaktionsfähigkeit sichern, faire Ressourcenverteilung

**Wichtig für Windows 11:** Der Task Manager zeigt Prozesse, CPU-Auslastung und Thread-Anzahl in Echtzeit – ideal zur Beobachtung von Scheduling-Effekten.

### 2. Race Conditions: Das Hauptproblem

**Szenario:** Zwei Threads greifen gleichzeitig auf dieselben Daten zu (z.B. Bankkonto-Saldo).

**Beispiel-Fehler:**

- Thread 1: Liest $100, berechnet +$50 = $150
- _Context Switch erfolgt vor dem Speichern_
- Thread 2: Liest $100 (noch!), berechnet -$30 = $70, speichert $70
- Thread 1: Speichert nun $150 (überschreibt Thread 2)
- **Resultat:** $150 statt korrekter $120 – die $30 Auszahlung ging verloren

**Kritische Sektion:** Codebereich, wo geteilte Daten verändert werden – muss geschützt werden.

### 3. Synchronisation mit Mutexes

**Mutex = Schlüssel zum kritischen Bereich:**

1. Thread versucht Lock zu erwerben (acquire)
2. Wenn verfügbar → Thread betritt kritische Sektion
3. Wenn besetzt → Thread wartet (blockiert)
4. Nach Abschluss → Thread gibt Lock frei (release)

**Effekt:** Nur ein Thread kann gleichzeitig im kritischen Bereich sein → **Mutual Exclusion** ist gewährleistet → Race Conditions werden verhindert.

### 4. Neue Probleme durch Synchronisation

**Deadlock (Verklemmung):**

- Thread A: Hält Lock X, wartet auf Lock Y
- Thread B: Hält Lock Y, wartet auf Lock X
- Beide warten ewig aufeinander → System eingefroren

**Starvation (Verhungern):**

- Thread wird wiederholt übergangen und erhält nie Zugriff auf Ressource
- Andere Threads bekommen immer zuerst den Lock

### Praktische Bedeutung für Windows 11

**Tools zur Beobachtung:**

- **Task Manager:** CPU-Auslastung, Prozesse, Threads
- **Resource Monitor:** Detaillierte Thread-Aktivitäten
- **Process Explorer:** Erweiterte Prozess-/Thread-Analyse

**Anwendung:** Diese Konzepte sind fundamental für Systemadministration, Performance-Tuning und das Verständnis von System-Freezes oder Performance-Problemen in Windows-Umgebungen.