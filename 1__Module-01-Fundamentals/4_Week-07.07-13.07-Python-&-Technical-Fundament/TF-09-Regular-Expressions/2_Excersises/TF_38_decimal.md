# 🖥️ The Pointy End - Dezimalzahlen matchen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der verschiedene Dezimalzahlenformate (positiv/negativ, mit Komma, wissenschaftliche Notation) korrekt erkennt, aber keine alphanumerischen Strings wie "720p" matched.

**Problem-URL:** [https://regexone.com/problem/matching_decimal_numbers](https://regexone.com/problem/matching_decimal_numbers)

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
- `3.14529` - positive Dezimalzahl
- `-255.34` - negative Dezimalzahl
- `128` - Ganzzahl
- `1.9e10` - wissenschaftliche Notation
- `123,340.00` - Zahl mit Tausender-Trennzeichen
- `720p` - soll NICHT gematcht werden

**Schritt 2:** Regex-Konstruktion
```regex
^-?\d+(,\d+)*(\.\d+)?(e\d+)?$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `-?` - optionales Minuszeichen
- `\d+` - eine oder mehr Ziffern
- `(,\d+)*` - null oder mehr Komma-getrennte Zifferngruppen
- `(\.\d+)?` - optionaler Dezimalpunkt mit Nachkommastellen
- `(e\d+)?` - optionaler Exponent
- `$` - Zeilenende

**Schritt 3:** Validierung
Alle Testfälle werden korrekt verarbeitet:
- ✓ Zahlen werden gematcht
- ✓ "720p" wird übersprungen (wegen `$` Anker)

---

## Ergebnisse

| Test-Fall | Ergebnis | Begründung |
|-----------|----------|------------|
| 3.14529 | ✓ Match | Positive Dezimalzahl |
| -255.34 | ✓ Match | Negative Dezimalzahl |
| 128 | ✓ Match | Ganzzahl |
| 1.9e10 | ✓ Match | Wissenschaftliche Notation |
| 123,340.00 | ✓ Match | Mit Tausender-Trennzeichen |
| 720p | ✓ Skip | Endet nicht mit Zahl (Buchstabe 'p') |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `\.` matched einen literalen Punkt (nicht beliebiges Zeichen wie `.`)
  - `$` Anker ist entscheidend, um Strings mit nachfolgenden Buchstaben auszuschließen
  - Optionale Gruppen mit `?` ermöglichen Flexibilität bei verschiedenen Zahlenformaten

- **Tipp:** Bei Zahlenformaten immer Zeilenenden-Anker (`$`) verwenden, um unerwünschte Teilmatches zu vermeiden