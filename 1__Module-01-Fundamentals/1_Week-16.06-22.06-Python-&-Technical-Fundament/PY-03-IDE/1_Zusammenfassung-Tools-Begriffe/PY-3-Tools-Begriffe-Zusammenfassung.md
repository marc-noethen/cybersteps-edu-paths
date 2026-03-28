## 📊 Zusammenfassung nach dem 80/20-Prinzip

**1. Was ist ein IDE und warum VS Code?**

- **IDE = "Profi-Werkbank" zum Programmieren** mit Editor, Terminal, Debugger und mehr an einem Ort
- **VS Code = kostenlos, beliebt, leistungsstark** und läuft auf Windows, macOS und Linux
- **Vorteil:** Schnelleres Arbeiten durch Auto-Vervollständigung, Fehlersuche und alles in einem Fenster

**2. Installation auf Windows 11 (3 Schritte)**

**Schritt 1: VS Code installieren**

- Zur Webseite: https://code.visualstudio.com/download
- **Windows 64-bit User Installer** herunterladen
- `.exe` Datei ausführen und Installationsassistent folgen
- **Wichtig:** Bei Installation "Add to PATH" anhaken (ermöglicht `code` Befehl im Terminal)

**Schritt 2: Python Extension installieren**

- VS Code starten
- **Extensions-Symbol** (4 Quadrate) in der linken Leiste anklicken
- Nach `Python` suchen
- Extension "Python" von **Microsoft** installieren (sollte erster Treffer sein)

**Schritt 3: Fertig!**

- VS Code ist nun bereit für Python-Entwicklung

**3. Die wichtigsten VS Code-Bereiche kennen**

```
┌─────────────────────────────────────────────────┐
│ Menüleiste (Datei, Bearbeiten, Ansicht, ...)   │
├───┬─────────────────────────────────────────────┤
│ A │                                             │
│ c │          Editor Group                       │
│ t │     (Hier wird Code geschrieben)            │
│ i │                                             │
│ v │                                             │
│ i │─────────────────────────────────────────────│
│ t │          Panel (Terminal, Debug, ...)       │
│ y │                                             │
│   ├─────────────────────────────────────────────┤
│ B │ Status Bar (Zeile, Python-Version, Fehler)  │
│ a └─────────────────────────────────────────────┘
│ r
└───
```

- **Activity Bar (Links):** Symbole für File Explorer, Suche, Extensions, Debug
- **Editor Group (Mitte):** Hauptbereich zum Schreiben – mehrere Dateien in Tabs öffnen
- **Panel (Unten):** Terminal einblenden mit `` Ctrl + ` ``
- **Status Bar (Ganz unten):** Zeigt Zeilennummer, Python-Interpreter, Fehleranzahl

**4. Die 5 wichtigsten Features, die dein Leben leichter machen**

✅ **Syntax Highlighting** → Code ist farbig: Keywords blau, Strings grün, etc.  
✅ **Auto-completion** → Tippt `pri` → VS Code schlägt `print()` vor  
✅ **Integriertes Terminal** → Kein Wechsel zwischen Fenstern mehr! `` Ctrl + ` ``  
✅ **Debugger** → Code Zeile für Zeile durchgehen und Variablen prüfen  
✅ **Fehler sofort sehen** → Rote Wellenlinien zeigen Fehler, bevor du das Programm startest

**5. Command Palette – Der Zaubertrick**

- Tastenkombination: `Ctrl + Shift + P` (Windows)
- **Öffnet Suchfeld für ALLE VS Code-Befehle**
- Beispiele:
    - `Python: Select Interpreter` → Python-Version wählen
    - `Format Document` → Code automatisch formatieren
    - `Terminal: Create New Terminal` → Neues Terminal öffnen

**6. Schnellstart: Erste Schritte nach Installation**

**Eine Python-Datei erstellen:**

1. `Datei` → `Neuer Ordner` erstellen (z.B. `mein_python_projekt`)
2. `Datei` → `Neue Datei` → Speichern als `test.py`
3. Code schreiben:

```python
name = "Max"
print(f"Hallo {name}!")
```

4. Terminal öffnen (`` Ctrl + ` `` )
5. Code ausführen: `python test.py`

**7. Häufige Anfängerfragen**

❓ **Welche Python-Version nutzt VS Code?**  
→ Rechts unten in der Status Bar steht die aktuelle Python-Version. Mit Klick darauf kannst du eine andere wählen.

❓ **Warum sehe ich keine Farben im Code?**  
→ Datei muss als `.py` gespeichert werden UND Python Extension installiert sein.

❓ **Wie öffne ich einen Ordner?**  
→ `Datei` → `Ordner öffnen` oder im Terminal: `code mein_ordner`

### Merksatz:

**VS Code = Dein neuer bester Freund beim Programmieren!**  
Statt zwischen Editor, Terminal und Browser zu wechseln, hast du jetzt alles in einem Fenster – schneller, übersichtlicher, professioneller.

---

## Kategorisierung der Themen

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Visual Studio Code (VS Code)|Kostenloser, quelloffener Code-Editor von Microsoft für Windows, macOS und Linux|
||Python Extension für VS Code|Offizielle Microsoft-Erweiterung für Python-Unterstützung in VS Code|
||Integrated Terminal (Integriertes Terminal)|Eingebaute Kommandozeile in VS Code (erspart Wechsel zu externer Eingabeaufforderung)|
||Command Palette (Befehlspalette)|Schnellzugriff auf VS Code-Befehle (Windows: `Ctrl + Shift + P`)|
||Debugger|Werkzeug zum schrittweisen Durchlaufen und Fehlersuchen im Code|
||Extensions Marketplace|Erweiterungsbibliothek für zusätzliche Funktionen|
||Git Integration|Eingebaute Versionsverwaltung in VS Code|
|**Technische Fachbegriffe**|IDE (Integrated Development Environment)|Integrierte Entwicklungsumgebung - Komplette Software zum Programmieren|
||Syntax Highlighting (Syntaxhervorhebung)|Farbliche Kennzeichnung von Code-Elementen (Schlüsselwörter, Variablen, Strings)|
||Auto-completion / IntelliSense|Automatische Codevervollständigung während der Eingabe|
||Code Formatting (Code-Formatierung)|Automatische Anpassung des Codes an Stilrichtlinien (z.B. PEP 8)|
||Breakpoint (Haltepunkt)|Markierung im Code, an der die Ausführung beim Debuggen pausiert|
||Call Stack (Aufrufstapel)|Reihenfolge der Funktionsaufrufe während der Programmausführung|
||Build Automation Tools|Werkzeuge zur Automatisierung von Kompilierung und Paketierung|
||Source Control (Quellcodeverwaltung)|Versionskontrolle des Codes (z.B. mit Git)|
||Activity Bar|Linke Symbolleiste in VS Code mit Hauptfunktionen|
||Side Bar|Seitenleiste, die Inhalte je nach Auswahl in der Activity Bar anzeigt|
||Editor Group|Hauptbereich zum Schreiben von Code mit Tab-Funktion|
||Status Bar|Untere Statusleiste mit Informationen (Zeilennummer, Python-Version, Fehler)|
||Panel|Unterer Bereich für Terminal, Debug-Konsole, Probleme, Ausgabe|
|**Wichtige Vokabeln**|Download Page (Download-Seite)|https://code.visualstudio.com/download|
||Stable Build|Stabile, getestete Version (nicht Beta)|
||Extension (Erweiterung)|Zusatzmodul zur Funktionserweiterung|
||File Explorer|Datei-Explorer in der Activity Bar|
||Search (Suche)|Suchfunktion in der Activity Bar|
||Run & Debug|Ausführen und Debuggen in der Activity Bar|
||View Menu (Ansicht-Menü)|Menü zum Ein-/Ausblenden von Bereichen|
||Terminal Toggle|Terminal ein-/ausblenden (Windows: `` Ctrl + ` `` )|
||Typo (Tippfehler)|Schreibfehler, die durch Auto-completion vermieden werden|
||Dependencies (Abhängigkeiten)|Externe Bibliotheken/Module, die ein Projekt benötigt|

---

## Anpassungen für Windows 11 (statt macOS)

|macOS-Anweisung|Windows 11-Äquivalent|
|---|---|
|**Download:** Mac Universal Stable Build|**Download:** Windows 64-bit User Installer (oder System Installer)|
|`.zip` Datei extrahieren → `Visual Studio Code.app` in `Applications` ziehen|`.exe` Installationsdatei ausführen → Installationsassistent folgen|
|VS Code aus `Applications` starten|VS Code über Startmenü oder Desktop-Verknüpfung starten|
|**Command Palette:** `Shift + Command + P`|**Command Palette:** `Ctrl + Shift + P`|
|**Terminal öffnen:** ` Control + `` `|**Terminal öffnen:** `` Ctrl + ` ``|
|`Shell Command: Install 'code' command in PATH`|`code` Befehl wird automatisch bei Installation hinzugefügt (Option "Add to PATH" ankreuzen)|
|Administrator-Passwort eingeben|Bei Installation als Administrator ausführen (Rechtsklick → "Als Administrator ausführen")|