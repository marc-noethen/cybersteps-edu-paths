## 📊 Zusammenfassung nach dem 80/20-Prinzip

---

## **TEIL 1: WAS SIND BUGS?**

### **1. Definition: Bug**

**Bug = Fehler im Code, der zu falschem oder unerwartetem Verhalten führt**

```python
# Beispiel: Dieser Code soll "Hallo" ausgeben
print("Halo")  # Tippfehler = Bug!
```

**Debugging = Prozess des Findens und Behebens von Bugs**

**Historischer Fakt:** Der Begriff "Bug" kommt von echten Insekten, die früher in Computer-Hardware krochen und Fehler verursachten! 🐛

---

## **TEIL 2: DIE 3 ARTEN VON FEHLERN**

### **2. Syntaxfehler (Syntax Errors) – Code läuft gar nicht erst**

**Definition:** Grammatikalische Fehler – Python kann Code nicht verstehen

**Häufigste Ursachen:**

- Vergessener Doppelpunkt `:`
- Falsch geschriebene Keywords
- Fehlende/falsche Klammern
- Fehlende Einrückung

**Beispiele:**

```python
# ❌ Fehler 1: Vergessener Doppelpunkt
if x > 5
    print("Groß")
# SyntaxError: invalid syntax

# ✅ Richtig:
if x > 5:
    print("Groß")

# ❌ Fehler 2: Falsch geschriebenes Keyword
whlie count < 10:  # "whlie" statt "while"
    print(count)
# SyntaxError: invalid syntax

# ✅ Richtig:
while count < 10:
    print(count)

# ❌ Fehler 3: Ungleiche Klammern
print("Hallo"
# SyntaxError: unexpected EOF while parsing

# ✅ Richtig:
print("Hallo")
```

**Erkennung:** Python zeigt sofort Fehlermeldung mit Zeilennummer

---

### **3. Laufzeitfehler (Runtime Errors) – Code crasht während Ausführung**

**Definition:** Code startet, aber etwas geht während der Ausführung schief

**Häufigste Ursachen:**

- Division durch Null
- Zugriff auf nicht existierenden Listen-Index
- Verwendung undefinierter Variable
- Falscher Datentyp

**Beispiele:**

```python
# ❌ Fehler 1: Division durch Null
x = 10
y = 0
print(x / y)
# ZeroDivisionError: division by zero

# ✅ Lösung: Vor Division prüfen
if y != 0:
    print(x / y)
else:
    print("Division durch Null nicht möglich")

# ❌ Fehler 2: IndexError
liste = [1, 2, 3]
print(liste[5])
# IndexError: list index out of range

# ✅ Lösung: Index prüfen
if 5 < len(liste):
    print(liste[5])
else:
    print("Index existiert nicht")

# ❌ Fehler 3: NameError (undefinierte Variable)
print(ergebnis)
# NameError: name 'ergebnis' is not defined

# ✅ Lösung: Variable zuerst definieren
ergebnis = 42
print(ergebnis)
```

**Erkennung:** Python zeigt **Traceback** (Fehlerprotokoll) mit:

- Fehlertyp (z.B. `IndexError`, `ZeroDivisionError`)
- Zeilennummer
- Fehlerbeschreibung

---

### **4. Logikfehler (Logic Errors) – Code läuft, Ergebnis ist falsch**

**Definition:** Kein Crash, aber Programm macht nicht das, was es soll

**Häufigste Ursachen:**

- Falsche mathematische Formel
- Falsche Bedingung in `if`-Statement
- Falscher Operator (`>` statt `>=`)
- Falscher Startwert

**Beispiele:**

```python
# ❌ Fehler: Durchschnitt falsch berechnet
zahlen = [10, 20, 30]
durchschnitt = sum(zahlen) / 2  # Sollte durch 3 teilen!
print(durchschnitt)  # Output: 30.0 (FALSCH! Sollte 20.0 sein)

# ✅ Richtig:
durchschnitt = sum(zahlen) / len(zahlen)
print(durchschnitt)  # Output: 20.0

# ❌ Fehler: Falsche Bedingung
alter = 18
if alter > 18:  # Sollte >= sein!
    print("Volljährig")
# Gibt nichts aus, obwohl Person mit 18 volljährig ist

# ✅ Richtig:
if alter >= 18:
    print("Volljährig")

# ❌ Fehler: Schleife läuft nie
count = 0
while count > 5:  # Sollte < sein!
    print(count)
    count += 1
# Gibt nichts aus, weil 0 nicht > 5

# ✅ Richtig:
count = 0
while count < 5:
    print(count)
    count += 1
```

**Erkennung:** Am schwierigsten! Keine Fehlermeldung, nur falsches Ergebnis

---

## **TEIL 3: DER DEBUGGING-PROZESS (4 SCHRITTE)**

### **5. Systematisches Debugging**

**Schritt 1: Problem verstehen**

- Wie reproduziere ich den Fehler?
- Was ist die **erwartete** Ausgabe?
- Was ist die **tatsächliche** Ausgabe?

**Schritt 2: Fehlerquelle finden (isolieren)**

- Wo im Code tritt der Fehler auf?
- Welche Variable hat falschen Wert?
- Welcher Code-Abschnitt ist betroffen?

**Schritt 3: Fehler beheben**

- Code korrigieren

**Schritt 4: Fix testen**

- Code erneut ausführen
- Grenzfälle (Edge Cases) testen
- Neue Bugs ausschließen

---

## **TEIL 4: DEBUGGING MIT `print()`-STATEMENTS**

### **6. Die einfachste Debugging-Methode**

**Prinzip:** `print()` an verschiedenen Stellen einfügen, um:

- Variablenwerte zu überprüfen
- Ausführungsfluss zu verfolgen
- Herauszufinden, welcher Code-Teil läuft

**Praktisches Beispiel:**

```python
# ❌ Buggy Code: Summe ist falsch
zahlen = [1, 2, 3, 4, 5]
summe = 10  # Fehler: Sollte 0 sein!

for zahl in zahlen:
    summe = summe + zahl

print(f"Endsumme: {summe}")
# Output: Endsumme: 25 (FALSCH! Sollte 15 sein)

# ✅ Debugging mit print()
zahlen = [1, 2, 3, 4, 5]
summe = 10

print(f"Startwert summe: {summe}")  # Debug-Print

for zahl in zahlen:
    print(f"Aktuelle Zahl: {zahl}")  # Debug-Print
    summe = summe + zahl
    print(f"Summe nach Addition: {summe}")  # Debug-Print

print(f"Endsumme: {summe}")

# Output:
# Startwert summe: 10  ← Hier ist das Problem!
# Aktuelle Zahl: 1
# Summe nach Addition: 11
# Aktuelle Zahl: 2
# Summe nach Addition: 13
# ...
```

**Nachdem Fehler gefunden:** `print()`-Statements entfernen oder auskommentieren

---

### **7. Strategisch `print()` einsetzen**

```python
def berechne_rabatt(preis, prozent):
    """Berechnet reduzierten Preis nach Rabatt."""
    print(f"DEBUG: Eingabe preis={preis}, prozent={prozent}")  # Input prüfen
    
    rabatt = preis * prozent
    print(f"DEBUG: Rabattbetrag={rabatt}")  # Zwischenwert prüfen
    
    neuer_preis = preis - rabatt
    print(f"DEBUG: Neuer Preis={neuer_preis}")  # Output prüfen
    
    return neuer_preis

ergebnis = berechne_rabatt(100, 0.2)
print(f"Endpreis: {ergebnis}")
```

**Vorteile:** ✅ Einfach und schnell ✅ Funktioniert überall ✅ Keine zusätzlichen Tools nötig

**Nachteile:** ❌ Muss manuell eingefügt/entfernt werden ❌ Kann Code unübersichtlich machen ❌ Nicht ideal für große Programme

---

## **TEIL 5: VS CODE DEBUGGER (PROFESSIONELLES DEBUGGING)**

### **8. Was ist ein IDE-Debugger?**

**Debugger = Professionelles Werkzeug zum schrittweisen Durchlaufen von Code**

**Vorteile gegenüber `print()`:**

- ✅ Code Zeile für Zeile durchgehen
- ✅ Alle Variablen live sehen
- ✅ Kein Ändern des Codes nötig
- ✅ Funktionen durchlaufen
- ✅ Ausführung pausieren und fortsetzen

---

### **9. Breakpoints setzen (Windows 11)**

**Was ist ein Breakpoint?** Markierung im Code, an der die Ausführung **pausiert**

**Wie setzen (VS Code):**

1. Python-Datei in VS Code öffnen
2. Links neben Zeilennummer in **Gutter** (grauer Bereich) klicken
3. **Roter Punkt** erscheint = Breakpoint gesetzt
4. Erneut klicken = Breakpoint entfernen

```python
def addiere(a, b):
    result = a + b      # ← Hier Breakpoint setzen (roter Punkt)
    return result

x = 5
y = 10
summe = addiere(x, y)   # ← Hier zweiten Breakpoint setzen
print(f"Summe: {summe}")
```

---

### **10. Debugger starten (Windows 11)**

**Schritt-für-Schritt:**

1. **Datei öffnen:** Python-Datei in VS Code
2. **Breakpoint setzen:** Roten Punkt neben Zeile setzen
3. **Run and Debug öffnen:**
    - Linke Seitenleiste → Symbol mit Play-Button + Bug-Icon
    - Oder: `Ctrl + Shift + D`
4. **Debugging starten:**
    - Button "Run and Debug" klicken
    - Konfiguration wählen: "Python File"
5. **Programm pausiert** an erstem Breakpoint

---

### **11. Debug-Steuerung: Die 4 Hauptfunktionen**

**Steuerungselemente (oben im Debug-Fenster):**

|Symbol|Name|Tastenkombination|Funktion|
|---|---|---|---|
|▶️|**Continue**|`F5`|Läuft bis zum nächsten Breakpoint|
|⤵️|**Step Over**|`F10`|Führt nächste Zeile aus (geht NICHT in Funktionen)|
|⬇️|**Step Into**|`F11`|Geht IN Funktion hinein|
|⬆️|**Step Out**|`Shift + F11`|Springt AUS aktueller Funktion heraus|
|⏹️|**Stop**|`Shift + F5`|Beendet Debugging|

**Praktisches Beispiel:**

```python
def multipliziere(a, b):
    ergebnis = a * b
    return ergebnis

x = 5
y = 3
resultat = multipliziere(x, y)  # ← Breakpoint hier
print(resultat)
```

**Debugging-Ablauf:**

1. Programm pausiert bei `resultat = multipliziere(x, y)`
2. **Step Into (F11):** Springt in `multipliziere()` Funktion
3. **Step Over (F10):** Führt `ergebnis = a * b` aus
4. **Step Over (F10):** Führt `return ergebnis` aus
5. **Step Out (Shift+F11):** Springt zurück zu `print(resultat)`
6. **Continue (F5):** Läuft bis Ende (oder nächster Breakpoint)

---

### **12. Variables Panel – Variablen live beobachten**

**Wo finden (Windows 11):**

- Linke Seitenleiste während Debugging
- Bereich "VARIABLES"

**Was sichtbar:**

- **Locals:** Lokale Variablen (in aktueller Funktion)
- **Globals:** Globale Variablen

**Praktisches Beispiel:**

```python
def berechne(a, b):
    summe = a + b      # ← Breakpoint hier
    produkt = a * b
    return summe, produkt

x = 10
y = 5
ergebnis = berechne(x, y)
```

**Variables Panel zeigt während Pause:**

```
Locals:
  a = 10
  b = 5
  summe = 15
  produkt = (noch nicht berechnet)

Globals:
  x = 10
  y = 5
  ergebnis = (noch nicht zugewiesen)
```

---

### **13. Call Stack – Funktionsaufruf-Reihenfolge**

**Was ist Call Stack?** Zeigt Reihenfolge der Funktionsaufrufe bis zur aktuellen Position

**Beispiel:**

```python
def funktion_a():
    funktion_b()

def funktion_b():
    funktion_c()

def funktion_c():
    x = 5 + 3  # ← Breakpoint hier

funktion_a()
```

**Call Stack zeigt:**

```
funktion_c (aktuelle Position)
  ↑ aufgerufen von
funktion_b
  ↑ aufgerufen von
funktion_a
  ↑ aufgerufen von
<module> (Hauptprogramm)
```

---

## **TEIL 6: DEBUGGER VS. PRINT() – WANN WAS?**

### **14. Entscheidungshilfe**

|Situation|Methode|Grund|
|---|---|---|
|Schneller Check|`print()`|Einfach und schnell|
|Kleine Skripte|`print()`|Kein Setup nötig|
|Komplexe Logik|Debugger|Schritt-für-Schritt durchgehen|
|Viele Variablen prüfen|Debugger|Alle auf einmal sehen|
|Funktionen durchlaufen|Debugger|Step Into/Out|
|Produktions-Code|Debugger|Kein Code-Ändern nötig|

---

## **SCHNELLREFERENZ**

### **Debugging-Workflow:**

```
1. Fehler identifizieren
   ↓
2. Fehlertyp bestimmen (Syntax/Runtime/Logic)
   ↓
3. Debugging-Methode wählen:
   - Einfach: print()
   - Komplex: Debugger
   ↓
4. Fehlerquelle isolieren
   ↓
5. Code korrigieren
   ↓
6. Testen (auch Grenzfälle!)
```

### **VS Code Debugger Cheatsheet (Windows 11):**

```
Breakpoint setzen:      Klick links neben Zeilennummer
Debugging starten:      Ctrl + Shift + D → "Run and Debug"
Continue:               F5
Step Over:              F10
Step Into:              F11
Step Out:               Shift + F11
Stop Debugging:         Shift + F5
```

---

## **HÄUFIGE FEHLER UND DEBUGGING-STRATEGIEN**

### **15. Häufiger Fehler 1: Endlosschleife**

```python
# ❌ Problem
count = 0
while count < 10:
    print(count)
    # count wird nie erhöht → Endlosschleife!
```

**Debugging-Strategie:**

1. Breakpoint in Schleife setzen
2. Variables Panel prüfen: Ändert sich `count`?
3. Wenn nein: `count += 1` fehlt

---

### **16. Häufiger Fehler 2: Falsche Bedingung**

```python
# ❌ Problem
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    if zahl > 3:  # Sollte >= sein
        print(zahl)
# Output: 4, 5 (FALSCH! Sollte 3, 4, 5 sein)
```

**Debugging-Strategie:**

1. Breakpoint in `if`-Block
2. Variables Panel: Wert von `zahl` prüfen
3. Bedingung manuell testen: `3 > 3` = `False` → Fehler gefunden!

---

### **17. Häufiger Fehler 3: Off-by-One Error**

```python
# ❌ Problem
zahlen = [10, 20, 30, 40, 50]
for i in range(len(zahlen)):
    print(zahlen[i+1])  # IndexError beim letzten Element!
```

**Debugging-Strategie:**

1. Breakpoint in Schleife
2. Variables Panel: `i` und `len(zahlen)` beobachten
3. Wenn `i = 4`: `zahlen[5]` → IndexError!

---

## **PRAXISAUFGABEN**

**Aufgabe 1:** Finde den Fehler (Logikfehler):

```python
def ist_gerade(zahl):
    if zahl % 2 == 1:  # Was ist hier falsch?
        return True
    else:
        return False
```

**Aufgabe 2:** Debugge mit `print()`:

```python
zahlen = [1, 2, 3, 4, 5]
produkt = 0
for zahl in zahlen:
    produkt = produkt * zahl
# Warum ist produkt immer 0?
```

**Aufgabe 3:** Setze Breakpoints und durchlaufe:

```python
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n-1)

print(fakultaet(5))
# Durchlaufe mit Step Into und beobachte Call Stack
```

---

### **Merksätze:**

🎯 **3 Fehlertypen: Syntax (läuft nicht), Runtime (crasht), Logic (falsche Ausgabe)**  
🎯 **`print()` = schnell & einfach, Debugger = professionell & mächtig**  
🎯 **Breakpoint = roter Punkt, Code pausiert hier**  
🎯 **F10 = Step Over (nächste Zeile), F11 = Step Into (in Funktion)**  
🎯 **Variables Panel zeigt ALLE Werte während Pause**  
🎯 **Debugging ist systematisch: Verstehen → Isolieren → Beheben → Testen**

---

## Kategorisierung der Themen

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Visual Studio Code (VS Code)|IDE mit eingebautem Debugger für Python|
||Python Extension|VS Code-Erweiterung für Python-Debugging-Funktionen|
||`print()` Funktion|Einfachste Debugging-Methode zur Ausgabe von Werten|
||Debugger (IDE-Debugger)|Integriertes Werkzeug zum schrittweisen Durchlaufen von Code|
||Breakpoint (Haltepunkt)|Markierung, an der Code-Ausführung pausiert|
||Run and Debug View|Bereich in VS Code für Debugging-Funktionen (Seitenleiste mit Play+Bug-Icon)|
||Variables Panel|Fenster zur Anzeige aktueller Variablenwerte während des Debuggings|
||Debug Controls|Steuerungselemente: Continue, Step Over, Step Into, Step Out|
||Watch Expressions|Überwachung spezifischer Variablen/Ausdrücke während Debugging|
||Call Stack View|Anzeige der Funktionsaufruf-Reihenfolge|
|**Technische Fachbegriffe**|Bug (Fehler)|Fehler oder Defekt im Code, der falsches Verhalten verursacht|
||Debugging (Fehlersuche)|Prozess des Findens und Behebens von Bugs|
||Syntax Error (Syntaxfehler)|Grammatikalischer Fehler, Python kann Code nicht ausführen|
||Runtime Error (Laufzeitfehler)|Fehler während der Ausführung (Code startet, crasht dann)|
||Logic Error (Logikfehler)|Code läuft ohne Fehler, aber Ergebnis ist falsch|
||Traceback|Fehlerbericht von Python mit Informationen über Fehlerort|
||Expected Output (Erwartete Ausgabe)|Was das Programm tun sollte|
||Actual Output (Tatsächliche Ausgabe)|Was das Programm wirklich tut|
||Reproduce (Reproduzieren)|Fehler konstant zum Wiederauftreten bringen|
||Isolate (Isolieren)|Fehlerquelle im Code eingrenzen|
||Edge Cases (Grenzfälle)|Extremwerte oder Sonderfälle zum Testen|
||Breakpoint|Markierung zum Pausieren der Code-Ausführung|
||Step Over|Nächste Zeile ausführen ohne in Funktionen zu gehen|
||Step Into|In Funktion hineingehen und schrittweise durchlaufen|
||Step Out|Aus aktueller Funktion herausspringen|
||Continue|Ausführung bis zum nächsten Breakpoint fortsetzen|
||Execution Flow (Ausführungsfluss)|Reihenfolge, in der Code ausgeführt wird|
||Inspect Variables (Variablen inspizieren)|Variablenwerte während Pause betrachten|
||Gutter|Bereich links neben Zeilennummern (zum Setzen von Breakpoints)|
|**Wichtige Vokabeln**|Syntax|Regelwerk, wie Code geschrieben werden muss|
||Colon `:`|Doppelpunkt (häufig vergessen bei `if`, `for`, `def`)|
||Mismatched Parentheses|Ungleiche/fehlende Klammern `()`, `[]`, `{}`|
||Divide by Zero|Division durch Null (verursacht RuntimeError)|
||IndexError|Zugriff auf nicht existierenden Listen-Index|
||NameError|Verwendung undefinierter Variable|
||Crash|Programmabsturz während Ausführung|
||Red Dot|Roter Punkt = gesetzter Breakpoint in VS Code|
||Debug Console|Konsole während Debugging zur Eingabe von Befehlen|
||Play Icon|Symbol zum Fortsetzen der Ausführung (Continue)|
||Bug Icon|Symbol für Debugging-Funktionen in VS Code|