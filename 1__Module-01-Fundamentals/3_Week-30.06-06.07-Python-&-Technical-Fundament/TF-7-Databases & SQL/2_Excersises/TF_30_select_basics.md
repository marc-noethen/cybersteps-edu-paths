# 🖥️ Selecting the Scene - SQL SELECT Basics

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Grundlegende `SELECT`-Abfragen in SQLBolt Lesson 1 üben.

**Link:** [SQLBolt Lesson 1](https://sqlbolt.com/lesson/select_queries_introduction)

---

## Lösung

### Task 1: Alle Spalten einer Tabelle
```sql
SELECT * FROM movies;
```

### Task 2: Titel aller Filme
```sql
SELECT title FROM movies;
```

### Task 3: Regisseur aller Filme
```sql
SELECT director FROM movies;
```

### Task 4: Titel und Regisseur
```sql
SELECT title, director FROM movies;
```

### Task 5: Titel und Jahr
```sql
SELECT title, year FROM movies;
```

### Task 6: Alle Informationen
```sql
SELECT * FROM movies;
```

---

## Ergebnisse

| Task | Status |
|------|--------|
| Task 1-6 | ✅ Alle checkmarks |

---

## Notizen

- **`SELECT *`:** Alle Spalten auswählen
- **`SELECT spalte1, spalte2`:** Bestimmte Spalten auswählen
- **`FROM tabelle`:** Gibt die Quelltabelle an
- **Reihenfolge:** SELECT → FROM
