# 🐍 Formal Greeting Generator

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** Erstelle eine Funktion, die basierend auf dem Alter eine formelle Begrüßung generiert oder den Zugang verweigert

**Anforderungen:**
- Funktion: `generate_formal_greeting(name, title, age)`
- Parameter: `name` (str), `title` (str), `age` (int)
- Rückgabe: String
- Logik: Alter >= 18 → Begrüßung, Alter < 18 → "Access denied."
- Edge Cases: Genau 18 Jahre → Zugang gewährt

---

## Lösung

```python
def generate_formal_greeting(name, title, age):
    """
    Generiert eine formelle Begrüßung basierend auf Alter.
    
    Args:
        name: Name der Person (str)
        title: Titel der Person (str)
        age: Alter der Person (int)
    
    Returns:
        Begrüßungsstring oder "Access denied."
    """
    if age >= 18:
        return f"Welcome, {title} {name}!"
    else:
        return "Access denied."
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `generate_formal_greeting("Alice", "Mx.", 30)` | `"Welcome, Mx. Alice!"` | `"Welcome, Mx. Alice!"` | ✅ |
| `generate_formal_greeting("Bob", "Mr.", 17)` | `"Access denied."` | `"Access denied."` | ✅ |
| `generate_formal_greeting("Charlie", "Dr.", 18)` | `"Welcome, Dr. Charlie!"` | `"Welcome, Dr. Charlie!"` | ✅ |

---

## Notizen

- **Konzept:** Bedingte Anweisungen (`if/else`), String-Formatierung mit f-strings
- **Grenzfall:** `age >= 18` bedeutet 18 ist eingeschlossen
- **Alternative:** Ternärer Operator `return f"Welcome, {title} {name}!" if age >= 18 else "Access denied."`