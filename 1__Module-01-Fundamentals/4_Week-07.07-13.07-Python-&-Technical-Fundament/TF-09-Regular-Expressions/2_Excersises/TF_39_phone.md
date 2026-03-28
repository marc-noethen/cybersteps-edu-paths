# 🖥️ Dial M for Match - Telefonnummern matchen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der verschiedene Telefonnummernformate erkennt und die Vorwahl (Area Code) in einer Capture Group erfasst.

**Problem-URL:** [https://regexone.com/problem/matching_phone_numbers](https://regexone.com/problem/matching_phone_numbers)

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
- `415-555-1234` - mit Bindestrichen
- `650-555-2345` - mit Bindestrichen
- `(416)555-3456` - Vorwahl in Klammern
- `202 555 4567` - mit Leerzeichen
- `4035555678` - ohne Trennzeichen
- `1 416 555 9292` - mit Ländervorwahl

**Schritt 2:** Regex-Konstruktion
```regex
^1?\s*\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `1?` - optionale Ländervorwahl "1"
- `\s*` - null oder mehr Leerzeichen
- `\(?` - optionale öffnende Klammer
- `(\d{3})` - **CAPTURE GROUP: genau 3 Ziffern (Vorwahl)**
- `\)?` - optionale schließende Klammer
- `[\s-]?` - optionales Leerzeichen oder Bindestrich
- `\d{3}` - genau 3 Ziffern (Exchange)
- `[\s-]?` - optionales Leerzeichen oder Bindestrich
- `\d{4}` - genau 4 Ziffern (Anschlussnummer)
- `$` - Zeilenende

**Schritt 3:** Validierung
Alle Testfälle werden korrekt verarbeitet und die Vorwahl wird erfasst.

---

## Ergebnisse

| Test-Fall | Captured Area Code | Format |
|-----------|-------------------|--------|
| 415-555-1234 | 415 | Mit Bindestrichen |
| 650-555-2345 | 650 | Mit Bindestrichen |
| (416)555-3456 | 416 | Vorwahl in Klammern |
| 202 555 4567 | 202 | Mit Leerzeichen |
| 4035555678 | 403 | Ohne Trennzeichen |
| 1 416 555 9292 | 416 | Mit Ländervorwahl |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `\(` und `\)` matchen literale Klammern (escaped, da `()` Metazeichen sind)
  - `[\s-]?` erlaubt flexible Trennzeichen (Leerzeichen, Bindestrich oder nichts)
  - Capture Groups `()` extrahieren spezifische Teile des Matches

- **Tipp:** Bei Telefonnummern verschiedene Formatierungsstile berücksichtigen (Klammern, Bindestriche, Leerzeichen)