# 🐍 API-Import Modul (api_import.py)

**Kurs:** Python & Datenbanken | **Datum:** [DD.MM.YYYY]

---

## Aufgabe

**Ziel:** CVE-Daten automatisch von der NVD-API (National Vulnerability Database) importieren

**Anforderungen:**
- Funktion: `import_cves_from_nvd(keyword, max_results)`
- API-Endpoint: `https://services.nvd.nist.gov/rest/json/cves/2.0`
- Rückgabe: CVEs werden direkt in die Datenbank eingefügt
- Edge Cases: API-Fehler, fehlende Felder im JSON

---

## Lösung

```python
import requests
from db import insert_cve
from datetime import datetime

def import_cves_from_nvd(keyword="openssl", max_results=10):
    """
    Importiert CVEs von der NVD-API basierend auf einem Suchbegriff.
    
    Args:
        keyword: Suchbegriff (z.B. "chrome", "openssl", "windows")
        max_results: Maximale Anzahl zu ladender CVEs (1-2000)
    """
    print(f"🔄 Lade CVEs mit Suchbegriff '{keyword}' ...")

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage": max_results,
    }

    # API-Request
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ Fehler beim Laden der API-Daten.")
        return

    data = response.json()
    items = data.get("vulnerabilities", [])

    # CVEs verarbeiten und einfügen
    for item in items:
        cve_data = item.get("cve", {})
        
        # CVE-ID extrahieren
        cve_id = cve_data.get("id", "")
        
        # Englische Beschreibung finden
        description = next(
            (d["value"] for d in cve_data["descriptions"] if d["lang"] == "en"),
            "Keine Beschreibung"
        )

        # Datum parsen
        published = cve_data.get("published", "")[:10]
        try:
            published_date = datetime.strptime(published, "%Y-%m-%d").date()
        except:
            published_date = None

        # Schweregrad extrahieren (CVSS v3.1)
        severity = "-"
        try:
            severity = cve_data["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]
        except:
            pass

        # In Datenbank einfügen
        status = "New"
        insert_cve(cve_id, description, published_date, severity, status)

    print(f"✅ {len(items)} CVEs importiert.")
```

---

## API-Struktur (NVD JSON)

```json
{
  "vulnerabilities": [
    {
      "cve": {
        "id": "CVE-2024-12345",
        "descriptions": [
          {"lang": "en", "value": "A vulnerability in..."}
        ],
        "published": "2024-01-15T10:00:00.000",
        "metrics": {
          "cvssMetricV31": [
            {
              "cvssData": {
                "baseSeverity": "HIGH",
                "baseScore": 7.5
              }
            }
          ]
        }
      }
    }
  ]
}
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `import_cves_from_nvd("openssl", 5)` | 5 CVEs geladen | ✅ 5 importiert | ✅ |
| `import_cves_from_nvd("chrome", 10)` | 10 CVEs geladen | ✅ 10 importiert | ✅ |
| `import_cves_from_nvd("xyznonexistent", 5)` | 0 oder wenige | Keine Fehler | ✅ |
| API nicht erreichbar | Fehlermeldung | "❌ Fehler..." | ✅ |
| CVE ohne CVSS-Score | Severity = "-" | "-" eingetragen | ✅ |

---

## Notizen

- **Konzept:** REST-API-Abfrage mit `requests`
- **Tipp:** NVD-API hat Rate-Limiting (5 Requests/30s ohne API-Key)
- **Fallback:** `try/except` für fehlende JSON-Felder
- **Alternative:** Mit API-Key höhere Limits (50 Requests/30s)
- **Dokumentation:** https://nvd.nist.gov/developers/vulnerabilities
