# 🐍 Item Cost Calculator (int und float kombinieren)

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 17.06.2025

---

## Aufgabe

**Ziel:** Artikelname, Menge und Preis einlesen, Gesamtkosten berechnen.

**Anforderungen:**
- Prompt 1: `Enter item name: `
- Prompt 2: `Enter quantity: ` (als Ganzzahl)
- Prompt 3: `Enter price per item: ` (als Dezimalzahl)
- Berechnung: `Gesamtkosten = Menge × Preis`
- Ausgabe: `[Quantity] [Item Name] cost $[Total Cost]`

---

## Lösung

```python
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total_cost = quantity * price
print(f"{quantity} {item_name} cost ${total_cost}")
```

**Alternative Lösungen:**
```python
# Mit formatierter Dezimalzahl (2 Nachkommastellen)
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total_cost = quantity * price
print(f"{quantity} {item_name} cost ${total_cost:.2f}")

# Mit String-Konkatenation
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total_cost = quantity * price
print(str(quantity) + " " + item_name + " cost $" + str(total_cost))
```

---

## Tests

| Item | Quantity | Price | Erwartet | Ergebnis | ✓ |
|------|----------|-------|----------|----------|---|
| `Gadget` | `3` | `12.5` | `3 Gadget cost $37.5` | `3 Gadget cost $37.5` | ✅ |
| `Apple` | `5` | `0.99` | `5 Apple cost $4.95` | `5 Apple cost $4.95` | ✅ |
| `Book` | `2` | `19.99` | `2 Book cost $39.98` | `2 Book cost $39.98` | ✅ |

---

## Notizen

- **Konzept:** Kombination von `int()` und `float()` Typkonvertierung
- **`int()`:** Für Ganzzahlen (Menge)
- **`float()`:** Für Dezimalzahlen (Preis)
- **Formatierung:** `:.2f` für 2 Nachkommastellen

**Zahlenformatierung in f-Strings:**
| Format | Beispiel | Ergebnis |
|--------|----------|----------|
| `{x}` | `{37.5}` | `37.5` |
| `{x:.2f}` | `{37.5:.2f}` | `37.50` |
| `{x:.0f}` | `{37.5:.0f}` | `38` |
| `{x:,.2f}` | `{1234.5:,.2f}` | `1,234.50` |

- **Tipp:** Bei Geldbeträgen `:.2f` für konsistente Darstellung verwenden
