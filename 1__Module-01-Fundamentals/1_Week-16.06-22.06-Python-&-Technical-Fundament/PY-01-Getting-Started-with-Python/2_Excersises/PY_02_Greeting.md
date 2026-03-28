# 🐍 Greeting (Benutzereingabe)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Benutzernamen abfragen und personalisierte Begrüßung ausgeben.

**Anforderungen:**
- Prompt: `Enter your name: ` (mit Leerzeichen am Ende)
- Ausgabe: `Hello, [Name]! Welcome to Python.`
- Verwende: `input()` und `print()` Funktionen

---

## Lösung

```python
save_name = input("Enter your name: ")
print(f"Hello, {save_name}! Welcome to Python.")
```

**Alternative Lösungen:**
```python
# Mit String-Konkatenation
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")

# Mit Komma-Separator (Achtung: zusätzliche Leerzeichen)
name = input("Enter your name: ")
print("Hello,", name + "! Welcome to Python.")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `Max` | `Hello, Max! Welcome to Python.` | `Hello, Max! Welcome to Python.` | ✅ |
| `Anna` | `Hello, Anna! Welcome to Python.` | `Hello, Anna! Welcome to Python.` | ✅ |
| `` (leer) | `Hello, ! Welcome to Python.` | `Hello, ! Welcome to Python.` | ✅ |

---

## Notizen

- **Konzept:** `input()` gibt immer einen String zurück
- **Wichtig:** Leerzeichen im Prompt beachten (`"Enter your name: "`)
- **f-String:** Beste Methode für String-Formatierung
- **Tipp:** `input()` wartet auf Eingabe + Enter
