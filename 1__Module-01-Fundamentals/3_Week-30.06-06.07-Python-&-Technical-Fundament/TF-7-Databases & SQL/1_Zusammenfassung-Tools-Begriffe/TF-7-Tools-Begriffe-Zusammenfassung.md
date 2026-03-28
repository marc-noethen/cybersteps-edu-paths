## 📊 Zusammenfassung nach dem 80/20-Prinzip

## Installation für Windows 11 (statt macOS)

**DB Browser for SQLite Installation:**

1. **Download:** Besuchen Sie https://sqlitebrowser.org/dl/ und laden Sie die `.msi`-Datei für Windows herunter
2. **Installation:** Führen Sie die `.msi`-Datei aus und folgen Sie dem Installationsassistenten
3. **Verifizierung:** Starten Sie "DB Browser for SQLite" aus dem Startmenü

---

## 80/20 Zusammenfassung (Die wichtigsten 20%)

### Grundkonzept: Was sind Datenbanken?

Eine **Datenbank** ist wie ein hochorganisierter digitaler Aktenschrank, der große Mengen an Informationen effizient speichert, verwaltet und zugänglich macht. Ohne Datenbanken wäre es unmöglich, schnell spezifische Informationen in großen Datenmengen zu finden.

**Die 5 Hauptfunktionen:**

1. **Speichern** – Daten zuverlässig sichern
2. **Organisieren** – Daten logisch strukturieren
3. **Abrufen** – Schnelles Finden spezifischer Daten
4. **Aktualisieren** – Änderungen durchführen
5. **Verwalten** – Zugriffsrechte kontrollieren

### Relationale Datenbanken: Tabellenstruktur

**Tabellen** sind das Herzstück relationaler Datenbanken und funktionieren wie Spreadsheets:

- **Spalten (Columns)** = Kategorien von Informationen (z.B. Name, Email, Geburtsdatum)
- **Zeilen (Rows)** = Einzelne Datensätze (z.B. ein bestimmter Kunde)
- **Primärschlüssel** = Eindeutige ID zur Identifizierung jeder Zeile (z.B. CustomerID)

**Beispiel einer Customers-Tabelle:**

- Zeile 1: CustomerID=1, FirstName=Alice, Email=alice@email.com
- Zeile 2: CustomerID=2, FirstName=Bob, Email=bob@email.com

Der Begriff "relational" kommt daher, dass verschiedene Tabellen über gemeinsame Spalten miteinander verknüpft werden können (z.B. Orders-Tabelle verknüpft mit Customers über CustomerID).

### SQL: Die Sprache der Datenbanken

**SQL (Structured Query Language)** ist DIE Standardsprache für Datenbankoperationen.

**Die 4 wichtigsten SQL-Befehle (CRUD-Operationen):**

1. **SELECT** – Daten abrufen (Read)
    
    ```sql
    SELECT * FROM Customers;
    SELECT FirstName, Email FROM Customers WHERE CustomerID = 2;
    ```
    
2. **INSERT INTO** – Neue Daten einfügen (Create)
    
    ```sql
    INSERT INTO Customers (FirstName, Email) VALUES ('David', 'david@email.com');
    ```
    
3. **UPDATE** – Bestehende Daten ändern (Update)
    
    ```sql
    UPDATE Customers SET Email = 'newemail@email.com' WHERE CustomerID = 1;
    ```
    
4. **DELETE FROM** – Daten löschen (Delete)
    
    ```sql
    DELETE FROM Customers WHERE CustomerID = 3;
    ```
    

### SELECT-Befehl im Detail (80% aller Abfragen)

**Grundstruktur:**

```sql
SELECT spalten
FROM tabelle
WHERE bedingung;
```

- `SELECT *` = Alle Spalten
- `SELECT Name, Email` = Nur bestimmte Spalten
- `WHERE` = Filter (z.B. `WHERE SignupDate = '2023-01-15'`)
- Text in WHERE-Bedingungen benötigt Anführungszeichen: `WHERE FirstName = 'Alice'`

### Praktische Anwendung: DB Browser for SQLite

**Workflow in 5 Schritten:**

1. **Neue Datenbank erstellen** → Datei mit `.sqlite`-Endung speichern
2. **Tabelle definieren** → Spalten mit Namen und Datentypen festlegen
3. **Primärschlüssel setzen** → Eine Spalte als eindeutige ID markieren (z.B. FriendID)
4. **Daten eingeben** → Über "Browse Data" Zeilen hinzufügen
5. **SQL-Abfragen ausführen** → Im "Execute SQL"-Tab Befehle eingeben und ausführen

### Relevanz für Cybersecurity

**Warum Datenbanken in der IT-Sicherheit wichtig sind:**

- **Log-Analyse:** Sicherheitslogs werden oft in Datenbanken gespeichert und mit SQL analysiert
- **Schwachstellen-Datenbanken:** CVE-Datenbanken nutzen SQL für Abfragen
- **SQL-Injection:** Verstehen von SQL ist essentiell zum Erkennen dieser Angriffe
- **Forensik:** Untersuchung von Datenbank-Aktivitäten bei Sicherheitsvorfällen
- **User-Management:** Zugriffsrechte und Benutzerkonten werden in Datenbanken verwaltet

### Merksätze

- **Eine Tabelle** = Eine Kategorie von Objekten (z.B. Customers, Orders, Products)
- **Eine Zeile** = Ein konkretes Objekt (z.B. der Kunde Alice)
- **Eine Spalte** = Eine Eigenschaft (z.B. Email-Adresse)
- **Primärschlüssel** = Die eindeutige "Ausweisnummer" jeder Zeile
- **SELECT** ist wie "Zeig mir..." – der meistgenutzte SQL-Befehl

---

## Verwendete Tools

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Verwendete Tools**|DB Browser for SQLite (Windows 11)|Kostenlose grafische Anwendung zum Erstellen und Verwalten von SQLite-Datenbanken|
||SQLite|Leichtgewichtiges, dateibasiertes Datenbanksystem ohne separaten Server|
||SQL-Editor|Integrierter Texteditor zum Schreiben und Ausführen von SQL-Befehlen|
||Tabelleneditor|Grafisches Interface zum Erstellen und Bearbeiten von Datenbankstrukturen|
||Query-Executor|Funktion zum Ausführen von SQL-Abfragen und Anzeigen der Ergebnisse|

---

## Technische Fachbegriffe

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Technische Fachbegriffe**|Datenbank (Database)|Organisierte, elektronisch gespeicherte Sammlung von Daten für effiziente Verwaltung|
||Relationale Datenbank|Datenbank, die Daten in miteinander verknüpften Tabellen organisiert|
||Tabelle (Table)|Sammlung von zusammengehörigen Dateneinträgen in Zeilen und Spalten|
||Zeile/Datensatz (Row/Record)|Einzelner Eintrag in einer Tabelle mit allen Werten für ein Objekt|
||Spalte/Feld (Column/Field)|Vertikale Kategorie in einer Tabelle, die einen bestimmten Datentyp enthält|
||Primärschlüssel (Primary Key)|Spalte mit eindeutigem Wert zur Identifizierung jeder Zeile (z.B. CustomerID)|
||Strukturierte Daten|Daten, die in einem vordefinierten Format (Tabellen) organisiert sind|
||SQL (Structured Query Language)|Standardsprache zur Verwaltung und Abfrage relationaler Datenbanken|
||SELECT-Statement|SQL-Befehl zum Abrufen von Daten aus einer Tabelle|
||WHERE-Klausel|Filter-Bedingung in SQL-Abfragen zur Einschränkung der Ergebnisse|
||INSERT INTO|SQL-Befehl zum Einfügen neuer Datensätze|
||UPDATE|SQL-Befehl zum Ändern bestehender Datensätze|
||DELETE FROM|SQL-Befehl zum Löschen von Datensätzen|
||CREATE TABLE|SQL-Befehl zum Erstellen neuer Tabellen|
||Datentypen|Kategorien von Daten (INTEGER für Ganzzahlen, TEXT für Text, DATE für Datumsangaben)|
||Query (Abfrage)|Anfrage an die Datenbank zur Datenabfrage oder -manipulation|
||Relation|Verknüpfung zwischen Tabellen über gemeinsame Spalten (z.B. CustomerID)|
|**Wichtige Vokabeln**|Retrieve (Abrufen)|Daten aus der Datenbank holen und anzeigen|
||Store (Speichern)|Daten dauerhaft in der Datenbank ablegen|
||Organize (Organisieren)|Daten logisch strukturieren und ordnen|
||Update (Aktualisieren)|Bestehende Daten ändern oder ergänzen|
||Manage (Verwalten)|Datenbank-Struktur und Zugriffsrechte kontrollieren|
||Field (Feld)|Synonym für Spalte in einer Tabelle|
||Record (Datensatz)|Synonym für Zeile in einer Tabelle|
||Unique identifier (Eindeutiger Bezeichner)|Wert, der nur einmal in einer Spalte vorkommt|
||Condition (Bedingung)|Kriterium zur Filterung von Datensätzen (z.B. WHERE CustomerID = 2)|
||Execute (Ausführen)|SQL-Befehl an die Datenbank senden und verarbeiten lassen|
||Results (Ergebnisse)|Von der Datenbank zurückgegebene Daten nach einer Abfrage|