# 🐍 Name and Hobby Summary (String-Konkatenation)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Name und Hobby abfragen und als Zusammenfassung formatiert ausgeben.

**Anforderungen:**
- Prompt 1: `First name:` (ohne Leerzeichen am Ende)
- Prompt 2: `Favorite hobby:` (ohne Leerzeichen am Ende)
- Ausgabe: `Summary: [Name]'s favorite hobby is [Hobby].`
- String-Konkatenation mit `+` oder f-Strings verwenden

---

## Lösung

```python
Name = input("First name: ")
Hobby = input("Favorite hobby: ")
print("Summary: " + Name + "'s favorite hobby is " + Hobby + ".")
```

**Alternative Lösungen:**
```python
# Mit f-String (empfohlen)
name = input("First name: ")
hobby = input("Favorite hobby: ")
print(f"Summary: {name}'s favorite hobby is {hobby}.")

# Mit .format()
name = input("First name: ")
hobby = input("Favorite hobby: ")
print("Summary: {}'s favorite hobby is {}.".format(name, hobby))

# Mit mehreren print-Argumenten (Achtung: Leerzeichen!)
name = input("First name: ")
hobby = input("Favorite hobby: ")
print("Summary:", name + "'s favorite hobby is", hobby + ".")
```

---

## Tests

| Name | Hobby | Erwartet | Ergebnis | ✓ |
|------|-------|----------|----------|---|
| `Max` | `Gaming` | `Summary: Max's favorite hobby is Gaming.` | `Summary: Max's favorite hobby is Gaming.` | ✅ |
| `Anna` | `Reading` | `Summary: Anna's favorite hobby is Reading.` | `Summary: Anna's favorite hobby is Reading.` | ✅ |
| `Tom` | `Coding` | `Summary: Tom's favorite hobby is Coding.` | `Summary: Tom's favorite hobby is Coding.` | ✅ |

---

## Notizen

- **Konzept:** String-Konkatenation mit `+` Operator
- **Wichtig:** Bei `+` keine automatischen Leerzeichen!
- **Apostroph:** `'s` ist Teil des Strings, kein Escape nötig in `""`
- **Best Practice:** Variablennamen klein schreiben (`name` statt `Name`)
- **Vergleich:**

| Methode | Code | Lesbarkeit |
|---------|------|------------|
| `+` Operator | `"Hi " + name + "!"` | Mittel |
| f-String | `f"Hi {name}!"` | Sehr gut |
| `.format()` | `"Hi {}!".format(name)` | Gut |
