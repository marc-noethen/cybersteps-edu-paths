# 🐍 Diamond Pattern

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Erstelle ein zentriertes Diamant-Muster aus Sternchen mit Höhe und Breite n

**Anforderungen:**
- Input: Ungerade positive Ganzzahl `n` (User-Eingabe)
- Prompt: `"Enter an odd positive integer for diamond size: "`
- Ausgabe: Diamant-Form aus `*` mit maximaler Breite n
- Format: Zentriert mit führenden Leerzeichen
- Edge Cases: n = 1 → nur ein einzelnes `*`

---

## Lösung

```python
# User-Eingabe
n = int(input("Enter an odd positive integer for diamond size: "))

# Obere Hälfte (inklusive Mitte)
for i in range(n // 2 + 1):
    spaces = " " * (n // 2 - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Untere Hälfte
for i in range(n // 2 - 1, -1, -1):
    spaces = " " * (n // 2 - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `5` | `Enter an odd positive integer for diamond size: 5`<br>`  *`<br>` ***`<br>`*****`<br>` ***`<br>`  *` | Korrekt | ✅ |
| `3` | `Enter an odd positive integer for diamond size: 3`<br>` *`<br>`***`<br>` *` | Korrekt | ✅ |
| `1` | `Enter an odd positive integer for diamond size: 1`<br>`*` | `*` | ✅ |

---

## Notizen

- **Konzept:** Verschachtelte Muster, String-Multiplikation, Symmetrie
- **Obere Hälfte:** Leerzeichen nehmen ab, Sterne nehmen zu
- **Untere Hälfte:** Spiegelt obere Hälfte (ohne Mitte)
- **Formel:** Zeile i hat `(n // 2 - i)` Leerzeichen und `(2 * i + 1)` Sterne
- **Alternative:** Einzelne Schleife mit Bedingung für obere/untere Hälfte