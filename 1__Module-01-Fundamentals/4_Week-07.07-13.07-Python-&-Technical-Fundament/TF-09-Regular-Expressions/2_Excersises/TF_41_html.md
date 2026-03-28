# 🖥️ Web 2.0 - HTML-Tags matchen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der HTML-Tags matched und den Tag-Namen in einer Capture Group erfasst, inklusive Handling von Attributen und geschachtelten Tags.

**Problem-URL:** [https://regexone.com/problem/matching_html](https://regexone.com/problem/matching_html)

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
- `<a>This is a link</a>` - einfacher Anchor-Tag
- `<a href='https://regexone.com'>Link</a>` - mit Attribut
- `<div class='test_style'>Test</div>` - Div mit Class-Attribut
- `<div>Hello <span>world</span></div>` - geschachtelte Tags

**Schritt 2:** Regex-Konstruktion
```regex
^<(\w+).*?>.*?</\1>$
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `<` - literale öffnende spitze Klammer
- `(\w+)` - **CAPTURE GROUP: Wortzeichen (Tag-Name)**
- `.*?` - beliebige Zeichen, non-greedy (Attribute)
- `>` - literale schließende spitze Klammer
- `.*?` - beliebige Zeichen, non-greedy (Inhalt zwischen Tags)
- `</` - literale öffnende Closing-Tag-Sequenz
- `\1` - Backreference zur ersten Capture Group (gleicher Tag-Name)
- `>` - literale schließende spitze Klammer
- `$` - Zeilenende

**Schritt 3:** Validierung
Alle Testfälle werden korrekt verarbeitet, Tag-Namen werden erfasst.

---

## Ergebnisse

| Test-Fall | Captured Tag | Besonderheit |
|-----------|--------------|--------------|
| `<a>This is a link</a>` | a | Einfacher Tag |
| `<a href='https://regexone.com'>Link</a>` | a | Mit Attribut |
| `<div class='test_style'>Test</div>` | div | Mit Class-Attribut |
| `<div>Hello <span>world</span></div>` | div | Äußerer Tag (geschachtelt) |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `(\w+)` erfasst den Opening-Tag-Namen
  - `.*?` ist non-greedy und matched minimal (wichtig bei geschachtelten Tags)
  - `\1` ist eine Backreference, die sicherstellt, dass Closing-Tag dem Opening-Tag entspricht
  - Non-greedy `.*?` verhindert zu langes Matching über mehrere Tags hinweg

- **Tipp:** 
  - Für produktives HTML-Parsing sollten spezialisierte Parser wie Beautiful Soup verwendet werden
  - Regex ist für einfache Editor-Operationen oder wohlgeformtes HTML geeignet
  - Non-greedy Quantifier (`*?`) sind essentiell bei verschachteltem Content