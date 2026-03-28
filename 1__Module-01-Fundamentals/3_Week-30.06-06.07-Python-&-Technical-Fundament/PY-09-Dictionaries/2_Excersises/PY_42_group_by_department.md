# 🐍 Group By Department - Nach Abteilung gruppieren

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Gruppiere Mitarbeiter-Liste nach Abteilung.

**Anforderungen:**
- Funktion: `group_by_department(employees)`
- Input: Liste von Dicts mit `'name'` und `'department'`
- Rückgabe: Neues Dict `{abteilung: [namen]}`

---

## Lösung

```python
def group_by_department(employees):
    """Gruppiert Mitarbeiter nach Abteilung."""
    grouped = {}
    
    for employee in employees:
        dept = employee['department']
        name = employee['name']
        
        if dept not in grouped:
            grouped[dept] = []
        grouped[dept].append(name)
    
    return grouped
```

**Alternative (mit .setdefault()):**
```python
def group_by_department(employees):
    grouped = {}
    for emp in employees:
        grouped.setdefault(emp['department'], []).append(emp['name'])
    return grouped
```

---

## Tests

| Input | Erwartet | ✓ |
|-------|----------|---|
| `[{'name': 'Alice', 'department': 'HR'}, {'name': 'Bob', 'department': 'IT'}, {'name': 'Charlie', 'department': 'HR'}, {'name': 'David', 'department': 'IT'}]` | `{'HR': ['Alice', 'Charlie'], 'IT': ['Bob', 'David']}` | ✅ |
| `[]` | `{}` | ✅ |

---

## Notizen

- **Konzept:** Gruppierung mit Dictionary
- **`.setdefault(key, default)`:** Gibt Wert zurück, setzt `default` wenn Key fehlt
- **Alternative:** `collections.defaultdict(list)`
- **Zugriff:** `dict['key']` wirft Error wenn Key fehlt, `dict.get('key')` gibt `None`
