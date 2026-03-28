# 🐍 Bug Squasher (Fehlersuche & Debugging)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Syntax-Fehler mit VS Code erkennen, im Problems-Panel analysieren und beheben.

**Anforderungen:**
- `buggy.py` mit fehlerhaftem Code erstellen
- Fehler identifizieren und beschreiben
- Alle Fehler korrigieren
- Skript erfolgreich ausführen

---

## Fehlerhafter Code (Original)

```python
# This code contains deliberate errors for practice!

user_name = "Ada Lovelace"
print(user_name # Error 1: Missing closing parenthesis

def calculate_area(length, width):
return length * width # Error 2: Unexpected indent

area = calculate_area(10, 5
# Error 3: Missing closing parenthesis on the line above

print(f"The area is: {ares}") # Error 4: Typo in variable name 'area'
```

---

## Fehleranalyse

| Fehler | Zeile | Problem | Beschreibung |
|--------|-------|---------|--------------|
| Error 1 | 4 | `)` fehlt | `print(user_name` → `print(user_name)` |
| Error 2 | 7 | Einrückung fehlt | `return` muss eingerückt sein |
| Error 3 | 9 | `)` fehlt | `calculate_area(10, 5` → `calculate_area(10, 5)` |
| Error 4 | 12 | Tippfehler | `ares` → `area` |

---

## Korrigierter Code (Lösung)

```python
# This code contains deliberate errors for practice!

user_name = "Ada Lovelace"
print(user_name)  # Error 1: FIXED - Added closing parenthesis

def calculate_area(length, width):
    return length * width  # Error 2: FIXED - Added proper indentation

area = calculate_area(10, 5)  # Error 3: FIXED - Added closing parenthesis

print(f"The area is: {area}")  # Error 4: FIXED - Corrected typo 'ares' to 'area'
```

---

## Antworten auf die Fragen

### Frage 1: Visuelle Hinweise in VS Code
**Antwort:** VS Code zeigt Fehler mit folgenden visuellen Hinweisen:
- **Rote Unterstreichung:** Syntax-Fehler werden rot unterstrichen
- **Gelbe Unterstreichung:** Warnungen (z.B. unbenutzte Variablen)
- **Rotes X im Rand:** Fehler-Symbol neben der Zeilennummer
- **Rote Zahl in der Statusleiste:** Anzahl der Fehler unten links

### Frage 2: Anzahl der Probleme im Problems-Panel
**Antwort:** Das Problems-Panel zeigt initial **4 Probleme** (oder mehr, da Folgefehler entstehen können). Die genaue Anzahl kann variieren, da ein Fehler oft weitere Fehler auslöst.

### Frage 3: Erfolgreiche Ausführung
**Antwort:** **Ja**, das Skript läuft ohne Fehler durch.

**Ausgabe:**
```
Ada Lovelace
The area is: 50
```

---

## Ausführung im Terminal

```bash
# Zum Ordner navigieren
cd ~/cybersteps/python/03_ide

# Korrigiertes Skript ausführen
python3 buggy.py
```

**Erwartete Ausgabe:**
```
Ada Lovelace
The area is: 50
```

---

## Screenshot-Checkliste

Für die Einreichung muss der Screenshot zeigen:
- [ ] VS Code mit korrigiertem `buggy.py` Code
- [ ] Problems-Panel leer oder 0 Fehler
- [ ] Integriertes Terminal sichtbar
- [ ] Erfolgreiche Ausgabe im Terminal

---

## Notizen

- **Problems-Panel öffnen:** `View > Problems` oder `Cmd+Shift+M`
- **Häufige Syntax-Fehler:**

| Fehlertyp | Beispiel | Lösung |
|-----------|----------|--------|
| Missing parenthesis | `print("Hi"` | `print("Hi")` |
| Indentation error | `return x` (ohne Einrückung) | `    return x` |
| Undefined variable | `prnt("Hi")` | `print("Hi")` |
| Typo in variable | `naem` statt `name` | Korrektur zu `name` |

- **Tipp:** Fehler von oben nach unten beheben (ein Fehler kann weitere verursachen)
- **Einrückung in Python:** 4 Leerzeichen oder 1 Tab (konsistent bleiben!)
- **Pylance Extension:** Verbessert Fehlererkennung in VS Code
