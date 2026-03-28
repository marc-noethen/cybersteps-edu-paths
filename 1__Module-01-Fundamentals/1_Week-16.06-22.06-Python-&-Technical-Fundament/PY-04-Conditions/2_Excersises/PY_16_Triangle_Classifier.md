# 🐍 Triangle Classifier (Dreieck-Klassifizierung)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Drei Seitenlängen einlesen, prüfen ob ein Dreieck möglich ist, und es klassifizieren.

**Anforderungen:**
- Prompt 1: `Enter length of side 1:`
- Prompt 2: `Enter length of side 2:`
- Prompt 3: `Enter length of side 3:`
- Dreieck-Ungleichung prüfen: Summe zweier Seiten > dritte Seite
- Seiten ≤ 0 → Kein Dreieck
- Ausgabe:
  - `Cannot form a triangle.`
  - `Equilateral triangle` (alle gleich)
  - `Isosceles triangle` (zwei gleich)
  - `Scalene triangle` (alle verschieden)

---

## Lösung

```python
s1 = int(input("Enter length of side 1: "))
s2 = int(input("Enter length of side 2: "))
s3 = int(input("Enter length of side 3: "))

# Prüfe auf positive Werte und Dreiecksungleichung
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Cannot form a triangle.")
elif s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print("Cannot form a triangle.")
elif s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
```

**Alternative (kompakter):**
```python
s1 = int(input("Enter length of side 1: "))
s2 = int(input("Enter length of side 2: "))
s3 = int(input("Enter length of side 3: "))

# Kombinierte Prüfung
if s1 <= 0 or s2 <= 0 or s3 <= 0 or s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print("Cannot form a triangle.")
elif s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
```

---

## Tests

| Side 1 | Side 2 | Side 3 | Erwartet | Ergebnis | ✓ |
|--------|--------|--------|----------|----------|---|
| `3` | `3` | `3` | `Equilateral triangle` | `Equilateral triangle` | ✅ |
| `5` | `5` | `3` | `Isosceles triangle` | `Isosceles triangle` | ✅ |
| `3` | `4` | `5` | `Scalene triangle` | `Scalene triangle` | ✅ |
| `1` | `2` | `10` | `Cannot form a triangle.` | `Cannot form a triangle.` | ✅ |
| `0` | `5` | `5` | `Cannot form a triangle.` | `Cannot form a triangle.` | ✅ |
| `-1` | `3` | `3` | `Cannot form a triangle.` | `Cannot form a triangle.` | ✅ |
| `1` | `1` | `2` | `Cannot form a triangle.` | `Cannot form a triangle.` | ✅ |

---

## Dreieck-Typen erklärt

| Typ | Deutsch | Eigenschaft |
|-----|---------|-------------|
| Equilateral | Gleichseitig | Alle 3 Seiten gleich |
| Isosceles | Gleichschenklig | Genau 2 Seiten gleich |
| Scalene | Ungleichseitig | Alle 3 Seiten verschieden |

**Dreiecksungleichung:**
```
a + b > c
a + c > b
b + c > a
```
Alle drei Bedingungen müssen erfüllt sein!

---

## Notizen

- **Konzept:** Mehrfache Bedingungen, Verkettete Vergleiche
- **Verkettung:** `s1 == s2 == s3` ist gültig in Python!
- **Reihenfolge wichtig:**
  1. Erst prüfen ob Dreieck möglich
  2. Dann klassifizieren
- **Edge Cases:**
  - Seite ≤ 0 → Kein Dreieck
  - `a + b = c` (Summe gleich) → Kein Dreieck (muss **größer** sein)

- **Tipp:** Bei `or` wird die erste wahre Bedingung genommen (Short-Circuit)
