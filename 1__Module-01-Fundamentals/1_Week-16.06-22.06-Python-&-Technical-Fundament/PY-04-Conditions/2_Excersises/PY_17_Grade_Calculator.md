# 🐍 Grade Calculator (Notenberechnung)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Punktzahl in Note umwandeln und Pass/Fail bestimmen.

**Anforderungen:**
- Prompt: `Enter score (0-100):`
- Validierung: < 0 oder > 100 → `Invalid score.`
- Notenskala:
  - 90-100: A
  - 80-89: B
  - 70-79: C
  - 60-69: D
  - 0-59: F
- D und F = Fail, sonst Pass
- Ausgabe: `Grade: <Letter> (<Pass/Fail>)`

---

## Lösung

```python
score = int(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score.")
elif score >= 90:
    print("Grade: A (Pass)")
elif score >= 80:
    print("Grade: B (Pass)")
elif score >= 70:
    print("Grade: C (Pass)")
elif score >= 60:
    print("Grade: D (Fail)")
else:
    print("Grade: F (Fail)")
```

**Alternative (mit Variablen):**
```python
score = int(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score.")
else:
    # Note bestimmen
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Pass/Fail bestimmen
    if grade in ["D", "F"]:
        status = "Fail"
    else:
        status = "Pass"
    
    print(f"Grade: {grade} ({status})")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `95` | `Grade: A (Pass)` | `Grade: A (Pass)` | ✅ |
| `82` | `Grade: B (Pass)` | `Grade: B (Pass)` | ✅ |
| `75` | `Grade: C (Pass)` | `Grade: C (Pass)` | ✅ |
| `60` | `Grade: D (Fail)` | `Grade: D (Fail)` | ✅ |
| `45` | `Grade: F (Fail)` | `Grade: F (Fail)` | ✅ |
| `100` | `Grade: A (Pass)` | `Grade: A (Pass)` | ✅ |
| `0` | `Grade: F (Fail)` | `Grade: F (Fail)` | ✅ |
| `-5` | `Invalid score.` | `Invalid score.` | ✅ |
| `105` | `Invalid score.` | `Invalid score.` | ✅ |

---

## Notenskala-Übersicht

| Punkte | Note | Status |
|--------|------|--------|
| 90-100 | A | Pass ✅ |
| 80-89 | B | Pass ✅ |
| 70-79 | C | Pass ✅ |
| 60-69 | D | Fail ❌ |
| 0-59 | F | Fail ❌ |

---

## Notizen

- **Konzept:** Input-Validierung, mehrstufige Bedingungen
- **Reihenfolge:** Von oben nach unten prüfen (90 → 80 → 70 → 60 → else)
- **Warum `>=` funktioniert:** 
  - Bei `score = 85` wird `score >= 90` False
  - Dann wird `score >= 80` True → "B"
  - Die restlichen Bedingungen werden nicht geprüft

- **`in` Operator:** Prüft ob Element in Liste enthalten ist
  ```python
  grade in ["D", "F"]  # True wenn grade D oder F ist
  ```

- **Grenzwerte testen:** Immer 0, 59, 60, 69, 70, 79, 80, 89, 90, 100 testen!
