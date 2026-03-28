# 🐍 Analyze File Path

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 07.07.2025

---

## Aufgabe

**Ziel:** Extrahiere Verzeichnis, Dateiname und Dateierweiterung aus einem Dateipfad

**Anforderungen:**
- Funktion: `analyze_path(file_path_string)`
- Rückgabe: Dictionary mit 'directory', 'filename', 'extension'
- Edge Cases: Kein Verzeichnis → '.', Keine Extension → ''

---

## Lösung

```python
import os

def analyze_path(file_path_string):
    """Analysiert Dateipfad und extrahiert Komponenten."""
    directory = os.path.dirname(file_path_string)
    filename = os.path.basename(file_path_string)
    extension = os.path.splitext(file_path_string)[1]
    
    if directory == '':
        directory = '.'
    
    return {
        'directory': directory,
        'filename': filename,
        'extension': extension
    }
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `analyze_path("/home/user/documents/report.txt")` | `{'directory': '/home/user/documents', 'filename': 'report.txt', 'extension': '.txt'}` | `{'directory': '/home/user/documents', 'filename': 'report.txt', 'extension': '.txt'}` | ✅ |
| `analyze_path("myfile.zip")` | `{'directory': '.', 'filename': 'myfile.zip', 'extension': '.zip'}` | `{'directory': '.', 'filename': 'myfile.zip', 'extension': '.zip'}` | ✅ |
| `analyze_path("noextension")` | `{'directory': '.', 'filename': 'noextension', 'extension': ''}` | `{'directory': '.', 'filename': 'noextension', 'extension': ''}` | ✅ |

---

## Notizen

- **Konzept:** Verwendung von `os.path` Modul für Pfadmanipulation
- **Alternative:** `pathlib.Path` (modernerer Ansatz ab Python 3.4)