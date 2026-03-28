# 🐍 Name and Hobby (Mehrere Eingaben)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Zwei Benutzereingaben abfragen und als Zusammenfassung ausgeben.

**Anforderungen:**
- Prompt 1: `First name:` (ohne Leerzeichen am Ende)
- Prompt 2: `Favorite hobby:` (ohne Leerzeichen am Ende)
- Ausgabe: `Summary: [Name]'s favorite hobby is [Hobby].`
- Verwende: String-Konkatenation oder f-Strings

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
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `Max`, `Gaming` | `Summary: Max's favorite hobby is Gaming.` | `Summary: Max's favorite hobby is Gaming.` | ✅ |
| `Anna`, `Lesen` | `Summary: Anna's favorite hobby is Lesen.` | `Summary: Anna's favorite hobby is Lesen.` | ✅ |

---

## Notizen

- **Konzept:** String-Konkatenation mit `+`
- **Wichtig:** Bei `+` werden KEINE Leerzeichen automatisch eingefügt
- **Apostroph:** `'s` muss manuell im String stehen
- **Best Practice:** Variablennamen klein schreiben (`name` statt `Name`)
- **Tipp:** f-Strings sind lesbarer als `+`-Verkettung
