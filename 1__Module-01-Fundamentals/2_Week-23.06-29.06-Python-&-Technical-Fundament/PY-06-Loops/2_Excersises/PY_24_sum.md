# 🐍 Sum Calculator

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Berechnung der Summe aller ganzen Zahlen von 1 bis n mit einer Schleife

**Anforderungen:**
- Input: Positive Ganzzahl `n` (User-Eingabe)
- Prompt: `"Enter a positive integer: "`
- Berechnung: Summe von 1 + 2 + 3 + ... + n
- Ausgabe: `"The sum is: [result]"`
- Edge Cases: Annahme, dass User positive Ganzzahl eingibt

---

## Lösung

```python
# User-Eingabe
n = int(input("Enter a positive integer: "))

# Summe berechnen mit Schleife
total = 0
for i in range(1, n + 1):
    total += i

# Ausgabe
print(f"The sum is: {total}")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `5` | `Enter a positive integer: 5`<br>`The sum is: 15` | `The sum is: 15` | ✅ |
| `10` | `The sum is: 55` | `The sum is: 55` | ✅ |
| `1` | `The sum is: 1` | `The sum is: 1` | ✅ |

---

## Notizen

- **Konzept:** `for`-Schleife mit `range()`, Akkumulator-Variable
- **range():** `range(1, n + 1)` erzeugt Zahlen von 1 bis n (inklusive)
- **Alternative:** Gaußsche Summenformel `n * (n + 1) // 2` (ohne Schleife)