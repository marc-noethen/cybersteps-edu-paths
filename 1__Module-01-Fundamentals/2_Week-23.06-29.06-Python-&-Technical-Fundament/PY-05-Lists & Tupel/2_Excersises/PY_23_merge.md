# 🐍 Merge and Remove Middle

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Zwei sortierte Listen zusammenführen und das mittlere Element entfernen

**Anforderungen:**
- Listen: `list_a`, `list_b` (beide vordefiniert und sortiert)
- Rückgabe: Liste `merged_list`
- Schritt 1: Beide Listen zu einer sortierten Liste vereinen
- Schritt 2: Mittleres Element entfernen
  - Ungerade Anzahl: Mittleres Element (Index `len//2`)
  - Gerade Anzahl: Element vor der Mitte (Index `len//2 - 1`)
- Edge Cases: Leere Liste → bleibt leer; 1 Element → wird leer

---

## Lösung

```python
# 1. Listen zusammenführen und sortieren
merged_list = sorted(list_a + list_b)

# 2. Mittleres Element entfernen
if len(merged_list) > 0:
    # Berechne Index des zu entfernenden Elements
    if len(merged_list) % 2 == 1:
        # Ungerade: mittleres Element
        middle_index = len(merged_list) // 2
    else:
        # Gerade: Element vor der Mitte
        middle_index = len(merged_list) // 2 - 1
    
    # Element entfernen
    del merged_list[middle_index]
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `list_a = [1, 4, 7]`<br>`list_b = [2, 5, 8]` | `[1, 2, 5, 7, 8]` | `[1, 2, 5, 7, 8]` | ✅ |
| `list_a = [1]`<br>`list_b = [2, 3]` | `[2, 3]` | `[2, 3]` | ✅ |
| `list_a = []`<br>`list_b = []` | `[]` | `[]` | ✅ |

---

## Notizen

- **Konzept:** List concatenation mit `+`, `sorted()`, `del`, Modulo-Operation
- **Indexberechnung:** 
  - Ungerade (z.B. 5 Elemente): Index 2 (mittleres)
  - Gerade (z.B. 6 Elemente): Index 2 (vor der Mitte)
- **Alternative:** `merged_list.pop(middle_index)` statt `del`