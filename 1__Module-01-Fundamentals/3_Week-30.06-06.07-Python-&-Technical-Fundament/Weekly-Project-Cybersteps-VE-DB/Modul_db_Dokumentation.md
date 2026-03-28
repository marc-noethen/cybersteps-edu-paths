# 🐍 Datenbankmodul (db.py)

**Kurs:** Python & Datenbanken | **Datum:** [DD.MM.YYYY]

---

## Aufgabe

**Ziel:** Datenbankschicht für die CVE-Verwaltung implementieren

**Anforderungen:**
- Funktionen: `connect()`, `init_db()`, `insert_cve()`, `search_cves()`, `get_statistics()`, u.a.
- Rückgabe: Connection-Objekte, Listen, Dictionaries
- Edge Cases: Duplikate abfangen, leere Suchergebnisse

---

## Lösung

### Kernfunktionen

```python
import sqlite3

DB_NAME = "cvedb.sqlite"

def connect():
    """Stellt Verbindung zur SQLite-Datenbank her."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initialisiert die Datenbank mit schema.sql."""
    with open("schema.sql", "r") as f:
        schema = f.read()
    conn = connect()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def insert_cve(cve_id, description, published_date, severity, status="New"):
    """Fügt eine neue CVE ein. Fängt Duplikate ab."""
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO cve (cve_id, description, published_date, severity, status) VALUES (?, ?, ?, ?, ?)",
            (cve_id, description, published_date, severity, status)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"⚠️ CVE {cve_id} bereits vorhanden.")
    conn.close()

def search_cves(keyword=None, severity=None, date_range=None):
    """Durchsucht CVEs mit optionalen Filtern."""
    conn = connect()
    cur = conn.cursor()
    query = "SELECT cve_id, description, published_date, severity, status FROM cve WHERE 1=1"
    params = []

    if keyword:
        query += " AND description LIKE ?"
        params.append(f"%{keyword}%")
    if severity:
        query += " AND severity = ?"
        params.append(severity)
    if date_range:
        start, end = date_range
        query += " AND published_date BETWEEN ? AND ?"
        params.extend([start, end])

    cur.execute(query, params)
    results = cur.fetchall()
    conn.close()
    return results
```

### Export-Funktionen

```python
import csv
import json

def export_cves_to_csv(filename="export.csv"):
    """Exportiert alle CVEs als CSV-Datei."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cve")
    rows = cur.fetchall()
    conn.close()

    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cve_id", "description", "published_date", "severity", "status"])
        writer.writerows(rows)

def export_cves_to_json(filename="export.json"):
    """Exportiert alle CVEs als JSON-Datei."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cve")
    rows = cur.fetchall()
    conn.close()

    data = [
        {"cve_id": row[0], "description": row[1], "published_date": row[2], 
         "severity": row[3], "status": row[4]}
        for row in rows
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
```

---

## Tests

| Funktion | Input | Erwartet | Ergebnis | ✓ |
|----------|-------|----------|----------|---|
| `connect()` | - | Connection-Objekt | sqlite3.Connection | ✅ |
| `init_db()` | - | Tabellen erstellt | 5 Tabellen | ✅ |
| `insert_cve("CVE-2024-1234", ...)` | Gültige Daten | Eintrag erstellt | Erfolgreich | ✅ |
| `insert_cve("CVE-2024-1234", ...)` | Duplikat | Warnung | "⚠️ bereits vorhanden" | ✅ |
| `search_cves("buffer")` | Keyword | Passende CVEs | Liste | ✅ |
| `search_cves(severity="HIGH")` | Filter | Nur HIGH | Gefilterte Liste | ✅ |
| `export_cves_to_csv("test.csv")` | Dateiname | CSV erstellt | Datei existiert | ✅ |

---

## Notizen

- **Konzept:** Parametrisierte SQL-Queries gegen SQL-Injection
- **Pattern:** `WHERE 1=1` für dynamische Filter-Erweiterung
- **Tipp:** `IntegrityError` fängt UNIQUE-Constraint-Verletzungen ab
- **Alternative:** ORM wie SQLAlchemy für komplexere Projekte
