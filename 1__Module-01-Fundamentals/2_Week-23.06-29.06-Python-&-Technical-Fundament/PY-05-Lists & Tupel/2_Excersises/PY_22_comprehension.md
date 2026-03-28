# 🐍 Positive Squares

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Mit List Comprehension Quadrate von Zahlen berechnen, die größer als ein Mindestwert sind

**Anforderungen:**
- Listen: `data` (vordefiniert), `minimum_value` (int, vordefiniert)
- Rückgabe: Liste `positive_squares`
- Methode: **List Comprehension** verwenden
- Filter: Nur Zahlen strikt größer als `minimum_value` (nicht gleich!)
- Edge Cases: Leere Liste → leeres Ergebnis

---

## Lösung

```python
# List Comprehension: Quadrate von Werten > minimum_value
positive_squares = [x * x for x in data if x > minimum_value]
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `data = [12, -5, 20, 7, -3, 0, 15, 8]`<br>`minimum_value = 0` | `[144, 400, 49, 225, 64]` | `[144, 400, 49, 225, 64]` | ✅ |
| `data = [1, 2, 3]`<br>`minimum_value = 5` | `[]` | `[]` | ✅ |
| `data = []`<br>`minimum_value = 0` | `[]` | `[]` | ✅ |

---

## Notizen

- **Konzept:** List Comprehension mit Bedingung (`if`)
- **Syntax:** `[ausdruck for element in liste if bedingung]`
- **Wichtig:** `>` nicht `>=` verwenden (strikt größer)
- **Alternative:** Mit `for`-Schleife und `append()` (weniger pythonic)