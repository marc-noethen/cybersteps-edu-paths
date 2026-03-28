# 🐍 Leap Year Calculator (Schaltjahr-Berechnung)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Bestimmen, ob ein Jahr ein Schaltjahr ist.

**Anforderungen:**
- Prompt: `Enter a year:`
- Schaltjahr-Regeln:
  - Durch 4 teilbar → Schaltjahr, **AUSSER**
  - Durch 100 teilbar → KEIN Schaltjahr, **AUSSER**
  - Durch 400 teilbar → Schaltjahr
- Ausgabe: `<Year> is a leap year.` oder `<Year> is not a leap year.`

---

## Lösung

```python
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

**Alternative (ausführlicher):**
```python
year = int(input("Enter a year: "))

if year % 400 == 0:
    # Durch 400 teilbar → Schaltjahr
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    # Durch 100 teilbar (aber nicht 400) → KEIN Schaltjahr
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    # Durch 4 teilbar (aber nicht 100) → Schaltjahr
    print(f"{year} is a leap year.")
else:
    # Nicht durch 4 teilbar → KEIN Schaltjahr
    print(f"{year} is not a leap year.")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `2000` | `2000 is a leap year.` | `2000 is a leap year.` | ✅ |
| `1900` | `1900 is not a leap year.` | `1900 is not a leap year.` | ✅ |
| `2024` | `2024 is a leap year.` | `2024 is a leap year.` | ✅ |
| `2023` | `2023 is not a leap year.` | `2023 is not a leap year.` | ✅ |
| `2100` | `2100 is not a leap year.` | `2100 is not a leap year.` | ✅ |

---

## Schaltjahr-Logik erklärt

```
Jahr eingegeben
    │
    ├─ Durch 400 teilbar? ──── JA ──→ SCHALTJAHR ✓
    │         │
    │        NEIN
    │         │
    ├─ Durch 100 teilbar? ──── JA ──→ KEIN Schaltjahr ✗
    │         │
    │        NEIN
    │         │
    └─ Durch 4 teilbar? ────── JA ──→ SCHALTJAHR ✓
              │
             NEIN
              │
              └──────────────────────→ KEIN Schaltjahr ✗
```

---

## Notizen

- **Konzept:** Verschachtelte Bedingungen, Modulo-Operator
- **Modulo `%`:** Gibt den Rest einer Division zurück
  - `2000 % 400 == 0` → True (kein Rest)
  - `1900 % 400 == 300` → False (Rest 300)
- **Logische Operatoren:**

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `and` | UND | `a > 0 and b > 0` |
| `or` | ODER | `a > 0 or b > 0` |
| `not` | NICHT | `not a > 0` |

- **Tipp:** Reihenfolge der Prüfung ist wichtig (400 vor 100 vor 4)!
