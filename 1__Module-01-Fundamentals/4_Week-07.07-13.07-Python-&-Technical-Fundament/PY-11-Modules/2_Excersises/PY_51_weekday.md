# 🐍 Find Next Weekday

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Finde das nächste Vorkommen eines bestimmten Wochentags nach einem Startdatum

**Anforderungen:**
- Funktion: `find_next_weekday(start_date_str, target_weekday_name)`
- Rückgabe: Nächstes Datum als String "YYYY-MM-DD"
- Edge Cases: Datum muss NACH dem Startdatum liegen

---

## Lösung

```python
from datetime import datetime, timedelta

def find_next_weekday(start_date_str, target_weekday_name):
    """Findet nächstes Vorkommen eines Wochentags nach Startdatum."""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]
    target_weekday = weekdays.index(target_weekday_name)
    
    days_ahead = (target_weekday - start_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    
    next_date = start_date + timedelta(days=days_ahead)
    return next_date.strftime("%Y-%m-%d")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `find_next_weekday("2024-04-30", "Friday")` | `2024-05-03` | `2024-05-03` | ✅ |
| `find_next_weekday("2024-04-30", "Tuesday")` | `2024-05-07` | `2024-05-07` | ✅ |
| `find_next_weekday("2024-04-30", "Wednesday")` | `2024-05-01` | `2024-05-01` | ✅ |

---

## Notizen

- **Konzept:** Modulo-Arithmetik für Wochentagsberechnung
- **Alternative:** Schleife mit täglicher Inkrementierung (weniger effizient)