# 🐍 Count Lines in File

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Funktion zum Zählen der Zeilen in einer Datei

**Anforderungen:**
- Funktion: `count_lines(filename)`
- Parameter: `filename` (string)
- Rückgabe: Integer (Anzahl der Zeilen)
- Edge Cases: Datei nicht gefunden → 0

---

## Lösung

```python
def count_lines(filename):
    """Zählt Zeilen in einer Datei. Gibt 0 zurück bei Fehler."""
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `count_lines("sample_data.txt")` | 9 | 9 | ✅ |
| `count_lines("nicht_vorhanden.txt")` | 0 | 0 | ✅ |

---

## Notizen

- **Konzept:** Exception Handling mit `try/except` für FileNotFoundError
- **Alternative:** `len(f.readlines())` (benötigt mehr Speicher)
- **Effizient:** Generator-Expression `sum(1 for _ in f)` zählt ohne komplette Liste im Speicher
