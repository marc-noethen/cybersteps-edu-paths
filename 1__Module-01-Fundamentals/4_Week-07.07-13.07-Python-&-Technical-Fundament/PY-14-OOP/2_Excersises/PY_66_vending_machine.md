# 🐍 Vending Machine - Objektkomposition

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 10.07.2025

---

## Aufgabe

**Ziel:** Simulation eines Snackautomaten mit Bestandsverwaltung

**Anforderungen:**
- Klasse: `SnackItem(name, quantity)` - Repräsentiert einen Snack
  - `has_stock()`: Prüft ob Vorrat vorhanden
  - `sell_one()`: Verkauft ein Item (reduziert Quantity)
- Klasse: `VendingMachine()` - Verwaltet Snacks in Slots
  - `add_snack(snack_object, slot_id)`: Fügt Snack zu Slot hinzu
  - `vend(slot_id)`: Verkauft Item aus Slot
- Rückgabe: Boolean (True bei Erfolg, False bei Fehler)
- Edge Cases: Kein Vorrat, Slot existiert nicht

---

## Lösung

```python
class SnackItem:
    """Repräsentiert einen Snack mit Namen und Menge."""
    
    def __init__(self, name, quantity):
        """Initialisiert Snack mit Namen und Menge."""
        self.name = name
        self.quantity = quantity
    
    def has_stock(self):
        """Prüft ob Vorrat vorhanden ist."""
        return self.quantity > 0
    
    def sell_one(self):
        """Verkauft ein Item. Gibt True zurück bei Erfolg, False wenn kein Vorrat."""
        if self.has_stock():
            self.quantity -= 1
            return True
        return False


class VendingMachine:
    """Verwaltet Snacks in verschiedenen Slots."""
    
    def __init__(self):
        """Initialisiert leeren Automaten."""
        self.slots = {}
    
    def add_snack(self, snack_object, slot_id):
        """Fügt einen Snack zu einem Slot hinzu."""
        self.slots[slot_id] = snack_object
    
    def vend(self, slot_id):
        """Verkauft Item aus Slot. Gibt True bei Erfolg, False bei Fehler."""
        if slot_id not in self.slots:
            return False
        snack = self.slots[slot_id]
        return snack.sell_one()
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `crisps = SnackItem("Crisps", 5); vm = VendingMachine(); vm.add_snack(crisps, "A1"); vm.vend("A1")` | True | True | ✅ |
| `crisps.quantity` | 4 | 4 | ✅ |
| `vm.vend("A1")` | True | True | ✅ |
| `crisps.quantity` | 3 | 3 | ✅ |
| `choc = SnackItem("Chocolate", 0); vm.add_snack(choc, "A2"); vm.vend("A2")` | False | False | ✅ |
| `vm.vend("B1")` | False | False | ✅ |

---

## Notizen

- **Konzept:** Objektkomposition - VendingMachine enthält SnackItem Objekte
- **Dictionary:** `slots` speichert Slot-ID als Key, SnackItem als Value
- **Zustandsverwaltung:** `quantity` wird direkt im SnackItem-Objekt verwaltet
- **Delegation:** `vend()` delegiert Verkauf an `sell_one()` Methode
- **in operator:** Prüft ob Schlüssel im Dictionary existiert
- **Design Pattern:** Composition over Inheritance
