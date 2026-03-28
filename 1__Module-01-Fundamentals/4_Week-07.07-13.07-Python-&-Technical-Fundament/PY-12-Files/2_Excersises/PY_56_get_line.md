# 🐍 Get Specific Line from File

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Funktion zum Lesen einer bestimmten Zeile aus einer Datei

**Anforderungen:**
- Funktion: `get_line(filename, line_number)`
- Parameter: `filename` (string), `line_number` (integer, 1-basiert)
- Rückgabe: String (Zeileninhalt ohne Whitespace) oder None
- Edge Cases: Ungültige Zeilennummer, Datei nicht gefunden → None

---

## Lösung

```python
def get_line(filename, line_number):
    """Liest eine bestimmte Zeile (1-basiert) aus einer Datei. Gibt None zurück bei Fehler."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if line_number < 1 or line_number > len(lines):
                return None
            return lines[line_number - 1].strip()
    except FileNotFoundError:
        return None
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `get_line("sample_data.txt", 2)` | "Line 2: Python Files" | Line 2: Python Files | ✅ |
| `get_line("sample_data.txt", 9)` | "Line 9: End of sample" | Line 9: End of sample | ✅ |
| `get_line("sample_data.txt", 0)` | None | None | ✅ |
| `get_line("sample_data.txt", 100)` | None | None | ✅ |
| `get_line("nicht_vorhanden.txt", 1)` | None | None | ✅ |

---

## Notizen

- **Konzept:** 1-basierte Indexierung (User-freundlich) vs. 0-basierte Python-Listen
- **strip():** Entfernt führende/nachgestellte Whitespaces und Newlines
- **Validierung:** Prüfung auf gültige Zeilennummer vor Zugriff
