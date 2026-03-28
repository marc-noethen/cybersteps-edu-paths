# 🖥️ Config Cleanup Crew (Konfiguration bereinigen)

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 19.06.2025

---

## Aufgabe

**Ziel:** Mit Multi-Cursor, Find/Replace und anderen Sublime Text Features eine Konfigurationsdatei effizient bereinigen.

---

## Lösung

### Umgebung
```
OS: macOS
Editor: Sublime Text
```

### Ausgangstext

```
# Server Settings - Needs Review

server_name: webserver_alpha # Old naming convention
port_number: 8080 # Standard HTTP port
isEnabled: true # Should be boolean
admin_email: 'admin@example.com' # Contact point
log_level: 'DEBUG' # TODO: Change to INFO for production

server_name: appserver_beta # Old naming convention
port_number: 9001 # Custom app port
isEnabled: true # Should be boolean
admin_email: 'admin@example.com' # Contact point
log_level: 'DEBUG' # TODO: Change to INFO for production

server_name: dbserver_gamma # Old naming convention
port_number: 5432 # Standard DB port
isEnabled: false # Should be boolean
admin_email: 'support@example.com' # Different contact
log_level: 'WARN' # TODO: Change to INFO for production
```

---

### Durchführung

**Aufgabe 1:** `_v2` nach Server-Namen hinzufügen

```
1. Cmd+F              → Find öffnen
2. "server_alpha" eingeben
3. Cmd+D              → Alle finden (oder Find All)
4. Cmd+Right Arrow    → Zum Ende des Wortes
5. "_v2" tippen

Wiederholen für "server_beta" und "server_gamma"
```

**Alternative (effizienter):**
```
1. Cmd+H                     → Find & Replace öffnen
2. Find: "server_alpha"
   Replace: "server_alpha_v2"
3. Replace All klicken (oder Cmd+Alt+Enter)

Wiederholen für _beta und _gamma
```

---

**Aufgabe 2:** `isEnabled: true` → `enabled: true`

```
1. Cmd+H                     → Find & Replace
2. Find: "isEnabled: true"
   Replace: "enabled: true"
3. Cmd+Alt+Enter             → Replace All
```

---

**Aufgabe 3:** `isEnabled: false` → `enabled: false`

```
1. Cmd+H                     → Find & Replace
2. Find: "isEnabled: false"
   Replace: "enabled: false"
3. Cmd+Alt+Enter             → Replace All
```

---

**Aufgabe 4:** TODO-Zeilen komplett entfernen

```
1. Cmd+F                     → Find öffnen
2. "# TODO: Change to INFO for production" eingeben
3. Find All                  → Alle Vorkommen auswählen
4. Cmd+L                     → Gesamte Zeilen auswählen
5. Backspace/Delete          → Zeilen löschen
```

**Alternative:**
```
1. Cmd+H                     → Find & Replace
2. Regex aktivieren (Alt+Cmd+R oder Button)
3. Find: ".*# TODO: Change to INFO for production\n"
   Replace: (leer lassen)
4. Replace All
```

---

**Aufgabe 5:** Speichern

```
Cmd+S → "cleaned_config.txt" → Enter
```

---

## Endergebnis

```
# Server Settings - Needs Review

server_name: webserver_alpha_v2 # Old naming convention
port_number: 8080 # Standard HTTP port
enabled: true # Should be boolean
admin_email: 'admin@example.com' # Contact point

server_name: appserver_beta_v2 # Old naming convention
port_number: 9001 # Custom app port
enabled: true # Should be boolean
admin_email: 'admin@example.com' # Contact point

server_name: dbserver_gamma_v2 # Old naming convention
port_number: 5432 # Standard DB port
enabled: false # Should be boolean
admin_email: 'support@example.com' # Different contact
```

---

## Zusammenfassung der Aktionen

| Aufgabe | Methode | Shortcuts |
|---------|---------|-----------|
| 1. `_v2` hinzufügen | Find & Replace (3x) | `Cmd+H`, `Cmd+Alt+Enter` |
| 2. `isEnabled: true` | Find & Replace | `Cmd+H`, `Cmd+Alt+Enter` |
| 3. `isEnabled: false` | Find & Replace | `Cmd+H`, `Cmd+Alt+Enter` |
| 4. TODO-Zeilen löschen | Find All + Zeile löschen | `Cmd+F`, `Find All`, `Cmd+L`, `Delete` |
| 5. Speichern | Save As | `Cmd+S` |

---

## Notizen

- **Gelernt:** Find & Replace, Multi-Cursor, Regex
- **Multi-Cursor:** `Cmd+D` für gleiches Wort, `Cmd+Click` für beliebige Positionen
- **Tipp:** Regex für komplexe Muster aktivieren mit `Alt+Cmd+R`
- **Find & Replace Shortcuts:**

| Shortcut | Aktion |
|----------|--------|
| `Cmd+F` | Find |
| `Cmd+H` | Find & Replace |
| `Cmd+G` | Find Next |
| `Cmd+Shift+G` | Find Previous |
| `Cmd+Alt+Enter` | Replace All |
| `Alt+Cmd+R` | Toggle Regex |
