# 🖥️ Data Director - SQLite mit Python erstellen

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 03.07.2025

---

## Aufgabe

**Ziel:** Eigene SQLite-Datenbank mit Python erstellen, Tabelle definieren, Daten einfügen und abfragen.

---

## Lösung

### Python Script (create_database.py)

```python
import sqlite3

# 1. Verbindung zur Datenbank erstellen (wird neu angelegt falls nicht vorhanden)
conn = sqlite3.connect("my_creation.db")
cursor = conn.cursor()

# 2. Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT,
        release_year INTEGER
    )
""")

# 3. Daten einfügen
games_data = [
    ("The Witcher 3", "RPG", 2015),
    ("Minecraft", "Sandbox", 2011),
    ("Portal 2", "Puzzle", 2011),
    ("Elden Ring", "RPG", 2022)
]

cursor.executemany("""
    INSERT INTO games (title, genre, release_year) 
    VALUES (?, ?, ?)
""", games_data)

# Änderungen speichern
conn.commit()

# 4. Daten abfragen und ausgeben
cursor.execute("SELECT * FROM games")
results = cursor.fetchall()

print("Alle Spiele in der Datenbank:")
print("-" * 40)
for row in results:
    print(f"ID: {row[0]}, Titel: {row[1]}, Genre: {row[2]}, Jahr: {row[3]}")

# 5. Verbindung schließen
conn.close()

print("\nDatenbank erfolgreich erstellt: my_creation.db")
```

### Ausgabe

```
Alle Spiele in der Datenbank:
----------------------------------------
ID: 1, Titel: The Witcher 3, Genre: RPG, Jahr: 2015
ID: 2, Titel: Minecraft, Genre: Sandbox, Jahr: 2011
ID: 3, Titel: Portal 2, Genre: Puzzle, Jahr: 2011
ID: 4, Titel: Elden Ring, Genre: RPG, Jahr: 2022

Datenbank erfolgreich erstellt: my_creation.db
```

---

## Verifikation

**DB Browser for SQLite:**
1. Datei `my_creation.db` öffnen
2. Tab "Browse Data" auswählen
3. Tabelle "games" anklicken
4. Screenshot der Daten erstellen

---

## Notizen

- **`sqlite3.connect()`:** Erstellt/öffnet Datenbank
- **`cursor.execute()`:** Führt SQL-Befehl aus
- **`cursor.executemany()`:** Führt Befehl für mehrere Datensätze aus
- **`?` Placeholder:** Verhindert SQL-Injection
- **`conn.commit()`:** Speichert Änderungen
- **`cursor.fetchall()`:** Holt alle Ergebnisse
- **`CREATE TABLE IF NOT EXISTS`:** Erstellt nur wenn nicht vorhanden
- **`INTEGER PRIMARY KEY`:** Auto-Increment in SQLite
