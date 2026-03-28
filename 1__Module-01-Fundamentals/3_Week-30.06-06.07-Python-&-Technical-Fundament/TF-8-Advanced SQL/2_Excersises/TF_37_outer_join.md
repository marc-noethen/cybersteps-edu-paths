# 🖥️ Feeling Left Out?

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 04.07.2025

---

## Aufgabe

**Ziel:** `OUTER JOIN`s (speziell `LEFT JOIN`) verwenden, um Daten einzuschließen, auch wenn kein Match in der anderen Tabelle existiert.

**Quelle:** [SQLBolt Lesson 7: OUTER JOINs](https://sqlbolt.com/lesson/select_queries_with_outer_joins)

---

## Lösung

### Umgebung
```
Browser: Chrome / Firefox / Safari
Plattform: SQLBolt (Online)
```

### Durchführung

**Schritt 1:** Erklärungen auf der Seite lesen
- Verstehen, wie `LEFT JOIN`, `RIGHT JOIN` und `FULL JOIN` funktionieren
- Syntax: `SELECT ... FROM tabelle1 LEFT JOIN tabelle2 ON tabelle1.id = tabelle2.id`

**Schritt 2:** Query-Aufgaben lösen

**Aufgabe 1:** [Beschreibung der Aufgabe]
```sql
-- Query hier einfügen
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

**Aufgabe 2:** [Beschreibung der Aufgabe]
```sql
-- Query hier einfügen
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

**Aufgabe 3:** [Beschreibung der Aufgabe]
```sql
-- Query hier einfügen
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

*(Weitere Aufgaben nach Bedarf hinzufügen)*

---

## Ergebnisse

| Aufgabe | Status |
|---------|--------|
| Task 1 | ✓ |
| Task 2 | ✓ |
| Task 3 | ✓ |
| ... | ✓ |

---

## Abgabe

📸 **Screenshot:** SQLBolt Lesson 7 mit allen sichtbaren Checkmarks (✓)

---

## Notizen

- **Gelernt:** `LEFT JOIN` gibt alle Zeilen der linken Tabelle zurück, auch wenn kein Match existiert
- **Tipp:** Bei fehlendem Match werden die Spalten der rechten Tabelle mit `NULL` gefüllt
- **Unterschied zu INNER JOIN:** `OUTER JOIN` behält Zeilen ohne Match, `INNER JOIN` nicht
- **Wichtig:** `LEFT JOIN` = `LEFT OUTER JOIN` (gleiche Bedeutung)
