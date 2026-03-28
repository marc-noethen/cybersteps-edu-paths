# 🖥️ Address Book - E-Mail-Adressen matchen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der E-Mail-Adressen matched und dabei nur den Namen-Teil (vor dem @) extrahiert, ohne Plus-Adressierung (+filter).

**Problem-URL:** [https://regexone.com/problem/matching_emails](https://regexone.com/problem/matching_emails)

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
- `tom@hogwarts.com` - einfache E-Mail
- `tom.riddle@hogwarts.com` - Name mit Punkt
- `tom.riddle+regexone@hogwarts.com` - mit Plus-Adressierung
- `tom@hogwarts.eu.com` - mehrkomponentige Domain
- `potter@hogwarts.com` - einfache E-Mail
- `harry@hogwarts.com` - einfache E-Mail
- `hermione+regexone@hogwarts.com` - mit Plus-Adressierung

**Schritt 2:** Regex-Konstruktion
```regex
^([\w.]+)\+?.*@[\w.]+$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `([\w.]+)` - **CAPTURE GROUP: Wortzeichen oder Punkte (E-Mail-Name)**
- `\+?` - optionales Plus-Zeichen (Beginn der Filterung)
- `.*` - beliebige Zeichen (Filter-Text, nicht erfasst)
- `@` - literales @-Symbol
- `[\w.]+` - Wortzeichen oder Punkte (Domain)
- `$` - Zeilenende

**Schritt 3:** Validierung
Alle Testfälle werden korrekt verarbeitet, nur der E-Mail-Name wird erfasst.

---

## Ergebnisse

| Test-Fall | Captured Name | Besonderheit |
|-----------|---------------|--------------|
| tom@hogwarts.com | tom | Einfacher Name |
| tom.riddle@hogwarts.com | tom.riddle | Name mit Punkt |
| tom.riddle+regexone@hogwarts.com | tom.riddle | Plus-Filter ausgeschlossen |
| tom@hogwarts.eu.com | tom | Multi-Domain |
| potter@hogwarts.com | potter | Einfacher Name |
| harry@hogwarts.com | harry | Einfacher Name |
| hermione+regexone@hogwarts.com | hermione | Plus-Filter ausgeschlossen |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `[\w.]+` matched Wortzeichen (Buchstaben, Ziffern, Underscore) und Punkte
  - `\+?.*` matched optionale Plus-Adressierung, erfasst sie aber nicht in der Gruppe
  - `[\w.]+` nach `@` behandelt mehrkomponentige Domains wie "hogwarts.eu.com"

- **Tipp:** 
  - Plus-Adressierung ist eine nützliche Funktion für Filterung und Tracking
  - `\w` ist Shorthand für `[a-zA-Z0-9_]`
  - Für produktive E-Mail-Validierung Standardbibliotheken verwenden