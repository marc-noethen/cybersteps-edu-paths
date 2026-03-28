# 🖥️ Natural Selection - SELECT Review

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 03.07.2025

---

## Aufgabe

**Ziel:** Alle bisherigen SELECT-Konzepte in einer Review-Aufgabe anwenden.

**Link:** [SQLBolt SELECT Review](https://sqlbolt.com/lesson/select_queries_review)

---

## Lösung

### Task 1: Städte in Nordamerika
```sql
SELECT city, population 
FROM north_american_cities 
WHERE country = "Canada";
```

### Task 2: US-Städte sortiert nach Breitengrad
```sql
SELECT * 
FROM north_american_cities 
WHERE country = "United States" 
ORDER BY latitude DESC;
```

### Task 3: Städte westlich von Chicago
```sql
SELECT city 
FROM north_american_cities 
WHERE longitude < -87.629798 
ORDER BY longitude;
```

### Task 4: Zwei größte Städte in Mexiko
```sql
SELECT city 
FROM north_american_cities 
WHERE country = "Mexico" 
ORDER BY population DESC 
LIMIT 2;
```

### Task 5: Dritte und vierte größte US-Stadt
```sql
SELECT city 
FROM north_american_cities 
WHERE country = "United States" 
ORDER BY population DESC 
LIMIT 2 OFFSET 2;
```

---

## Ergebnisse

| Task | Status |
|------|--------|
| Task 1-5 | ✅ Alle checkmarks |

---

## Notizen

- **Kombinierte Abfragen:** WHERE + ORDER BY + LIMIT + OFFSET
- **Geografische Daten:** Longitude (Ost/West), Latitude (Nord/Süd)
- **Negative Longitude:** Westen von Greenwich
- **Query-Reihenfolge:** SELECT → FROM → WHERE → ORDER BY → LIMIT → OFFSET
