## 📊 Zusammenfassung nach dem 80/20-Prinzip
### **1. Was ist Python?**

Python ist eine **einsteigerfreundliche Programmiersprache**, die:

- **Lesbar** wie normales Englisch geschrieben ist
- **Vielseitig** für viele Bereiche genutzt wird (Web, KI, Cybersecurity, Automatisierung)
- **Interpretiert** wird (Code wird direkt ausgeführt, keine Kompilierung nötig)
- Eine **riesige Community** und viele fertige **Bibliotheken** hat

**Warum Python in Cybersecurity?**

- Automatisierung von Sicherheitstests
- Entwicklung von Security-Tools
- Malware-Analyse
- Netzwerkanalyse

---

### **2. Python-Installation überprüfen (Windows 11)**

**Schritt 1: PowerShell öffnen**

```
Windows-Taste + R → cmd oder powershell
```

**Schritt 2: Python-Version prüfen**

```powershell
python --version
```

**Erwartete Ausgabe:** `Python 3.x.y` (z.B. `Python 3.11.5`)

**Wenn nicht installiert:**

1. Download von [python.org/downloads](https://www.python.org/downloads/)
2. **Wichtig:** Bei Installation "Add Python to PATH" anhaken!
3. Nach Installation PowerShell neu starten
4. Erneut `python --version` testen

**Alternative Befehle (falls `python` nicht funktioniert):**

```powershell
python3 --version
py --version
```

---

### **3. Der Python REPL (Interaktiver Modus)**

**REPL starten:**

```powershell
python
```

**Was passiert:**

```
Python 3.11.5 (...)
>>>
```

Der `>>>` Prompt zeigt: Python wartet auf deine Befehle!

**REPL = Read-Eval-Print Loop:**

1. **Read**: Liest deinen Befehl
2. **Eval**: Führt ihn aus
3. **Print**: Zeigt das Ergebnis
4. **Loop**: Wartet auf nächsten Befehl

**Beispiele zum Ausprobieren:**

```python
>>> 2 + 2
4

>>> print("Hallo Cybersecurity!")
Hallo Cybersecurity!

>>> 10 * 5
50
```

**REPL beenden:**

```python
>>> exit()
```

oder `Strg + Z` → `Enter` (Windows)

---

### **4. Die wichtigsten Konzepte**

**Funktionen:**

```python
print("Text")  # Gibt Text aus
```

- `print()` ist eine **Funktion**
- Text muss in **Anführungszeichen** ("..." oder '...')

**Strings (Text):**

```python
"Das ist ein String"
'Das auch'
```

**Mathematik:**

```python
2 + 2        # Addition
10 * 5       # Multiplikation
100 / 4      # Division
2 ** 3       # Potenz (2³ = 8)
```

---

### **5. Windows 11 vs. macOS - Die Unterschiede**

|Aufgabe|macOS|Windows 11|
|---|---|---|
|Terminal öffnen|`Cmd + Space` → "Terminal"|`Win + R` → `cmd` oder `powershell`|
|Python starten|`python3`|`python` oder `py`|
|Version prüfen|`python3 --version`|`python --version`|
|REPL beenden|`Ctrl + D` oder `exit()`|`Ctrl + Z` → `Enter` oder `exit()`|
|Download-Link|python.org/downloads/macos|python.org/downloads/windows|

---

### **6. Warum Python für Anfänger ideal ist**

✅ **Einfache Syntax** - fast wie normales Englisch ✅ **Sofortiges Feedback** - REPL zeigt direkt Ergebnisse ✅ **Vielseitig** - von Web bis Cybersecurity alles möglich ✅ **Riesige Community** - viel Hilfe und Tutorials verfügbar ✅ **Viele Bibliotheken** - fertiger Code für fast alles

---

### **Schnellstart-Checkliste:**

```
☐ PowerShell öffnen (Win + R → powershell)
☐ python --version ausführen
☐ Falls nicht installiert: Von python.org installieren
☐ python eingeben → REPL starten
☐ print("Hallo Welt!") testen
☐ 2 + 2 berechnen
☐ exit() zum Beenden
```

---

**Merksatz:** Python ist eine einsteigerfreundliche, interpretierte Sprache. Mit `python` startest du den Interpreter, mit `>>>` siehst du den REPL-Modus, und mit `print()` gibst du Text aus. Alles läuft direkt in PowerShell (Windows) oder Terminal (Mac).

---

## Tabelle 1: Verwendete Tools

|Verwendete Tools (Windows 11)|Bedeutung|
|---|---|
|**PowerShell / CMD**|Kommandozeile in Windows (ersetzt Terminal auf macOS)|
|**Python Interpreter**|Programm, das Python-Code ausführt|
|**REPL (Read-Eval-Print Loop)**|Interaktiver Python-Modus zum direkten Testen von Code|
|**Python IDLE**|Vorinstallierte Python-Entwicklungsumgebung (optional)|
|**VS Code**|Code-Editor zum Schreiben von Python-Programmen|
|**python.org**|Offizielle Website zum Download von Python|

---

## Tabelle 2: Technische Fachbegriffe

| Technische Fachbegriffe  | Bedeutung                                                                  |
| ------------------------ | -------------------------------------------------------------------------- |
| **Programmiersprache**   | Sprache zur Kommunikation zwischen Mensch und Computer                     |
| **Syntax**               | Grammatik/Regeln einer Programmiersprache                                  |
| **Interpreter**          | Programm, das Code Zeile für Zeile ausführt (im Gegensatz zu Compiler)     |
| **Compiled Language**    | Sprache, bei der Code erst komplett übersetzt wird (z.B. C++, Java)        |
| **Interpreted Language** | Sprache, bei der Code direkt Zeile für Zeile ausgeführt wird (z.B. Python) |
| **Library / Modul**      | Vorgefertigte Code-Sammlung für bestimmte Aufgaben                         |
| **REPL**                 | Read-Eval-Print Loop - interaktiver Interpreter-Modus                      |
| **Funktion**             | Wiederverwendbarer Code-Block (z.B. `print()`)                             |
| **String**               | Textdaten in Anführungszeichen ("Text" oder 'Text')                        |
| **Command Line / CLI**   | Textbasierte Benutzeroberfläche (PowerShell/CMD in Windows)                |
| **Version**              | Spezifische Ausgabe der Software (z.B. Python 3.12.3)                      |
| **Stable Release**       | Offiziell freigegebene, getestete Version                                  |
| **Pre-release**          | Vorab-Version, noch in Entwicklung                                         |

---

## Tabelle 3: Wichtige Vokabeln

|Wichtige Vokabeln|Bedeutung|
|---|---|
|**Versatile**|Vielseitig, für viele Zwecke einsetzbar|
|**Automation**|Automatisierung von wiederholenden Aufgaben|
|**Execute / Run**|Code ausführen/laufen lassen|
|**Output**|Ausgabe eines Programms|
|**Prompt**|Eingabeaufforderung (z.B. `>>>` in Python oder `PS C:\>` in PowerShell)|
|**Command**|Befehl, der ausgeführt wird|
|**Error Message**|Fehlermeldung bei Problemen|
|**Install**|Software installieren/einrichten|
|**Verify**|Überprüfen, ob etwas funktioniert|
|**Download**|Herunterladen von Dateien|
