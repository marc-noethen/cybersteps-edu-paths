# 🐍 Product Code Validation - Produktcode prüfen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Validiere Produktcode im Format `PREFIX-####-SUFFIX` mit spezifischen Regeln.

**Anforderungen:**
- Format: `PREFIX-####-SUFFIX`
- PREFIX: 3 Buchstaben, nur `INV`, `ORD`, `USR`
- ####: 4 Ziffern, Summe > 10
- SUFFIX: 2 Buchstaben, nicht `XX` oder `ZZ`

---

## Lösung

```python
# Code einlesen
code = input("Enter product code: ")

# Validierung
valid = False

# Format prüfen: genau 2 Bindestriche an richtigen Positionen
parts = code.split("-")
if len(parts) == 3:
    prefix, digits, suffix = parts
    
    # Alle Bedingungen prüfen
    if (prefix in ['INV', 'ORD', 'USR'] and      # Gültiges Prefix
        len(digits) == 4 and                      # 4 Zeichen
        digits.isdigit() and                      # Nur Ziffern
        sum(int(d) for d in digits) > 10 and     # Summe > 10
        len(suffix) == 2 and                      # 2 Zeichen
        suffix.isalpha() and                      # Nur Buchstaben
        suffix.isupper() and                      # Großbuchstaben
        suffix not in ['XX', 'ZZ']):              # Nicht XX/ZZ
        valid = True

# Ausgabe
if valid:
    print("Valid code")
else:
    print("Invalid code")
```

---

## Tests

| Input | Output | Grund | ✓ |
|-------|--------|-------|---|
| `INV-1235-AB` | `Valid code` | Alle Regeln erfüllt (1+2+3+5=11>10) | ✅ |
| `ORD-0111-CD` | `Invalid code` | Summe 0+1+1+1=3 ≤ 10 | ✅ |
| `USR-9876-XX` | `Invalid code` | Suffix `XX` verboten | ✅ |
| `ABC-1234-AB` | `Invalid code` | Prefix nicht erlaubt | ✅ |

---

## Notizen

- **`.split("-")`:** Trennt String an Bindestrichen
- **`.isdigit()`:** `True` wenn nur Ziffern
- **`.isalpha()`:** `True` wenn nur Buchstaben
- **`.isupper()`:** `True` wenn alle Großbuchstaben
- **`sum(int(d) for d in digits)`:** Ziffernsumme berechnen
