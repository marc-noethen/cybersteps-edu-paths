## 📊 Zusammenfassung nach dem 80/20-Prinzip

**1. Variablen erstellen und verwenden (5 Minuten Praxis)**

- Syntax: `variable_name = wert`
- Beispiel: `alter = 25` oder `name = "Max"`
- Variablennamen: Kleinbuchstaben mit Unterstrichen `mein_name`, nicht `MeinName`)
- Wert ausgeben: `print(alter)` oder einfach `alter` im Interpreter eingeben

**2. Die 4 grundlegenden Datentypen kennen**

- **int** → Ganze Zahlen: `5`, `100`, `-3`
- **float** → Dezimalzahlen: `3.14`, `2.0`
- **str** → Text in Anführungszeichen: `"Hallo"` oder `'Welt'`
- **bool** → Wahrheitswerte: `True`, `False`

**3. Datentyp prüfen**

- `type(variable)` zeigt den Datentyp
- Beispiel: `type(25)` → `<class 'int'>`

**4. Grundrechenarten mit Zahlen**

- Addition: `10 + 5` → `15`
- Subtraktion: `10 - 3` → `7`
- Multiplikation: `4 * 5` → `20`
- Division: `10 / 3` → `3.333...` (immer float!)
- Ganzzahldivision: `10 // 3` → `3`
- Rest (Modulo): `10 % 3` → `1`
- Potenz: `2 ** 3` → `8`

**5. Text verarbeiten**

- Verkettung: `"Hallo" + " " + "Welt"` → `"Hallo Welt"`
- Wiederholung: `"Python " * 3` → `"Python Python Python "`
- **Wichtig:** Man kann keine Zahlen und Text direkt mischen! `5 + "Text"` → **Fehler!**

**6. Typkonvertierung bei Fehlern**

- Zahl zu Text: `str(5)` → `"5"`
- Text zu Zahl: `int("100")` → `100`
- Praktisch: `"Ich bin " + str(25) + " Jahre alt"` funktioniert!
- Noch besser: f-strings verwenden: `f"Ich bin {25} Jahre alt"`

**7. Python Interpreter benutzen (Windows 11)**

- Terminal/Eingabeaufforderung öffnen
- `python` oder `python3` eingeben
- Code Zeile für Zeile testen
- Beenden mit `exit()` oder `Ctrl+D`

### Häufigster Anfängerfehler:

❌ `"100" / 2` → **TypeError** (Text kann nicht durch Zahl geteilt werden)  
✅ `int("100") / 2` → `50.0` (erst zu Zahl konvertieren!)

**Merksatz:** Python ist flexibel bei Variablen (dynamische Typisierung), aber streng bei Operationen zwischen verschiedenen Datentypen!

---

## Kategorisierung der Themen

| Kategorie                   | Begriff                                                  | Bedeutung                                                                            |
| --------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Verwendete Tools**        | Python Interpreter                                       | Interaktive Entwicklungsumgebung zum Ausführen von Python-Code                       |
|                             | Terminal/Eingabeaufforderung                             | Kommandozeile zum Starten des Python Interpreters (Windows: `python` oder `python3`) |
| `>>>` Prompt                | Eingabeaufforderung des Python Interpreters              |                                                                                      |
| `print()` Funktion          | Gibt Werte in der Konsole aus                            |                                                                                      |
| `type()` Funktion           | Zeigt den Datentyp einer Variable oder eines Wertes an   |                                                                                      |
| `isinstance()` Funktion     | Prüft, ob ein Objekt zu einem bestimmten Datentyp gehört |                                                                                      |
| **Technische Fachbegriffe** | Variable (Variable)                                      | Benannter Speicherplatz für Daten                                                    |
|                             | Assignment Operator (Zuweisungsoperator)                 | Das Gleichheitszeichen `=` zum Zuweisen von Werten                                   |
|                             | Data Type (Datentyp)                                     | Die Art der gespeicherten Daten (z.B. Zahl, Text)                                    |
|                             | Dynamic Typing (Dynamische Typisierung)                  | Datentyp einer Variable kann sich zur Laufzeit ändern                                |
|                             | snake_case                                               | Namenskonvention mit Unterstrichen (z.B. `mein_name`)                                |
|                             | PEP 8                                                    | Python Enhancement Proposal - Styleguide für Python-Code                             |
|                             | TypeError                                                | Fehlermeldung bei inkompatiblen Datentypen                                           |
|                             | Concatenation (Verkettung)                               | Zusammenfügen von Strings mit `+`                                                    |
|                             | f-string (formatierter String)                           | Moderne Methode zur String-Formatierung mit `f"..."`                                 |
|                             | Floor Division (Ganzzahldivision)                        | Division mit Abrunden `//`                                                           |
|                             | Modulo (Rest)                                            | Rest einer Division `%`                                                              |
| **Wichtige Vokabeln**       | int (Integer)                                            | Ganzzahl ohne Dezimalstellen (z.B. 10, -3, 0)                                        |
|                             | float                                                    | Fließkommazahl mit Dezimalstellen (z.B. 3.14, 2.0)                                   |
|                             | str (String)                                             | Zeichenkette/Text in Anführungszeichen (z.B. "Hallo")                                |
|                             | bool (Boolean)                                           | Wahrheitswert: `True` oder `False`                                                   |
|                             | Exponentiation (Potenzierung)                            | Hochrechnen mit `**` (z.B. `2**3 = 8`)                                               |
|                             | Type Conversion (Typkonvertierung)                       | Umwandlung zwischen Datentypen: `int()`, `float()`, `str()`                          |
|                             | Keyword (Schlüsselwort)                                  | Reservierte Wörter in Python (z.B. if, else, for)                                    |
|                             | Case-sensitive (Groß-/Kleinschreibung)                   | Python unterscheidet zwischen `Variable` und `variable`                              |