# 🖥️ Filter Fanatic - ORDER BY, LIMIT, OFFSET

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 03.07.2025

---

## Aufgabe

**Ziel:** Ergebnisse filtern und sortieren mit `ORDER BY`, `LIMIT`, `OFFSET`.

**Link:** [SQLBolt Lesson 4](https://sqlbolt.com/lesson/filtering_sorting_query_results)

---

## Lösung

### Task 1: Regisseure (ohne Duplikate, alphabetisch)
```sql
SELECT DISTINCT director FROM movies ORDER BY director;
```

### Task 2: Letzte 4 Filme (nach Jahr)
```sql
SELECT * FROM movies ORDER BY year DESC LIMIT 4;
```

### Task 3: Erste 5 Filme (alphabetisch nach Titel)
```sql
SELECT * FROM movies ORDER BY title LIMIT 5;
```

### Task 4: Nächste 5 Filme (alphabetisch, nach den ersten 5)
```sql
SELECT * FROM movies ORDER BY title LIMIT 5 OFFSET 5;
```

---

## Ergebnisse

| Task | Status |
|------|--------|
| Task 1-4 | ✅ Alle checkmarks |

---

## Notizen

- **`ORDER BY spalte`:** Aufsteigend sortieren (ASC, Standard)
- **`ORDER BY spalte DESC`:** Absteigend sortieren
- **`LIMIT n`:** Nur n Ergebnisse zurückgeben
- **`OFFSET n`:** Erste n Ergebnisse überspringen
- **`DISTINCT`:** Duplikate entfernen
- **Reihenfolge:** SELECT → FROM → WHERE → ORDER BY → LIMIT → OFFSET
