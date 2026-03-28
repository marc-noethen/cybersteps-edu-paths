# 🐍 Discount System (Rabattsystem)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Rabattsystem mit gestapelten Rabatten implementieren.

**Anforderungen:**
- Prompt 1: `Enter purchase amount (EUR):`
- Prompt 2: `Do you have a membership card (yes/no)?`
- Rabatt-Regeln:
  - Betrag > 50.0 EUR → 10% Rabatt
  - Mitgliedskarte (`yes`) → zusätzlich 5% Rabatt
  - Beide Rabatte werden auf den **Originalbetrag** berechnet
- Ausgabe: `Final price: XX.XX EUR` (2 Nachkommastellen)

---

## Lösung

```python
amount = float(input("Enter purchase amount (EUR): "))
membership = input("Do you have a membership card (yes/no)? ")

discount = 0

# 10% Rabatt wenn Betrag > 50
if amount > 50.0:
    discount += amount * 0.10

# 5% Rabatt für Mitglieder (immer auf Originalbetrag)
if membership == "yes":
    discount += amount * 0.05

final_price = amount - discount
print(f"Final price: {final_price:.2f} EUR")
```

**Alternative (mit Prozent-Variable):**
```python
amount = float(input("Enter purchase amount (EUR): "))
membership = input("Do you have a membership card (yes/no)? ")

discount_percent = 0

if amount > 50.0:
    discount_percent += 10

if membership == "yes":
    discount_percent += 5

final_price = amount * (1 - discount_percent / 100)
print(f"Final price: {final_price:.2f} EUR")
```

---

## Tests

| Amount | Membership | Rabatt | Erwartet | Ergebnis | ✓ |
|--------|------------|--------|----------|----------|---|
| `60.0` | `yes` | 10% + 5% = 15% | `Final price: 51.00 EUR` | `Final price: 51.00 EUR` | ✅ |
| `40.0` | `yes` | 0% + 5% = 5% | `Final price: 38.00 EUR` | `Final price: 38.00 EUR` | ✅ |
| `100.0` | `no` | 10% + 0% = 10% | `Final price: 90.00 EUR` | `Final price: 90.00 EUR` | ✅ |
| `50.0` | `yes` | 0% + 5% = 5% | `Final price: 47.50 EUR` | `Final price: 47.50 EUR` | ✅ |
| `50.0` | `no` | 0% | `Final price: 50.00 EUR` | `Final price: 50.00 EUR` | ✅ |
| `30.0` | `no` | 0% | `Final price: 30.00 EUR` | `Final price: 30.00 EUR` | ✅ |

---

## Rabatt-Berechnung erklärt

**Beispiel: 60.0 EUR mit Mitgliedskarte**
```
Originalbetrag:     60.00 EUR
10% Rabatt (>50):   60.00 × 0.10 = 6.00 EUR
5% Mitglied:        60.00 × 0.05 = 3.00 EUR
─────────────────────────────────────────
Gesamtrabatt:       6.00 + 3.00 = 9.00 EUR
Endpreis:           60.00 - 9.00 = 51.00 EUR
```

**Wichtig:** Beide Rabatte werden auf den **Originalbetrag** berechnet, nicht nacheinander!

---

## Rabatt-Matrix

| Betrag | Mitglied | Rabatt |
|--------|----------|--------|
| ≤ 50 | no | 0% |
| ≤ 50 | yes | 5% |
| > 50 | no | 10% |
| > 50 | yes | 15% |

---

## Notizen

- **Konzept:** Mehrere unabhängige `if`-Bedingungen (keine `elif`!)
- **Wichtig:** `>` (strikt größer) nicht `>=`! 50.0 EUR bekommt KEINEN 10%-Rabatt
- **`+=` Operator:** `discount += x` ist gleich `discount = discount + x`
- **Formatierung:** `:.2f` für genau 2 Nachkommastellen

**Unterschied `if` vs `elif`:**
```python
# Mit elif - nur EINE Bedingung wird ausgeführt
if amount > 50:
    # ...
elif membership == "yes":
    # Wird NICHT geprüft wenn amount > 50!

# Mit separaten if - BEIDE werden geprüft
if amount > 50:
    # ...
if membership == "yes":
    # Wird AUCH geprüft!
```

- **Tipp:** Separates `if` wenn Bedingungen unabhängig sind und sich stapeln können!
