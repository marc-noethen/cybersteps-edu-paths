# 🐍 Message Repeater (String-Multiplikation)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Eine Nachricht einlesen und diese mehrfach wiederholen.

**Anforderungen:**
- Prompt 1: `Enter message: `
- Prompt 2: `Repeat count: ` (als Ganzzahl)
- Berechnung: String × Anzahl
- Ausgabe: Wiederholter String

---

## Lösung

```python
message = input("Enter message: ")
repeat_count = int(input("Repeat count: "))
count_message = message * repeat_count
print(count_message)
```

**Alternative Lösungen:**
```python
# Kompakt
message = input("Enter message: ")
repeat_count = int(input("Repeat count: "))
print(message * repeat_count)

# Mit Zeilenumbruch zwischen Wiederholungen
message = input("Enter message: ")
repeat_count = int(input("Repeat count: "))
print((message + "\n") * repeat_count)

# Mit Leerzeichen zwischen Wiederholungen
message = input("Enter message: ")
repeat_count = int(input("Repeat count: "))
print((message + " ") * repeat_count)
```

---

## Tests

| Message | Count | Erwartet | Ergebnis | ✓ |
|---------|-------|----------|----------|---|
| `Hi` | `3` | `HiHiHi` | `HiHiHi` | ✅ |
| `Python ` | `2` | `Python Python ` | `Python Python ` | ✅ |
| `!` | `5` | `!!!!!` | `!!!!!` | ✅ |
| `Test` | `0` | `` (leer) | `` (leer) | ✅ |
| `X` | `1` | `X` | `X` | ✅ |

---

## Notizen

- **Konzept:** String-Multiplikation mit `*` Operator
- **Syntax:** `"text" * n` wiederholt den String n-mal
- **Wichtig:** Funktioniert nur mit `int`, nicht mit `float`!

**String-Operationen:**
| Operation | Beispiel | Ergebnis |
|-----------|----------|----------|
| Konkatenation | `"Hi" + "!"` | `"Hi!"` |
| Multiplikation | `"Hi" * 3` | `"HiHiHi"` |
| Länge | `len("Hi")` | `2` |

**Spezialfälle:**
- `"text" * 0` → `""` (leerer String)
- `"text" * 1` → `"text"` (keine Änderung)
- `"text" * -1` → `""` (negative Zahlen = leerer String)

- **Tipp:** Nützlich für Trennlinien: `print("-" * 50)`
