# 🐍 Shelf Management

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Manipulation einer vordefinierten Liste `shelf` durch Hinzufügen, Einfügen und Entfernen von Elementen

**Anforderungen:**
- Liste: `shelf` (vordefiniert, z.B. `["Book", "Vase", "Clock"]`)
- Operation 1: "Photo Frame" ans rechte Ende hinzufügen
- Operation 2: "Candle" zwischen "Book" und "Vase" einfügen
- Operation 3: "Clock" entfernen (falls vorhanden)
- Edge Cases: Falls "Clock" nicht vorhanden → Liste unverändert lassen

---

## Lösung

```python
# 1. "Photo Frame" ans Ende hinzufügen
shelf.append("Photo Frame")

# 2. "Candle" zwischen "Book" und "Vase" einfügen
book_index = shelf.index("Book")
shelf.insert(book_index + 1, "Candle")

# 3. "Clock" entfernen, falls vorhanden
if "Clock" in shelf:
    shelf.remove("Clock")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `shelf = ["Book", "Vase", "Clock"]` | `['Book', 'Candle', 'Vase', 'Photo Frame']` | `['Book', 'Candle', 'Vase', 'Photo Frame']` | ✅ |

---

## Notizen

- **Konzept:** List methods (`append`, `insert`, `remove`, `index`)
- **Wichtig:** Reihenfolge der Operationen beachten - erst `append`, dann `insert`, dann `remove`
- **Alternative:** Mit festen Indizes arbeiten (weniger robust)