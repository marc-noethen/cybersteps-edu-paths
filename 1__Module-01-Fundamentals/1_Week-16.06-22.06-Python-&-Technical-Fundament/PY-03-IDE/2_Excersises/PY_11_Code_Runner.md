# 🐍 Code Runner (VS Code Setup)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 18.06.2025

---

## Aufgabe

**Ziel:** Ein einfaches Python-Skript in VS Code erstellen, speichern und ausführen.

**Anforderungen:**
- VS Code starten und neue Datei erstellen
- Skript mit Name und Hobby schreiben
- Als `hello_vscode.py` speichern
- Im Terminal ausführen

---

## Lösung

### Schritt 1-4: Skript erstellen und speichern

```python
# hello_vscode.py
print("Mein Name ist Max Mustermann")
print("Mein Lieblingshobby ist Programmieren")
```

**Alternative mit f-String:**
```python
# hello_vscode.py
name = "Max Mustermann"
hobby = "Programmieren"

print(f"Mein Name ist {name}")
print(f"Mein Lieblingshobby ist {hobby}")
```

### Schritt 5-7: Terminal und Ausführung

```bash
# Terminal öffnen: View > Terminal oder Ctrl+`

# Zum Ordner navigieren
cd ~/cybersteps/python/03_ide

# Skript ausführen
python3 hello_vscode.py
```

**Erwartete Ausgabe:**
```
Mein Name ist Max Mustermann
Mein Lieblingshobby ist Programmieren
```

---

## Tests

| Aktion | Erwartet | Ergebnis | ✓ |
|--------|----------|----------|---|
| Datei erstellen | Neue leere Datei | Neue leere Datei | ✅ |
| Speichern als `.py` | Syntax-Highlighting aktiv | Syntax-Highlighting aktiv | ✅ |
| `python3 hello_vscode.py` | Ausgabe im Terminal | Ausgabe im Terminal | ✅ |

---

## Screenshot-Checkliste

Für die Einreichung muss der Screenshot zeigen:
- [ ] VS Code Fenster mit `hello_vscode.py` geöffnet
- [ ] Code im Editor sichtbar
- [ ] Integriertes Terminal sichtbar
- [ ] Ausgeführter Befehl im Terminal
- [ ] Ausgabe des Skripts im Terminal

---

## Notizen

- **Neue Datei:** `Cmd+N` (Mac) / `Ctrl+N` (Windows)
- **Speichern:** `Cmd+S` (Mac) / `Ctrl+S` (Windows)
- **Terminal öffnen:** `Ctrl+`` (Backtick)
- **Wichtig:** Dateiendung `.py` für Python-Syntax-Highlighting
- **Tipp:** `Tab`-Taste für Auto-Vervollständigung im Terminal
- **Python3:** Auf manchen Systemen `python` statt `python3`
