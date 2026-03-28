# 🖥️ Tasty Pickle - Python-Objekte speichern/laden

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Demonstriere `pickle` zum Serialisieren und Deserialisieren von Python-Objekten.

---

## Lösung

### Script 1: save_state.py

```python
import pickle

# Anwendungszustand erstellen
app_state = {
    "user": "rick",
    "level": 5,
    "inventory": ["grandson", "time-machine"]
}

# In Datei speichern (binary write)
with open("saved_state.pkl", "wb") as f:
    pickle.dump(app_state, f)

print("State saved.")
```

### Script 2: load_state.py

```python
import pickle

# Aus Datei laden (binary read)
with open("saved_state.pkl", "rb") as f:
    loaded_state = pickle.load(f)

# Geladene Daten anzeigen
print("Loaded state:", loaded_state)
print("User:", loaded_state["user"])
```

### Ausführung

```bash
$ python save_state.py
State saved.

$ python load_state.py
Loaded state: {'user': 'rick', 'level': 5, 'inventory': ['grandson', 'time-machine']}
User: rick
```

---

## Frage & Antwort

**Q:** Wann ist `pickle` nützlicher als JSON?

**A:** Pickle ist nützlich wenn:
- **Komplexe Python-Objekte** gespeichert werden (Klassen, Funktionen, verschachtelte Strukturen)
- **Datentypen erhalten** bleiben sollen (datetime, sets, tuples)
- **Nur Python** die Daten lesen muss (keine Interoperabilität nötig)
- **Performance** wichtig ist (pickle ist schneller als JSON)

JSON ist besser für Interoperabilität mit anderen Sprachen und menschenlesbare Daten.

---

## Notizen

- **`pickle.dump(obj, file)`:** Serialisiert Objekt in Datei
- **`pickle.load(file)`:** Deserialisiert Objekt aus Datei
- **`"wb"` / `"rb"`:** Binary-Modus (write/read) erforderlich
- **⚠️ Sicherheit:** Niemals pickle-Dateien aus unbekannten Quellen laden!
