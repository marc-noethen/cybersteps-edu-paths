# 🐍 Rectangle Area (Typkonvertierung)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Rechteckfläche aus Benutzereingaben berechnen.

**Anforderungen:**
- Prompt 1: `Enter length:`
- Prompt 2: `Enter width:`
- Berechnung: `Fläche = Länge × Breite`
- Ausgabe: `The area is: [Area]`
- Wichtig: `int()` für Typkonvertierung verwenden

---

## Lösung

```python
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("The area is:", area)
```

**Alternative Lösungen:**
```python
# Mit f-String
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print(f"The area is: {length * width}")

# Mit float für Dezimalzahlen
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("The area is:", area)

# Mit separater Konvertierung
length_str = input("Enter length: ")
width_str = input("Enter width: ")
length = int(length_str)
width = int(width_str)
area = length * width
print("The area is:", area)
```

---

## Tests

| Length | Width | Erwartet | Ergebnis | ✓ |
|--------|-------|----------|----------|---|
| `5` | `4` | `The area is: 20` | `The area is: 20` | ✅ |
| `10` | `10` | `The area is: 100` | `The area is: 100` | ✅ |
| `7` | `3` | `The area is: 21` | `The area is: 21` | ✅ |

---

## Notizen

- **Konzept:** Typkonvertierung (Type Casting)
- **Wichtig:** `input()` gibt IMMER einen String zurück!
- **`int()`:** Konvertiert String zu Ganzzahl
- **`float()`:** Konvertiert String zu Dezimalzahl
- **Fehler ohne `int()`:** `"5" * "4"` → TypeError!
- **String-Multiplikation:** `"5" * 4` → `"5555"` (Wiederholung)

**Typkonvertierungs-Funktionen:**
| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `int()` | String → Ganzzahl | `int("42")` → `42` |
| `float()` | String → Dezimalzahl | `float("3.14")` → `3.14` |
| `str()` | Zahl → String | `str(42)` → `"42"` |
