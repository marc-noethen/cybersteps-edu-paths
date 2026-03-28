# 🐍 Shape Inheritance - Vererbung und Polymorphismus

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 10.07.2025

---

## Aufgabe

**Ziel:** Implementierung einer Vererbungshierarchie für geometrische Formen

**Anforderungen:**
- Basisklasse: `Shape` mit abstrakter Methode `calculate_area()`
- Subklasse: `Rectangle(width, height)` - Berechnet Rechteck-Fläche
- Subklasse: `Circle(radius)` - Berechnet Kreis-Fläche (auf 4 Dezimalstellen gerundet)
- Rückgabe: Float (Flächeninhalt)
- Edge Cases: Basis-Methode wirft NotImplementedError

---

## Lösung

```python
import math

class Shape:
    """Basisklasse für geometrische Formen."""
    
    def calculate_area(self):
        """Muss von Subklassen implementiert werden."""
        raise NotImplementedError("Subclass must implement this method")


class Rectangle(Shape):
    """Rechteck mit Breite und Höhe."""
    
    def __init__(self, width, height):
        """Initialisiert Rechteck mit Breite und Höhe."""
        self.width = width
        self.height = height
    
    def calculate_area(self):
        """Berechnet die Fläche des Rechtecks."""
        return self.width * self.height


class Circle(Shape):
    """Kreis mit Radius."""
    
    def __init__(self, radius):
        """Initialisiert Kreis mit Radius."""
        self.radius = radius
    
    def calculate_area(self):
        """Berechnet die Fläche des Kreises (gerundet auf 4 Dezimalstellen)."""
        return round(math.pi * self.radius ** 2, 4)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `Rectangle(5, 10).calculate_area()` | 50 | 50 | ✅ |
| `Circle(8).calculate_area()` | 201.0619 | 201.0619 | ✅ |
| `Rectangle(3, 7).calculate_area()` | 21 | 21 | ✅ |
| `Circle(5).calculate_area()` | 78.5398 | 78.5398 | ✅ |

---

## Notizen

- **Konzept:** Vererbung (Inheritance) und Methodenüberschreibung (Override)
- **NotImplementedError:** Erzwingt Implementierung in Subklassen (Abstract Method Pattern)
- **math.pi:** Konstante für π (≈ 3.14159...)
- **round(x, 4):** Rundet auf 4 Nachkommastellen
- **Polymorphismus:** Verschiedene Formen implementieren gleiche Schnittstelle unterschiedlich
- **Alternative:** Abstract Base Classes (ABC) mit `@abstractmethod` Decorator
