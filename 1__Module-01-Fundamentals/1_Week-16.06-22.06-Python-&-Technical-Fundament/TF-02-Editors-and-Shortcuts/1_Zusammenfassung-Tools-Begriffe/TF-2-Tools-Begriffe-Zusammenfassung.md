## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Texteditor - Was ist der Unterschied?

**Plain Text vs. Rich Text - Der kritische Unterschied:**

- **Plain Text Editoren** (Sublime Text, Notepad, Notepad++, VS Code): Nur Zeichen, keine versteckte Formatierung. **IMMER verwenden für Code, Konfigurationsdateien, Skripte, Logs.**
    
- **Word Processors** (Word, Google Docs): Formatierung mit Schriftarten, Farben, eingebetteten Objekten. **NIEMALS für Code verwenden** - die versteckte Formatierung zerstört Code und Konfigurationen!
    

### Warum Sublime Text? (Windows-Alternativen)

**Sublime Text** ist der Kurs-Standard (kostenlose Testversion ohne Zeitlimit), weil es:

- Schnell und stabil ist
- Syntax-Highlighting bietet (Code wird farbig dargestellt)
- Multi-Cursor ermöglicht (an mehreren Stellen gleichzeitig schreiben)
- Erweiterbar ist (Package Control für Plugins)

**Windows-Alternativen:**

- **Notepad++**: Kostenlos, leicht, gut für Anfänger
- **VS Code**: Kostenlos, sehr mächtig, von Microsoft, ähnlich zu Sublime Text

### CLI vs. GUI Editoren

**CLI-Editoren** (Nano, Vim):

- Laufen im Terminal
- Nur Tastatur-Steuerung
- **Unverzichtbar** bei Remote-Servern ohne grafische Oberfläche
- Nano: Einfach für Anfänger (Befehle unten angezeigt)
- Vim: Sehr mächtig, aber steile Lernkurve

**GUI-Editoren** (Sublime Text, Notepad++, VS Code):

- Grafische Oberfläche mit Menüs
- Maus- und Tastatur-Steuerung
- Besser für lokale Arbeit und Anfänger

### Die 10 wichtigsten Tastenkombinationen für Windows

**Basis-Bearbeitung (funktioniert fast überall):**

1. **`Strg + C`** - Kopieren
2. **`Strg + V`** - Einfügen
3. **`Strg + X`** - Ausschneiden
4. **`Strg + Z`** - Rückgängig
5. **`Strg + S`** - Speichern

**Navigation & Effizienz:** 6. **`Strg + F`** - Suchen 7. **`Strg + A`** - Alles markieren 8. **`Alt + Tab`** - Zwischen Programmen wechseln 9. **`Strg + W`** - Tab/Fenster schließen 10. **`Windows-Taste`** - Startmenü/Suche öffnen

**Bonus für Textbearbeitung:**

- **`Strg + Pfeiltasten`** - Wortweise springen
- **`Pos1` / `Ende`** - Zeilenanfang/-ende
- **`Shift + Pfeiltasten`** - Text markieren beim Bewegen

### Sublime Text Installation (Windows)

1. Gehe zu: https://www.sublimetext.com/download
2. Lade die Windows-Version herunter (`.exe` Installer)
3. Führe die Installation aus (Standardeinstellungen OK)
4. Starte Sublime Text
5. (Optional) Rechtsklick auf Icon in Taskleiste → "An Taskleiste anheften"

### Praktischer Nano-Test (Windows mit WSL/Git Bash)

Wenn du WSL (Windows Subsystem for Linux) oder Git Bash installiert hast:

```bash
nano testdatei.txt
# Schreibe etwas Text
# Strg+X zum Beenden
# Y für Ja (Speichern)
# Enter bestätigen
type testdatei.txt    # CMD
Get-Content testdatei.txt  # PowerShell
del testdatei.txt     # Löschen (CMD)
```

**Ohne WSL:** Verwende Notepad oder installiere Sublime Text sofort.

### Kernbotschaft

**Die 3 entscheidenden Punkte:**

1. **Plain Text für Code**: Niemals Word für Code/Konfigurationen - immer Sublime Text, Notepad++ oder VS Code
2. **Tastenkombinationen = Geschwindigkeit**: Die 10 Basis-Shortcuts sparen dir Stunden pro Woche
3. **CLI-Editor = Notwendigkeit**: Lerne mindestens Nano-Grundlagen - du **wirst** sie auf Servern brauchen

**Windows-Spezifisch:**

- `Strg` ersetzt `Cmd` (Mac)
- `Alt` ersetzt `Option` (Mac)
- `Windows-Taste` ersetzt `Cmd+Space` (Mac Spotlight)

---

## Verwendete Tools, Technische Fachbegriffe und Wichtige Vokabeln

|Begriff|Bedeutung|
|---|---|
|**Verwendete Tools**||
|Text Editor|Programm zum Bearbeiten von reinen Textdateien ohne Formatierung|
|Sublime Text|Professioneller Code-Editor (verfügbar für Windows, macOS, Linux) - Hauptwerkzeug des Kurses|
|Nano|Einfacher CLI-Texteditor für Anfänger (Windows-Alternative: `nano` in WSL oder Git Bash)|
|Vim / Vi|Fortgeschrittener modaler CLI-Editor (verfügbar in WSL, Git Bash oder als separate Installation)|
|Notepad|Standard-Texteditor in Windows (einfach, wenig Features)|
|Notepad++|Kostenloser erweiterter Texteditor für Windows (Alternative zu Sublime Text)|
|VS Code|Kostenloser, beliebter Code-Editor von Microsoft (Alternative zu Sublime Text)|
|Word Processor (Word, Google Docs)|Textverarbeitungsprogramm - NICHT geeignet für Code/Konfigurationsdateien|
|**Technische Fachbegriffe**||
|Plain Text|Reiner Text ohne Formatierung - nur Zeichen (`.txt`, `.py`, `.conf`, `.log`, `.xml`, `.css`, `.js`)|
|Rich Text|Formatierter Text mit Schriftarten, Farben, Bildern (`.docx`, `.rtf`)|
|CLI Editor|Texteditor, der im Terminal läuft - nur Tastatursteuerung|
|GUI Editor|Texteditor mit grafischer Oberfläche - Maus- und Menübedienung möglich|
|Syntax Highlighting|Farbliche Hervorhebung von Code-Elementen (Schlüsselwörter, Variablen, Strings)|
|Command Palette|Schnellzugriff auf Befehle per Tastatur (in Sublime Text: `Ctrl+Shift+P` statt `Cmd+Shift+P`)|
|Multi-Cursor / Multi-Select|Gleichzeitiges Bearbeiten an mehreren Stellen im Text|
|Package Control|Erweiterungs-Manager für zusätzliche Funktionen in Sublime Text|
|Modal Editor|Editor mit verschiedenen Modi (Vim: Normal-Modus, Einfüge-Modus, etc.)|
|Keyboard Shortcuts / Hotkeys|Tastenkombinationen zur schnellen Ausführung von Befehlen|
|**Wichtige Dateiformate**||
|`.txt`|Einfache Textdatei|
|`.py`|Python-Programmdatei|
|`.sh`|Shell-Skript (Linux/Mac) / `.bat` oder `.ps1` (Windows-Skripte)|
|`.conf` / `.ini`|Konfigurationsdateien|
|`.log`|Protokolldateien|
|`.xml`, `.json`, `.yaml`|Strukturierte Datendateien|
|`.css`, `.js`, `.html`|Webentwicklungs-Dateien|
|**Terminal-Befehle (Beispiele)**||
|`nano datei.txt`|Öffnet Datei in Nano-Editor (Windows: WSL/Git Bash oder alternativer Editor)|
|`cat datei.txt`|Zeigt Dateiinhalt an (Windows CMD: `type datei.txt`, PowerShell: `Get-Content datei.txt`)|
|`rm datei.txt`|Löscht Datei (Windows CMD: `del datei.txt`, PowerShell: `Remove-Item datei.txt`)|

---

## Windows 11 Tastenkombinationen (macOS-Äquivalente)

|Funktion|macOS|Windows 11|
|---|---|---|
|**Basis-Bearbeitung**|||
|Kopieren|`Cmd + C`|`Strg + C`|
|Ausschneiden|`Cmd + X`|`Strg + X`|
|Einfügen|`Cmd + V`|`Strg + V`|
|Rückgängig|`Cmd + Z`|`Strg + Z`|
|Wiederholen|`Cmd + Shift + Z`|`Strg + Y` oder `Strg + Shift + Z`|
|Alles markieren|`Cmd + A`|`Strg + A`|
|**Datei-Operationen**|||
|Speichern|`Cmd + S`|`Strg + S`|
|Drucken|`Cmd + P`|`Strg + P`|
|Suchen|`Cmd + F`|`Strg + F`|
|Neuer Tab|`Cmd + T`|`Strg + T`|
|Tab/Fenster schließen|`Cmd + W`|`Strg + W` oder `Strg + F4`|
|Anwendung schließen|`Cmd + Q`|`Alt + F4`|
|**Navigation**|||
|Wort nach links/rechts|`Option + Pfeil`|`Strg + Pfeil`|
|Zeilenanfang/-ende|`Cmd + Pfeil`|`Pos1` / `Ende`|
|Text markieren|`Shift + Pfeiltasten`|`Shift + Pfeiltasten`|
|Wortweise markieren|`Shift + Option + Pfeil`|`Shift + Strg + Pfeil`|
|**System**|||
|App-Wechsel|`Cmd + Tab`|`Alt + Tab`|
|Suche öffnen|`Cmd + Space` (Spotlight)|`Windows-Taste` oder `Windows + S`|
|Screenshot (ganzer Bildschirm)|`Cmd + Shift + 3`|`Windows + Druck` oder `Druck`|
|Screenshot (Ausschnitt)|`Cmd + Shift + 4`|`Windows + Shift + S` (Snipping Tool)|
|**Sublime Text spezifisch**|||
|Command Palette|`Cmd + Shift + P`|`Strg + Shift + P`|