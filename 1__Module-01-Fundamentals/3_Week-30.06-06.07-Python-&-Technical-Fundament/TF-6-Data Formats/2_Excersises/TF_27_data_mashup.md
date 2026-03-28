# 🖥️ Data Mashup - JSON und CSV kombinieren

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Kombiniere Daten aus JSON und CSV zu einem einheitlichen JSON-Output.

---

## Lösung

### Python Script

```python
import json
import csv
from io import StringIO

# Quelldaten
products_json_str = """
[
  {"id": "prod001", "name": "Wireless Mouse"},
  {"id": "prod002", "name": "USB Keyboard"},
  {"id": "prod003", "name": "24-inch Monitor"},
  {"id": "prod004", "name": "Webcam HD"}
]
"""

inventory_csv_str = """ProductID,Quantity,Warehouse
prod001,55,Main
prod003,12,West Wing
prod002,78,Main
prod004,30,Annex
"""

# 1. JSON parsen
products = json.loads(products_json_str)

# 2. CSV parsen
inventory = {}
reader = csv.DictReader(StringIO(inventory_csv_str))
for row in reader:
    inventory[row["ProductID"]] = {
        "quantity": int(row["Quantity"]),
        "warehouse": row["Warehouse"]
    }

# 3. Daten kombinieren
combined = []
for product in products:
    prod_id = product["id"]
    combined.append({
        "id": prod_id,
        "name": product["name"],
        "quantity": inventory[prod_id]["quantity"],
        "warehouse": inventory[prod_id]["warehouse"]
    })

# 4. Als JSON ausgeben
result = json.dumps(combined, indent=2)
print(result)
```

### Ausgabe

```json
[
  {
    "id": "prod001",
    "name": "Wireless Mouse",
    "quantity": 55,
    "warehouse": "Main"
  },
  {
    "id": "prod002",
    "name": "USB Keyboard",
    "quantity": 78,
    "warehouse": "Main"
  },
  {
    "id": "prod003",
    "name": "24-inch Monitor",
    "quantity": 12,
    "warehouse": "West Wing"
  },
  {
    "id": "prod004",
    "name": "Webcam HD",
    "quantity": 30,
    "warehouse": "Annex"
  }
]
```

---

## Notizen

- **`json.loads()`:** Parst JSON-String zu Python-Objekt
- **`json.dumps(indent=2)`:** Formatierte JSON-Ausgabe
- **`csv.DictReader()`:** Liest CSV als Liste von Dictionaries
- **`StringIO()`:** Behandelt String wie eine Datei
- **Lookup-Dict:** Inventory als Dict für schnellen Zugriff per ID
