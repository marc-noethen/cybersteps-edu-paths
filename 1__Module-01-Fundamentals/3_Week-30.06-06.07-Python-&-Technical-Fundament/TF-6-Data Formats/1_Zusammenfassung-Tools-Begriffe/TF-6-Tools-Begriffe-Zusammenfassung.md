## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Kernkonzepte

**Serialisierung und Deserialisierung** sind die fundamentalen Prozesse beim Datenaustausch:

- **Serialisierung** wandelt Datenstrukturen im Speicher in speicher- oder übertragbare Formate um
- **Deserialisierung** wandelt diese Formate zurück in verwendbare Datenstrukturen
- Analogie: Packen (Serialisierung) und Auspacken (Deserialisierung) von Daten für den Transport

### Die vier wichtigsten Datenformate

**1. CSV (Comma-Separated Values)**

- Einfachstes Format für tabellarische Daten
- Zeilen = Datensätze, Kommas trennen Werte
- Ideal für Spreadsheet-artige Daten
- Einschränkung: Problematisch bei komplexen, verschachtelten Strukturen

**2. JSON (JavaScript Object Notation)**

- Beliebtestes Format für Web-APIs und Konfiguration
- Verwendet Schlüssel-Wert-Paare in `{}` und Listen in `[]`
- Gut lesbar für Menschen und Maschinen
- Unterstützt verschachtelte Strukturen

**3. XML (eXtensible Markup Language)**

- Flexibles Format mit selbstdefinierten Tags `<tag>Wert</tag>`
- Unterstützt Attribute und verschachtelte Elemente
- Wortreicher als JSON, aber sehr strukturiert
- Häufig in älteren Systemen und komplexen Datenstrukturen

**4. YAML (YAML Ain't Markup Language)**

- Minimalistisch und menschenlesbar
- Verwendet Einrückung (Leerzeichen!) zur Strukturierung
- Beliebt für Konfigurationsdateien
- Vorsicht: Einrückungsfehler führen zu Parsing-Fehlern

### Relevanz für Cybersecurity (80% der praktischen Anwendungen)

1. **Konfigurationsdateien** von Security-Tools verwenden JSON, XML oder YAML
2. **API-Kommunikation** mit Sicherheitsdiensten erfolgt meist über JSON
3. **Log-Analyse** profitiert von strukturierten Formaten (oft JSON)
4. **Datenexport/-import** zwischen Security-Tools nutzt CSV, XML oder JSON
5. **Payload-Analyse** bei Netzwerkverkehr erfordert Deserialisierung

### Praktische Fähigkeit

Sie müssen kein Expert:in im Programmieren von Parsern sein, aber sollten:

- Formate auf Anhieb erkennen können
- Die Grundstruktur verstehen
- Einfache Konfigurationen lesen und anpassen können
- Wissen, wann welches Format geeignet ist

---

## Verwendete Tools

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Verwendete Tools**|CSV-Editor (z.B. Excel, LibreOffice Calc)|Programme zum Bearbeiten von Comma-Separated Values Dateien|
||JSON-Parser (z.B. jq, Python json-Modul)|Werkzeuge zum Verarbeiten und Validieren von JSON-Daten|
||XML-Parser (z.B. xmllint, Python xml-Modul)|Werkzeuge zum Verarbeiten und Validieren von XML-Dokumenten|
||YAML-Parser (z.B. yamllint, Python yaml-Modul)|Werkzeuge zum Verarbeiten und Validieren von YAML-Dateien|
||Text-Editoren (Notepad++, VS Code)|Editoren zum Anzeigen und Bearbeiten strukturierter Datendateien|

---

## Technische Fachbegriffe

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Technische Fachbegriffe**|Serialisierung|Umwandlung von Datenstrukturen im Arbeitsspeicher in ein speicher- oder übertragbares Format|
||Deserialisierung|Rückumwandlung von serialisierten Daten in verwendbare Datenstrukturen im Arbeitsspeicher|
||Strukturierte Daten|Daten, die einem konsistenten Muster oder Modell folgen|
||Key-Value-Pair (Schlüssel-Wert-Paar)|Datenpaar bestehend aus einem eindeutigen Schlüssel und dem zugehörigen Wert|
||JSON Object|Sammlung von Schlüssel-Wert-Paaren in geschweiften Klammern {}|
||JSON Array|Geordnete Liste von Werten in eckigen Klammern []|
||XML-Tag|Markierungselement in spitzen Klammern <> zur Strukturierung von Daten|
||XML-Attribut|Zusätzliche Information innerhalb eines XML-Tags|
||YAML-Mapping|Zuordnung von Schlüsseln zu Werten (entspricht JSON-Objekt)|
||YAML-Sequence|Geordnete Liste von Elementen (entspricht JSON-Array)|
||API (Application Programming Interface)|Schnittstelle zum Datenaustausch zwischen Programmen|
||Delimiter (Trennzeichen)|Zeichen zur Trennung von Datenwerten (z.B. Komma in CSV)|
||Indentation (Einrückung)|Verwendung von Leerzeichen zur Strukturierung (wichtig bei YAML)|
||Parsing|Analysieren und Verarbeiten strukturierter Daten|
|**Wichtige Vokabeln**|Tabular data (Tabellarische Daten)|Daten in Zeilen und Spalten organisiert|
||Header row (Kopfzeile)|Erste Zeile mit Spaltennamen|
||Record (Datensatz)|Eine vollständige Zeile mit zusammengehörigen Informationen|
||Nested (Verschachtelt)|Hierarchisch angeordnete Datenstrukturen|
||Portable (Portabel)|Zwischen verschiedenen Systemen übertragbar|
||Persistent (Persistent)|Dauerhaft gespeichert (nicht temporär)|
||Human-readable (Menschenlesbar)|Für Menschen verständlich formatiert|
||Machine-readable (Maschinenlesbar)|Von Computern effizient verarbeitbar|
||Verbose (Wortreich)|Viele Zeichen zur Darstellung der gleichen Information|
||Configuration file (Konfigurationsdatei)|Datei mit Einstellungen für Programme|
||Payload|Nutzdaten, die übertragen oder verarbeitet werden|
||Log file (Protokolldatei)|Datei mit Aufzeichnungen von Systemereignissen|