# 🖥️ System Navigator (macOS Navigation)

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 19.06.2025

---

## Aufgabe

**Ziel:** macOS Dateisystem und Anwendungen effizient mit Keyboard Shortcuts und Systemfunktionen wie Finder und Spotlight navigieren.

---

## Lösung

### Umgebung
```
OS: macOS
Shell: Finder / Spotlight
```

---

## Challenge A: File System Frenzy

### Durchführung

**1. Zum Desktop navigieren**
```
Cmd+Shift+D              → Desktop in Finder öffnen
```
Alternative: Im Finder `Cmd+Shift+G` → "~/Desktop" eingeben

**2. Neuen Ordner "TF2_Challenge" erstellen**
```
Cmd+Shift+N              → Neuer Ordner
"TF2_Challenge" tippen
Enter
```

**3. Datei duplizieren**
```
1. shortcut_practice.txt auswählen (Pfeiltasten)
2. Cmd+D                 → Duplizieren
```
Ergebnis: `shortcut_practice copy.txt`

**4. Datei umbenennen**
```
1. Kopierte Datei auswählen
2. Enter                 → Umbenennen aktivieren
3. "practice_copy.txt" tippen
4. Enter
```

**5. Datei in Ordner verschieben**
```
1. practice_copy.txt auswählen
2. Cmd+C                 → Kopieren
3. TF2_Challenge Ordner öffnen (Enter)
4. Cmd+Option+V          → Verschieben (statt Kopieren)
```

**Alternative für Verschieben:**
```
1. practice_copy.txt auswählen
2. Cmd+X funktioniert NICHT in Finder!
3. Stattdessen: Datei markieren, Cmd+C
4. Im Zielordner: Cmd+Option+V (Move)
```

### Shortcuts für Challenge A

| Shortcut | Aktion |
|----------|--------|
| `Cmd+Shift+D` | Desktop öffnen |
| `Cmd+Shift+N` | Neuer Ordner |
| `Cmd+D` | Duplizieren |
| `Enter` | Umbenennen (bei Auswahl) |
| `Cmd+C` → `Cmd+Option+V` | Ausschneiden & Einfügen |

---

## Challenge B: Quick Launch & Capture

### Durchführung

**1. Calculator mit Spotlight öffnen**
```
Cmd+Space                → Spotlight öffnen
"Calculator" tippen
Enter
```

**2. Zurück zu Sublime Text wechseln**
```
Cmd+Tab                  → App-Switcher
(Tab halten und mit Pfeiltasten navigieren)
```
Alternative: `Cmd+Tab` mehrfach drücken

**3. Screenshot nur von Sublime Text Fenster**
```
Cmd+Shift+4              → Screenshot-Tool
Spacebar                 → Fenster-Modus (Kamera-Icon)
Auf Sublime Text Fenster klicken
```
Datei wird auf Desktop gespeichert.

### Shortcuts für Challenge B

| Shortcut | Aktion |
|----------|--------|
| `Cmd+Space` | Spotlight |
| `Cmd+Tab` | App-Switcher |
| `Cmd+Shift+3` | Screenshot (ganzer Bildschirm) |
| `Cmd+Shift+4` | Screenshot (Auswahl) |
| `Cmd+Shift+4, Space` | Screenshot (Fenster) |
| `Cmd+Shift+5` | Screenshot-Toolbar |

---

## Challenge C: File Inspector

### Durchführung

**1. Zur Datei im Finder navigieren**
```
Cmd+Shift+D              → Desktop öffnen
Pfeiltasten              → Zu shortcut_practice.txt navigieren
```

**2. Quick Look (Vorschau)**
```
Space                    → Quick Look öffnen
Space (oder Esc)         → Quick Look schließen
```

**3. Get Info (Informationen)**
```
Cmd+I                    → Get Info öffnen
Cmd+W                    → Get Info schließen
```

### Shortcuts für Challenge C

| Shortcut | Aktion |
|----------|--------|
| `Space` | Quick Look (Vorschau) |
| `Cmd+I` | Get Info |
| `Cmd+W` | Fenster schließen |
| `Esc` | Quick Look schließen |

---

## Ergebnisse Zusammenfassung

| Challenge | Hauptaktionen | Shortcuts |
|-----------|---------------|-----------|
| A: File System | Ordner erstellen, Datei duplizieren, umbenennen, verschieben | `Cmd+Shift+N`, `Cmd+D`, `Enter`, `Cmd+Option+V` |
| B: Launch & Capture | Spotlight, App-Switch, Fenster-Screenshot | `Cmd+Space`, `Cmd+Tab`, `Cmd+Shift+4+Space` |
| C: File Inspector | Quick Look, Get Info | `Space`, `Cmd+I` |

---

## Notizen

- **Gelernt:** Finder-Navigation, Spotlight, Screenshots, Quick Look
- **Wichtig:** Finder hat KEIN `Cmd+X`! Stattdessen `Cmd+C` → `Cmd+Option+V`
- **Quick Look:** Schnelle Vorschau ohne App zu öffnen

**Weitere nützliche Finder-Shortcuts:**

| Shortcut | Aktion |
|----------|--------|
| `Cmd+Shift+G` | Go to Folder |
| `Cmd+Shift+H` | Home-Verzeichnis |
| `Cmd+Shift+A` | Applications |
| `Cmd+Shift+U` | Utilities |
| `Cmd+Up Arrow` | Übergeordneter Ordner |
| `Cmd+Down Arrow` | Öffnen |
| `Cmd+Delete` | In Papierkorb |
| `Cmd+1/2/3/4` | Ansicht ändern (Icons/Liste/Spalten/Galerie) |
