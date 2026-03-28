# 🐍 Rename Files with Word Match

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 08.07.2025

---

## Aufgabe

**Ziel:** Funktion zum Umbenennen von .txt-Dateien, die ein bestimmtes Wort enthalten

**Anforderungen:**
- Funktion: `rename_files_with_word(word)`
- Parameter: `word` (string)
- Verhalten: Sucht alle .txt-Dateien im aktuellen Verzeichnis
- Matching: Ganzes Wort (case-insensitive), nicht Teil eines anderen Wortes
- Umbenennung: `datei.txt` → `datei_FOUND.txt`
- Edge Cases: Nicht lesbare Dateien überspringen, nur reguläre Dateien verarbeiten

---

## Lösung

```python
import os
import re

def rename_files_with_word(word):
    """Benennt .txt-Dateien um, die das gesuchte Wort (ganz) enthalten."""
    # Pattern für whole-word match (case-insensitive)
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    
    for filename in os.listdir():
        # Prüfe ob reguläre .txt-Datei (case-insensitive)
        if not os.path.isfile(filename):
            continue
        if not filename.lower().endswith('.txt'):
            continue
        
        # Versuche Datei zu lesen und nach Wort zu suchen
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                if pattern.search(content):
                    # Erstelle neuen Dateinamen
                    name_without_ext = filename[:-4]
                    new_filename = name_without_ext + '_FOUND.txt'
                    os.rename(filename, new_filename)
        except (OSError, UnicodeDecodeError):
            # Überspringe nicht lesbare Dateien
            continue
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `rename_files_with_word("scatter")` → `os.listdir()` | `['notes.txt', 'scatter_FOUND.txt']` | ['notes.txt', 'scatter_FOUND.txt'] | ✅ |
| `rename_files_with_word("quick")` → `os.listdir()` | `['notes_FOUND.txt', 'scatter.txt']` | ['notes_FOUND.txt', 'scatter.txt'] | ✅ |

---

## Notizen

- **Konzept:** Regex für Whole-Word-Matching mit `\b` (Word Boundary)
- **re.escape():** Escaped Sonderzeichen im Suchwort
- **re.IGNORECASE:** Case-insensitive Suche
- **Exception Handling:** OSError (Dateizugriff) und UnicodeDecodeError (keine UTF-8-Datei)
- **os.path.isfile():** Filtert Verzeichnisse und symbolische Links aus
- **String-Slicing:** `filename[:-4]` entfernt die letzten 4 Zeichen (.txt)
