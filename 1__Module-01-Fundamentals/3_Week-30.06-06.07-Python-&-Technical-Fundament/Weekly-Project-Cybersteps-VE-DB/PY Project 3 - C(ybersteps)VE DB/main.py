# Datei: main.py
from db import *
import datetime

def cve_suche():
    print("\n🔍 CVE-Suche")
    keyword = input("Suchbegriff (Enter = überspringen): ") or None
    severity = input("Schweregrad (Low/Medium/High/Critical, Enter = alle): ") or None
    use_date = input("Nach Datum filtern? (j/n): ").lower()
    date_range = None
    if use_date == "j":
        start = input("Startdatum (YYYY-MM-DD): ")
        end = input("Enddatum (YYYY-MM-DD): ")
        date_range = (start, end)

    results = search_cves(keyword, severity, date_range)
    print(f"\n🔎 {len(results)} Ergebnis(se):\n")
    for r in results:
        print(f"{r[0]} | {r[2]} | {r[3]} | {r[4]}\n→ {r[1]}")

def status_aktualisieren():
    print("\n🛠 CVE-Status aktualisieren")
    cve_id = input("Gib die CVE-ID ein (z. B. CVE-2023-12345): ")
    new_status = input("Neuer Status (z. B. New, Patched, Investigating): ")

    update_cve_status(cve_id, new_status)
    print(f"✅ Status von {cve_id} wurde auf '{new_status}' gesetzt.")

def cve_exportieren():
    print("\n📄 CVE-Export")
    format = input("Format wählen (csv/json): ").lower()
    filename = input("Dateiname (ohne Endung): ")

    if format == "csv":
        export_cves_to_csv(filename + ".csv")
        print(f"✅ Exportiert nach {filename}.csv")
    elif format == "json":
        export_cves_to_json(filename + ".json")
        print(f"✅ Exportiert nach {filename}.json")
    else:
        print("❌ Ungültiges Format.")

def statistik_anzeigen():
    print("\n📊 Statistik")
    stats = get_cve_stats()

    print(f"🔢 Gesamtanzahl CVEs: {stats['total']}")
    print(f"📅 CVEs im aktuellen Monat: {stats['this_month']}")
    print("🔥 Nach Schweregrad:")
    for severity, count in stats["by_severity"].items():
        print(f"  - {severity}: {count}")

from api_import import import_cves_from_nvd

def api_import():
    print("\n🌐 CVEs per API laden")
    keyword = input("Suchbegriff (z. B. openssl, chrome, printer): ")
    max_results = int(input("Wie viele Ergebnisse laden? (z. B. 5, 10, 20): "))

    import_cves_from_nvd(keyword, max_results)

def menu():
    while True:
        print("\n=== CVEDB Menü ===")
        print("1. Neue CVE einfügen")
        print("2. Hersteller & Produkt hinzufügen")
        print("3. CVE mit Produkt verknüpfen")
        print("4. Datenbank initialisieren")
        print("5. Beenden")
        print("6. CVEs durchsuchen") 
        print("7. CVE-Status aktualisieren")  
        print("8. CVEs exportieren (CSV/JSON)")
        print("9. Bericht / Statistik anzeigen")
        print("10. CVEs per API laden")

        choice = input("Auswahl: ")

        if choice == "1":
            cve_id = input("CVE-ID: ")
            desc = input("Beschreibung: ")
            date = input("Veröffentlichungsdatum (YYYY-MM-DD): ")
            severity = input("Schweregrad (Low/Medium/High/Critical): ")
            status = input("Status (New/Patched/Investigating): ")
            insert_cve(cve_id, desc, date, severity, status)
            print("✔️ CVE eingetragen.")
        
        elif choice == "2":
            vendor = input("Herstellername: ")
            product = input("Produktname: ")
            insert_vendor(vendor)
            insert_product(product, vendor)
            print("✔️ Produkt & Hersteller hinzugefügt.")
        
        elif choice == "3":
            cve_id = input("CVE-ID: ")
            product = input("Produktname: ")
            link_cve_to_product(cve_id, product)
            print("🔗 Verknüpfung erstellt.")
        
        elif choice == "4":
            init_db()
            print("✅ Datenbank erstellt.")
        
        elif choice == "5":
            break
        
        elif choice == "6":
            cve_suche()

        elif choice == "7":
            status_aktualisieren()
        
        elif choice == "8":
            cve_exportieren()

        elif choice == "9":
            statistik_anzeigen()

        elif choice == "10":
            api_import()

        else:
            print("Ungültige Auswahl.")

# if __name__ == "__main__":
#     menu()

from gui import run_gui

if __name__ == "__main__":
    run_gui()


