## 📊 Zusammenfassung nach dem 80/20-Prinzip

## **TEIL 1: WARUM SCHLEIFEN?**

### **1. Das Problem ohne Schleifen**

**Ohne Schleife (umständlich):**

```python
print(1)
print(2)
print(3)
print(4)
print(5)
# Was, wenn wir bis 1000 zählen müssen? 😱
```

**Mit Schleife (elegant):**

```python
for i in range(1, 6):
    print(i)
# Gleicher Output, aber flexibel und wartbar!
```

**Schleifen = Automatisierung von Wiederholungen**

---

## **TEIL 2: DIE `for`-SCHLEIFE**

### **2. Grundstruktur der `for`-Schleife**

```python
for variable in sequenz:
    # Code-Block (eingerückt!)
    # Wird für jedes Element wiederholt
```

**Komponenten:**

- **`for`** = Keyword zum Starten
- **`variable`** = nimmt nacheinander jeden Wert aus der Sequenz an
- **`in`** = verbindet Variable mit Sequenz
- **`sequenz`** = Liste, Tupel, String, range() etc.
- **`:`** = Doppelpunkt (Pflicht!)
- **Einrückung** = 4 Leerzeichen (definiert, was zur Schleife gehört)

---

### **3. `for`-Schleife mit Listen**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]

for frucht in fruechte:
    print(f"Ich mag {frucht}")

# Output:
# Ich mag Apfel
# Ich mag Banane
# Ich mag Kirsche
```

**Was passiert:**

1. Erste Iteration: `frucht = "Apfel"` → Code ausführen
2. Zweite Iteration: `frucht = "Banane"` → Code ausführen
3. Dritte Iteration: `frucht = "Kirsche"` → Code ausführen
4. Liste zu Ende → Schleife stoppt

---

### **4. Die `range()`-Funktion: Zahlenfolgen erzeugen**

**Drei Varianten:**

**Variante 1: `range(stop)` – von 0 bis stop-1**

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

**Variante 2: `range(start, stop)` – von start bis stop-1**

```python
for i in range(3, 7):
    print(i)
# Output: 3, 4, 5, 6
```

**Variante 3: `range(start, stop, step)` – mit Schrittweite**

```python
# Gerade Zahlen von 0 bis 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# Rückwärts zählen
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

**⚠️ Wichtig:** `stop` wird NICHT erreicht!

- `range(5)` → 0, 1, 2, 3, 4 (NICHT 5!)
- `range(1, 4)` → 1, 2, 3 (NICHT 4!)

---

### **5. Praktische `for`-Schleife Beispiele**

**Beispiel 1: Quadratzahlen berechnen**

```python
for zahl in range(1, 6):
    quadrat = zahl ** 2
    print(f"{zahl} hoch 2 = {quadrat}")

# Output:
# 1 hoch 2 = 1
# 2 hoch 2 = 4
# 3 hoch 2 = 9
# 4 hoch 2 = 16
# 5 hoch 2 = 25
```

**Beispiel 2: Über String iterieren**

```python
wort = "Python"
for buchstabe in wort:
    print(buchstabe)

# Output:
# P
# y
# t
# h
# o
# n
```

**Beispiel 3: Summe berechnen**

```python
zahlen = [10, 20, 30, 40, 50]
summe = 0

for zahl in zahlen:
    summe = summe + zahl

print(f"Summe: {summe}")  # Output: Summe: 150
```

---

## **TEIL 3: DIE `while`-SCHLEIFE**

### **6. Grundstruktur der `while`-Schleife**

```python
while bedingung:
    # Code-Block (eingerückt!)
    # Läuft, solange bedingung True ist
```

**Unterschied zu `for`:**

- `for` = "Wiederhole X-mal" oder "für jedes Element"
- `while` = "Wiederhole, solange Bedingung wahr ist"

---

### **7. `while`-Schleife Beispiele**

**Beispiel 1: Countdown**

```python
count = 5

while count > 0:
    print(count)
    count = count - 1  # WICHTIG: Bedingung muss irgendwann False werden!

print("Start!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Start!
```

**Beispiel 2: Benutzereingabe**

```python
passwort = ""

while passwort != "geheim":
    passwort = input("Passwort eingeben: ")

print("Zugang gewährt!")
```

**Beispiel 3: Summieren bis Grenze**

```python
summe = 0
zahl = 1

while summe < 50:
    summe = summe + zahl
    zahl = zahl + 1

print(f"Summe: {summe}, Letzte Zahl: {zahl-1}")
# Output: Summe: 55, Letzte Zahl: 10
```

---

### **8. ⚠️ Endlosschleife vermeiden!**

**❌ FALSCH (Endlosschleife):**

```python
count = 0
while count < 5:
    print(count)
    # count wird nie erhöht → läuft unendlich!
```

**✅ RICHTIG:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1  # Bedingung wird irgendwann False
```

**So erkennst du Endlosschleifen:**

- Variable in Bedingung wird nie geändert
- Bedingung wird nie `False`

**Notfall-Stop:** `Ctrl + C` im Terminal stoppt laufendes Programm!

---

## **TEIL 4: FLUSSKONTROLLE MIT `break` UND `continue`**

### **9. `break` – Schleife sofort verlassen**

**Syntax:**

```python
for item in sequenz:
    if bedingung:
        break  # Schleife wird sofort beendet
    # Code hier wird übersprungen nach break
```

**Praktisches Beispiel: Suche ersten Treffer**

```python
zahlen = [1, 2, 4, 3, 5, 6]

for zahl in zahlen:
    print(f"Prüfe {zahl}...")
    if zahl % 3 == 0:  # Teilbar durch 3?
        print(f"Gefunden: {zahl}")
        break  # Schleife beenden

print("Fertig!")

# Output:
# Prüfe 1...
# Prüfe 2...
# Prüfe 4...
# Prüfe 3...
# Gefunden: 3
# Fertig!
```

**Wann `break` verwenden:**

- Gesuchtes Element gefunden
- Fehler aufgetreten
- Bedingung erfüllt, weitere Iterationen unnötig

---

### **10. `continue` – Aktuelle Iteration überspringen**

**Syntax:**

```python
for item in sequenz:
    if bedingung:
        continue  # Springe zur nächsten Iteration
    # Code hier wird übersprungen, wenn continue ausgeführt
```

**Praktisches Beispiel: Nur gerade Zahlen ausgeben**

```python
for zahl in range(1, 11):
    if zahl % 2 != 0:  # Ungerade Zahl?
        continue  # Überspringe Rest, gehe zur nächsten Zahl
    print(zahl)  # Wird nur bei geraden Zahlen ausgeführt

# Output:
# 2
# 4
# 6
# 8
# 10
```

**Wann `continue` verwenden:**

- Element soll übersprungen werden
- Bestimmte Bedingung nicht erfüllt
- Filter-Logik

---

### **11. `break` vs. `continue` – Der Unterschied**

```python
# Mit break (stoppt bei 5)
print("Mit break:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Output: 1, 2, 3, 4

print("\nMit continue:")
# Mit continue (überspringt 5)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output: 1, 2, 3, 4, 6, 7, 8, 9, 10
```

**Merkhilfe:**

- **`break`** = "Abbrechen, ich bin fertig!" (Schleife endet)
- **`continue`** = "Dieses Element auslassen, weiter zum nächsten!" (Schleife läuft weiter)

---

## **TEIL 5: `for` VS. `while` – WANN WAS?**

### **12. Entscheidungshilfe**

|Situation|Verwende|Beispiel|
|---|---|---|
|Anzahl Iterationen bekannt|`for`|"10 Mal wiederholen"|
|Über Liste/Sequenz iterieren|`for`|"Jedes Element verarbeiten"|
|Anzahl Iterationen unbekannt|`while`|"Bis Benutzer 'quit' eingibt"|
|Bedingungsbasiert|`while`|"Solange Summe < 100"|
|Zähler von X bis Y|`for` mit `range()`|"Von 1 bis 100"|

**Faustregel:**

- ✅ `for` = Wenn du weißt, WIE OFT oder ÜBER WAS
- ✅ `while` = Wenn du weißt, BIS WANN (Bedingung)

---

## **SCHNELLREFERENZ**

### **`for`-Schleife Cheatsheet:**

```python
# Über Liste
for item in liste:
    print(item)

# Mit range (0 bis 4)
for i in range(5):
    print(i)

# Mit range (Start, Stop)
for i in range(2, 6):
    print(i)

# Mit Schrittweite
for i in range(0, 10, 2):
    print(i)

# Mit break
for i in range(10):
    if i == 5:
        break

# Mit continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### **`while`-Schleife Cheatsheet:**

```python
# Einfache while
count = 0
while count < 5:
    print(count)
    count += 1

# Mit break
while True:
    antwort = input("Weiter? (j/n): ")
    if antwort == "n":
        break

# Mit continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

---

## **HÄUFIGE FEHLER UND LÖSUNGEN**

❌ **Fehler 1: Vergessener Doppelpunkt**

```python
for i in range(5)  # SyntaxError!
    print(i)
```

✅ **Lösung:** Doppelpunkt hinzufügen

```python
for i in range(5):
    print(i)
```

---

❌ **Fehler 2: Fehlende Einrückung**

```python
for i in range(5):
print(i)  # IndentationError!
```

✅ **Lösung:** Code einrücken

```python
for i in range(5):
    print(i)
```

---

❌ **Fehler 3: Endlosschleife**

```python
x = 0
while x < 10:
    print(x)
    # x wird nie erhöht!
```

✅ **Lösung:** Variable ändern

```python
x = 0
while x < 10:
    print(x)
    x += 1
```

---

❌ **Fehler 4: `range()` falsch verstanden**

```python
# Erwartet: 1, 2, 3, 4, 5
for i in range(1, 5):  # Gibt nur 1, 2, 3, 4
    print(i)
```

✅ **Lösung:** Stop-Wert um 1 erhöhen

```python
for i in range(1, 6):  # Gibt 1, 2, 3, 4, 5
    print(i)
```

---

## **PRAXISAUFGABEN ZUM ÜBEN**

**Aufgabe 1:** Schreibe eine `for`-Schleife, die alle Zahlen von 1 bis 10 ausgibt.

**Aufgabe 2:** Schreibe eine `while`-Schleife, die von 10 bis 1 rückwärts zählt.

**Aufgabe 3:** Schreibe eine Schleife, die nur die ungeraden Zahlen von 1 bis 20 ausgibt (verwende `continue`).

**Aufgabe 4:** Schreibe eine Schleife, die bei der ersten Zahl > 50 stoppt:

```python
zahlen = [10, 25, 30, 55, 60, 70]
```

---

### **Merksätze:**

🎯 **`for` = "für jedes Element", `while` = "solange Bedingung wahr"**  
🎯 **`range(stop)` geht von 0 bis stop-1, NICHT bis stop!**  
🎯 **`break` = Schleife verlassen, `continue` = Iteration überspringen**  
🎯 **Vergiss nie den Doppelpunkt `:` und die Einrückung!**  
🎯 **Bei `while`: Variable in Bedingung MUSS sich ändern, sonst Endlosschleife!**

---

## Kategorisierung der Themen

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Python Interpreter|Zum interaktiven Testen von Schleifen|
||VS Code|Editor zum Schreiben von Python-Skripten mit Schleifen|
||`print()` Funktion|Ausgabe von Werten innerhalb von Schleifen|
||`range()` Funktion|Erzeugt Zahlenfolgen für `for`-Schleifen|
||`input()` Funktion|Benutzereingabe in `while`-Schleifen (nicht im Dokument, aber relevant)|
|**Technische Fachbegriffe**|Loop (Schleife)|Wiederholung eines Code-Blocks mehrfach|
||`for` Loop|Schleife, die über eine Sequenz iteriert (Liste, Tupel, String, etc.)|
||`while` Loop|Schleife, die läuft, solange eine Bedingung `True` ist|
||Iteration (Durchlauf)|Ein einzelner Durchgang durch die Schleife|
||Iterate (Iterieren)|Durch Elemente einer Sequenz gehen|
||Sequence (Sequenz)|Geordnete Sammlung (Liste, Tupel, String, range)|
||Iterable Object|Objekt, über das man iterieren kann|
||Variable (Schleifenvariable)|Variable, die in jeder Iteration den nächsten Wert annimmt|
||Code Block (Code-Block)|Eingerückter Code innerhalb der Schleife|
||Indentation (Einrückung)|Pflicht-Einrückung für Code innerhalb der Schleife (4 Leerzeichen)|
||Infinite Loop (Endlosschleife)|Schleife, die nie endet (Bedingung bleibt immer `True`)|
||Condition (Bedingung)|Boolescher Ausdruck, der `True` oder `False` ist|
||Increment (Inkrementieren)|Wert erhöhen (z.B. `count = count + 1` oder `count += 1`)|
||Modulo Operator `%`|Rest einer Division (z.B. `7 % 3 = 1`)|
||Nested Loop (Verschachtelte Schleife)|Schleife innerhalb einer anderen Schleife|
||Flow Control (Flusskontrolle)|Steuerung des Ablaufs mit `break` und `continue`|
|**Wichtige Vokabeln**|`for` Keyword|Startet eine `for`-Schleife|
||`while` Keyword|Startet eine `while`-Schleife|
||`in` Keyword|Verbindet Schleifenvariable mit Sequenz (`for item in list`)|
||`range(stop)`|Erzeugt Zahlen von 0 bis `stop-1`|
||`range(start, stop)`|Erzeugt Zahlen von `start` bis `stop-1`|
||`range(start, stop, step)`|Erzeugt Zahlen von `start` bis `stop-1` mit Schrittweite `step`|
||`break` Statement|Beendet Schleife sofort und springt nach der Schleife weiter|
||`continue` Statement|Überspringt Rest der aktuellen Iteration, geht zur nächsten|
||Colon `:`|Doppelpunkt am Ende der Schleifen-Kopfzeile (Pflicht!)|
||Loop Body (Schleifenkörper)|Der eingerückte Code, der wiederholt wird|
||Start Value (Startwert)|Erster Wert in `range()`|
||Stop Value (Endwert)|Letzter Wert +1 in `range()` (wird NICHT erreicht)|
||Step Value (Schrittweite)|Um wie viel erhöht wird in `range()`|