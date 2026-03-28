# 🐍 Safe Division with Error Handling

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 08.07.2025

---

## Aufgabe

**Ziel:** Funktion zur sicheren Division zweier String-Zahlen mit spezifischen Fehlermeldungen

**Anforderungen:**
- Funktion: `safe_divide(numerator_str, denominator_str)`
- Parameter: Zwei Strings (numerator, denominator)
- Rückgabe: Float (bei Erfolg), "Invalid number format" (bei ValueError), "Cannot divide by zero" (bei ZeroDivisionError)
- Edge Cases: Ungültige Zahlenformate, Division durch Null

---

## Lösung

```python
def safe_divide(numerator_str, denominator_str):
    """Dividiert zwei Strings als Floats. Gibt spezifische Fehlermeldungen zurück."""
    try:
        numerator = float(numerator_str)
        denominator = float(denominator_str)
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return "Cannot divide by zero"
    except ValueError:
        return "Invalid number format"
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `safe_divide("10", "2")` | 5.0 | 5.0 | ✅ |
| `safe_divide("10", "0")` | "Cannot divide by zero" | Cannot divide by zero | ✅ |
| `safe_divide("abc", "2")` | "Invalid number format" | Invalid number format | ✅ |
| `safe_divide("10", "xyz")` | "Invalid number format" | Invalid number format | ✅ |
| `safe_divide("15", "3")` | 5.0 | 5.0 | ✅ |

---

## Notizen

- **Konzept:** Nested try-except Blöcke für unterschiedliche Exception-Typen
- **ValueError:** Tritt bei float() auf, wenn String nicht konvertierbar ist
- **ZeroDivisionError:** Tritt bei Division durch 0 auf
- **Alternative:** try-except-else Struktur (Division im else-Block)
