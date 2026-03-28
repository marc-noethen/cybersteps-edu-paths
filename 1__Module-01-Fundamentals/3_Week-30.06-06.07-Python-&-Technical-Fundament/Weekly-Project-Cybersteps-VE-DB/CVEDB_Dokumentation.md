# 🐍 CVE-Datenbank (CVEDB)

**Kurs:** Python & Datenbanken | **Datum:** [DD.MM.YYYY]

---

## Aufgabe

**Ziel:** Entwicklung einer eigenen CVE-Datenbank (Common Vulnerabilities and Exposures) zur Verwaltung, Analyse und Recherche von Sicherheitslücken.

**Anforderungen:**
- Relationale SQLite-Datenbank mit mehreren verknüpften Tabellen
- CRUD-Operationen (Create, Read, Update, Delete)
- API-Integration zur automatischen Datenabfrage von NVD
- Grafische Benutzeroberfläche (GUI) mit tkinter
- Export-Funktionen (CSV/JSON)
- Statistik- und Analysefunktionen

---

## Projektstruktur

```
CVEDB/
├── main.py           # Hauptprogramm (CLI + GUI-Start)
├── db.py             # Datenbankfunktionen
├── api_import.py     # NVD API-Import
├── gui.py            # Grafische Oberfläche
├── utils.py          # Hilfsfunktionen (leer)
├── schema.sql        # Datenbankschema
├── cvedb.sqlite      # SQLite-Datenbank
└── readme.md         # Projektbeschreibung
```

---

## Lösung

### 1. Datenbankschema (`schema.sql`)

```sql
-- Hersteller-Tabelle
CREATE TABLE IF NOT EXISTS vendor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Produkt-Tabelle (verknüpft mit Hersteller)
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    vendor_id INTEGER NOT NULL,
    FOREIGN KEY (vendor_id) REFERENCES vendor(id)
);

-- CVE-Haupttabelle
CREATE TABLE IF NOT EXISTS cve (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT NOT NULL UNIQUE,
    description TEXT,
    published_date TEXT,
    severity TEXT CHECK(severity IN ('Low', 'Medium', 'High', 'Critical')),
    status TEXT CHECK(status IN ('New', 'Patched', 'Investigating'))
);

-- Verknüpfungstabelle: CVE ↔ Produkt (n:m Beziehung)
CREATE TABLE IF NOT EXISTS cve_product (
    cve_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    PRIMARY KEY (cve_id, product_id),
    FOREIGN KEY (cve_id) REFERENCES cve(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Referenz-URLs zu CVEs
CREATE TABLE IF NOT EXISTS reference (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (cve_id) REFERENCES cve(id)
);
```

**ER-Diagramm (Beziehungen):**
```
vendor (1) ──────< product (n)
                      │
                      │ (n:m)
                      │
cve (n) >────────< cve_product
  │
  └────< reference (1:n)
```

---

### 2. Datenbankmodul (`db.py`)

```python
import sqlite3

DB_NAME = "cvedb.sqlite"

def connect():
    """Stellt Verbindung zur Datenbank her."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initialisiert die Datenbank mit dem Schema."""
    with open("schema.sql", "r") as f:
        schema = f.read()
    conn = connect()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def insert_cve(cve_id, description, published_date, severity, status="New"):
    """Fügt eine neue CVE ein."""
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
    """Durchsucht CVEs nach Kriterien."""
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

def get_statistics():
    """Gibt Statistiken zur Datenbank zurück."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM cve")
    total = cur.fetchone()[0]

    def count_by_sev(sev):
        cur.execute("SELECT COUNT(*) FROM cve WHERE severity = ?", (sev,))
        return cur.fetchone()[0]

    stats = {
        "total": total,
        "critical": count_by_sev("CRITICAL"),
        "high": count_by_sev("HIGH"),
        "medium": count_by_sev("MEDIUM"),
        "low": count_by_sev("LOW"),
    }
    conn.close()
    return stats
```

---

### 3. API-Import (`api_import.py`)

```python
import requests
from db import insert_cve
from datetime import datetime

def import_cves_from_nvd(keyword="openssl", max_results=10):
    """Importiert CVEs von der NVD-API."""
    print(f"🔄 Lade CVEs mit Suchbegriff '{keyword}' ...")

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage": max_results,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ Fehler beim Laden der API-Daten.")
        return

    data = response.json()
    items = data.get("vulnerabilities", [])

    for item in items:
        cve_data = item.get("cve", {})
        cve_id = cve_data.get("id", "")
        description = next(
            (d["value"] for d in cve_data["descriptions"] if d["lang"] == "en"),
            "Keine Beschreibung"
        )

        published = cve_data.get("published", "")[:10]
        try:
            published_date = datetime.strptime(published, "%Y-%m-%d").date()
        except:
            published_date = None

        severity = "-"
        try:
            severity = cve_data["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]
        except:
            pass

        status = "New"
        insert_cve(cve_id, description, published_date, severity, status)

    print(f"✅ {len(items)} CVEs importiert.")
```

---

### 4. GUI (`gui.py`)

```python
import tkinter as tk
from tkinter import messagebox, ttk
from db import search_cves, get_statistics
from api_import import import_cves_from_nvd

def run_gui():
    """Startet die grafische Benutzeroberfläche."""
    root = tk.Tk()
    root.title("🛡️ CVE-Datenbank")
    root.geometry("900x600")

    # Suchbereich mit Eingabefeldern
    # Treeview-Tabelle für Ergebnisse
    # Buttons für Import und Statistik
    
    root.mainloop()
```

---

## Tests

### Funktionstest: Datenbankoperationen

| Funktion | Input | Erwartet | Ergebnis | ✓ |
|----------|-------|----------|----------|---|
| `init_db()` | - | Tabellen erstellt | Tabellen vorhanden | ✅ |
| `insert_cve()` | CVE-2024-1234, "Test", ... | CVE eingefügt | Erfolgreich | ✅ |
| `insert_cve()` | Duplikat CVE-ID | Warnung | "⚠️ bereits vorhanden" | ✅ |
| `search_cves("ssl")` | Keyword | Passende Ergebnisse | Liste mit Matches | ✅ |
| `get_statistics()` | - | Dict mit Zahlen | {"total": n, ...} | ✅ |

### Funktionstest: API-Import

| Funktion | Input | Erwartet | Ergebnis | ✓ |
|----------|-------|----------|----------|---|
| `import_cves_from_nvd("chrome", 5)` | Keyword, Anzahl | 5 CVEs geladen | ✅ Importiert | ✅ |
| `import_cves_from_nvd("xyz123", 10)` | Unbekannt | 0 oder wenige | Keine Fehler | ✅ |

---

## Ausführung

### Voraussetzungen

```bash
# Virtual Environment erstellen und aktivieren
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder: .\venv\Scripts\activate  # Windows

# Abhängigkeiten installieren
pip install requests
```

### Programm starten

```bash
# GUI starten (Standard)
python main.py

# Oder: CLI-Menü aktivieren (in main.py anpassen)
# if __name__ == "__main__":
#     menu()  # Statt run_gui()
```

### CLI-Menü Optionen

```
=== CVEDB Menü ===
1. Neue CVE einfügen
2. Hersteller & Produkt hinzufügen
3. CVE mit Produkt verknüpfen
4. Datenbank initialisieren
5. Beenden
6. CVEs durchsuchen
7. CVE-Status aktualisieren
8. CVEs exportieren (CSV/JSON)
9. Bericht / Statistik anzeigen
10. CVEs per API laden
```

---

## Erreichte Stages

| Stage | Beschreibung | Status |
|-------|--------------|--------|
| **Stage 1** | Foundations (Schema, Manual Entry, Query) | ✅ Erledigt |
| **Stage 2** | Core (Bulk Import, Analyze, Smart Filters) | ✅ Erledigt |
| **Stage 3** | Live Data (NVD API Sync) | ✅ Erledigt |
| **Stage 4** | AI Query Generation | ❌ Nicht implementiert |
| **Stage 5** | Eigene Features (GUI, Export) | ✅ Erledigt |

---

## Notizen

### Gelernt
- **SQLite mit Python:** Verwendung des `sqlite3`-Moduls für CRUD-Operationen
- **API-Integration:** Abrufen von JSON-Daten mit `requests`
- **GUI-Entwicklung:** Aufbau einer Oberfläche mit `tkinter` und `ttk.Treeview`
- **Datenbankdesign:** Normalisierung mit Foreign Keys und n:m-Beziehungen

### Design-Entscheidungen
- **SQLite gewählt:** Einfach, serverlos, kommt mit Python
- **Severity als CHECK-Constraint:** Nur erlaubte Werte (Low/Medium/High/Critical)
- **Separate Module:** Klare Trennung von DB, API, GUI und Main

### Herausforderungen
- **API-Datenstruktur:** NVD-JSON ist verschachtelt, Severity nicht immer vorhanden
- **GUI-Layout:** Treeview-Spaltenbreiten und Responsive Design
- **Encoding:** Umlaute in Beschreibungen korrekt speichern/anzeigen

### Verbesserungsideen
- [ ] AI-gestützte Query-Generierung (Stage 4)
- [ ] Automatische regelmäßige Synchronisation
- [ ] Visualisierungen mit matplotlib
- [ ] Alerting bei kritischen CVEs
