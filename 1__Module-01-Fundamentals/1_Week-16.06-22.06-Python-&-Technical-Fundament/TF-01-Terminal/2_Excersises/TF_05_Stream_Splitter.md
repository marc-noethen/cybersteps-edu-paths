# 🖥️ Stream Splitter

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Einen Befehl ausführen, der sowohl stdout als auch stderr erzeugt, und beide Streams in separate Dateien umleiten.

---

## Lösung

### Umgebung
```
OS: Win11 (WSL/Ubuntu)
Shell: bash
```

### Durchführung

**Schritt 1:** Zum TF1_Exercises Verzeichnis navigieren und Testdatei erstellen
```bash
cd ~/TF1_Exercises
touch my_commands.txt
```

**Schritt 2:** Befehl testen (erzeugt stdout und stderr)
```bash
ls my_commands.txt non_existent_file.txt
```
**Ausgabe:**
```
ls: cannot access 'non_existent_file.txt': No such file or directory
my_commands.txt
```
- Zeile 1 = stderr (Fehlermeldung)
- Zeile 2 = stdout (normale Ausgabe)

**Schritt 3:** Beide Streams in separate Dateien umleiten
```bash
ls my_commands.txt non_existent_file.txt > stdout.log 2> stderr.log
```
**Erklärung:**
- `> stdout.log` = Leitet stdout (File Descriptor 1) in stdout.log
- `2> stderr.log` = Leitet stderr (File Descriptor 2) in stderr.log

**Schritt 4:** Ergebnis überprüfen
```bash
cat stdout.log
```
**Ausgabe:** `my_commands.txt`

```bash
cat stderr.log
```
**Ausgabe:** `ls: cannot access 'non_existent_file.txt': No such file or directory`

---

## Ergebnisse

| Schritt | Befehl |
|---------|--------|
| Schritt 3 (Beide Streams trennen) | `ls my_commands.txt non_existent_file.txt > stdout.log 2> stderr.log` |

---

## Notizen

- **File Descriptors:**
  - `0` = stdin (Standard Input)
  - `1` = stdout (Standard Output) - implizit bei `>`
  - `2` = stderr (Standard Error)

- **Redirection-Syntax:**
  - `> file` = stdout nach file (überschreiben)
  - `>> file` = stdout nach file (anhängen)
  - `2> file` = stderr nach file
  - `2>> file` = stderr nach file (anhängen)
  - `&> file` = stdout UND stderr nach file
  - `2>&1` = stderr zu stdout umleiten

- **Tipp:** Die Reihenfolge der Redirections ist wichtig!
- **Gelernt:** stdout und stderr sind separate Kanäle, die unabhängig umgeleitet werden können
