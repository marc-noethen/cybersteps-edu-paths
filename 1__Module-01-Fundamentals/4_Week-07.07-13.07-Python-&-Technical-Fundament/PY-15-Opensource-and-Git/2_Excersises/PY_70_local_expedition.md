# 🐍 Local Expedition

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Practice the core local Git workflow: cloning a remote repository, making changes locally, committing them, and pushing them back to GitHub.

**Anforderungen:**
- Repository klonen: `hello-world`
- Lokale Änderung: README.md bearbeiten
- Kommandos: `git status`, `git add`, `git commit`, `git push`
- Rückgabe: Screenshots von `git log` und GitHub Repository

---

## Lösung

**Durchgeführte Schritte:**

1. **Repository geklont:**
```bash
git clone <repository-url>
cd hello-world
```

2. **README.md lokal bearbeitet:**
   - Zeile hinzugefügt: "Lokale Änderung vorgenommen!"

3. **Status überprüft:**
```bash
git status
# Output: Modified README.md erkannt
```

4. **Änderung gestaged:**
```bash
git add README.md
```

5. **Änderung committed:**
```bash
git commit -m "Update README from local machine"
```

6. **Zu GitHub gepusht:**
```bash
git push origin main
```

7. **Auf GitHub verifiziert:**
   - Repository zeigt aktualisierte README.md mit lokaler Änderung

**Nachweis:** 
- Screenshot 1: Terminal mit `git log` Output
- Screenshot 2: GitHub Repository mit aktualisierter README.md

---

## Tests

| Schritt | Kommando | Ergebnis | ✓ |
|---------|----------|----------|---|
| Repository klonen | `git clone` | ✅ Erfolgreich | ✅ |
| Änderung vornehmen | README.md editiert | ✅ "Lokale Änderung" hinzugefügt | ✅ |
| Status prüfen | `git status` | ✅ Modified angezeigt | ✅ |
| Staging | `git add README.md` | ✅ Datei staged | ✅ |
| Commit | `git commit -m "..."` | ✅ Commit erstellt | ✅ |
| Push | `git push origin main` | ✅ Zu GitHub gepusht | ✅ |
| Verifizierung | GitHub Check | ✅ Änderung sichtbar | ✅ |

---

## Notizen

- **Konzept:** Clone → Edit → Add → Commit → Push Workflow
- **Wichtig:** HTTPS vs SSH für Authentifizierung
- **Git Log:** Zeigt Commit-Historie mit Hashes, Autor, Datum und Message
- **Best Practice:** Aussagekräftige Commit-Messages verwenden
