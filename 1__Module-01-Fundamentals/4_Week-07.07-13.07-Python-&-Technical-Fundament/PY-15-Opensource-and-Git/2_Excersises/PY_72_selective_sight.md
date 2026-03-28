# 🐍 Selective Sight

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Understand the purpose of a `.gitignore` file and practice using it to prevent Git from tracking specific files or patterns.

**Anforderungen:**
- Dummy-Datei erstellen: `my_secret_api_key.txt`
- `.gitignore` Datei anlegen
- Git Status vor und nach `.gitignore` vergleichen
- Rückgabe: 3 Screenshots (Status vorher, .gitignore Inhalt, Status nachher)

---

## Lösung

**Durchgeführte Schritte:**

1. **Secret-Datei erstellt:**
```bash
touch my_secret_api_key.txt
```

2. **Status vor .gitignore:**
```bash
git status
```
**Output:** `my_secret_api_key.txt` erscheint unter "Untracked files"

3. **.gitignore erstellt und editiert:**
```bash
# .gitignore Datei erstellt
echo "my_secret_api_key.txt" > .gitignore
```

**Inhalt von .gitignore:**
```
my_secret_api_key.txt
```

4. **Status nach .gitignore:**
```bash
git status
```
**Output:** 
- `my_secret_api_key.txt` ist NICHT mehr gelistet
- `.gitignore` erscheint als untracked file

5. **.gitignore zum Repository hinzugefügt:**
```bash
git add .gitignore
git commit -m "Add .gitignore to exclude secret key file"
```

6. **Zu GitHub gepusht:**
```bash
git push origin main
```

---

## Tests

| Schritt | Erwartet | Ergebnis | ✓ |
|---------|----------|----------|---|
| Secret-Datei erstellt | `my_secret_api_key.txt` | ✅ Vorhanden | ✅ |
| Status (vor ignore) | Datei untracked | ✅ Sichtbar | ✅ |
| .gitignore erstellt | Datei existiert | ✅ Angelegt | ✅ |
| .gitignore Inhalt | `my_secret_api_key.txt` | ✅ Eingetragen | ✅ |
| Status (nach ignore) | Secret nicht gelistet | ✅ Ignoriert | ✅ |
| .gitignore committed | Im Repository | ✅ Committed | ✅ |
| Push zu GitHub | Remote aktualisiert | ✅ Gepusht | ✅ |

---

## Notizen

- **Konzept:** `.gitignore` schützt sensitive Daten vor versehentlichem Commit
- **Wichtig:** `.gitignore` selbst sollte IMMER committed werden
- **Patterns:** Unterstützt Wildcards (*.log, *.env, /temp/*)
- **Use Cases:** 
  - API Keys und Secrets
  - Build-Artefakte (dist/, build/)
  - Dependencies (node_modules/)
  - IDE-Configs (.vscode/, .idea/)
  - OS-Dateien (.DS_Store, Thumbs.db)
- **Best Practice:** Früh im Projekt anlegen, um Fehler zu vermeiden
- **Template:** GitHub bietet .gitignore Templates für verschiedene Sprachen
