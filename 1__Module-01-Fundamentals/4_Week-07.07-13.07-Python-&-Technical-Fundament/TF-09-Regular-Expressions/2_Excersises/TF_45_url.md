# 🖥️ UR.*L - URLs parsen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 11.07.2025

---

## Aufgabe

**Ziel:** Erstellen eines regulären Ausdrucks, der URLs/URIs parsed und Protokoll (Scheme), Hostname und Port (optional) in separaten Capture Groups extrahiert.

**Problem-URL:** [https://regexone.com/problem/parsing_and_extracting_data_from_a_url](https://regexone.com/problem/parsing_and_extracting_data_from_a_url)

---

## Lösung

### Umgebung
```
Tool: RegexOne Web Interface
Browser: Chrome/Firefox
Regex Flavor: Standard
```

### Durchführung

**Schritt 1:** Analyse der URL-Struktur
```
protokoll://hostname:port/pfad
```

**Schritt 2:** Analyse der Test-Fälle
- `ftp://file_server.com:21/top_secret/life_changing_plans.pdf`
- `https://regexone.com/lesson/introduction#section`
- `file://localhost:4040/zip_file`
- `https://s3cur3-server.com:9999/`
- `market://search/angry%20birds`

**Schritt 3:** Regex-Konstruktion
```regex
^(\w+)://([\w\-\.]+):?(\d+)?
```

**Erklärung der Komponenten:**
- `^` - Zeilenanfang
- `(\w+)` - **CAPTURE GROUP 1: Wortzeichen (Protokoll/Scheme)**
- `://` - literale Sequenz "://"
- `([\w\-\.]+)` - **CAPTURE GROUP 2: Wortzeichen, Bindestriche, Punkte (Hostname)**
- `:?` - optionaler Doppelpunkt
- `(\d+)?` - **CAPTURE GROUP 3: optionale Ziffern (Port)**

**Schritt 4:** Validierung
Alle URLs werden korrekt geparst, Protokoll, Hostname und Port werden extrahiert.

---

## Ergebnisse

| Test-Fall | Protocol | Hostname | Port | Besonderheit |
|-----------|----------|----------|------|--------------|
| `ftp://file_server.com:21/...` | ftp | file_server.com | 21 | Mit Port |
| `https://regexone.com/...` | https | regexone.com | - | Ohne Port |
| `file://localhost:4040/...` | file | localhost | 4040 | Localhost mit Port |
| `https://s3cur3-server.com:9999/` | https | s3cur3-server.com | 9999 | Hostname mit Ziffern/Bindestrich |
| `market://search/...` | market | search | - | Custom Protokoll ohne Port |

**Status:** ✓ Solution is correct!

---

## Notizen

- **Gelernt:** 
  - `\w+` erfasst alphanumerische Protokollnamen
  - `[\w\-\.]+` behandelt Hostnames mit Bindestrichen und Punkten (z.B. "s3cur3-server.com")
  - `:?(\d+)?` macht sowohl Doppelpunkt als auch Port optional
  - Regex stoppt nach Port, ignoriert Pfad und Query-Parameter
  - URIs haben Format: `scheme://host:port/path`

- **Tipp:** 
  - Für produktives URL-Parsing: Standardbibliotheken verwenden (z.B. `urllib.parse` in Python)
  - Bindestriche in Character Classes nicht escapen, außer am Anfang/Ende
  - Optionale Komponenten mit `?` kennzeichnen
  - Port ist immer numerisch, daher `\d+` statt `\w+`