# 🖥️ X Files - Dateinamen matchen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der nur Bilddateien (.jpg, .png, .gif) matched und dabei Dateiname und Extension separat in Capture Groups erfasst. Temporäre Dateien (.tmp) und andere Dateitypen sollen ignoriert werden.

**Problem-URL:** [https://regexone.com/problem/matching_filenames](https://regexone.com/problem/matching_filenames)

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
- `.bash_profile` - versteckte Datei → skip
- `workspace.doc` - kein Bild → skip
- `img0912.jpg` - Bilddatei → match
- `updated_img0912.png` - Bilddatei → match
- `documentation.html` - kein Bild → skip
- `favicon.gif` - Bilddatei → match
- `img0912.jpg.tmp` - temporäre Datei → skip
- `access.lock` - kein Bild → skip

**Schritt 2:** Regex-Konstruktion
```regex
^(\w+)\.(jpg|png|gif)$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `(\w+)` - **CAPTURE GROUP 1: Wortzeichen (Dateiname)**
- `\.` - literaler Punkt (escaped)
- `(jpg|png|gif)` - **CAPTURE GROUP 2: eine der drei Bild-Extensions**
- `$` - Zeilenende

**Schritt 3:** Validierung
Nur Bilddateien werden gematcht, temporäre und andere Dateien werden übersprungen.

---

## Ergebnisse

| Test-Fall | Ergebnis | Dateiname | Extension | Begründung |
|-----------|----------|-----------|-----------|------------|
| .bash_profile | ✓ Skip | - | - | Beginnt mit Punkt (keine Dateiname vor `.`) |
| workspace.doc | ✓ Skip | - | - | Falsche Extension |
| img0912.jpg | ✓ Match | img0912 | jpg | Gültige Bilddatei |
| updated_img0912.png | ✓ Match | updated_img0912 | png | Gültige Bilddatei |
| documentation.html | ✓ Skip | - | - | Falsche Extension |
| favicon.gif | ✓ Match | favicon | gif | Gültige Bilddatei |
| img0912.jpg.tmp | ✓ Skip | - | - | Endet mit .tmp, nicht mit Bild-Extension |
| access.lock | ✓ Skip | - | - | Falsche Extension |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `\.` matched einen literalen Punkt (nicht beliebiges Zeichen)
  - `(jpg|png|gif)` verwendet Alternation (`|`) für mehrere Optionen
  - `$` Anker ist entscheidend, um `.tmp` Dateien auszuschließen
  - `\w+` matched alphanumerische Zeichen und Unterstriche

- **Tipp:** 
  - Zeilenende-Anker (`$`) verhindert Matching von Dateien mit zusätzlichen Extensions
  - Für versteckte Dateien (beginnend mit `.`) fehlt der Dateiname vor dem Punkt