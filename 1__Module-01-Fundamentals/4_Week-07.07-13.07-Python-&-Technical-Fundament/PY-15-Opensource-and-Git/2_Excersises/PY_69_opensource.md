# 🐍 Open Source Explorer

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Explore a popular open-source Python project on GitHub, understand its contribution guidelines, and see how changes are actually submitted and reviewed.

**Anforderungen:**
- Repository: [psf/requests](https://github.com/psf/requests)
- Aufgaben: Contribution Guidelines lesen, Issues analysieren, gemergten Pull Request untersuchen
- Rückgabe: Antworten auf 3 Fragen

---

## Lösung

### Question 1: Bevorzugte Methode für Contributions

**Antwort:** GitHub issue search

Die Contribution Guidelines des `requests`-Projekts erwarten von Contributors primär, dass sie die GitHub Issue Search nutzen, um zunächst zu prüfen, ob ein Problem bereits gemeldet wurde, bevor sie neue Issues oder Pull Requests erstellen.

---

### Question 2: Ausgewähltes Issue

**Title:** builtin_str(method) incorrectly converts binary method names

**Issue Number:** #7152

**Beschreibung:** 
In diesem Issue beschreibt ein Entwickler ein Problem mit der Methode `builtin_str` in `requests/models.py`. Der Code `method = builtin_str(method)` verursacht Fehler bei der Verwendung von binären Methodennamen, da die Funktion Bytes korrekt in Strings dekodieren sollte.

---

### Question 3: Analysierter Pull Request

**Title:** ValueError when calling requests.get on Windows systems

**Pull Request Number:** #6104

**Hauptzweck:** Workaround für einen ValueError, der auf Windows-Systemen beim Aufruf von `requests.get` auftrat.

**Geänderte Dateien:**
- `utils.py`

---

## Tests

| Frage | Status | ✓ |
|-------|--------|---|
| Question 1: Contribution-Methode identifiziert | GitHub issue search | ✅ |
| Question 2: Issue gefunden und beschrieben | #7152 - builtin_str Problem | ✅ |
| Question 3: Pull Request analysiert | #6104 - Windows ValueError Fix | ✅ |

---

## Notizen

- **Konzept:** Open Source Contribution Workflow
- **Repository:** [psf/requests](https://github.com/psf/requests) - beliebte HTTP-Library für Python
- **Lernziel:** Verstehen, wie Open-Source-Projekte strukturiert sind und wie Contributions ablaufen
- **Best Practice:** Immer zuerst nach existierenden Issues suchen, bevor man neue erstellt
