# 🖥️ Terminal Bandit

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Command-Line-Skills durch die OverTheWire Bandit Challenge stärken.

---

## Lösung

### Umgebung
```
OS: Win11
Shell: PowerShell / WSL
```

### Verbindung herstellen

**SSH-Befehl:**
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
Passwort für Level 0: `bandit0`

---

### Durchführung

**Level 0 → 1**
```bash
# Hinweis: Das Passwort liegt in einer Datei im Home-Verzeichnis
cat readme
```
**Passwort für Level 1:** `___________________________`

---

**Level 1 → 2**
```bash
# Hinweis: Dateiname beginnt mit "-" (Sonderzeichen)
cat ./-
```
**Passwort für Level 2:** `___________________________`

---

**Level 2 → 3**
```bash
# Hinweis: Dateiname enthält Leerzeichen
cat "spaces in this filename"
# Alternative: cat spaces\ in\ this\ filename
```
**Passwort für Level 3:** `___________________________`

---

**Level 3 → 4**
```bash
# Hinweis: Versteckte Datei in einem Unterverzeichnis
cd inhere
ls -la
cat ...Hiding-From-You
```
**Passwort für Level 4:** `___________________________`

---

**Level 4 → 5**
```bash
# Hinweis: Finde die einzige menschenlesbare Datei
cd inhere
file ./-file*
cat ./-file07
```
**Passwort für Level 5:** `___________________________`

---

**Level 5 → 6**
```bash
# Hinweis: Datei mit spezifischer Größe (1033 bytes), nicht ausführbar
find ./inhere -type f -size 1033c ! -executable
cat [gefundene Datei]
```
**Passwort für Level 6:** `___________________________`

---

**Level 6 → 7**
```bash
# Hinweis: Datei gehört user bandit7, group bandit6, 33 bytes
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat [gefundene Datei]
```
**Passwort für Level 7:** `___________________________`

---

**Level 7 → 8**
```bash
# Hinweis: Passwort neben dem Wort "millionth" in data.txt
grep "millionth" data.txt
```
**Passwort für Level 8:** `___________________________`

---

**Level 8 → 9**
```bash
# Hinweis: Die einzige Zeile, die nur einmal vorkommt
sort data.txt | uniq -u
```
**Passwort für Level 9:** `___________________________`

---

**Level 9 → 10**
```bash
# Hinweis: Menschenlesbarer String, beginnt mit "="
strings data.txt | grep "^="
```
**Passwort für Level 10:** `___________________________`

---

*Weitere Level nach Bedarf fortsetzen...*

---

## Ergebnisse

| Level | Passwort |
|-------|----------|
| 0 → 1 | _________________________ |
| 1 → 2 | _________________________ |
| 2 → 3 | _________________________ |
| 3 → 4 | _________________________ |
| 4 → 5 | _________________________ |
| 5 → 6 | _________________________ |
| 6 → 7 | _________________________ |
| 7 → 8 | _________________________ |
| 8 → 9 | _________________________ |
| 9 → 10 | _________________________ |

**Höchstes erreichtes Level:** ___

---

## Notizen

- **Gelernt:**
  - `cat ./-` für Dateien die mit `-` beginnen
  - `cat "file name"` für Dateien mit Leerzeichen
  - `ls -la` zeigt versteckte Dateien
  - `file` erkennt Dateitypen
  - `find` mit Optionen wie `-size`, `-user`, `-group`
  - `grep` für Textsuche
  - `sort | uniq -u` findet einzigartige Zeilen
  - `strings` extrahiert lesbare Strings aus Binärdateien

- **Nützliche Befehle:**
  - `ssh user@host -p port` - SSH-Verbindung
  - `2>/dev/null` - Fehlermeldungen unterdrücken
  - `man [befehl]` - Hilfe anzeigen

- **Tipp:** Die Bandit-Seite gibt Hinweise zu benötigten Befehlen für jedes Level!
