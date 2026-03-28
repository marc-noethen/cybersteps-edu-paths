# 🐍 Get Value from Nested Dictionary

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 09.07.2025

---

## Aufgabe

**Ziel:** Funktion zum sicheren Zugriff auf Werte in verschachtelten Dictionaries

**Anforderungen:**
- Funktion: `get_value_from_nested_dict(data_dict, keys)`
- Parameter: `data_dict` (Dictionary), `keys` (Liste von Schlüsseln)
- Rückgabe: Wert (bei Erfolg), "Key not found: {key}" (KeyError), "Invalid path: Not a dictionary at key {key}" (TypeError)
- Verhalten: Sequenzieller Zugriff durch verschachtelte Dictionaries
- Edge Cases: Fehlender Schlüssel, Zugriff auf Nicht-Dictionary-Wert

---

## Lösung

```python
def get_value_from_nested_dict(data_dict, keys):
    """Greift sicher auf verschachtelte Dictionary-Werte zu."""
    current = data_dict
    
    for key in keys:
        try:
            # Prüfe ob current ein Dictionary ist
            if not isinstance(current, dict):
                return f"Invalid path: Not a dictionary at key {key}"
            current = current[key]
        except KeyError:
            return f"Key not found: {repr(key)}"
    
    return current
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `get_value_from_nested_dict({'a': {'b': {'c': 100}}}, ['a', 'b', 'c'])` | 100 | 100 | ✅ |
| `get_value_from_nested_dict({'a': {'b': {'c': 100}}}, ['a', 'x', 'c'])` | "Key not found: 'x'" | Key not found: 'x' | ✅ |
| `get_value_from_nested_dict({'a': 1}, ['a', 'b'])` | "Invalid path: Not a dictionary" | Invalid path: Not a dictionary at key b | ✅ |
| `get_value_from_nested_dict({'x': {'y': 'value'}}, ['x', 'y'])` | "value" | value | ✅ |

---

## Notizen

- **Konzept:** KeyError und TypeError Handling für Dictionary-Zugriff
- **isinstance():** Prüft ob Objekt vom Typ dict ist, bevor auf Schlüssel zugegriffen wird
- **repr(key):** Gibt String-Repräsentation mit Anführungszeichen zurück (z.B. 'x')
- **KeyError:** Tritt auf wenn Schlüssel nicht im Dictionary existiert
- **Sequential Access:** Durchläuft keys-Liste und greift schrittweise auf tiefere Ebenen zu
- **Alternative:** Rekursive Implementierung möglich
