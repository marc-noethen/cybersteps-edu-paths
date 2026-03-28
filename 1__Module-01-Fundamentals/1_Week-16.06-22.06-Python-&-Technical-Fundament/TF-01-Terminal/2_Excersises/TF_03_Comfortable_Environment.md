# 🖥️ Comfortable Environment

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Übung mit Umgebungsvariablen und Output-Redirection (`>`, `>>`)

---

## Lösung

### Umgebung
```
OS: Win11 (WSL/Ubuntu)
Shell: bash
```

### Durchführung

**Schritt 1:** Befehl zum Anzeigen aller Umgebungsvariablen
```bash
env
```
Alternative: `printenv`

**Schritt 2:** Umgebungsvariablen in Datei umleiten
```bash
env > my_env.txt
```

**Schritt 3:** PATH-Variable ausgeben
```bash
echo $PATH
```
**Beispielausgabe:** `/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin`

**Antwort Frage 3:** Der erste Ordner in der Liste ist `/usr/local/bin` (oder je nach System z.B. `/home/username/.local/bin`)

**Schritt 4:** Variable GREETINGS_NAME erstellen und überprüfen
```bash
GREETINGS_NAME="Hello"
echo $GREETINGS_NAME
```
**Ausgabe:** `Hello`

**Schritt 5:** Variable GREETINGS_USER mit Wert von USER erstellen
```bash
GREETINGS_USER=$USER
echo $GREETINGS_USER
```
**Ausgabe:** `username` (dein Benutzername)

**Schritt 6:** Beide Variablen in Datei speichern (2 separate Zeilen)
```bash
echo $GREETINGS_NAME > greetings.txt
echo $GREETINGS_USER >> greetings.txt
```
Alternative (eine Zeile):
```bash
echo -e "$GREETINGS_NAME\n$GREETINGS_USER" > greetings.txt
```

**Schritt 7:** Neues Terminal öffnen und Befehl wiederholen
```bash
echo $GREETINGS_NAME > greetings.txt
echo $GREETINGS_USER >> greetings.txt
```

**Antwort Frage 7:** 
**Nein, es funktioniert nicht richtig!** Die Variablen `GREETINGS_NAME` und `GREETINGS_USER` existieren im neuen Terminal nicht mehr. Die Datei wird erstellt, aber mit leeren Werten.

**Erklärung:** Die erstellten Variablen sind nur **Shell-Variablen** (lokal), keine **exportierten Umgebungsvariablen**. Sie existieren nur in der aktuellen Shell-Session. Um sie in neuen Terminals verfügbar zu machen, müsste man:
- `export GREETINGS_NAME="Hello"` verwenden, ODER
- Sie in `~/.bashrc` oder `~/.profile` eintragen

---

## Ergebnisse

| Schritt | Befehl |
|---------|--------|
| Schritt 1 | `env` |
| Schritt 2 | `env > my_env.txt` |
| Schritt 3 | `echo $PATH` |
| Schritt 4 | `GREETINGS_NAME="Hello"` |
| Schritt 5 | `GREETINGS_USER=$USER` |
| Schritt 6 | `echo $GREETINGS_NAME > greetings.txt` und `echo $GREETINGS_USER >> greetings.txt` |

| Frage | Antwort |
|-------|---------|
| Frage 3 | Erster Ordner in PATH: `/usr/local/bin` (systemabhängig) |
| Frage 7 | Nein - Variablen sind nur in der aktuellen Shell-Session gültig, nicht exportiert |

---

## Notizen

- **Gelernt:** Unterschied zwischen `>` (überschreiben) und `>>` (anhängen)
- **Wichtig:** Shell-Variablen vs. exportierte Umgebungsvariablen
- **Tipp:** `export VAR=value` macht Variable für Child-Prozesse verfügbar
- **Tipp:** `$VAR` greift auf Variablenwert zu
