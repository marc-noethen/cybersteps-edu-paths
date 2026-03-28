# 🐍 Count Above Average

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** Zähle die Anzahl der Werte in einer Liste, die strikt größer als der Durchschnitt sind

**Anforderungen:**
- Funktion: `count_above_average(numbers)`
- Parameter: `numbers` (Liste von int/float)
- Rückgabe: Integer (Anzahl der Werte > Durchschnitt)
- Berechnung: Durchschnitt berechnen, dann Werte zählen
- Edge Cases: Leere Liste → return 0

---

## Lösung

```python
def count_above_average(numbers):
    """
    Zählt die Anzahl der Zahlen, die über dem Durchschnitt liegen.
    
    Args:
        numbers: Liste von Zahlen (int oder float)
    
    Returns:
        Anzahl der Werte strikt größer als Durchschnitt (int)
    """
    # Edge Case: Leere Liste
    if len(numbers) == 0:
        return 0
    
    # Durchschnitt berechnen
    average = sum(numbers) / len(numbers)
    
    # Werte über Durchschnitt zählen
    count = 0
    for num in numbers:
        if num > average:
            count += 1
    
    return count
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `count_above_average([1, 2, 3, 4, 5])` | `2` | `2` | ✅ |
| `count_above_average([10, 10, 10])` | `0` | `0` | ✅ |
| `count_above_average([])` | `0` | `0` | ✅ |
| `count_above_average([1, 100])` | `1` | `1` | ✅ |

---

## Notizen

- **Konzept:** `sum()`, `len()`, Durchschnittsberechnung, Iteration
- **Wichtig:** Strikt größer (`>`) nicht größer-gleich (`>=`)
- **Alternative:** List Comprehension: `return sum(1 for num in numbers if num > average)`
- **Beispiel:** [1, 2, 3, 4, 5] → Ø = 3.0 → [4, 5] sind > 3.0 → count = 2