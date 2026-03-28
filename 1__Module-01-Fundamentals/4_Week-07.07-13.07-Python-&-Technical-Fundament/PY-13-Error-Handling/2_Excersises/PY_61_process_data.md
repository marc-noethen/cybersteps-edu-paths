# 🐍 Process Data List with Try-Except-Finally

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 09.07.2025

---

## Aufgabe

**Ziel:** Funktion zur Berechnung der Summe von Reziproken mit detailliertem Error Handling

**Anforderungen:**
- Funktion: `process_data_list(data)`
- Parameter: `data` (Liste mit gemischten Datentypen)
- Rückgabe: Float (Summe aller erfolgreichen Reziproken)
- Verhalten: Try-Except-Finally Struktur für jedes Element
  - Try: Berechne 1.0/item und addiere zur Summe
  - Except: Fange TypeError und ZeroDivisionError, gebe Fehlermeldung aus
  - Finally: Gebe "Finished processing item: {item}" aus
- Edge Cases: Nicht-numerische Werte, Division durch Null

---

## Lösung

```python
def process_data_list(data):
    """Berechnet Summe der Reziproken mit Try-Except-Finally Error Handling."""
    total = 0.0
    
    for item in data:
        try:
            reciprocal = 1.0 / item
            total += reciprocal
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error processing {item}: {str(e)}")
        finally:
            print(f"Finished processing item: {item}")
    
    return total
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `process_data_list([2, 4, 'abc', 0, 10])` | 0.85 (mit Fehlerausgaben) | 0.85 | ✅ |
| `process_data_list([10, 0, -2, 5, 'skip'])` | -0.2 (mit Fehlerausgaben) | -0.2 | ✅ |
| `process_data_list([1, 1, 1, 1])` | 4.0 | 4.0 | ✅ |

---

## Notizen

- **Konzept:** Try-Except-Finally Struktur - Finally wird IMMER ausgeführt
- **TypeError:** Tritt auf bei 1.0 / 'string' (nicht-numerischer Wert)
- **ZeroDivisionError:** Tritt auf bei 1.0 / 0
- **str(e):** Extrahiert die Fehlermeldung aus dem Exception-Objekt
- **Finally-Block:** Ideal für Cleanup-Operationen oder Logging
- **Berechnung:** 1/2 + 1/4 + 1/10 = 0.5 + 0.25 + 0.1 = 0.85
