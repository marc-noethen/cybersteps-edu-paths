# 🖥️ Editor Acrobatics (Text-Manipulation)

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 19.06.2025

---

## Aufgabe

**Ziel:** Text-Manipulationen mit Sublime Text Keyboard-Aktionen lösen: Uppercase, Sortieren, Spalten-Extraktion.

---

## Lösung

### Umgebung
```
OS: macOS
Editor: Sublime Text
```

---

## Challenge A: Case Closed (UPPERCASE)

### Ausgangstext
```
error: file not found
WARNING: disk space low
Info: user logged in successfully
ERROR: connection timed out
```

### Durchführung

```
1. Cmd+A                     → Alles auswählen
2. Cmd+K, Cmd+U              → To Uppercase
```

**Alternative via Command Palette:**
```
1. Cmd+A                     → Alles auswählen
2. Cmd+Shift+P               → Command Palette öffnen
3. "upper" tippen            → "Convert Case: Upper Case" auswählen
4. Enter
```

### Ergebnis
```
ERROR: FILE NOT FOUND
WARNING: DISK SPACE LOW
INFO: USER LOGGED IN SUCCESSFULLY
ERROR: CONNECTION TIMED OUT
```

### Shortcuts für Challenge A

| Shortcut | Aktion |
|----------|--------|
| `Cmd+K, Cmd+U` | To UPPERCASE |
| `Cmd+K, Cmd+L` | To lowercase |
| `Cmd+Shift+P` | Command Palette |

---

## Challenge B: Line Dance (Alphabetisch sortieren)

### Ausgangstext
```
Zulu
Alpha
Charlie
Bravo
Delta
```

### Durchführung

```
1. Cmd+A                     → Alles auswählen
2. F5                        → Sort Lines
```

**Alternative via Command Palette:**
```
1. Cmd+A                     → Alles auswählen
2. Cmd+Shift+P               → Command Palette öffnen
3. "sort" tippen             → "Sort Lines" auswählen
4. Enter
```

### Ergebnis
```
Alpha
Bravo
Charlie
Delta
Zulu
```

### Shortcuts für Challenge B

| Shortcut | Aktion |
|----------|--------|
| `F5` | Sort Lines |
| `Ctrl+F5` | Sort Lines (Case Sensitive) |

---

## Challenge C: Column Extraction (Spalten-Auswahl)

### Ausgangstext
```
ID001:UserA:Admin
ID002:UserB:Editor
ID003:UserC:Viewer
ID004:UserD:Admin
```

### Durchführung

**Methode 1: Column Selection Mode**
```
1. Cursor vor "UserA" positionieren
2. Ctrl+Shift+Down Arrow     → Spalten-Selektion nach unten
   (oder Option+Click und nach unten ziehen)
3. Shift+Option+Right Arrow  → Wort auswählen (für jede Zeile)
4. Cmd+C                     → Kopieren
5. Cmd+N                     → Neue Datei
6. Cmd+V                     → Einfügen
```

**Methode 2: Regex Find**
```
1. Cmd+F                     → Find öffnen
2. Alt+Cmd+R                 → Regex aktivieren
3. ":User[A-Z]:" eingeben    → Findet alle Usernames
4. Find All
5. Cmd+C                     → Kopieren
```

**Methode 3: Multi-Cursor mit Suche**
```
1. "User" markieren
2. Cmd+D (4x)                → Alle "User" auswählen
3. Shift+Option+Right        → "UserA", "UserB" etc. auswählen
4. Cmd+C                     → Kopieren
5. Cmd+N                     → Neue Datei
6. Cmd+V                     → Einfügen
```

### Ergebnis (in neuer Datei)
```
UserA
UserB
UserC
UserD
```

### Shortcuts für Challenge C

| Shortcut | Aktion |
|----------|--------|
| `Ctrl+Shift+Up/Down` | Column Selection |
| `Option+Click+Drag` | Rechteck-Selektion |
| `Cmd+D` | Nächstes gleiches Wort auswählen |
| `Cmd+Shift+L` | Cursor an jedes Zeilenende (bei Selektion) |

---

## Ergebnisse Zusammenfassung

| Challenge | Hauptaktion | Shortcut |
|-----------|-------------|----------|
| A: UPPERCASE | Convert to Upper Case | `Cmd+K, Cmd+U` |
| B: Sortieren | Sort Lines | `F5` |
| C: Spalten | Column Selection | `Ctrl+Shift+Down` + `Option+Shift+Right` |

---

## Notizen

- **Gelernt:** Case Conversion, Sorting, Column/Block Selection
- **Column Selection:** Auch "Block Selection" oder "Rectangular Selection" genannt
- **Tipp:** `Cmd+Shift+P` (Command Palette) für alle Befehle durchsuchen
- **Wichtig:** Bei Column Selection wird pro Zeile ein Cursor erstellt

**Weitere nützliche Befehle:**
| Command Palette | Aktion |
|-----------------|--------|
| "Sort Lines" | Alphabetisch sortieren |
| "Reverse Lines" | Zeilen umkehren |
| "Shuffle Lines" | Zeilen zufällig mischen |
| "Remove Duplicate Lines" | Duplikate entfernen |
| "Convert Case" | Groß-/Kleinschreibung ändern |
