# 🐍 Sum Calculator (Zwei Zahlen addieren)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Zwei Zahlen vom Benutzer einlesen und deren Summe berechnen.

**Anforderungen:**
- Prompt 1: `Enter first number: `
- Prompt 2: `Enter second number: `
- Berechnung: Summe der beiden Zahlen
- Eingaben als Ganzzahlen (`int`) behandeln

---

## Lösung

```python
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
calc = first_num + second_num
print(calc)
```

**Alternative Lösungen:**
```python
# Mit f-String Ausgabe
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
print(f"The sum is: {first_num + second_num}")

# Kompakt (nicht empfohlen für Lesbarkeit)
print(int(input("Enter first number: ")) + int(input("Enter second number: ")))
```

---

## Tests

| Input 1 | Input 2 | Erwartet | Ergebnis | ✓ |
|---------|---------|----------|----------|---|
| `5` | `3` | `8` | `8` | ✅ |
| `10` | `20` | `30` | `30` | ✅ |
| `-5` | `5` | `0` | `0` | ✅ |
| `0` | `0` | `0` | `0` | ✅ |

---

## Notizen

- **Konzept:** Typkonvertierung mit `int()` und arithmetische Operationen
- **Wichtig:** Ohne `int()` würde `"5" + "3"` = `"53"` (String-Konkatenation!)
- **Arithmetische Operatoren:**
  - `+` Addition
  - `-` Subtraktion
  - `*` Multiplikation
  - `/` Division (Ergebnis: float)
  - `//` Ganzzahldivision
  - `%` Modulo (Rest)
  - `**` Potenz
