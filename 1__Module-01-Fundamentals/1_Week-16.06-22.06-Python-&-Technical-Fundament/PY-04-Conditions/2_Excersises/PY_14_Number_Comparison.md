# 🐍 Number Comparison (Zahlenvergleich)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Zwei Ganzzahlen vergleichen und das größere ausgeben.

**Anforderungen:**
- Prompt 1: `Enter the first integer:`
- Prompt 2: `Enter the second integer:`
- Ausgabe je nach Vergleich:
  - `First number is larger.`
  - `Second number is larger.`
  - `The numbers are equal.`

---

## Lösung

```python
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first > second:
    print("First number is larger.")
elif second > first:
    print("Second number is larger.")
else:
    print("The numbers are equal.")
```

**Alternative mit Variablen:**
```python
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    result = "First number is larger."
elif num1 < num2:
    result = "Second number is larger."
else:
    result = "The numbers are equal."

print(result)
```

---

## Tests

| Input 1 | Input 2 | Erwartet | Ergebnis | ✓ |
|---------|---------|----------|----------|---|
| `10` | `5` | `First number is larger.` | `First number is larger.` | ✅ |
| `7` | `12` | `Second number is larger.` | `Second number is larger.` | ✅ |
| `8` | `8` | `The numbers are equal.` | `The numbers are equal.` | ✅ |
| `-5` | `-10` | `First number is larger.` | `First number is larger.` | ✅ |
| `0` | `0` | `The numbers are equal.` | `The numbers are equal.` | ✅ |

---

## Notizen

- **Konzept:** `if`, `elif`, `else` Kontrollstrukturen
- **Vergleichsoperatoren:**

| Operator | Bedeutung |
|----------|-----------|
| `>` | Größer als |
| `<` | Kleiner als |
| `>=` | Größer oder gleich |
| `<=` | Kleiner oder gleich |
| `==` | Gleich |
| `!=` | Ungleich |

- **Wichtig:** `=` ist Zuweisung, `==` ist Vergleich!
- **Einrückung:** Code-Block nach `:` muss eingerückt sein (4 Leerzeichen)
