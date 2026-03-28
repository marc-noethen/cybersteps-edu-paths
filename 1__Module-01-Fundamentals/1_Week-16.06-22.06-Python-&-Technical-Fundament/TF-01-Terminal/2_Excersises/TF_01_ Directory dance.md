# 🖥️ Directory dance

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Navigieren durch eine Verzeichnisstruktur mithilfe von absoluten und relativen Pfaden, mit Überprüfung des Standorts bei jedem Schritt.

---

## Lösung

### Umgebung
```
OS: Win11
Shell: Powershell
```

### Durchführung

**Schritt 1:** Terminal öffnen und Home-Verzeichnis überprüfen
```bash
pwd
```
**Ausgabe:** `/Users/username`

**Schritt 2:** Verzeichnisstruktur erstellen
```bash
mkdir -p ~/TF1_Exercises/Level1/SubLevelA
mkdir -p ~/TF1_Exercises/Level1/SubLevelB
mkdir -p ~/TF1_Exercises/Level2
```

**Schritt 3:** Struktur überprüfen
```bash
tree ~/TF1_Exercises
```
**Ausgabe:**
```
/Users/username/TF1_Exercises/
├── Level1/
│   ├── SubLevelA/
│   └── SubLevelB/
└── Level2/
```

**Schritt 4:** Mit relativem Pfad zu SubLevelA navigieren
```bash
cd TF1_Exercises/Level1/SubLevelA
```

**Schritt 5:** Standort überprüfen (Frage 5)
```bash
pwd
```
**Ausgabe:** `/Users/username/TF1_Exercises/Level1/SubLevelA`

**Schritt 6:** Mit relativem Pfad von SubLevelA zu Level2 navigieren
```bash
cd ../../Level2
```

**Schritt 7:** Standort überprüfen (Frage 7)
```bash
pwd
```
**Ausgabe:** `/Users/username/TF1_Exercises/Level2`

**Schritt 8:** Zurück zum Home-Verzeichnis (kürzester Befehl)
```bash
cd ~
```
Alternative: `cd` (ohne Argumente führt auch zum Home-Verzeichnis)

**Schritt 9:** Home-Verzeichnis überprüfen
```bash
pwd
```
**Ausgabe:** `/Users/username`

**Schritt 10:** Mit absolutem Pfad zu SubLevelB navigieren
```bash
cd /Users/username/TF1_Exercises/Level1/SubLevelB
```

**Schritt 11:** Standort überprüfen (Frage 11)
```bash
pwd
```
**Ausgabe:** `/Users/username/TF1_Exercises/Level1/SubLevelB`

---

## Ergebnisse

| Frage | Antwort |
|-------|---------|
| Frage 5 | `/Users/username/TF1_Exercises/Level1/SubLevelA` |
| Frage 7 | `/Users/username/TF1_Exercises/Level2` |
| Frage 11 | `/Users/username/TF1_Exercises/Level1/SubLevelB` |

---

## Notizen

- **Gelernt:** Unterschied absolute vs. relative Pfade
- **Relative Pfade:** Beginnen vom aktuellen Verzeichnis (z.B. `TF1_Exercises/Level1`)
- **Absolute Pfade:** Beginnen vom Root oder Home (z.B. `/Users/username/...`)
- **Tipp:** `~` = Home-Verzeichnis, `..` = Elternverzeichnis, `.` = aktuelles Verzeichnis
- **Wichtig:** `cd ../../Level2` bedeutet: 2 Ebenen hoch, dann in Level2
