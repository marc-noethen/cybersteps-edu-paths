# 🖥️ The Void Trimmer - Whitespace trimmen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der den Textinhalt von Zeilen erfasst, dabei aber führende und nachfolgende Leerzeichen/Tabs entfernt (trimmt).

**Problem-URL:** [https://regexone.com/problem/trimming_whitespace](https://regexone.com/problem/trimming_whitespace)

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
- `\t\t\tThe quick brown fox...` - drei Tabs am Anfang
- `   jumps over the lazy dog.` - drei Leerzeichen am Anfang

**Schritt 2:** Erste Regex-Version (einfach)
```regex
^\s*(.*)\s*$
```

**Problem:** `.*` ist greedy und matched auch trailing Whitespace.

**Schritt 3:** Verbesserte Regex-Konstruktion
```regex
^\s*(\S.*\S|\S)\s*$
```

**Alternative (einfacher, aber weniger präzise):**
```regex
^\s*(.*?)\s*$
```

**Erklärung der Komponenten (verbesserte Version):**
- `^` - Zeilenanfang
- `\s*` - null oder mehr Whitespace-Zeichen (nicht erfasst)
- `(\S.*\S|\S)` - **CAPTURE GROUP:**
  - `\S.*\S` - nicht-Whitespace, dann beliebige Zeichen, dann nicht-Whitespace
  - `|` - ODER
  - `\S` - einzelnes nicht-Whitespace-Zeichen
- `\s*` - null oder mehr Whitespace-Zeichen (nicht erfasst)
- `$` - Zeilenende

**Schritt 4:** Validierung
Der Textinhalt wird ohne führende/nachfolgende Whitespaces erfasst.

---

## Ergebnisse

| Test-Fall | Captured Content | Entfernte Whitespaces |
|-----------|------------------|----------------------|
| `\t\t\tThe quick brown fox...` | `The quick brown fox...` | 3 Tabs am Anfang |
| `   jumps over the lazy dog.` | `jumps over the lazy dog.` | 3 Leerzeichen am Anfang |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `\s` matched jedes Whitespace-Zeichen (Leerzeichen, Tabs, Zeilenumbrüche)
  - `\S` matched jedes Nicht-Whitespace-Zeichen
  - `.*?` ist non-greedy (minimal matching)
  - `\S.*\S` stellt sicher, dass trailing Whitespace nicht erfasst wird
  - Alternative `|\S` behandelt Einzelzeichen-Strings

- **Tipp:** 
  - Für echtes Trimming: von erstem bis letztem Nicht-Whitespace-Zeichen matchen
  - `^\s*` und `\s*$` entfernen Whitespace an Zeilenanfang/-ende
  - In der Praxis oft einfacher: eingebaute `.trim()` Funktionen verwenden