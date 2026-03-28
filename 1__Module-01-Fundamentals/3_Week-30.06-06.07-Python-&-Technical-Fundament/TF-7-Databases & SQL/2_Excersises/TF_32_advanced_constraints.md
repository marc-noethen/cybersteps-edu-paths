# 🖥️ Constraint Comforts Part 2 - Advanced WHERE

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Erweiterte Constraints wie `LIKE`, `IN`, `AND`, `OR` üben.

**Link:** [SQLBolt Lesson 3](https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2)

---

## Lösung

### Task 1: Filme mit "Toy Story" im Titel
```sql
SELECT * FROM movies WHERE title LIKE "Toy Story%";
```

### Task 2: Filme von Regisseur John Lasseter
```sql
SELECT * FROM movies WHERE director = "John Lasseter";
```

### Task 3: Filme NICHT von John Lasseter
```sql
SELECT * FROM movies WHERE director != "John Lasseter";
```

### Task 4: Filme mit "WALL" im Titel
```sql
SELECT * FROM movies WHERE title LIKE "%WALL%";
```

---

## Ergebnisse

| Task | Status |
|------|--------|
| Task 1-4 | ✅ Alle checkmarks |

---

## Notizen

- **`LIKE "text%"`:** Beginnt mit "text"
- **`LIKE "%text"`:** Endet mit "text"
- **`LIKE "%text%"`:** Enthält "text"
- **`%`:** Wildcard für beliebige Zeichen (0 oder mehr)
- **`_`:** Wildcard für genau ein Zeichen
- **String-Vergleiche:** Mit Anführungszeichen `"` oder `'`
