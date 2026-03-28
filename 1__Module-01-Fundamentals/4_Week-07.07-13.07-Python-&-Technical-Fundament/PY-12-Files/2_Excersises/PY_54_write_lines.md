# 🐍 Write Lines to File

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Funktion zum Schreiben mehrerer Zeilen in eine neue Datei

**Anforderungen:**
- Funktion: `write_lines(filename, lines)`
- Parameter: `filename` (string), `lines` (list of strings)
- Rückgabe: None (erstellt Datei)
- Edge Cases: Jede Zeile aus der Liste wird in eine neue Zeile geschrieben

---

## Lösung

```python
def write_lines(filename, lines):
    """Schreibt eine Liste von Strings in eine Datei, jeder String in eine neue Zeile."""
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `write_lines("output1.txt", ["First line", "Second line", "Third"])` | Datei mit 3 Zeilen | First line<br>Second line<br>Third | ✅ |

---

## Notizen

- **Konzept:** File Writing mit `open()` im Write-Modus
- **Alternative:** `f.write('\n'.join(lines) + '\n')` (kompakter)
- **Wichtig:** Newline (`\n`) manuell hinzufügen, da `write()` dies nicht automatisch tut
