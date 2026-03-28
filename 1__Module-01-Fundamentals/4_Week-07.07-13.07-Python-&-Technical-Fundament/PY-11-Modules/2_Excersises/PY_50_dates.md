# 🐍 Days Between Dates

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Berechnung der absoluten Differenz in Tagen zwischen zwei Datumswerten

**Anforderungen:**
- Funktion: `days_between_dates(date_str1, date_str2)`
- Rückgabe: Nicht-negative Ganzzahl (Tagesdifferenz)
- Edge Cases: Ungültiges Datumsformat → `None`

---

## Lösung

```python
from datetime import datetime

def days_between_dates(date_str1, date_str2):
    """Berechnet absolute Differenz in Tagen zwischen zwei Daten."""
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return None
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `days_between_dates("2024-01-01", "2024-01-11")` | `10` | `10` | ✅ |
| `days_between_dates("2024-01-11", "2024-01-01")` | `10` | `10` | ✅ |
| `days_between_dates("2024-13-01", "2024-01-01")` | `None` | `None` | ✅ |

---

## Notizen

- **Konzept:** Exception Handling mit `try/except` für ungültige Datumswerte
- **Alternative:** `datetime.fromisoformat()` (ab Python 3.7)