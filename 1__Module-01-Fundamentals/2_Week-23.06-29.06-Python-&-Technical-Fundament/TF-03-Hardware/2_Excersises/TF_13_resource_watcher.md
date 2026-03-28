# 🖥️ Resource Watcher - Activity Monitor

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** CPU-, Memory- und Disk-Auslastung mit Activity Monitor unter verschiedenen Lastszenarien beobachten und analysieren

**Aufgabenstellung:**
- Teil 1: CPU-Last durch Terminal-Befehl erzeugen und beobachten
- Teil 2: Memory-Druck durch viele Browser-Tabs simulieren
- Teil 3: Disk-Aktivität beim Kopieren großer Dateien überwachen

---

## Lösung

### Umgebung
```
OS: macOS [Version]
Apps: Activity Monitor, Terminal, Web Browser
```

### Durchführung

**Teil 1: CPU Load Observation**

**Schritt 1:** Vorbereitung
```bash
# Alle nicht-essentiellen Apps schließen
# Activity Monitor öffnen: Applications > Utilities > Activity Monitor
# CPU-Tab auswählen
```

**Schritt 2:** CPU-Last erzeugen
```bash
# Terminal öffnen
# Befehl ausführen (erzeugt CPU-Last)
yes > /dev/null &
```
**Wirkung:** Erzeugt einen Hintergrundprozess, der CPU zu 100% auslastet

**Schritt 3:** Beobachtung (15-20 Sekunden)
- Activity Monitor: Nach `% CPU` sortieren (Spaltenüberschrift klicken)
- Prozess `yes` sollte an der Spitze erscheinen mit hoher CPU-Auslastung
- **Screenshot erstellen** von Activity Monitor (CPU-Tab)

**Schritt 4:** Aufräumen
```bash
# Im Terminal
killall yes
```

---

**Teil 2: Memory Load Observation**

**Schritt 1:** Baseline erfassen
- Activity Monitor → **Memory** Tab wählen
- "Memory Pressure" Graph beobachten (initial: grün = gut)

**Schritt 2:** Memory-Last erzeugen
- Web Browser öffnen
- 20-30+ Tabs gleichzeitig öffnen (media-heavy sites: News, Videos, Bildergalerien)

**Schritt 3:** Beobachtung
- Zu Activity Monitor wechseln
- Memory Pressure Graph beobachten (Farbwechsel: grün → gelb → rot)
- **Screenshot erstellen** (Memory-Tab mit Pressure Graph sichtbar)

**Schritt 4:** Aufräumen
- Browser-Tabs schließen

---

**Teil 3: Disk Activity Observation**

**Schritt 1:** Baseline erfassen
- Activity Monitor → **Disk** Tab wählen
- Initiale Read/Write-Aktivität notieren (meist nahe 0)

**Schritt 2:** Große Datei vorbereiten
```bash
# Option A: Vorhandene große Datei finden (>500MB Video/Installer)
# Option B: Test-Datei erstellen
mkfile 1g large_test_file
```
**Ausgabe:** Erstellt 1GB große Datei im Home-Verzeichnis

**Schritt 3:** Disk-Last erzeugen
```bash
# Im Finder:
# Datei finden → Rechtsklick → Duplicate (oder Cmd+D)
# Während Kopiervorgang läuft: Zu Activity Monitor wechseln
```

**Schritt 4:** Beobachtung
- Disk-Tab in Activity Monitor
- "Data written/sec" und "Data read/sec" beobachten
- Verantwortlichen Prozess identifizieren (`Finder` oder `kernel_task`)
- **Screenshot erstellen** während aktiver Kopieraktivität

**Schritt 5:** Aufräumen
```bash
# Test-Datei und Kopie löschen
rm large_test_file
rm "large_test_file copy"
```

---

## Ergebnisse

**Teil 1 - CPU:**
- Screenshot: [CPU-Tab mit `yes` Prozess bei ~100% CPU]
- Beobachtung: Ein einzelner Prozess kann einen CPU-Core vollständig auslasten

**Teil 2 - Memory:**
- Screenshot: [Memory-Tab mit erhöhtem Memory Pressure]
- Beobachtung: Viele offene Tabs erhöhen RAM-Nutzung → Memory Pressure steigt

**Teil 3 - Disk:**
- Screenshot: [Disk-Tab mit aktiver Read/Write-Aktivität]
- Beobachtung: File-Operationen erzeugen messbare Disk I/O-Aktivität

---

## Notizen

- **Gelernt:** Ressourcen-Monitoring, künstliche Last erzeugen, Bottleneck-Erkennung
- **CPU:** `yes` command erzeugt Endlosschleife → volle Core-Auslastung
- **Memory Pressure:** 
  - Grün = genug freier RAM
  - Gelb = System beginnt Swap zu nutzen
  - Rot = starker Memory-Druck, Performance-Einbußen
- **Disk I/O:** Große File-Operationen deutlich in Activity Monitor sichtbar
- **Tipp:** Activity Monitor ist essentiell für Performance-Diagnose