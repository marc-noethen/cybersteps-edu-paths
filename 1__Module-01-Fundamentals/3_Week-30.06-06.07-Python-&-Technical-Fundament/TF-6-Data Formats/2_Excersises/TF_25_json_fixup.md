# 🖥️ The Fix-Up - JSON Syntax korrigieren

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Korrigiere die Syntax-Fehler im JSON-Snippet, um es valide zu machen.

---

## Lösung

### Fehlerhaftes JSON (Original)

```json
{
  "username": 'alice',
  "userID"- 101,
  "isActive": true,
  "interests": [hiking, reading,],
  "last_login": 2023-10-26T10:00:00Z
```

### Korrigiertes JSON

```json
{
  "username": "alice",
  "userID": 101,
  "isActive": true,
  "interests": ["hiking", "reading"],
  "last_login": "2023-10-26T10:00:00Z"
}
```

---

## Fehleranalyse

| Zeile | Fehler | Korrektur |
|-------|--------|-----------|
| 2 | `'alice'` (einfache Anführungszeichen) | `"alice"` (doppelte) |
| 3 | `"userID"- 101` (Bindestrich) | `"userID": 101` (Doppelpunkt) |
| 5 | `[hiking, reading,]` (keine Strings, trailing comma) | `["hiking", "reading"]` |
| 6 | Datum ohne Anführungszeichen | `"2023-10-26T10:00:00Z"` |
| 7 | Fehlende schließende `}` | `}` hinzugefügt |

---

## Notizen

- **JSON-Regel:** Strings immer mit `"` (doppelte Anführungszeichen)
- **JSON-Regel:** Key-Value-Trennung mit `:` (Doppelpunkt)
- **JSON-Regel:** Kein trailing comma nach letztem Array-Element
- **Validator:** jsonlint.com oder VS Code JSON-Extension
