# 🖥️ Log 'Dis - Log-Dateien parsen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der aus Android adb Stack-Traces die Methodennamen, Dateinamen und Zeilennummern extrahiert.

**Problem-URL:** [https://regexone.com/problem/extracting_log_data](https://regexone.com/problem/extracting_log_data)

---

## Lösung

### Umgebung
```
Tool: RegexOne Web Interface
Browser: Chrome/Firefox
Regex Flavor: Standard
```

### Durchführung

**Schritt 1:** Analyse der Test-Fälle
- `W/dalvikvm( 1553): threadid=1: uncaught exception` → skip
- `E/( 1553): FATAL EXCEPTION: main` → skip
- `E/( 1553): java.lang.StringIndexOutOfBoundsException` → skip
- `E/( 1553):   at widget.List.makeView(ListView.java:1727)` → capture
- `E/( 1553):   at widget.List.fillDown(ListView.java:652)` → capture
- `E/( 1553):   at widget.List.fillFrom(ListView.java:709)` → capture

**Format:** `at package.class.methodname(filename:linenumber)`

**Schritt 2:** Regex-Konstruktion
```regex
^\w/.*at\s+[\w.]+\.(\w+)\((\w+\.java):(\d+)\)$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `\w/` - Log-Level (E/, W/, etc.)
- `.*` - beliebige Zeichen (Prozess-ID und Leerzeichen)
- `at\s+` - literales "at" gefolgt von Whitespace
- `[\w.]+\.` - Package und Klassenname (nicht erfasst)
- `(\w+)` - **CAPTURE GROUP 1: Methodenname**
- `\(` - literale öffnende Klammer
- `(\w+\.java)` - **CAPTURE GROUP 2: Dateiname**
- `:` - literaler Doppelpunkt
- `(\d+)` - **CAPTURE GROUP 3: Zeilennummer**
- `\)` - literale schließende Klammer
- `$` - Zeilenende

**Schritt 3:** Validierung
Nur relevante Stack-Trace-Zeilen werden gematcht und die drei Informationen extrahiert.

---

## Ergebnisse

| Test-Fall | Ergebnis | Method | Filename | Line |
|-----------|----------|--------|----------|------|
| `W/dalvikvm( 1553): threadid=1: uncaught exception` | ✓ Skip | - | - | - |
| `E/( 1553): FATAL EXCEPTION: main` | ✓ Skip | - | - | - |
| `E/( 1553): java.lang.StringIndexOutOfBoundsException` | ✓ Skip | - | - | - |
| `E/( 1553):   at widget.List.makeView(ListView.java:1727)` | ✓ Match | makeView | ListView.java | 1727 |
| `E/( 1553):   at widget.List.fillDown(ListView.java:652)` | ✓ Match | fillDown | ListView.java | 652 |
| `E/( 1553):   at widget.List.fillFrom(ListView.java:709)` | ✓ Match | fillFrom | ListView.java | 709 |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `[\w.]+\.` matched Package/Klassenpfad (z.B. "widget.List.")
  - `\(` und `\)` matchen literale Klammern (escaped)
  - `\w+\.java` matched spezifisch Java-Dateinamen
  - `\d+` erfasst numerische Zeilennummern
  - Zeilen ohne "at" und Stack-Trace-Format werden nicht gematcht

- **Tipp:** 
  - Bei Log-Parsing: genaues Format der relevanten Zeilen identifizieren
  - Mehrere Capture Groups für strukturierte Datenextraktion verwenden
  - Package/Klassenpfade mit `[\w.]+` matchen