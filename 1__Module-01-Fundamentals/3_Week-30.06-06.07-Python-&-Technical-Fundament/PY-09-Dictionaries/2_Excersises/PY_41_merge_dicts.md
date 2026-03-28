# 🐍 Merge Dicts - Dictionaries zusammenführen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Führe `dict2` in `dict1` zusammen (in-place). Bei gleichen Keys überschreibt `dict2`.

**Anforderungen:**
- Funktion: `merge_dicts(dict1, dict2)`
- Rückgabe: Modifiziertes `dict1`
- Wichtig: **In-place** Modifikation (kein neues Dict)

---

## Lösung

```python
def merge_dicts(dict1, dict2):
    """Merged dict2 in dict1 (in-place). dict2 überschreibt bei Konflikten."""
    for key, value in dict2.items():
        dict1[key] = value
    return dict1
```

**Alternative (mit .update()):**
```python
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1
```

---

## Tests

| Test | Ergebnis | ✓ |
|------|----------|---|
| `d1 = {'a': 10, 'b': 20}` | - | - |
| `merge_dicts(d1, {'b': 30, 'c': 40})` | `{'a': 10, 'b': 30, 'c': 40}` | ✅ |
| `d1 is returned_dict` | `True` (gleiches Objekt) | ✅ |

---

## Notizen

- **In-place:** Das Original-Dict wird verändert, kein neues erstellt
- **`.update()`:** Eingebaute Methode für Dictionary-Merge
- **Überschreiben:** Bei gleichen Keys gewinnt `dict2`
- **`is` vs `==`:** `is` prüft Identität (gleiches Objekt), `==` prüft Wert
