# 🐍 Sensible Intelligence (IntelliSense & Debugger)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** VS Code IntelliSense, Syntax-Highlighting beobachten und einen Breakpoint im Debugger setzen.

**Anforderungen:**
- `clues.py` erstellen mit vorgegebenem Code
- Farbgebung und IntelliSense beobachten
- Breakpoint setzen und Debugger starten

---

## Lösung

### Code für `clues.py`

```python
# Observe the color of this comment line
investigator_name = "Sherlock Coder"
clue_count = 0

print("Investigator:", investigator_name)

def find_clue(clue_number):
    # Observe the color of the 'def' keyword above
    location = "Study" # Observe the color of this text string
    global clue_count
    clue_count = clue_count + 1
    print(f"Found clue {clue_number} in the {location}. Total clues: {clue_count}") # Breakpoint goes here!

# Start typing 'find' below this line. Does VS Code suggest 'find_clue'?
find_clue(1)

# Now start typing 'inv'. Does VS Code suggest 'investigator_name'?
print("Checking investigator:", investigator_name)

# Hover your mouse cursor over the function name 'find_clue' on the line above.
# Hover your mouse cursor over the built-in function name 'print'.
```

---

## Antworten auf die Fragen

### Frage 4a: Farbe der Kommentarzeile
**Antwort:** Kommentare sind typischerweise **grün** oder **grau** dargestellt und erscheinen heller/gedämpfter als der ausführbare Code. Sie heben sich deutlich vom restlichen Code ab.

### Frage 4b: Farbe des `def` Keywords
**Antwort:** Das Keyword `def` ist typischerweise **blau** oder **lila/magenta** dargestellt (je nach Farbschema).

### Frage 4c: IntelliSense für `find`
**Antwort:** **Ja** - VS Code zeigt einen Vorschlag für `find_clue` an.

### Frage 4d: IntelliSense für `inv`
**Antwort:** **Ja** - VS Code zeigt einen Vorschlag für `investigator_name` an.

### Frage 4e: Hover über `print`
**Antwort:** Es erscheint ein Pop-up mit der **Funktionssignatur** und einer **Beschreibung** der `print()`-Funktion. Typischerweise wird angezeigt:
- Funktionsname und Parameter
- Kurze Beschreibung was die Funktion macht
- Parametertypen und Rückgabewert

---

## Debugger-Anleitung

### Breakpoint setzen
1. Klicke links neben der Zeilennummer bei `print(f"Found clue...")`
2. Ein **roter Punkt** erscheint

### Debugger starten
1. Klicke auf das **Run and Debug** Icon (Play-Button mit Bug)
2. Klicke auf **"Run and Debug"** (grüner Button)
3. Wähle **"Python File"** wenn gefragt
4. Ausführung stoppt an der Breakpoint-Zeile (gelb markiert)

---

## Screenshot-Checkliste

Für die Einreichung muss der Screenshot zeigen:
- [ ] `clues.py` in VS Code geöffnet
- [ ] Breakpoint (roter Punkt) sichtbar
- [ ] Zeile ist gelb markiert (Ausführung pausiert)
- [ ] Debug-Toolbar sichtbar (Continue, Step Over, etc.)

---

## Notizen

- **IntelliSense:** Automatische Code-Vervollständigung
- **Syntax-Highlighting:** Farbliche Unterscheidung von Code-Elementen
- **Breakpoint:** Haltepunkt für den Debugger
- **Debugger-Shortcuts:**
  - `F5` = Debugger starten/fortsetzen
  - `F10` = Step Over (nächste Zeile)
  - `F11` = Step Into (in Funktion springen)
  - `Shift+F5` = Debugger stoppen

**Typische Farbgebung (Dark Theme):**
| Element | Farbe |
|---------|-------|
| Kommentare | Grün/Grau |
| Keywords (`def`, `if`) | Blau/Lila |
| Strings | Orange/Gelb |
| Funktionsnamen | Gelb |
| Variablen | Weiß/Hellblau |
