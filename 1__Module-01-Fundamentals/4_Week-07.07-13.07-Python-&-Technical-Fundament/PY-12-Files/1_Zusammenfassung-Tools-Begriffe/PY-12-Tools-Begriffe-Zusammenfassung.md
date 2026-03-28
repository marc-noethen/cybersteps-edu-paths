## 📊 Zusammenfassung nach dem 80/20-Prinzip
## Anpassungen für Windows 11 (statt macOS)

|macOS/Linux|Windows 11|
|---|---|
|**Pfadtrennzeichen:** `/`|**Pfadtrennzeichen:** `\`|
|`/Users/yourname/Documents/file.txt`|`C:\Users\YourName\Documents\file.txt`|
|Backslash nicht escapen nötig|**Backslash escapen:** `\\` oder Raw String `r"..."`|
|`"/path/to/file"`|`"C:\\path\\to\\file"` oder `r"C:\path\to\file"`|
|Root: `/`|Root: `C:\` (oder andere Laufwerke)|
|Texteditor: TextEdit|Texteditor: Notepad, Notepad++|

**Beispiel Windows-Pfad:**

```python
# ❌ Falsch
pfad = "C:\Users\Admin\Documents\file.txt"  # Escape-Sequenzen!

# ✅ Richtig mit doppelten Backslashes
pfad = "C:\\Users\\Admin\\Documents\\file.txt"

# ✅ Oder mit Raw String
pfad = r"C:\Users\Admin\Documents\file.txt"
```

---

## Zusammenfassung nach dem 80/20-Prinzip

### Die 20% Kernwissen, die 80% der praktischen Anwendung abdecken:

---

## **TEIL 1: WARUM DATEIEN?**

### **1. Das Problem ohne Dateien**

```python
# Ohne Dateien: Daten verschwinden nach Programmende
name = "Alice"
punktestand = 1500
# Programm beendet → Alles weg!
```

**Mit Dateien: Permanente Speicherung**

```python
# Daten werden gespeichert
with open("spielstand.txt", "w") as file:
    file.write(f"{name}\n{punktestand}")
# Programm beendet → Daten bleiben erhalten!

# Später wieder laden
with open("spielstand.txt", "r") as file:
    content = file.read()
# Daten sind wieder da!
```

**Dateien = Daten überleben Programmende**

---

## **TEIL 2: DATEIEN ÖFFNEN**

### **2. Die `open()` Funktion**

**Syntax:**

```python
file_object = open(dateipfad, modus)
```

**Grundlegendes Beispiel:**

```python
# Datei öffnen
datei = open("beispiel.txt", "r")

# Mit Datei arbeiten
inhalt = datei.read()
print(inhalt)

# WICHTIG: Datei schließen!
datei.close()
```

**⚠️ Problem:** Was passiert bei Fehler? Datei wird nicht geschlossen!

---

## **TEIL 3: DATEIMODI – DIE 3 WICHTIGSTEN**

### **3. Modus `'r'` – Lesen (Read)**

**Eigenschaften:**

- Datei **muss existieren**, sonst `FileNotFoundError`
- Nur Lesen möglich, kein Schreiben
- Dateizeiger am Anfang
- **Standard-Modus** (wenn kein Modus angegeben)

```python
# Datei lesen
with open("notizen.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)

# ❌ Fehler wenn Datei nicht existiert
# with open("nicht_da.txt", "r") as file:  # FileNotFoundError!
```

---

### **4. Modus `'w'` – Schreiben (Write)**

**Eigenschaften:**

- **⚠️ ACHTUNG: Löscht existierende Inhalte!**
- Erstellt neue Datei, wenn nicht vorhanden
- Nur Schreiben möglich, kein Lesen

```python
# Neue Datei erstellen und schreiben
with open("ausgabe.txt", "w") as file:
    file.write("Erste Zeile\n")
    file.write("Zweite Zeile\n")

# ⚠️ Überschreibt existierende Datei!
with open("ausgabe.txt", "w") as file:
    file.write("Alles weg!\n")  # Alter Inhalt ist gelöscht!
```

**Merksatz:** `'w'` = Write = **Warnung: Löscht alles!**

---

### **5. Modus `'a'` – Anhängen (Append)**

**Eigenschaften:**

- Fügt am **Ende** der Datei hinzu
- Erstellt neue Datei, wenn nicht vorhanden
- Löscht **nichts**
- Nur Schreiben möglich

```python
# Inhalt anhängen (nicht überschreiben)
with open("log.txt", "a") as file:
    file.write("Neuer Log-Eintrag\n")

# Mehrfach ausführen → Alle Zeilen bleiben erhalten
with open("log.txt", "a") as file:
    file.write("Noch ein Eintrag\n")
```

**Merksatz:** `'a'` = Append = **Alles bleibt, wird nur erweitert**

---

### **6. Übersicht: Die 3 Hauptmodi**

|Modus|Name|Datei muss existieren?|Löscht Inhalt?|Erstellt Datei?|
|---|---|---|---|---|
|`'r'`|Read (Lesen)|✅ Ja|❌ Nein|❌ Nein|
|`'w'`|Write (Schreiben)|❌ Nein|⚠️ **JA!**|✅ Ja|
|`'a'`|Append (Anhängen)|❌ Nein|❌ Nein|✅ Ja|

---

## **TEIL 4: DATEIEN LESEN**

### **7. Methode 1: `.read()` – Gesamten Inhalt lesen**

```python
# Datei: beispiel.txt
# Zeile 1
# Zeile 2
# Zeile 3

with open("beispiel.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)

# Output:
# Zeile 1
# Zeile 2
# Zeile 3
```

**Eigenschaften:**

- Liest **alles** auf einmal
- Gibt **einen String** zurück
- ⚠️ Bei großen Dateien: Viel Speicher!

---

### **8. Methode 2: `.readline()` – Zeile für Zeile**

```python
with open("beispiel.txt", "r") as file:
    zeile1 = file.readline()
    print(f"Erste Zeile: {zeile1.strip()}")  # .strip() entfernt \n
    
    zeile2 = file.readline()
    print(f"Zweite Zeile: {zeile2.strip()}")
    
    zeile3 = file.readline()
    print(f"Dritte Zeile: {zeile3.strip()}")

# Output:
# Erste Zeile: Zeile 1
# Zweite Zeile: Zeile 2
# Dritte Zeile: Zeile 3
```

**Eigenschaften:**

- Liest **eine Zeile** pro Aufruf
- Enthält `\n` am Ende
- Gut für **große Dateien** (nicht alles im Speicher)

---

### **9. Methode 3: `.readlines()` – Alle Zeilen als Liste**

```python
with open("beispiel.txt", "r") as file:
    zeilen = file.readlines()
    print(zeilen)

# Output: ['Zeile 1\n', 'Zeile 2\n', 'Zeile 3\n']

# Jede Zeile verarbeiten
for i, zeile in enumerate(zeilen, start=1):
    print(f"Zeile {i}: {zeile.strip()}")

# Output:
# Zeile 1: Zeile 1
# Zeile 2: Zeile 2
# Zeile 3: Zeile 3
```

**Eigenschaften:**

- Gibt **Liste von Strings** zurück
- Jeder String = eine Zeile (mit `\n`)
- Gut für **Iteration**

---

### **10. Best Practice: Über Datei iterieren**

```python
# ✅ Empfohlen: Direkt über file-Objekt iterieren
with open("beispiel.txt", "r") as file:
    for zeile in file:
        print(zeile.strip())

# Vorteile:
# - Speichereffizient (lädt nicht alles auf einmal)
# - Sauberer Code
# - Pythonic
```

---

## **TEIL 5: DATEIEN SCHREIBEN**

### **11. Methode 1: `.write()` – String schreiben**

```python
# Neue Datei erstellen
with open("ausgabe.txt", "w") as file:
    file.write("Hallo Welt!\n")  # \n für neue Zeile!
    file.write("Zweite Zeile\n")

# ⚠️ Ohne \n: Alles in einer Zeile
with open("ausgabe2.txt", "w") as file:
    file.write("Erste")
    file.write("Zweite")
# Ergebnis: "ErsteZweite" (ohne Zeilenumbruch)
```

**Wichtig:** `.write()` fügt **kein** automatisches `\n` hinzu!

---

### **12. Methode 2: `.writelines()` – Liste schreiben**

```python
zeilen = ["Erste Zeile\n", "Zweite Zeile\n", "Dritte Zeile\n"]

with open("ausgabe.txt", "w") as file:
    file.writelines(zeilen)

# ⚠️ Auch hier: Keine automatischen \n
zeilen_ohne_n = ["Erste", "Zweite", "Dritte"]
with open("ausgabe2.txt", "w") as file:
    file.writelines(zeilen_ohne_n)
# Ergebnis: "ErsteZweiteDritte" (alles zusammen)
```

**Trick:** `\n` immer selbst hinzufügen!

---

### **13. Praktisches Beispiel: Log-Datei**

```python
import datetime

def log_ereignis(nachricht):
    """Schreibt Ereignis mit Zeitstempel in Log-Datei."""
    zeitstempel = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_zeile = f"[{zeitstempel}] {nachricht}\n"
    
    with open("anwendung.log", "a") as file:  # 'a' für Append!
        file.write(log_zeile)

# Verwendung
log_ereignis("Programm gestartet")
log_ereignis("Benutzer angemeldet: Alice")
log_ereignis("Daten gespeichert")

# anwendung.log Inhalt:
# [2024-01-15 10:30:00] Programm gestartet
# [2024-01-15 10:30:05] Benutzer angemeldet: Alice
# [2024-01-15 10:30:10] Daten gespeichert
```

---

## **TEIL 6: DAS `with`-STATEMENT**

### **14. Problem ohne `with`**

```python
# ❌ Manuell öffnen und schließen
file = open("beispiel.txt", "r")
inhalt = file.read()
# ... was passiert bei Fehler hier? ...
file.close()  # Wird vielleicht nie erreicht!
```

**Probleme:**

- Vergessen zu schließen → Ressourcen-Leak
- Fehler vor `close()` → Datei bleibt offen
- Daten nicht gespeichert (Puffer nicht geleert)

---

### **15. Lösung: `with`-Statement**

```python
# ✅ Mit 'with': Automatisches Schließen
with open("beispiel.txt", "r") as file:
    inhalt = file.read()
    # ... selbst bei Fehler hier ...
# Datei ist automatisch geschlossen!
```

**Vorteile:**

- ✅ Automatisches Schließen (auch bei Fehlern)
- ✅ Keine vergessenen `close()`
- ✅ Sauberer, lesbarer Code
- ✅ Garantiert gespeicherte Daten

**Regel:** Verwende **IMMER** `with` für Dateioperationen!

---

### **16. `with` mit Fehlerbehandlung**

```python
# Datei lesen mit Fehlerbehandlung
try:
    with open("config.txt", "r") as file:
        config = file.read()
        print(config)
except FileNotFoundError:
    print("Fehler: config.txt nicht gefunden!")
except IOError as e:
    print(f"Ein-/Ausgabe-Fehler: {e}")

# Datei schreiben mit Fehlerbehandlung
try:
    with open("ausgabe.txt", "w") as file:
        file.write("Wichtige Daten\n")
    print("Erfolgreich gespeichert!")
except IOError as e:
    print(f"Konnte nicht schreiben: {e}")
```

---

## **TEIL 7: DATEIPFADE**

### **17. Relativer Pfad (zum Skript)**

```python
# Datei im gleichen Ordner wie Skript
with open("notizen.txt", "r") as file:
    inhalt = file.read()

# Datei in Unterordner
with open("daten/eingabe.csv", "r") as file:
    daten = file.read()

# Datei im Eltern-Ordner
with open("../config.txt", "r") as file:
    config = file.read()
```

**Vorteil:** Code ist portabel (läuft auf jedem System)

---

### **18. Absoluter Pfad (Windows 11)**

```python
# ❌ Falsch: Einfache Backslashes
# pfad = "C:\Users\Admin\Documents\file.txt"  # Escape-Sequenzen!

# ✅ Richtig: Doppelte Backslashes
pfad = "C:\\Users\\Admin\\Documents\\file.txt"
with open(pfad, "r") as file:
    inhalt = file.read()

# ✅ Oder: Raw String (empfohlen!)
pfad = r"C:\Users\Admin\Documents\file.txt"
with open(pfad, "r") as file:
    inhalt = file.read()
```

**Windows-Regel:** Immer `\\` oder `r"..."` verwenden!

---

### **19. Plattformunabhängige Pfade mit `os`**

```python
import os

# Pfad zusammenbauen (funktioniert überall)
pfad = os.path.join("daten", "eingabe", "file.txt")
# Windows: "daten\eingabe\file.txt"
# Linux/Mac: "daten/eingabe/file.txt"

with open(pfad, "r") as file:
    inhalt = file.read()

# Aktuelles Arbeitsverzeichnis
aktuell = os.getcwd()
print(f"Arbeitsverzeichnis: {aktuell}")

# Prüfen, ob Datei existiert
if os.path.exists("config.txt"):
    with open("config.txt", "r") as file:
        config = file.read()
else:
    print("config.txt nicht gefunden")
```

---

## **PRAKTISCHE BEISPIELE**

### **20. Beispiel 1: Kontaktliste speichern/laden**

```python
# Speichern
kontakte = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

with open("kontakte.txt", "w") as file:
    for name, nummer in kontakte.items():
        file.write(f"{name}:{nummer}\n")

# Laden
kontakte_geladen = {}
with open("kontakte.txt", "r") as file:
    for zeile in file:
        zeile = zeile.strip()
        if ':' in zeile:
            name, nummer = zeile.split(':')
            kontakte_geladen[name] = nummer

print(kontakte_geladen)
# Output: {'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-9012'}
```

---

### **21. Beispiel 2: Spielstand speichern**

```python
# Spielstand speichern
def speichere_spielstand(name, level, punkte):
    with open("spielstand.txt", "w") as file:
        file.write(f"{name}\n")
        file.write(f"{level}\n")
        file.write(f"{punkte}\n")

# Spielstand laden
def lade_spielstand():
    try:
        with open("spielstand.txt", "r") as file:
            name = file.readline().strip()
            level = int(file.readline().strip())
            punkte = int(file.readline().strip())
            return name, level, punkte
    except FileNotFoundError:
        return None, 1, 0  # Neues Spiel

# Verwendung
speichere_spielstand("Hero", 5, 1500)

name, level, punkte = lade_spielstand()
print(f"Willkommen zurück, {name}!")
print(f"Level: {level}, Punkte: {punkte}")
```

---

### **22. Beispiel 3: CSV-Datei verarbeiten**

```python
# CSV lesen
produkte = []
with open("produkte.csv", "r") as file:
    header = file.readline()  # Erste Zeile überspringen
    for zeile in file:
        zeile = zeile.strip()
        if zeile:
            teile = zeile.split(',')
            name = teile[0]
            preis = float(teile[1])
            menge = int(teile[2])
            produkte.append({'name': name, 'preis': preis, 'menge': menge})

# Verarbeiten
gesamt = sum(p['preis'] * p['menge'] for p in produkte)
print(f"Gesamtwert: {gesamt:.2f} EUR")

# Ergebnis speichern
with open("zusammenfassung.txt", "w") as file:
    file.write("=== Produktzusammenfassung ===\n\n")
    for p in produkte:
        file.write(f"{p['name']}: {p['menge']}x {p['preis']:.2f} EUR\n")
    file.write(f"\nGesamtwert: {gesamt:.2f} EUR\n")
```

---

## **SCHNELLREFERENZ**

### **Datei-Cheatsheet:**

```python
# LESEN
with open("file.txt", "r") as file:
    inhalt = file.read()           # Alles
    zeile = file.readline()        # Eine Zeile
    zeilen = file.readlines()      # Liste aller Zeilen
    
    # Oder iterieren (empfohlen)
    for zeile in file:
        print(zeile.strip())

# SCHREIBEN (überschreibt!)
with open("file.txt", "w") as file:
    file.write("Text\n")
    file.writelines(["Zeile1\n", "Zeile2\n"])

# ANHÄNGEN (fügt hinzu)
with open("file.txt", "a") as file:
    file.write("Neuer Eintrag\n")

# WINDOWS-PFADE
pfad = r"C:\Users\Admin\file.txt"  # Raw String!
pfad = "C:\\Users\\Admin\\file.txt"  # Doppelte Backslashes

# FEHLERBEHANDLUNG
try:
    with open("file.txt", "r") as file:
        inhalt = file.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
except IOError as e:
    print(f"Fehler: {e}")
```

---

## **HÄUFIGE FEHLER UND LÖSUNGEN**

### **23. Fehler 1: Vergessen zu schließen**

```python
# ❌ Problem
file = open("data.txt", "w")
file.write("Daten")
# Programm crasht → Daten nicht gespeichert!

# ✅ Lösung: Verwende 'with'
with open("data.txt", "w") as file:
    file.write("Daten")
# Automatisch geschlossen und gespeichert
```

---

### **24. Fehler 2: Modus `'w'` löscht Daten**

```python
# ❌ Problem: Alles gelöscht!
with open("wichtig.txt", "w") as file:
    file.write("Neue Daten")
# Alle alten Daten sind weg!

# ✅ Lösung 1: Verwende 'a' zum Anhängen
with open("wichtig.txt", "a") as file:
    file.write("Neue Daten\n")

# ✅ Lösung 2: Erst lesen, dann schreiben
with open("wichtig.txt", "r") as file:
    alt = file.read()
with open("wichtig.txt", "w") as file:
    file.write(alt + "Neue Daten\n")
```

---

### **25. Fehler 3: Windows-Pfad falsch**

```python
# ❌ Problem
pfad = "C:\Users\Admin\file.txt"  # \U wird als Unicode interpretiert!

# ✅ Lösung 1: Raw String
pfad = r"C:\Users\Admin\file.txt"

# ✅ Lösung 2: Doppelte Backslashes
pfad = "C:\\Users\\Admin\\file.txt"

# ✅ Lösung 3: Forward Slashes (funktioniert auch auf Windows!)
pfad = "C:/Users/Admin/file.txt"
```

---

### **26. Fehler 4: Vergessen `\n` hinzuzufügen**

```python
# ❌ Problem: Alles in einer Zeile
with open("output.txt", "w") as file:
    file.write("Zeile 1")
    file.write("Zeile 2")
# Ergebnis: "Zeile 1Zeile 2"

# ✅ Lösung: \n hinzufügen
with open("output.txt", "w") as file:
    file.write("Zeile 1\n")
    file.write("Zeile 2\n")
```

---

## **ÜBUNGSAUFGABEN**

**Aufgabe 1:** Schreibe ein Programm, das 10 Zufallszahlen generiert und in eine Datei `zahlen.txt` schreibt (eine Zahl pro Zeile).

**Aufgabe 2:** Lies `zahlen.txt` und berechne Durchschnitt, Minimum und Maximum.

**Aufgabe 3:** Erstelle ein einfaches Tagebuch-Programm: Benutzer gibt Eintrag ein, der mit Datum in `tagebuch.txt` gespeichert wird.

**Aufgabe 4:** Lies eine Log-Datei und zähle, wie oft jeder Log-Level (INFO, WARNING, ERROR) vorkommt.

---

### **Merksätze:**

🎯 **Dateien = Daten überleben Programmende (persistent storage)**  
🎯 **Verwende IMMER `with open(...) as file:` (automatisches Schließen!)**  
🎯 **Modi: `'r'` = Lesen, `'w'` = Schreiben (löscht!), `'a'` = Anhängen**  
🎯 **`.write()` und `.writelines()` fügen KEIN `\n` automatisch hinzu!**  
🎯 **Windows-Pfade: `r"C:\path"` oder `"C:\\path"` verwenden**  
🎯 **Relativer Pfad = portabel, absoluter Pfad = systemspezifisch**  
🎯 **Bei Fehlern: `try`/`except` mit `FileNotFoundError` und `IOError`**

---

## Verwendete Tools

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Python Interpreter|Zum Testen von Dateioperationen|
||VS Code|Editor zum Schreiben von Python-Skripten mit Datei-Zugriff|
||`open()` Funktion|Eingebaute Funktion zum Öffnen von Dateien|
||`with` Statement|Kontext-Manager für sicheres Öffnen/Schließen von Dateien|
||`os` Modul|Modul für Dateipfad-Operationen (nicht im Detail behandelt)|
||Texteditor|Zum Überprüfen erstellter Dateien (Notepad, TextEdit, etc.)|

---

## Technische Fachbegriffe

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Technische Fachbegriffe**|File (Datei)|Benannter Speicherort auf Festplatte/SSD mit Daten|
||File Handling (Dateiverwaltung)|Programmatisches Lesen/Schreiben von Dateien|
||Persistent Storage (Permanente Speicherung)|Daten bleiben nach Programmende erhalten|
||File Object (Datei-Objekt)|Python-Objekt, das Verbindung zur Datei repräsentiert|
||File Path (Dateipfad)|Speicherort und Name der Datei|
||File Mode (Dateimodus)|Art des Zugriffs (Lesen, Schreiben, Anhängen)|
||File Pointer (Dateizeiger)|Position in Datei, wo gelesen/geschrieben wird|
||Buffer (Puffer)|Temporärer Speicher für Datei-Operationen|
||Flushing (Leeren)|Schreiben gepufferter Daten auf Festplatte|
||Context Manager (Kontext-Manager)|Automatisches Ressourcen-Management (mit `with`)|
||Current Working Directory|Aktuelles Arbeitsverzeichnis des Programms|
||Relative Path (Relativer Pfad)|Pfad relativ zum Arbeitsverzeichnis|
||Absolute Path (Absoluter Pfad)|Vollständiger Pfad vom Root-Verzeichnis|
||Raw String|String mit `r` Präfix für literale Backslashes|
||Binary Mode (Binär-Modus)|Behandlung als Rohbytes statt Text|
||Text Mode (Text-Modus)|Standard-Modus für Textdateien|
||Line Separator (Zeilentrennzeichen)|`\n` für neue Zeilen|
|**Wichtige Vokabeln**|`open(filepath, mode)`|Öffnet Datei mit angegebenem Modus|
||`'r'` Read Mode|Lese-Modus (Standard), Datei muss existieren|
||`'w'` Write Mode|Schreib-Modus, **löscht existierende Inhalte!**|
||`'a'` Append Mode|Anhänge-Modus, fügt am Ende hinzu|
||`'b'` Binary Mode|Binär-Modus (z.B. `'rb'`, `'wb'`)|
||`'+'` Update Mode|Lese- und Schreibzugriff kombiniert|
||`.read()`|Liest gesamten Dateiinhalt als String|
||`.readline()`|Liest einzelne Zeile (mit `\n`)|
||`.readlines()`|Liest alle Zeilen als Liste|
||`.write(string)`|Schreibt String in Datei (kein automatisches `\n`)|
||`.writelines(list)`|Schreibt Liste von Strings (kein automatisches `\n`)|
||`.close()`|Schließt Datei und speichert Änderungen|
||`with open(...) as file:`|Sichere Methode mit automatischem Schließen|
||`FileNotFoundError`|Fehler, wenn Datei im Lese-Modus nicht existiert|
||`IOError`|Allgemeiner Ein-/Ausgabe-Fehler|
||`\n` Newline|Zeilenumbruch-Zeichen|
||`.strip()`|Entfernt `\n` und Leerzeichen|
||`enumerate()`|Durchlaufen mit Index|