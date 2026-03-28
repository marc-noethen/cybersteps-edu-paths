# 🐍 Full Name Greeting (Vor- und Nachname)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Vor- und Nachname einlesen und personalisierte Begrüßung ausgeben.

**Anforderungen:**
- Prompt 1: `Enter your first name: `
- Prompt 2: `Enter your last name: `
- Ausgabe: `Hello, [first_name] [last_name]!`
- Leerzeichen zwischen Vor- und Nachname beachten

---

## Lösung

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greets = f"Hello, {first_name} {last_name}!"
print(greets)
```

**Alternative Lösungen:**
```python
# Mit String-Konkatenation
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, " + first_name + " " + last_name + "!")

# Kompakt mit f-String
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name} {last_name}!")

# Mit .format()
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, {} {}!".format(first_name, last_name))
```

---

## Tests

| First Name | Last Name | Erwartet | Ergebnis | ✓ |
|------------|-----------|----------|----------|---|
| `Max` | `Mustermann` | `Hello, Max Mustermann!` | `Hello, Max Mustermann!` | ✅ |
| `Anna` | `Schmidt` | `Hello, Anna Schmidt!` | `Hello, Anna Schmidt!` | ✅ |
| `John` | `Doe` | `Hello, John Doe!` | `Hello, John Doe!` | ✅ |

---

## Notizen

- **Konzept:** Mehrere Eingaben kombinieren mit f-Strings
- **Wichtig:** Leerzeichen im f-String zwischen `{first_name}` und `{last_name}`
- **Best Practice:** Variablennamen beschreibend wählen (`first_name` statt `fn`)
- **Tipp:** f-Strings erlauben auch Ausdrücke: `f"{name.upper()}"`
