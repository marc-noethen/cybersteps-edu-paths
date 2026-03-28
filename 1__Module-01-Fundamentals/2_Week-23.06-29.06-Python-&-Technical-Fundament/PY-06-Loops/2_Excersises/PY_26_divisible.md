# 🐍 First Divisible by 7

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Finde den Index der ersten Zahl in einer Liste, die durch 7 teilbar ist

**Anforderungen:**
- Liste: `numbers` (vordefiniert)
- Suche: Erste Zahl, die durch 7 teilbar ist (mit `break`)
- Ausgabe bei Fund: `"First multiple of 7 found at index: [index]"`
- Ausgabe bei Nicht-Fund: `"No multiple of 7 found in the list."`
- Edge Cases: Leere Liste oder keine Vielfachen von 7

---

## Lösung

```python
# Annahme: numbers ist bereits definiert
# numbers = [11, 23, 8, 44, 51, 68, 7, 21, 14]

found = False

for i in range(len(numbers)):
    if numbers[i] % 7 == 0:
        print(f"First multiple of 7 found at index: {i}")
        found = True
        break

if not found:
    print("No multiple of 7 found in the list.")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `numbers = [11, 23, 8, 44, 51, 68, 7, 21, 14]` | `First multiple of 7 found at index: 6` | `First multiple of 7 found at index: 6` | ✅ |
| `numbers = [1, 2, 3, 4, 5]` | `No multiple of 7 found in the list.` | `No multiple of 7 found in the list.` | ✅ |
| `numbers = [14, 3, 5]` | `First multiple of 7 found at index: 0` | `First multiple of 7 found at index: 0` | ✅ |

---

## Notizen

- **Konzept:** `for`-Schleife mit `break`, Modulo-Operator `%`, Flag-Variable
- **break:** Stoppt die Schleife sofort bei Fund
- **Modulo:** `x % 7 == 0` prüft Teilbarkeit durch 7
- **Alternative:** `enumerate()` verwenden für elegantere Index-Iteration