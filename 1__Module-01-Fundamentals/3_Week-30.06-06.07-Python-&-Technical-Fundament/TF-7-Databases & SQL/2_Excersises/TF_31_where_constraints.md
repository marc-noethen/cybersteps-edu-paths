# 🖥️ Constraint Comforts - WHERE Clause

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** `WHERE`-Klausel mit Gleichheit und numerischen Vergleichen üben.

**Link:** [SQLBolt Lesson 2](https://sqlbolt.com/lesson/select_queries_with_constraints)

---

## Lösung

### Task 1: Film mit id 6
```sql
SELECT * FROM movies WHERE id = 6;
```

### Task 2: Filme zwischen 2000 und 2010
```sql
SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
```

### Task 3: Filme NICHT zwischen 2000 und 2010
```sql
SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
```

### Task 4: Erste 5 Pixar-Filme
```sql
SELECT * FROM movies WHERE id <= 5;
```

---

## Ergebnisse

| Task | Status |
|------|--------|
| Task 1-4 | ✅ Alle checkmarks |

---

## Notizen

- **`WHERE spalte = wert`:** Gleichheit prüfen
- **`BETWEEN x AND y`:** Bereich (inklusiv)
- **`NOT BETWEEN`:** Außerhalb des Bereichs
- **Vergleichsoperatoren:** `=`, `!=`, `<`, `>`, `<=`, `>=`
- **Numerische Vergleiche:** Ohne Anführungszeichen
