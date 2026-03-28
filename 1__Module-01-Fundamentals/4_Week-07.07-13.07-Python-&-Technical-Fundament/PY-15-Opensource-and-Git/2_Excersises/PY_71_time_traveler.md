# 🐍 Time Traveler

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Practice navigating your project's history using `git log` to find past commits and `git checkout` to view the project state at that point in time.

**Anforderungen:**
- Zwei neue Commits erstellen
- Git History mit `git log` inspizieren
- Mit `git checkout` zu älterem Commit wechseln
- Rückgabe: Screenshots und Commit-Hash

---

## Lösung

**Durchgeführte Schritte:**

1. **Erste Änderung:**
```bash
# README.md editiert: "Hinzufügen einer weiteren Zeile für den Verlauf"
git add README.md
git commit -m "Add history line"
```

2. **Zweite Änderung:**
```bash
# README.md editiert: "Final line for log test"
git add README.md
git commit -m "Add final line"
```

3. **History inspiziert:**
```bash
git log
```

**Identifizierter Commit:**
- **Hash:** `9afa096bdbdeabcfc1692e4285c29b5213fe6731`
- **Message:** "Add history line"

4. **Zeitreise durchgeführt:**
```bash
git checkout 9afa096bdbdeabcfc1692e4285c29b5213fe6731
# HEAD detached at 9afa096
```

5. **Vergangenen Zustand verifiziert:**
   - README.md enthält: "Hinzufügen einer weiteren Zeile für den Verlauf"
   - README.md enthält NICHT: "Final line for log test"

6. **Zurück zur Gegenwart:**
```bash
git checkout main
```

---

## Tests

| Schritt | Erwartet | Ergebnis | ✓ |
|---------|----------|----------|---|
| Commit 1 erstellt | "Add history line" | ✅ Committed | ✅ |
| Commit 2 erstellt | "Add final line" | ✅ Committed | ✅ |
| Git Log ausgeführt | Commits sichtbar | ✅ History angezeigt | ✅ |
| Checkout zu altem Commit | Detached HEAD | ✅ Gewechselt | ✅ |
| README im alten Zustand | Nur erste Zeile | ✅ Korrekt | ✅ |
| Zurück zu main | Beide Zeilen | ✅ Zurück | ✅ |

---

## Notizen

- **Konzept:** Git History Navigation und Detached HEAD State
- **Commit Hash:** `9afa096bdbdeabcfc1692e4285c29b5213fe6731`
- **Detached HEAD:** Temporärer Zustand zum Inspizieren vergangener Versionen
- **Warnung:** Änderungen in detached HEAD gehen verloren ohne Branch
- **Alternative:** `git log --oneline` für kompakte Ansicht
- **Praktisch:** Nützlich zum Debuggen und Nachvollziehen von Änderungen
