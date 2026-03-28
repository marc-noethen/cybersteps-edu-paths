## 📊 Zusammenfassung nach dem 80/20-Prinzip

**Dictionaries** sind eine fundamentale Python-Datenstruktur, die Daten als **Schlüssel-Wert-Paare** speichert. Im Gegensatz zu Listen, bei denen auf Elemente über Indizes zugegriffen wird, nutzen Dictionaries eindeutige Schlüssel für den Datenzugriff.

**Kernkonzepte:**

- **Erstellung**: `my_dict = {"key": "value"}` oder `dict(key=value)`
- **Schlüssel**: Müssen unveränderlich sein (Strings, Zahlen, Tupel) - keine Listen oder Dictionaries
- **Werte**: Können jeden Datentyp haben (Strings, Zahlen, Listen, andere Dictionaries, etc.)
- **Zugriff**: `my_dict["key"]` (wirft KeyError bei fehlendem Schlüssel) oder `my_dict.get("key", default)` (sicherer)
- **Hinzufügen/Aktualisieren**: `my_dict["new_key"] = value`
- **Löschen**: `del my_dict["key"]`, `my_dict.pop("key")`, oder `my_dict.popitem()`
- **Prüfung**: `"key" in my_dict`
- **Wichtige Methoden**: `.keys()`, `.values()`, `.items()` geben View-Objekte zurück

**Hauptvorteil**: Schneller Datenzugriff über eindeutige Bezeichner statt Positionsnummern - ideal für Kontaktlisten, Konfigurationen, Datenbankähnliche Strukturen.

---

## Tools

|Tool/Werkzeug/Programm|Bedeutung/Funktion|
|---|---|
|Python|Programmiersprache, in der Dictionaries als eingebaute Datenstruktur verfügbar sind|
|VS Code|Code-Editor/IDE zum Experimentieren mit Python-Code|

---

## Technische Fachbegriffe

|Fachbegriff|Bedeutung/Erklärung|
|---|---|
|Dictionary (Wörterbuch)|Python-Datenstruktur zum Speichern von Schlüssel-Wert-Paaren; ungeordnet, aber schneller Zugriff über Schlüssel|
|Key (Schlüssel)|Eindeutiger Bezeichner zum Nachschlagen von Daten in einem Dictionary; muss unveränderlich sein|
|Value (Wert)|Die Daten, die mit einem Schlüssel verknüpft sind; kann jeden Datentyp haben|
|Key-Value Pair (Schlüssel-Wert-Paar)|Eine Kombination aus Schlüssel und zugehörigem Wert in einem Dictionary|
|Immutable (Unveränderlich)|Datentypen, die nach ihrer Erstellung nicht mehr geändert werden können (Strings, Zahlen, Tupel)|
|Mutable (Veränderlich)|Datentypen, die nach ihrer Erstellung geändert werden können (Listen, Dictionaries)|
|List (Liste)|Geordnete Sequenz von Elementen; Zugriff über Index|
|Tuple (Tupel)|Unveränderliche, geordnete Sequenz von Elementen|
|String (Zeichenkette)|Sequenz von Zeichen; unveränderlicher Datentyp|
|Integer (Ganzzahl)|Ganzzahliger Datentyp ohne Dezimalstellen|
|Float (Gleitkommazahl)|Zahlendatentyp mit Dezimalstellen|
|Boolean|Datentyp mit zwei Werten: True (Wahr) oder False (Falsch)|
|View Object (Ansichtsobjekt)|Dynamisches Objekt, das die aktuellen Schlüssel, Werte oder Paare eines Dictionaries zeigt|
|KeyError|Fehlertyp, der auftritt, wenn auf einen nicht existierenden Schlüssel zugegriffen wird|
|Method (Methode)|Funktion, die zu einem Objekt gehört und auf diesem ausgeführt wird|
|Constructor (Konstruktor)|Spezielle Funktion zum Erstellen neuer Objekte (z.B. `dict()`)|

---
