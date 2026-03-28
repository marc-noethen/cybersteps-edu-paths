# 🐍 Process Numbers - Gerade/Ungerade trennen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 30.06.2025

---

## Aufgabe

**Ziel:** Trenne eine Liste in gerade und ungerade Zahlen und gib beide Listen aus.

**Anforderungen:**
- Funktion: `process_numbers(numbers)`
- Ausgabe: `print()` für Evens und Odds
- Edge Cases: Leere Liste → leere Ausgaben

---

## Lösung

```python
def process_numbers(numbers):
    odds = []
    evens = []
    for num in numbers:
        if num % 2 == 0:       # Fix: % 2 statt % 3, Doppelpunkt
            evens.append(num)
        else:                   # Fix: Doppelpunkt hinzugefügt
            odds.append(num)    # Fix: odds statt evens
    print("Evens:", evens)
    print("Odds:", odds)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `[1, 2, 3, 4, 5, 6]` | Evens: [2, 4, 6], Odds: [1, 3, 5] | Evens: [2, 4, 6], Odds: [1, 3, 5] | ✅ |
| `[]` | Evens: [], Odds: [] | Evens: [], Odds: [] | ✅ |

---

## Notizen

- **Fehler 1:** `% 3` → `% 2` (Modulo 2 prüft gerade/ungerade)
- **Fehler 2:** Fehlende `:` nach `if` und `else`
- **Fehler 3:** Im `else`-Block wurde `evens` statt `odds` befüllt
