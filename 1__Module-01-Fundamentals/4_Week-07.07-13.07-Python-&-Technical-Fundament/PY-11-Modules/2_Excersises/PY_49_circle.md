# 🐍 Circle Properties Calculator

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Berechnung von Kreiseigenschaften (Durchmesser, Umfang, Fläche) basierend auf dem Radius

**Anforderungen:**
- Funktion: `calculate_circle_properties(radius)`
- Parameter: Nicht-negative Zahl (Radius)
- Rückgabe: Tuple mit (Durchmesser, Umfang, Fläche)
- Edge Cases: Verwendung von math.pi für präzise Berechnungen

---

## Lösung

```python
import math

def calculate_circle_properties(radius):
    """Berechnet Durchmesser, Umfang und Fläche eines Kreises."""
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    return (diameter, circumference, area)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `calculate_circle_properties(10)` | `(20.0, 62.83185307179586, 314.1592653589793)` | `(20.0, 62.83185307179586, 314.1592653589793)` | ✅ |
| `calculate_circle_properties(5)` | `(10.0, 31.41592653589793, 78.53981633974483)` | `(10.0, 31.41592653589793, 78.53981633974483)` | ✅ |
| `calculate_circle_properties(0)` | `(0, 0.0, 0.0)` | `(0, 0.0, 0.0)` | ✅ |

---

## Notizen

- **Konzept:** Verwendung von `math.pi` für präzise Berechnungen
- **Formeln:** Durchmesser = 2r, Umfang = 2πr, Fläche = πr²
- **Alternative:** `math.tau` (= 2π) für Umfang