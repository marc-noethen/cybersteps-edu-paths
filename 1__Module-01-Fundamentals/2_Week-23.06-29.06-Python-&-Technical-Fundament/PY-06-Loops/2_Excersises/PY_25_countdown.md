# 🐍 Countdown

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Countdown von einer eingegebenen Zahl bis 1 mit abschließender "Liftoff!"-Nachricht

**Anforderungen:**
- Input: Positive Ganzzahl (User-Eingabe)
- Prompt: `"Enter countdown start number: "`
- Ausgabe: Zahlen von n bis 1 (jede Zahl in neuer Zeile)
- Finale Ausgabe: `"Liftoff!"` nach der Schleife
- Edge Cases: Annahme, dass User positive Ganzzahl eingibt

---

## Lösung

```python
# User-Eingabe
n = int(input("Enter countdown start number: "))

# Countdown-Schleife
for i in range(n, 0, -1):
    print(i)

# Liftoff-Nachricht
print("Liftoff!")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `3` | `Enter countdown start number: 3`<br>`3`<br>`2`<br>`1`<br>`Liftoff!` | `3`<br>`2`<br>`1`<br>`Liftoff!` | ✅ |
| `5` | `5`<br>`4`<br>`3`<br>`2`<br>`1`<br>`Liftoff!` | Korrekt | ✅ |
| `1` | `1`<br>`Liftoff!` | `1`<br>`Liftoff!` | ✅ |

---

## Notizen

- **Konzept:** `for`-Schleife mit `range()` und negativem Step
- **range():** `range(n, 0, -1)` zählt von n bis 1 (rückwärts)
- **Wichtig:** Zweiter Parameter `0` bedeutet "bis ausschließlich 0"
- **Alternative:** `while`-Schleife mit Dekrement