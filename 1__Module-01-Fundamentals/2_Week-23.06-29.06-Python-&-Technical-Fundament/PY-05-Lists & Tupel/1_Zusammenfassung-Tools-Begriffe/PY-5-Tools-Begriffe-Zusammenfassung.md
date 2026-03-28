## 📊 Zusammenfassung nach dem 80/20-Prinzip
## **TEIL 1: LISTEN (LISTS)**

### **1. Was ist eine Liste?**

- **Liste = Container für mehrere Elemente in einer Variable**
- Syntax: Eckige Klammern `[]` mit Kommas getrennt
- **3 Haupteigenschaften:**
    - ✅ **Geordnet** (Reihenfolge bleibt erhalten)
    - ✅ **Veränderbar** (kann nach Erstellung geändert werden)
    - ✅ **Erlaubt Duplikate** (gleiche Werte mehrfach möglich)

```python
# Verschiedene Listen-Typen
zahlen = [1, 2, 3, 4, 5]
fruechte = ["Apfel", "Banane", "Kirsche"]
gemischt = ["Hallo", 100, True, 3.14]
leer = []
```

---

### **2. Indexierung: Elemente zugreifen**

**Positiver Index (von vorne):**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
#            Index:    0         1          2

print(fruechte[0])   # Output: Apfel
print(fruechte[1])   # Output: Banane
print(fruechte[2])   # Output: Kirsche
```

**Negativer Index (von hinten):**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
#            Index:   -3        -2         -1

print(fruechte[-1])  # Output: Kirsche (letztes Element)
print(fruechte[-2])  # Output: Banane (vorletztes Element)
```

**⚠️ Wichtig:** Python startet bei 0, nicht bei 1!

**❌ Fehler vermeiden:**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
# print(fruechte[3])  # IndexError! Nur Indizes 0, 1, 2 existieren
```

---

### **3. Listen ändern (Mutable)**

**Element ändern:**

```python
farben = ["rot", "grün", "blau"]
farben[1] = "gelb"
print(farben)  # Output: ['rot', 'gelb', 'blau']
```

**Element hinzufügen mit `.append()`:**

```python
aufgaben = ["E-Mail lesen", "Einkaufen"]
aufgaben.append("Sport machen")
print(aufgaben)  # Output: ['E-Mail lesen', 'Einkaufen', 'Sport machen']
```

---

### **4. Länge einer Liste mit `len()`**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
anzahl = len(fruechte)
print(anzahl)  # Output: 3

leere_liste = []
print(len(leere_liste))  # Output: 0
```

**Wichtige Regel:**

- Liste mit Länge 5 hat Indizes: `0, 1, 2, 3, 4`
- Letzter Index ist immer `len(liste) - 1`

---

### **5. Element in Liste prüfen mit `in`**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]

if "Banane" in fruechte:
    print("Ja, Banane ist in der Liste!")
    
if "Erdbeere" not in fruechte:
    print("Erdbeere ist nicht in der Liste!")
```

---

### **6. Die wichtigsten Listen-Methoden**

|Methode|Beschreibung|Beispiel|
|---|---|---|
|`.append(item)`|Fügt Element am Ende hinzu|`liste.append(5)`|
|`.remove(item)`|Entfernt erstes Vorkommen|`liste.remove("Apfel")`|
|`.sort()`|Sortiert Liste|`zahlen.sort()`|
|`.count(item)`|Zählt Vorkommen|`liste.count("Apfel")`|
|`.index(item)`|Gibt Index zurück|`liste.index("Banane")`|

```python
zahlen = [3, 1, 4, 1, 5, 9]

zahlen.append(2)
print(zahlen)  # Output: [3, 1, 4, 1, 5, 9, 2]

zahlen.sort()
print(zahlen)  # Output: [1, 1, 2, 3, 4, 5, 9]

print(zahlen.count(1))  # Output: 2 (1 kommt 2x vor)
```

---

## **TEIL 2: TUPEL (TUPLES)**

### **7. Was ist ein Tupel?**

- **Tupel = unveränderbare Liste**
- Syntax: Runde Klammern `()` statt eckige Klammern `[]`
- Kann NICHT geändert werden nach Erstellung

```python
koordinaten = (10.0, 20.0)
person = ("Alice", 30, "Ingenieur")
farben = ("rot", "grün", "blau")
```

**⚠️ Besonderheit bei einem Element:**

```python
# FALSCH:
einzel = ("Hallo")  # Dies ist ein String, kein Tupel!

# RICHTIG:
einzel = ("Hallo",)  # Komma ist Pflicht für 1-Element-Tupel!
```

---

### **8. Tupel vs. Liste: Der Hauptunterschied**

|Eigenschaft|Liste `[]`|Tupel `()`|
|---|---|---|
|**Veränderbar?**|✅ Ja|❌ Nein|
|**Elemente hinzufügen?**|✅ `.append()`|❌ Nicht möglich|
|**Elemente ändern?**|✅ `liste[0] = neu`|❌ Fehler!|
|**Geschwindigkeit**|Langsamer|Schneller|
|**Verwendung**|Daten, die sich ändern|Daten, die konstant bleiben|

```python
# Liste (veränderbar)
liste = [1, 2, 3]
liste[0] = 10
liste.append(4)
print(liste)  # Output: [10, 2, 3, 4]

# Tupel (unveränderbar)
tupel = (1, 2, 3)
# tupel[0] = 10  # TypeError! Nicht erlaubt
# tupel.append(4)  # AttributeError! Methode existiert nicht
```

---

### **9. Tupel zugreifen (wie bei Listen)**

```python
person = ("Alice", 30, "Ingenieur")

print(person[0])   # Output: Alice
print(person[-1])  # Output: Ingenieur
print(len(person)) # Output: 3
```

---

### **10. Tuple Unpacking: Der Geheimtrick!**

**Mehrere Variablen auf einmal zuweisen:**

```python
person = ("Alice", 30, "Ingenieur")

name, alter, beruf = person

print(name)   # Output: Alice
print(alter)  # Output: 30
print(beruf)  # Output: Ingenieur
```

**Werte tauschen ohne Hilfsvariable:**

```python
x = 10
y = 20

x, y = y, x  # Tausch!

print(x)  # Output: 20
print(y)  # Output: 10
```

**Funktion mit mehreren Rückgabewerten:**

```python
def hole_koordinaten():
    return (100, 200)

x, y = hole_koordinaten()
print(f"X: {x}, Y: {y}")  # Output: X: 100, Y: 200
```

---

### **11. Wann Tupel, wann Liste?**

**Verwende TUPEL wenn:**

- ✅ Daten sollen sich NICHT ändern (z.B. Wochentage, GPS-Koordinaten)
- ✅ Als Dictionary-Key (Listen können das nicht!)
- ✅ Mehrere Werte von Funktion zurückgeben
- ✅ Performance wichtig ist (Tupel sind schneller)

**Verwende LISTE wenn:**

- ✅ Daten sollen sich ändern können
- ✅ Elemente hinzufügen/entfernen
- ✅ Sortieren oder modifizieren

```python
# Gut: Tupel für feste Werte
WOCHENTAGE = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", 
              "Freitag", "Samstag", "Sonntag")

# Gut: Liste für veränderliche Daten
einkaufsliste = ["Milch", "Eier"]
einkaufsliste.append("Brot")
```

---

## **SCHNELLREFERENZ**

### **Listen-Cheatsheet:**

```python
# Erstellen
liste = [1, 2, 3]

# Zugriff
liste[0]      # Erstes Element
liste[-1]     # Letztes Element

# Ändern
liste[0] = 10

# Hinzufügen
liste.append(4)

# Länge
len(liste)

# Prüfen
if 2 in liste:
    print("Gefunden!")
```

### **Tupel-Cheatsheet:**

```python
# Erstellen
tupel = (1, 2, 3)

# Zugriff (wie Liste)
tupel[0]      # Erstes Element
tupel[-1]     # Letztes Element

# Unpacking
a, b, c = tupel

# Länge
len(tupel)

# NICHT möglich:
# tupel[0] = 10    # Fehler!
# tupel.append(4)  # Fehler!
```

---

## **HÄUFIGE FEHLER UND LÖSUNGEN**

❌ **Fehler 1: Index außerhalb des Bereichs**

```python
fruechte = ["Apfel", "Banane"]
# print(fruechte[2])  # IndexError!
```

✅ **Lösung:** Prüfe Länge mit `len()` oder verwende `-1` für letztes Element

---

❌ **Fehler 2: Tupel ohne Komma bei einem Element**

```python
falsch = ("Hallo")   # Dies ist ein String!
```

✅ **Lösung:** Komma hinzufügen:

```python
richtig = ("Hallo",)
```

---

❌ **Fehler 3: Tupel ändern wollen**

```python
tupel = (1, 2, 3)
# tupel[0] = 10  # TypeError!
```

✅ **Lösung:** Verwende eine Liste statt Tupel, oder erstelle neues Tupel

---

### **Merksätze:**

🎯 **Listen = veränderbar `[]`, Tupel = unveränderbar `()`**  
🎯 **Python zählt ab 0, nicht ab 1!**  
🎯 **Index `-1` = letztes Element**  
🎯 **Tupel mit 1 Element: `(item,)` – Komma nicht vergessen!**  
🎯 **Tuple Unpacking spart Code: `x, y = (10, 20)`**

---

## Kategorisierung der Themen

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Python Interpreter|Zum Testen von Listen-Operationen interaktiv|
||VS Code|Editor zum Schreiben von Python-Skripten mit Listen|
||`print()` Funktion|Ausgabe von Listen und deren Inhalten|
||`len()` Funktion|Gibt die Anzahl der Elemente in einer Liste/Tupel zurück|
||`type()` Funktion|Zeigt den Datentyp (list oder tuple) an|
|**Technische Fachbegriffe**|List (Liste)|Veränderbare Sammlung von Elementen in eckigen Klammern `[]`|
||Tuple (Tupel)|Unveränderbare Sammlung von Elementen in runden Klammern `()`|
||Index (Indexierung)|Position eines Elements in einer Liste (startet bei 0)|
||Zero-based Indexing|Erstes Element hat Index 0, nicht 1|
||Negative Indexing|Zugriff von hinten: `-1` = letztes Element, `-2` = vorletztes|
||Mutable (Veränderbar)|Inhalte können nach Erstellung geändert werden (Listen)|
||Immutable (Unveränderbar)|Inhalte können nach Erstellung NICHT geändert werden (Tupel)|
||Ordered (Geordnet)|Elemente behalten ihre Reihenfolge|
||Duplicates (Duplikate)|Gleiche Elemente können mehrfach vorkommen|
||IndexError|Fehler beim Zugriff auf nicht existierenden Index|
||Method (Methode)|Funktion, die zu einem Objekt gehört (mit `.` aufgerufen)|
||Dot Notation (Punkt-Notation)|Aufruf von Methoden: `liste.append()`|
||Mixed Data Types|Liste/Tupel mit verschiedenen Datentypen (int, str, bool, etc.)|
||Tuple Unpacking|Zuweisung mehrerer Werte aus Tupel an separate Variablen|
||Hashable|Kann als Dictionary-Key verwendet werden (Tupel ja, Liste nein)|
||Iteration (Durchlaufen)|Über alle Elemente einer Liste/Tupel mit Schleife gehen|
|**Wichtige Vokabeln**|`[]` Square Brackets|Eckige Klammern zum Erstellen von Listen|
||`()` Parentheses|Runde Klammern zum Erstellen von Tupeln|
||`.append(item)`|Fügt Element am Ende der Liste hinzu|
||`.count(value)`|Zählt, wie oft ein Wert vorkommt (Liste & Tupel)|
||`.index(value)`|Gibt Index des ersten Vorkommens zurück (Liste & Tupel)|
||`.remove(item)`|Entfernt erstes Vorkommen eines Elements (nur Liste)|
||`.sort()`|Sortiert Liste (nur Liste, nicht Tupel)|
||`in` Operator|Prüft, ob Element in Liste/Tupel existiert|
||Concatenation (Verkettung)|Listen/Tupel mit `+` verbinden|
||Length (Länge)|Anzahl der Elemente (mit `len()`)|
||First Item (Erstes Element)|Index `0` oder `liste[0]`|
||Last Item (Letztes Element)|Index `-1` oder `liste[-1]`|
||Empty List (Leere Liste)|`[]` ohne Elemente|
||Single Item Tuple|Tupel mit einem Element: `(item,)` – Komma ist Pflicht!|