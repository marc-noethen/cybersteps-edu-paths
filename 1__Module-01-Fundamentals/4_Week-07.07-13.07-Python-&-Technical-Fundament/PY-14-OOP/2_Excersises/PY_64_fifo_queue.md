# 🐍 FIFO Queue - First-In First-Out Datenstruktur

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 09.07.2025

---

## Aufgabe

**Ziel:** Implementierung einer FIFO (First-In, First-Out) Queue Datenstruktur

**Anforderungen:**
- Klasse: `FIFOQueue`
- `__init__(self)`: Initialisiert leere Liste `items`
- `enqueue(self, item)`: Fügt Element am Ende hinzu
- `dequeue(self)`: Entfernt und gibt erstes Element zurück
- `size(self)`: Gibt Anzahl der Elemente zurück
- Edge Cases: `dequeue()` bei leerer Queue → None

---

## Lösung

```python
class FIFOQueue:
    """Implementiert eine FIFO (First-In, First-Out) Queue."""
    
    def __init__(self):
        """Initialisiert eine leere Queue."""
        self.items = []
    
    def enqueue(self, item):
        """Fügt ein Element am Ende der Queue hinzu."""
        self.items.append(item)
    
    def dequeue(self):
        """Entfernt und gibt das erste Element zurück. None bei leerer Queue."""
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def size(self):
        """Gibt die Anzahl der Elemente in der Queue zurück."""
        return len(self.items)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `q = FIFOQueue(); q.enqueue("apple"); q.enqueue("banana"); q.size()` | 2 | 2 | ✅ |
| `q.dequeue()` | "apple" | apple | ✅ |
| `q.size()` | 1 | 1 | ✅ |
| `q.dequeue()` | "banana" | banana | ✅ |
| `q.size()` | 0 | 0 | ✅ |
| `q.dequeue()` | None | None | ✅ |

---

## Notizen

- **Konzept:** Queue-Datenstruktur (FIFO-Prinzip)
- **append():** Fügt Element am Ende der Liste hinzu
- **pop(0):** Entfernt und gibt erstes Element zurück
- **Alternative:** `collections.deque` (effizienter für große Queues)
- **Performance:** `pop(0)` ist O(n), `deque.popleft()` ist O(1)
