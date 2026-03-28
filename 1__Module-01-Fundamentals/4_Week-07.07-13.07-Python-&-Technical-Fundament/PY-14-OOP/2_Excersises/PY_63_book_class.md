# 🐍 Book Class - Einfache Klasse mit Attributen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 09.07.2025

---

## Aufgabe

**Ziel:** Einfache Klasse zur Repräsentation eines Buches mit Titel und Autor

**Anforderungen:**
- Klasse: `Book`
- `__init__(self, title, author)`: Initialisiert Attribute
- `get_details(self)`: Gibt formatierte Buchdetails zurück
- Rückgabe: String im Format "Title: [title], Author: [author]"
- Edge Cases: Keine besonderen Edge Cases

---

## Lösung

```python
class Book:
    """Repräsentiert ein Buch mit Titel und Autor."""
    
    def __init__(self, title, author):
        """Initialisiert ein Buch mit Titel und Autor."""
        self.title = title
        self.author = author
    
    def get_details(self):
        """Gibt die Buchdetails als formatierten String zurück."""
        return f"Title: {self.title}, Author: {self.author}"
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams").get_details()` | "Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams" | Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams | ✅ |
| `Book("1984", "George Orwell").get_details()` | "Title: 1984, Author: George Orwell" | Title: 1984, Author: George Orwell | ✅ |

---

## Notizen

- **Konzept:** Grundlegende Klassenstruktur mit `__init__` Konstruktor
- **self:** Referenz auf die Instanz selbst
- **Attribute:** `self.title` und `self.author` speichern Instanz-spezifische Daten
- **f-String:** Moderne String-Formatierung in Python
