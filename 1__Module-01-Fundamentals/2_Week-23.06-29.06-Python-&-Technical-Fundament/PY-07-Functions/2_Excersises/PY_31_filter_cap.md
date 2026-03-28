# 🐍 Filter and Capitalize by Length

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** Filtere Wörter nach Mindestlänge und wandle sie in Großbuchstaben um

**Anforderungen:**
- Funktion: `filter_cap_by_length(words, min_length)`
- Parameter: `words` (Liste von Strings), `min_length` (int)
- Rückgabe: Neue Liste mit gefilterten und großgeschriebenen Wörtern
- Filter: Nur Wörter mit Länge >= min_length
- Transformation: Alle Wörter in GROSSBUCHSTABEN (.upper())
- Edge Cases: Keine passenden Wörter → leere Liste []

---

## Lösung

```python
def filter_cap_by_length(words, min_length):
    """
    Filtert Wörter nach Mindestlänge und wandelt sie in Großbuchstaben um.
    
    Args:
        words: Liste von Strings
        min_length: Minimale Wortlänge (int)
    
    Returns:
        Neue Liste mit gefilterten, großgeschriebenen Wörtern
    """
    result = []
    for word in words:
        if len(word) >= min_length:
            result.append(word.upper())
    
    return result
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `filter_cap_by_length(["apple", "banana", "kiwi", "orange", "grape"], 5)` | `['APPLE', 'BANANA', 'ORANGE', 'GRAPE']` | `['APPLE', 'BANANA', 'ORANGE', 'GRAPE']` | ✅ |
| `filter_cap_by_length(["a", "b", "c"], 2)` | `[]` | `[]` | ✅ |
| `filter_cap_by_length(["test"], 4)` | `['TEST']` | `['TEST']` | ✅ |

---

## Notizen

- **Konzept:** List filtering, String-Methoden (`.upper()`), `len()`
- **Wichtig:** Neue Liste erstellen, Original nicht verändern
- **Reihenfolge:** Original-Reihenfolge beibehalten
- **Alternative (List Comprehension):** `return [word.upper() for word in words if len(word) >= min_length]`