# 🖥️ Log Lurker

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Verwendung von `ls` mit verschiedenen Optionen und Pipes, um Informationen über Dateien zu finden und Einträge in Systemverzeichnissen zu zählen.

---

## Lösung

### Umgebung
```
OS: Win11 (WSL/Ubuntu)
Shell: bash
```

### Durchführung

**Schritt 1:** Zum `/var/log` Verzeichnis navigieren
```bash
cd /var/log
```

**Schritt 2:** Dateien nach Größe sortieren (größte zuletzt)
```bash
ls -lS -r
```
**Erklärung:**
- `-l` = Long format (zeigt Größe an)
- `-S` = Sort by size (größte zuerst)
- `-r` = Reverse (umkehren, damit größte zuletzt)

**Schritt 3:** Dateien nach Änderungszeit sortieren (neueste zuletzt)
```bash
ls -lt -r
```
**Erklärung:**
- `-l` = Long format (zeigt Zeit an)
- `-t` = Sort by modification time (neueste zuerst)
- `-r` = Reverse (umkehren, damit neueste zuletzt)

**Schritt 4:** Zum `/etc` Verzeichnis navigieren
```bash
cd /etc
```

**Schritt 5:** Alle Einträge zählen (inkl. versteckte)
```bash
ls -a /etc | wc -l
```
**Erklärung:**
- `-a` = All (zeigt auch versteckte Dateien mit `.` am Anfang)
- `|` = Pipe (leitet Ausgabe weiter)
- `wc -l` = Word count, lines only (zählt Zeilen)

**Hinweis:** Das Ergebnis enthält auch `.` und `..`, für exakte Anzahl ohne diese:
```bash
ls -A /etc | wc -l
```
(`-A` zeigt versteckte, aber ohne `.` und `..`)

---

## Ergebnisse

| Schritt | Befehl |
|---------|--------|
| Schritt 2 (Größe, größte zuletzt) | `ls -lSr` |
| Schritt 3 (Zeit, neueste zuletzt) | `ls -ltr` |
| Schritt 5 (Einträge zählen) | `ls -a /etc \| wc -l` |

---

## Notizen

- **Gelernt:** `ls`-Optionen können kombiniert werden (`-lSr` statt `-l -S -r`)
- **Tipp:** `-r` kehrt jede Sortierung um
- **Wichtig:** `-a` zeigt ALLE Dateien, `-A` zeigt alle außer `.` und `..`
- **Pipe `|`:** Verbindet Ausgabe eines Befehls mit Eingabe des nächsten
