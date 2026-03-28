# 🖥️ Recurring Report Formatter (Makro-Transformation)

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 19.06.2025

---

## Aufgabe

**Ziel:** Einen wiederholbaren, tastaturgesteuerten Prozess in Sublime Text entwickeln, um Daten von Format X zu Format Y zu transformieren - idealerweise mit einem einzigen Shortcut.

---

## Lösung

### Umgebung
```
OS: macOS
Editor: Sublime Text
```

### Format X (Eingabe)
```
Hardware;Laptop;Operational
Software;Antivirus;Needs Update
Network;Firewall;Configured
Access;VPN;Enabled
Hardware;Monitor;Operational
Software;OS;Patched
```

### Format Y (Ziel)
```
* **Hardware:** Laptop (Status: Operational)
* **Software:** Antivirus (Status: Needs Update)
* **Network:** Firewall (Status: Configured)
* **Access:** VPN (Status: Enabled)
* **Hardware:** Monitor (Status: Operational)
* **Software:** OS (Status: Patched)
```

---

## Methode 1: Makro aufnehmen (EMPFOHLEN)

### Schritt 1: Makro-Aufnahme starten
```
Ctrl+Q                   → Makro-Aufnahme starten
```

### Schritt 2: Eine Zeile transformieren
Startposition: Cursor am Anfang von Zeile 1

```
1. "* **" tippen         → Prefix einfügen
2. Cmd+D                 → "Hardware" auswählen (bis zum ;)
   ODER: Ctrl+Shift+M    → Bis zum Trennzeichen
3. Option+Right (2x)     → Nach "Hardware" springen
4. Cmd+Shift+K           → Zeichen löschen? NEIN...

Besser so:
1. Cmd+Left              → Zeilenanfang
2. "* **" tippen
3. Cmd+F                 → Find
4. ";" eingeben, Enter   → Zum ersten ; springen
5. Esc                   → Find schließen
6. ":** " tippen         → ; ersetzen mit :** 
7. Backspace             → ; löschen (vorheriges Zeichen)
   ... (kompliziert!)
```

### Schritt 2 (EINFACHER): Find & Replace Ansatz

**Besser: Makro mit einfachen Schritten:**
```
Ctrl+Q                   → Aufnahme starten
Cmd+Left                 → Zeilenanfang
"* **" tippen
Cmd+Right                → Zeilenende
Down Arrow               → Nächste Zeile
Ctrl+Q                   → Aufnahme stoppen
```

---

## Methode 2: Find & Replace mit Regex (BESTE LÖSUNG)

### Durchführung

```
1. Cmd+H                 → Find & Replace öffnen
2. Alt+Cmd+R             → Regex aktivieren (Punkt wird hervorgehoben)
3. Find:    ^(.+);(.+);(.+)$
   Replace: * **$1:** $2 (Status: $3)
4. Cmd+Alt+Enter         → Replace All
```

### Regex erklärt

| Pattern | Bedeutung |
|---------|-----------|
| `^` | Zeilenanfang |
| `(.+)` | Gruppe: Ein oder mehr Zeichen (greedy) |
| `;` | Literal Semikolon |
| `$` | Zeilenende |
| `$1, $2, $3` | Rückreferenz auf Gruppen |

**Transformation:**
```
Hardware;Laptop;Operational
   $1      $2       $3

→ * **$1:** $2 (Status: $3)
→ * **Hardware:** Laptop (Status: Operational)
```

---

## Methode 3: Multi-Cursor Ansatz

### Durchführung

```
1. Cmd+A                 → Alles auswählen
2. Cmd+Shift+L           → Cursor an jedes Zeilenende
3. Cmd+Left              → Alle Cursor zum Zeilenanfang
4. "* **" tippen         → Wird in allen Zeilen eingefügt
5. Cmd+D (für jedes ";") → Kompliziert...
```

→ Nicht praktikabel für diese Aufgabe

---

## Empfohlene Lösung: Regex Find & Replace

### Komplette Anleitung

**Einmalige Einrichtung:**
```
1. Cmd+H                          → Find & Replace
2. Alt+Cmd+R                      → Regex aktivieren
3. Find:    ^(.+);(.+);(.+)$
4. Replace: * **$1:** $2 (Status: $3)
5. Cmd+Alt+Enter                  → Replace All
```

**Für zukünftige Verwendung als Makro:**
```
1. Ctrl+Q                         → Aufnahme starten
2. Alle obigen Schritte ausführen
3. Ctrl+Q                         → Aufnahme stoppen
4. Ctrl+Shift+Q                   → Makro abspielen
```

**Als Snippet speichern (fortgeschritten):**
- Tools → Developer → New Snippet
- Regex-Pattern speichern für Wiederverwendung

---

## Ergebnis

### Vorher (Format X)
```
Hardware;Laptop;Operational
Software;Antivirus;Needs Update
Network;Firewall;Configured
Access;VPN;Enabled
Hardware;Monitor;Operational
Software;OS;Patched
```

### Nachher (Format Y)
```
* **Hardware:** Laptop (Status: Operational)
* **Software:** Antivirus (Status: Needs Update)
* **Network:** Firewall (Status: Configured)
* **Access:** VPN (Status: Enabled)
* **Hardware:** Monitor (Status: Operational)
* **Software:** OS (Status: Patched)
```

---

## Shortcut-Übersicht

| Shortcut | Aktion |
|----------|--------|
| `Ctrl+Q` | Makro Aufnahme starten/stoppen |
| `Ctrl+Shift+Q` | Makro abspielen |
| `Cmd+H` | Find & Replace |
| `Alt+Cmd+R` | Regex Toggle |
| `Cmd+Alt+Enter` | Replace All |
| `Cmd+Shift+L` | Split Selection into Lines |

---

## Notizen

- **Gelernt:** Regex Find & Replace, Makros, Capture Groups
- **Beste Methode:** Regex für strukturierte Transformationen
- **Makros:** Gut für repetitive Tastatureingaben, weniger für komplexe Logik
- **Regex Capture Groups:** `(.+)` erfasst Text, `$1` referenziert ihn

**Nützliche Regex-Patterns:**
| Pattern | Bedeutung |
|---------|-----------|
| `.` | Ein beliebiges Zeichen |
| `+` | Ein oder mehr |
| `*` | Null oder mehr |
| `\d` | Ziffer |
| `\w` | Wort-Zeichen |
| `\s` | Whitespace |
| `^` | Zeilenanfang |
| `$` | Zeilenende |
| `()` | Capture Group |
| `$1` | Referenz auf 1. Gruppe |
