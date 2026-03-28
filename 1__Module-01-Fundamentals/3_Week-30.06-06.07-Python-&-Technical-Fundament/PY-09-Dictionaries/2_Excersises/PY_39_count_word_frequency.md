# 🐍 Count Word Frequency - Worthäufigkeit zählen

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 30.06.2025

---

## Aufgabe

**Ziel:** Zähle wie oft jedes Wort in einem Text vorkommt (case-insensitive).

**Anforderungen:**
- Funktion: `count_word_frequency(text)`
- Rückgabe: Dictionary `{wort: anzahl}`
- Edge Cases: Groß-/Kleinschreibung ignorieren

---

## Lösung

```python
def count_word_frequency(text):
    """Zählt Worthäufigkeiten in einem Text (case-insensitive)."""
    frequency = {}
    words = text.lower().split()
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency
```

**Alternative (kürzer):**
```python
def count_word_frequency(text):
    frequency = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `"This is a test sentence this test is simple"` | `{'this': 2, 'is': 2, 'a': 1, 'test': 2, 'sentence': 1, 'simple': 1}` | ✓ | ✅ |
| `""` | `{}` | `{}` | ✅ |
| `"Hello"` | `{'hello': 1}` | `{'hello': 1}` | ✅ |

---

## Notizen

- **Konzept:** Dictionary als Zähler, `str.lower()`, `str.split()`
- **`.get(key, default)`:** Gibt `default` zurück wenn Key nicht existiert
- **Alternative:** `collections.Counter(text.lower().split())`
