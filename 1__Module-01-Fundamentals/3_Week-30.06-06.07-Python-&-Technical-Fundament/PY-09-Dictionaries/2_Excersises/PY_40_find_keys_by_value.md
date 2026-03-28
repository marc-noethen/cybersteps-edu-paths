# 🐍 Find Keys By Value - Keys nach Wert suchen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 30.06.2025

---

## Aufgabe

**Ziel:** Finde alle Keys in einem Dictionary, die einen bestimmten Wert haben.

**Anforderungen:**
- Funktion: `find_keys_by_value(data_dict, value_to_find)`
- Rückgabe: Sortierte Liste der Keys
- Edge Cases: Kein Match → leere Liste `[]`

---

## Lösung

```python
def find_keys_by_value(data_dict, value_to_find):
    """Findet alle Keys mit einem bestimmten Wert, gibt sortierte Liste zurück."""
    keys = []
    for key, value in data_dict.items():
        if value == value_to_find:
            keys.append(key)
    return sorted(keys)
```

**Alternative (List Comprehension):**
```python
def find_keys_by_value(data_dict, value_to_find):
    return sorted([k for k, v in data_dict.items() if v == value_to_find])
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `({"apple": 5, "banana": 2, "cherry": 5, "date": 1}, 5)` | `['apple', 'cherry']` | `['apple', 'cherry']` | ✅ |
| `({"apple": 5, "banana": 2, "cherry": 5, "date": 1}, 10)` | `[]` | `[]` | ✅ |
| `({}, 5)` | `[]` | `[]` | ✅ |

---

## Notizen

- **Konzept:** Dictionary iteration mit `.items()`
- **`sorted()`:** Gibt neue sortierte Liste zurück
- **List Comprehension:** `[k for k, v in dict.items() if bedingung]`
