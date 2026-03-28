# 🐍 Number Triangle

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Drucke ein Zahlen-Dreieck mit n Zeilen, wobei Zeile i die Zahlen 1 bis i enthält

**Anforderungen:**
- Input: Positive Ganzzahl `n` (User-Eingabe)
- Prompt: `"Enter the number of rows: "`
- Ausgabe: Dreieck mit n Zeilen
- Format: Zeile i enthält Zahlen 1 bis i, durch Leerzeichen getrennt
- Edge Cases: n = 1 → nur eine Zeile mit "1"

---

## Lösung

```python
# User-Eingabe
n = int(input("Enter the number of rows: "))

# Nested Loop für Dreieck
for i in range(1, n + 1):
    # Zahlen von 1 bis i ausgeben
    row = []
    for j in range(1, i + 1):
        row.append(str(j))
    print(" ".join(row))
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `4` | `Enter the number of rows: 4`<br>`1`<br>`1 2`<br>`1 2 3`<br>`1 2 3 4` | Korrekt | ✅ |
| `1` | `Enter the number of rows: 1`<br>`1` | `1` | ✅ |
| `3` | `1`<br>`1 2`<br>`1 2 3` | Korrekt | ✅ |

---

## Notizen

- **Konzept:** Verschachtelte Schleifen (Nested Loops), `range()`, String-Manipulation
- **Äußere Schleife:** Iteriert über Zeilen (1 bis n)
- **Innere Schleife:** Erzeugt Zahlen für aktuelle Zeile (1 bis i)
- **Alternative:** `print(" ".join(str(j) for j in range(1, i + 1)))` (kompakter)