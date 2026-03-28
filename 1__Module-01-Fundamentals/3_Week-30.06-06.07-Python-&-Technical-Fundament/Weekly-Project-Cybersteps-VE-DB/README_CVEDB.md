# 🛡️ CVEDB - CVE-Datenbank

Eine Python-Anwendung zur Verwaltung und Analyse von Sicherheitslücken (CVEs).

## 🚀 Features

- **Datenbankmanagement:** SQLite-basierte Speicherung von CVEs
- **API-Integration:** Automatischer Import von der NVD (National Vulnerability Database)
- **Suchfunktion:** Filtern nach Stichwort, Schweregrad und Datum
- **GUI:** Grafische Oberfläche mit tkinter
- **Export:** Daten als CSV oder JSON exportieren
- **Statistiken:** Auswertung nach Schweregrad und Zeitraum

## 📋 Voraussetzungen

- Python 3.10+
- requests Bibliothek

## 🔧 Installation

```bash
# Repository klonen oder Dateien herunterladen
cd cvedb

# Virtual Environment erstellen
python -m venv venv

# Aktivieren
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Abhängigkeiten installieren
pip install requests
```

## ▶️ Verwendung

```bash
# GUI starten
python main.py
```

### GUI-Funktionen
- 🔍 **Suchen:** CVEs nach Stichwort und Schweregrad filtern
- 📥 **API-Import:** CVEs von NVD laden (Suchbegriff + Anzahl)
- 📊 **Statistik:** Übersicht über alle CVEs

## 📁 Projektstruktur

| Datei | Beschreibung |
|-------|--------------|
| `main.py` | Hauptprogramm (CLI + GUI) |
| `db.py` | Datenbankfunktionen |
| `api_import.py` | NVD API-Integration |
| `gui.py` | Grafische Oberfläche |
| `schema.sql` | Datenbankschema |
| `cvedb.sqlite` | SQLite-Datenbank |

## 🗄️ Datenbankschema

```
vendor ─────< product
                 │
                 │ (n:m)
                 │
cve >───────< cve_product
 │
 └────< reference
```

## 📊 Beispiel-Nutzung

```python
from db import search_cves, get_statistics
from api_import import import_cves_from_nvd

# CVEs von NVD importieren
import_cves_from_nvd("openssl", 10)

# CVEs suchen
results = search_cves(keyword="buffer", severity="HIGH")

# Statistiken abrufen
stats = get_statistics()
print(f"Gesamt: {stats['total']} CVEs")
```

## 📝 Lizenz

Dieses Projekt wurde im Rahmen eines Kurses erstellt.
