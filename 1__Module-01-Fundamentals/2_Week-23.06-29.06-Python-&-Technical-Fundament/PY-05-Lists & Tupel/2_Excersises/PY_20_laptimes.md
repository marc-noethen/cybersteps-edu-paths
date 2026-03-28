# 🐍 Lap Times Analysis

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Eine neue Rundenzeit hinzufügen, schnellste/langsamste Zeit finden und Differenz berechnen

**Anforderungen:**
- Listen: `lap_times` (vordefiniert), `new_lap` (float, vordefiniert)
- Rückgabe: Variable `difference` (float)
- Schritte: Neue Zeit hinzufügen, Min/Max finden, Differenz berechnen und ausgeben
- Edge Cases: Weniger als 2 Elemente → `difference = 0.0`

---

## Lösung

```python
# 1. Neue Rundenzeit hinzufügen
lap_times.append(new_lap)

# 2-4. Differenz berechnen
if len(lap_times) < 2:
    difference = 0.0
else:
    fastest = min(lap_times)
    slowest = max(lap_times)
    difference = slowest - fastest

# 5. Differenz ausgeben
print(difference)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `lap_times = [65.2, 68.1, 71.5, 66.1]`<br>`new_lap = 65` | `6.5` | `6.5` | ✅ |
| `lap_times = []`<br>`new_lap = 65.0` | `0.0` | `0.0` | ✅ |

---

## Notizen

- **Konzept:** `min()`, `max()`, List manipulation, Edge Case Handling
- **Edge Case:** Bei weniger als 2 Elementen gibt es keine sinnvolle Differenz
- **Alternative:** Liste sortieren statt `min()`/`max()` (ineffizienter)