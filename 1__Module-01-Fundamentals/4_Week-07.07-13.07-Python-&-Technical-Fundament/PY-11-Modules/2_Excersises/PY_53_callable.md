# 🐍 Check Callable Exists

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Prüfe ob ein Modul ein aufrufbares Member (Funktion/Klasse) besitzt

**Anforderungen:**
- Funktion: `check_callable_exists(module_name_string, callable_name_string)`
- Rückgabe: `True` wenn callable existiert und nicht mit `_` beginnt, sonst `False`
- Edge Cases: Modul nicht importierbar → `False`, Member nicht callable → `False`

---

## Lösung

```python
import importlib

def check_callable_exists(module_name_string, callable_name_string):
    """Prüft ob callable Member in Modul existiert."""
    try:
        module = importlib.import_module(module_name_string)
        
        if not hasattr(module, callable_name_string):
            return False
        
        member = getattr(module, callable_name_string)
        
        if callable_name_string.startswith('_'):
            return False
        
        if callable(member):
            return True
        
        return False
    except ImportError:
        return False
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `check_callable_exists("math", "sqrt")` | `True` | `True` | ✅ |
| `check_callable_exists("datetime", "date")` | `True` | `True` | ✅ |
| `check_callable_exists("math", "pi")` | `False` | `False` | ✅ |
| `check_callable_exists("nonexistent", "func")` | `False` | `False` | ✅ |

---

## Notizen

- **Konzept:** Dynamischer Import mit `importlib`, Prüfung mit `callable()`
- **Alternative:** `__import__()` (weniger empfohlen)