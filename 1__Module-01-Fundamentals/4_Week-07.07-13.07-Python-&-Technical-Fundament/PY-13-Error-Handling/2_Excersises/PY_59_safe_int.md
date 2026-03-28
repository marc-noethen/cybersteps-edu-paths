# 🐍 Safe Integer Conversion

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 08.07.2025

---

## Aufgabe

**Ziel:** Funktion zur sicheren Konvertierung eines Strings in einen Integer

**Anforderungen:**
- Funktion: `safe_int_convert(input_string)`
- Parameter: `input_string` (string)
- Rückgabe: Integer (bei Erfolg) oder None (bei Fehler)
- Edge Cases: Nicht-numerische Zeichen → None

---

## Lösung

```python
def safe_int_convert(input_string):
    """Konvertiert einen String sicher in einen Integer. Gibt None zurück bei Fehler."""
    try:
        return int(input_string)
    except ValueError:
        return None
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `safe_int_convert("123")` | 123 | 123 | ✅ |
| `safe_int_convert("abc")` | None | None | ✅ |
| `safe_int_convert("12.5")` | None | None | ✅ |
| `safe_int_convert("-42")` | -42 | -42 | ✅ |

---

## Notizen

- **Konzept:** ValueError Exception Handling bei Type Conversion
- **int():** Wirft ValueError wenn String nicht konvertierbar ist
- **Alternative:** Regex-Validierung vor Konvertierung (komplexer)
