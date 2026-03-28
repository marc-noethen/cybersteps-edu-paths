# 🐍 Count Grid Paths (Recursion)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 24.06.2025

---

## Aufgabe

**Ziel:** Berechne rekursiv die Anzahl eindeutiger Pfade von oben links nach unten rechts in einem Gitter

**Anforderungen:**
- Funktion: `count_paths(rows, cols)`
- Parameter: `rows` (int), `cols` (int) - beide >= 1
- Rückgabe: Integer (Anzahl eindeutiger Pfade)
- Bewegung: Nur **rechts** oder **runter** erlaubt
- Methode: **Rekursion**
- Edge Cases: 1×n oder n×1 Gitter → nur 1 Pfad möglich

---

## Lösung

```python
def count_paths(rows, cols):
    """
    Berechnet rekursiv die Anzahl eindeutiger Pfade in einem Gitter.
    
    Args:
        rows: Anzahl der Zeilen (int, >= 1)
        cols: Anzahl der Spalten (int, >= 1)
    
    Returns:
        Anzahl eindeutiger Pfade von (0,0) nach (rows-1, cols-1)
    """
    # Basis-Fälle: Nur eine Zeile oder eine Spalte
    if rows == 1 or cols == 1:
        return 1
    
    # Rekursiver Fall: Summe der Pfade von oben und von links
    # Von oben: ein Feld nach unten → rows-1 Zeilen bleiben
    # Von links: ein Feld nach rechts → cols-1 Spalten bleiben
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `count_paths(2, 2)` | `2` | `2` | ✅ |
| `count_paths(3, 3)` | `6` | `6` | ✅ |
| `count_paths(1, 5)` | `1` | `1` | ✅ |
| `count_paths(4, 1)` | `1` | `1` | ✅ |

---

## Notizen

- **Konzept:** Rekursion, Kombinatorik, Pfadsuche
- **Logik:** Pfade(r, c) = Pfade(r-1, c) + Pfade(r, c-1)
- **Basis:** Bei 1×n oder n×1 gibt es nur einen Pfad (geradeaus)
- **Beispiel:** 2×2 Gitter → 2 Pfade: rechts-runter, runter-rechts
- **Optimierung:** Memoization hinzufügen für größere Gitter (vermeidet Neuberechnungen)