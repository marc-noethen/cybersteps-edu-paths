# 🐍 Sum Nested Evens (Recursion)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** Berechne rekursiv die Summe aller geraden Zahlen in einer verschachtelten Liste

**Anforderungen:**
- Funktion: `sum_nested_evens(data)`
- Parameter: `data` (Liste mit Integers und/oder verschachtelten Listen)
- Rückgabe: Integer (Summe aller geraden Zahlen)
- Methode: **Rekursion** (Funktion ruft sich selbst auf)
- Edge Cases: Nur ungerade Zahlen → 0, leere Liste → 0

---

## Lösung

```python
def sum_nested_evens(data):
    """
    Berechnet rekursiv die Summe aller geraden Zahlen in verschachtelter Liste.
    
    Args:
        data: Liste mit Integers und/oder verschachtelten Listen
    
    Returns:
        Summe aller geraden Zahlen (int)
    """
    total = 0
    
    for item in data:
        if isinstance(item, list):
            # Rekursiver Aufruf für verschachtelte Liste
            total += sum_nested_evens(item)
        elif isinstance(item, int) and item % 2 == 0:
            # Gerade Zahl gefunden
            total += item
    
    return total
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `sum_nested_evens([1, 2, [3, 4, [5, 6]], 7, 8])` | `20` | `20` | ✅ |
| `sum_nested_evens([[[1]], [3, [5]], 7])` | `0` | `0` | ✅ |
| `sum_nested_evens([2, 4, 6])` | `12` | `12` | ✅ |
| `sum_nested_evens([])` | `0` | `0` | ✅ |

---

## Notizen

- **Konzept:** Rekursion, `isinstance()`, Modulo-Operator `%`
- **Rekursion:** Funktion ruft sich selbst für verschachtelte Listen auf
- **Basis-Fall:** Integer-Element wird geprüft und ggf. addiert
- **Beispiel:** [1, 2, [3, 4, [5, 6]], 7, 8] → 2 + 4 + 6 + 8 = 20
- **Alternative:** Iterativ mit Stack (komplexer)