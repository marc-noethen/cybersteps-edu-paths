## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Das Terminal - Was und Warum?

Das **Terminal** (Windows: Eingabeaufforderung/PowerShell) ist eine textbasierte Alternative zur grafischen Oberfläche. Statt Mausklicks gibst du Befehle ein. Es ist schneller, mächtiger und unverzichtbar in der Cybersecurity, weil viele Tools nur hier funktionieren und du Prozesse automatisieren kannst.

### Die 4 wichtigsten Navigations-Befehle (Windows-Äquivalente)

1. **`cd` (ohne Parameter)** oder **`pwd`** → Zeigt, wo du gerade bist
    
    - Windows CMD: `cd`
    - Windows PowerShell: `pwd` oder `Get-Location`
2. **`dir`** oder **`ls`** → Zeigt Dateien und Ordner im aktuellen Verzeichnis
    
    - Windows: `dir` (CMD) oder `ls` (PowerShell)
3. **`cd Ordnername`** → Wechselt in einen Ordner
    
    - Beispiel: `cd Documents`
4. **`cd ..`** → Geht eine Ebene nach oben
    
    - Windows: identisch

### Pfade verstehen

- **Absoluter Pfad**: Vollständige Adresse von der Festplatte aus
    - Windows: `C:\Users\DeinName\Documents\datei.txt`
- **Relativer Pfad**: Vom aktuellen Standort aus
    - `.\Documents` (aktuelles Verzeichnis → Documents)
    - `..\Bilder` (eine Ebene hoch → Bilder)

### Umgebungsvariablen - Das Wichtigste

Umgebungsvariablen sind Systemeinstellungen, die Programme nutzen. Die wichtigste ist **PATH** - sie sagt dem System, wo es Programme finden soll.

**Anzeigen:**

- Windows CMD: `set`
- Windows PowerShell: `Get-ChildItem Env:` oder `dir env:`
- Spezifisch: `echo %PATH%` (CMD) oder `$env:PATH` (PowerShell)

### Hilfe bekommen

- Windows CMD: `Befehl /?` (z.B. `dir /?`)
- Windows PowerShell: `Get-Help Befehl` (z.B. `Get-Help Get-ChildItem`)

### Praktischer Tipp für Windows

Das Windows-Äquivalent zu macOS Terminal ist:

- **Eingabeaufforderung (CMD)**: Klassisch, einfacher
- **PowerShell**: Moderner, mächtiger, ähnlicher zu Linux/Mac

**PowerShell öffnen**: Windows-Taste drücken → "PowerShell" eingeben → Enter

**Kernbotschaft**: Das Terminal wirkt zunächst ungewohnt, ist aber wie Autofahren lernen - anfangs kompliziert, dann unverzichtbar. Mit diesen vier Basis-Befehlen (`cd`, `dir`/`ls`, `cd ..`, `cd Ordner`) kannst du bereits 80% der Grundnavigation beherrschen.

---

## Verwendete Tools, Technische Fachbegriffe und Wichtige Vokabeln

|Begriff|Bedeutung|
|---|---|
|**Verwendete Tools**||
|Terminal / Command Prompt|Windows-Anwendung zur Texteingabe von Befehlen (unter Windows: Eingabeaufforderung oder PowerShell)|
|GUI (Graphical User Interface)|Grafische Benutzeroberfläche - Bedienung durch Mausklicks, Icons und Fenster|
|CLI (Command-Line Interface)|Kommandozeilen-Schnittstelle - Bedienung durch Texteingabe|
|Shell (bash/zsh/PowerShell)|Programm, das Befehle interpretiert und ausführt (Windows verwendet PowerShell oder CMD)|
|`man` / `Get-Help`|Hilfesystem für Befehle (Windows: `Get-Help` in PowerShell oder `command /?` in CMD)|
|**Technische Fachbegriffe**||
|Working Directory|Aktuelles Arbeitsverzeichnis - der Ordner, in dem man sich gerade befindet|
|Root Directory|Wurzelverzeichnis - oberste Ebene des Dateisystems (Windows: `C:\` statt `/`)|
|Home Directory|Benutzer-Heimatverzeichnis (Windows: `C:\Users\Benutzername`)|
|Absolute Path|Vollständiger Pfad von der Wurzel aus (Windows: `C:\Users\Name\Documents\datei.txt`)|
|Relative Path|Pfad relativ zum aktuellen Verzeichnis (`.\Documents\datei.txt` oder `..\Bilder`)|
|Environment Variables|Umgebungsvariablen - Systemweite Einstellungen und Konfigurationen|
|PATH Variable|Liste von Verzeichnissen, in denen nach ausführbaren Programmen gesucht wird|
|Parent Directory|Übergeordnetes Verzeichnis - eine Ebene höher in der Ordnerstruktur|
|Hidden Files|Versteckte Dateien - normalerweise nicht sichtbare Systemdateien|
|Script|Automatisiertes Programm aus mehreren Befehlen|
|**Wichtige Befehle**||
|`pwd` / `cd` (ohne Parameter)|Zeigt aktuellen Pfad an (Windows PowerShell: `Get-Location` oder `pwd`, CMD: `cd`)|
|`ls` / `dir`|Listet Dateien und Ordner auf (Windows: `dir` in CMD, `Get-ChildItem` oder `ls` in PowerShell)|
|`cd <Ordner>`|Wechselt in angegebenen Ordner (gleich in Windows)|
|`cd ..`|Wechselt eine Ebene nach oben (gleich in Windows)|
|`cd \`|Wechselt zum Root-Verzeichnis (Windows: `cd C:\`)|
|`cd ~` / `cd %USERPROFILE%`|Wechselt zum Home-Verzeichnis (Windows CMD: `cd %USERPROFILE%`, PowerShell: `cd ~`)|
|`printenv` / `env`|Zeigt Umgebungsvariablen (Windows CMD: `set`, PowerShell: `Get-ChildItem Env:`)|
|`echo $VARIABLE` / `echo %VARIABLE%`|Zeigt Wert einer Variable (Windows CMD: `echo %VARIABLE%`, PowerShell: `$env:VARIABLE`)|
|`export` / `set`|Setzt Umgebungsvariable temporär (Windows CMD: `set VAR=wert`, PowerShell: `$env:VAR="wert"`)|