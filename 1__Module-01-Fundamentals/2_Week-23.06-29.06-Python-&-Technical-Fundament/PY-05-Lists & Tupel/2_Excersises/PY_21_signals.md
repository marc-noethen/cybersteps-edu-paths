# 🐍 Signal Analysis

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 23.06.2025

---

## Aufgabe

**Ziel:** Analyse einer Liste von Signalen (0 und 1) - Anzahl, erster und letzter Index von 1en finden

**Anforderungen:**
- Liste: `signals` (vordefiniert, z.B. `[0, 1, 1, 0, 1]`)
- Variable 1: `count_of_ones` - Anzahl der 1en
- Variable 2: `first_index` - Index der ersten 1
- Variable 3: `last_index` - Index der letzten 1
- Edge Cases: Keine 1en vorhanden → `first_index = -1`, `last_index = -1`

---

## Lösung

```python
# 1. Anzahl der 1en zählen
count_of_ones = signals.count(1)

# 2. Index der ersten 1
if 1 in signals:
    first_index = signals.index(1)
else:
    first_index = -1

# 3. Index der letzten 1
if 1 in signals:
    # Von hinten suchen
    last_index = len(signals) - 1 - signals[::-1].index(1)
else:
    last_index = -1
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `signals = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]` | `count_of_ones = 6`<br>`first_index = 1`<br>`last_index = 9` | `6, 1, 9` | ✅ |
| `signals = [0, 0, 0]` | `count_of_ones = 0`<br>`first_index = -1`<br>`last_index = -1` | `0, -1, -1` | ✅ |

---

## Notizen

- **Konzept:** `count()`, `index()`, List slicing mit `[::-1]`
- **Trick:** Für letzten Index Liste umkehren und von vorne suchen
- **Alternative:** Mit Schleife von hinten iterieren (expliziter)