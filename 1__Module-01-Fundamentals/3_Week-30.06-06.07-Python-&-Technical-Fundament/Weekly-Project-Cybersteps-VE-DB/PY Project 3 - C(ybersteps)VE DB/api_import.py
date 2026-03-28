import requests
from db import insert_cve
from datetime import datetime

def import_cves_from_nvd(keyword="openssl", max_results=10):
    print(f"🔄 Lade CVEs mit Suchbegriff '{keyword}' ...")

    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0"
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
        description = next((d["value"] for d in cve_data["descriptions"] if d["lang"] == "en"), "Keine Beschreibung")

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
