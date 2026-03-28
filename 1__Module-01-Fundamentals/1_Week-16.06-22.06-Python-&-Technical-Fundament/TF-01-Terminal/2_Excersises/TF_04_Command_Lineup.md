# 🖥️ Command Lineup

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Erstellen von Command-Pipelines mit `ls`, `head`, `tail` und `sort`, um spezifische Befehle in `/usr/bin` basierend auf alphabetischer Position zu isolieren.

---

## Lösung

### Umgebung
```
OS: Win11 (WSL/Ubuntu)
Shell: bash
```

### Durchführung

**Schritt 1:** Verzeichnis `/usr/bin` erkunden
```bash
ls /usr/bin | head -10
```
**Ausgabe:** Zeigt die ersten 10 Befehle alphabetisch sortiert

**Schritt 2:** 5. Befehl alphabetisch finden
```bash
ls -1 /usr/bin | head -5 | tail -1
```
**Erklärung:**
- `ls -1` = Liste mit einem Eintrag pro Zeile
- `head -5` = Nimmt die ersten 5 Zeilen
- `tail -1` = Nimmt davon die letzte Zeile (= die 5.)

**Beispielausgabe:** `addpart` (systemabhängig)

**Schritt 3:** 3. Befehl von hinten finden
```bash
ls -1 /usr/bin | tail -3 | head -1
```
**Erklärung:**
- `ls -1` = Liste mit einem Eintrag pro Zeile
- `tail -3` = Nimmt die letzten 3 Zeilen
- `head -1` = Nimmt davon die erste Zeile (= 3. von hinten)

**Beispielausgabe:** `zmore` (systemabhängig)

---

## Ergebnisse

| Schritt | Befehl |
|---------|--------|
| Schritt 2 (5. alphabetisch) | `ls -1 /usr/bin \| head -5 \| tail -1` |
| Schritt 3 (3. von hinten) | `ls -1 /usr/bin \| tail -3 \| head -1` |

---

## Notizen

- **Gelernt:** Kombination von `head` und `tail` für präzise Zeilenauswahl
- **Wichtig:** `ls -1` (Ziffer Eins) erzwingt eine Zeile pro Eintrag
- **Tipp:** `ls` sortiert standardmäßig alphabetisch
- **Logik für n-ten Eintrag:** `head -n | tail -1`
- **Logik für n-ten von hinten:** `tail -n | head -1`
- **Pipe `|`:** Verkettet Befehle - Output wird zum Input des nächsten
