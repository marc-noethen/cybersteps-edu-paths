# 🐍 Multiline Print (Mehrzeilige Ausgabe)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Drei Textzeilen mit einem einzigen `print()`-Befehl ausgeben.

**Anforderungen:**
- Nur EIN `print()`-Befehl
- Ausgabe exakt:
  ```
  Line 1: Python is fun.
  Line 2: It is also powerful.
  Line 3: Let's learn more!
  ```

---

## Lösung

```python
print("Line 1: Python is fun.\n" + "Line 2: It is also powerful.\n" + "Line 3: Let's learn more!")
```

**Alternative Lösungen:**
```python
# Mit Triple-Quotes (Multi-Line String) - empfohlen
print("""Line 1: Python is fun.
Line 2: It is also powerful.
Line 3: Let's learn more!""")

# Nur mit \n (ohne +)
print("Line 1: Python is fun.\nLine 2: It is also powerful.\nLine 3: Let's learn more!")

# Mit Escape-Sequenz für Zeilenumbruch
print("Line 1: Python is fun.\n"
      "Line 2: It is also powerful.\n"
      "Line 3: Let's learn more!")
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| (keine) | 3 Zeilen wie oben | 3 Zeilen wie oben | ✅ |

**Ausgabe:**
```
Line 1: Python is fun.
Line 2: It is also powerful.
Line 3: Let's learn more!
```

---

## Notizen

- **Konzept:** Escape-Sequenzen und Multi-Line Strings
- **`\n`:** Newline (Zeilenumbruch)
- **Triple-Quotes:** `"""` oder `'''` für mehrzeilige Strings
- **Weitere Escape-Sequenzen:**
  - `\t` = Tab
  - `\\` = Backslash
  - `\'` = Apostroph
  - `\"` = Anführungszeichen
- **Tipp:** Triple-Quotes sind lesbarer für längere Texte
