# 🐍 Find Key-Value in File

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 08.07.2025

---

## Aufgabe

**Ziel:** Funktion zum Suchen und Extrahieren eines Integer-Werts aus einer Key-Value-Datei

**Anforderungen:**
- Funktion: `find_value(filename, key)`
- Parameter: `filename` (string), `key` (string)
- Format: Zeilen im Format `key,value` (Komma-separiert)
- Rückgabe: Integer (erster gefundener Wert) oder None
- Edge Cases: Key nicht gefunden, Datei nicht vorhanden, Konvertierung fehlgeschlagen → None

---

## Lösung

```python
def find_value(filename, key):
    """Sucht einen Key in einer Datei und gibt den zugehörigen Integer-Wert zurück."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith(key + ','):
                    try:
                        value_part = line.split(',', 1)[1]
                        return int(value_part)
                    except (ValueError, IndexError):
                        return None
        return None
    except FileNotFoundError:
        return None
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `find_value("sample_data.txt", "timeout")` | 120 | 120 | ✅ |
| `find_value("sample_data.txt", "max_users")` | 50 | 50 | ✅ |
| `find_value("sample_data.txt", "nicht_vorhanden")` | None | None | ✅ |
| `find_value("nicht_vorhanden.txt", "key")` | None | None | ✅ |

---

## Notizen

- **Konzept:** String-Parsing mit `startswith()` und `split()`
- **split(',', 1):** Splittet nur beim ersten Komma (falls Wert weitere Kommas enthält)
- **Nested try/except:** Behandelt sowohl FileNotFoundError als auch ValueError/IndexError
- **Erste Übereinstimmung:** Funktion stoppt bei erstem Match
