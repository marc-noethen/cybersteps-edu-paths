# 🐍 Invert Dictionary - Dictionary umkehren

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Kehre ein Dictionary um: Werte werden Keys, Keys werden Listen von Werten.

**Anforderungen:**
- Funktion: `invert_dictionary(d)`
- Rückgabe: Neues Dict `{alter_wert: [alte_keys]}`
- Edge Cases: Mutable Werte (Listen, Dicts) überspringen

---

## Lösung

```python
def is_hashable(obj):
    """Prüft ob ein Objekt hashbar (immutable) ist."""
    try:
        hash(obj)
        if isinstance(obj, tuple):
            return all(is_hashable(el) for el in obj)
        return True
    except TypeError:
        return False

def invert_dictionary(d):
    """Kehrt Dictionary um. Mutable Werte werden übersprungen."""
    inverted = {}
    
    for key, value in d.items():
        # Nur hashbare (immutable) Werte als neue Keys
        if not is_hashable(value):
            continue
        
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    
    return inverted
```

**Alternative (mit .setdefault()):**
```python
def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        if is_hashable(value):
            inverted.setdefault(value, []).append(key)
    return inverted
```

---

## Tests

| Input | Erwartet | ✓ |
|-------|----------|---|
| `{"a": 1, "b": 2, "c": 1, "d": [3,4], "e": 2}` | `{1: ['a', 'c'], 2: ['b', 'e']}` | ✅ |
| `{}` | `{}` | ✅ |
| `{"x": (1, 2)}` | `{(1, 2): ['x']}` | ✅ |

---

## Notizen

- **Hashbar:** Strings, Integers, Floats, Booleans, Tuples (mit hashbaren Elementen)
- **Nicht hashbar:** Listen, Dicts, Sets → können keine Dict-Keys sein
- **`hash()`:** Wirft `TypeError` bei nicht-hashbaren Objekten
- **Mehrere Keys → gleicher Wert:** Werden in Liste gesammelt
