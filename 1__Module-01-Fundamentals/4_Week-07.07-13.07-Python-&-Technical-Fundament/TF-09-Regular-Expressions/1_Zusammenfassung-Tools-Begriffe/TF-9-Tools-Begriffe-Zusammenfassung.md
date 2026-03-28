## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Was sind Regular Expressions?

**Regular Expressions (Regex)** sind Zeichenfolgen, die Suchmuster definieren – wie eine "Suchen & Ersetzen"-Funktion auf Steroiden. Statt nach festem Text zu suchen, können Sie nach **Mustern** suchen.

**Beispiele**:

- Alle E-Mail-Adressen in einem Dokument
- Alle IP-Adressen in Log-Dateien
- Alle Telefonnummern im Format XXX-XXX-XXXX
- Zeilen, die mit einem bestimmten Wort beginnen

---

### Warum Regex in der Cybersecurity?

**Die 6 Hauptanwendungen**:

1. **Log-Analyse**: Millionen Zeilen durchsuchen nach verdächtigen Mustern (z.B. fehlgeschlagene Login-Versuche)
2. **Intrusion Detection**: IDS/IPS-Systeme nutzen Regex für Malware-Signaturen
3. **Datenvalidierung**: Prüfung von Eingaben (E-Mail, Passwörter) gegen Angriffe
4. **Forensik**: Extraktion von Beweisen (E-Mails, Kreditkarten, URLs)
5. **Automatisierung**: Skripte zum Parsen von Outputs und Konfigurationsdateien
6. **Malware-Analyse**: Erkennung von Funktionsaufrufen, URLs, Verschlüsselungsschlüsseln

---

### Testing-Tool: Regex101.com

**Empfohlenes Tool**: https://regex101.com (plattformunabhängig, im Browser)

**Interface**:

- **REGULAR EXPRESSION** (oben): Regex-Muster eingeben
- **TEST STRING** (Mitte): Text zum Testen
- **EXPLANATION** (rechts): Automatische Erklärung des Musters
- **MATCH INFORMATION**: Zeigt alle Treffer an
- **FLAVOR**: PCRE2 (ähnlich zu Python) als Standard

---

### Die 6 fundamentalen Regex-Konzepte

#### 1. Literal Characters (Buchstäbliche Zeichen)

**Einfachste Form**: Zeichen matchen sich selbst

```regex
cat
```

Findet: "cat" in "The **cat** sat on the mat"

---

#### 2. Anchors (Anker) - Positionsmarkierungen

|Zeichen|Bedeutung|Beispiel|
|---|---|---|
|`^`|Zeilenanfang|`^Start` findet nur am Anfang|
|`$`|Zeilenende|`end$` findet nur am Ende|
|`\b`|Wortgrenze|`\bcat\b` findet "cat", nicht "catalog"|
|`\B`|Keine Wortgrenze|`\Bcat\B` findet "cat" in "concatenate"|

**Beispiel**:

```regex
^\d{3}     # Findet 3 Ziffern am Zeilenanfang
log$       # Findet "log" am Zeilenende
```

---

#### 3. Character Classes (Zeichenklassen)

|Zeichen|Bedeutung|Beispiel|
|---|---|---|
|`.`|Beliebiges Zeichen (außer Newline)|`a.c` → "abc", "a1c", "a@c"|
|`[abc]`|Eines der angegebenen Zeichen|`[aeiou]` → Vokale|
|`[a-z]`|Bereich von Zeichen|`[0-9]` → Ziffern|
|`[^abc]`|NICHT eines dieser Zeichen|`[^0-9]` → keine Ziffer|

**Predefined Classes (Shortcuts)**:

```regex
\d    # Ziffer [0-9]
\D    # Keine Ziffer [^0-9]
\w    # Wortzeichen [a-zA-Z0-9_]
\W    # Kein Wortzeichen
\s    # Whitespace (Leerzeichen, Tab, Newline)
\S    # Kein Whitespace
```

**Beispiel**:

```regex
\d\d\d-\d\d\d-\d\d\d\d    # Telefonnummer: 123-456-7890
[A-Z]\w+                   # Wort, das mit Großbuchstaben beginnt
```

---

#### 4. Quantifiers (Quantifizierer) - "Wie oft?"

|Zeichen|Bedeutung|Beispiel|
|---|---|---|
|`*`|0 oder mehr|`ab*c` → "ac", "abc", "abbc"|
|`+`|1 oder mehr|`ab+c` → "abc", "abbc" (NICHT "ac")|
|`?`|0 oder 1 (optional)|`colou?r` → "color", "colour"|
|`{n}`|Exakt n mal|`\d{3}` → exakt 3 Ziffern|
|`{n,}`|Mindestens n mal|`\d{2,}` → 2 oder mehr Ziffern|
|`{n,m}`|Zwischen n und m mal|`\d{2,4}` → 2 bis 4 Ziffern|

**Greedy vs. Non-Greedy**:

```regex
<div>.*</div>        # GREEDY: Matcht gesamten String
<div>.*?</div>       # NON-GREEDY: Matcht einzelne Tags
```

**Merksatz**: `?` nach Quantifizierer macht ihn "lazy" (minimal matchend)

---

#### 5. Grouping & Capturing (Gruppierung)

**Capturing Groups `()`**:

```regex
(\d{3})-(\d{3})-(\d{4})    # Telefonnummer mit 3 Gruppen
```

- Group 1: "123"
- Group 2: "456"
- Group 3: "7890"

**Non-Capturing Groups `(?:...)`**:

```regex
(?:ab)+       # Gruppiert "ab" für Quantifizierer, extrahiert aber nicht
```

**Alternation (OR) `|`**:

```regex
cat|dog              # Findet "cat" ODER "dog"
^(Error|Warning):    # Zeilen mit "Error:" oder "Warning:"
```

---

#### 6. Escaping (Maskierung)

**Problem**: Metazeichen literal matchen

```regex
\.        # Literal Punkt (nicht "beliebiges Zeichen")
\*        # Literal Stern (nicht "0 oder mehr")
\$        # Literal Dollar (nicht "Zeilenende")
\\        # Literal Backslash
\(        # Literal Klammer
```

**Beispiel**:

```regex
main\.py           # Findet "main.py" (nicht "mainXpy")
5\*4               # Findet "5*4" literal
192\.168\.1\.1     # IP-Adresse mit literal Punkten
```

---

### Praktische Beispiele für Cybersecurity

#### 1. IP-Adresse finden:

```regex
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
```

#### 2. E-Mail-Adresse (einfach):

```regex
\w+@\w+\.\w+
```

#### 3. Fehlgeschlagene Logins:

```regex
^.*Failed login.*from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
```

#### 4. URL extrahieren:

```regex
https?://[^\s]+
```

#### 5. Datum im Format YYYY-MM-DD:

```regex
\d{4}-\d{2}-\d{2}
```

#### 6. Hash (MD5/SHA):

```regex
\b[a-fA-F0-9]{32}\b      # MD5
\b[a-fA-F0-9]{40}\b      # SHA1
```

---

### Regex in Python (re-Modul)

**Wichtigste Funktionen**:

```python
import re

text = "My phone is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"    # Raw string r"" für Regex!

# 1. Erstes Match finden
match = re.search(pattern, text)
if match:
    print(match.group(0))  # "123-456-7890"

# 2. Alle Matches finden
matches = re.findall(r"\d+", "12 cats and 34 dogs")  # ['12', '34']

# 3. Ersetzen
new_text = re.sub(r"\d+", "X", text)  # "My phone is X-X-X"

# 4. Am Anfang matchen
if re.match(r"^My", text):
    print("Starts with 'My'")
```

---

### Cheat Sheet - Die wichtigsten Regex-Elemente

**Anchors**:

```
^     Zeilenanfang
$     Zeilenende
\b    Wortgrenze
```

**Character Classes**:

```
.     Beliebiges Zeichen
\d    Ziffer
\w    Wortzeichen
\s    Whitespace
[abc] Eines von a, b, c
[^abc] Nicht a, b, c
```

**Quantifiers**:

```
*     0 oder mehr
+     1 oder mehr
?     0 oder 1
{n}   Exakt n
{n,m} n bis m
```

**Groups**:

```
(...)    Capturing group
(?:...)  Non-capturing group
|        OR
```

**Escaping**:

```
\.  \*  \?  \+  \$  \^  \(  \)  \[  \]  \\
```

---

### Lernstrategie für Regex

**Der 80/20-Ansatz**:

1. **Beherrschen Sie diese 5 Muster** (decken 80% der Anwendungsfälle):
    
    - `\d+` (eine oder mehrere Ziffern)
    - `\w+` (ein oder mehrere Wortzeichen)
    - `.*` (beliebiger Text)
    - `^...$` (ganze Zeile)
    - `(...|...)` (Alternativen)
2. **Praxis auf Regex101.com**:
    
    - Muster eingeben
    - Testtext einfügen
    - Explanation-Panel lesen
    - Experimentieren!
3. **Häufige Fehler vermeiden**:
    
    - `.` ist NICHT ein literal Punkt (→ `\.` verwenden)
    - `*` kann 0 Vorkommen matchen (→ `+` für mindestens 1)
    - Greedy Matching kann zu viel matchen (→ `?` für lazy)
    - Vergessenes Escaping bei Metazeichen

---

### Merksätze

- **Literal = Sich selbst**: `cat` findet "cat"
- **Metazeichen = Spezielle Bedeutung**: `. * + ? ^ $ [ ] ( ) | \`
- **Anchors matchen Positionen**, nicht Zeichen
- **Quantifizierer sind greedy** (matchen maximal), außer mit `?`
- **Backslash escaped Metazeichen**: `\.` = literal Punkt
- **Raw Strings in Python**: `r"\d+"` verhindert doppeltes Escaping
- **Test, test, test**: Regex101.com ist Ihr bester Freund

---

### Typische Regex-Aufgaben in der Cybersecurity

|Aufgabe|Regex-Beispiel|
|---|---|
|IP-Adresse finden|`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`|
|E-Mail extrahieren|`[\w.-]+@[\w.-]+\.\w+`|
|Failed Logins|`Failed.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`|
|HTTP-Status-Codes|`HTTP/\d\.\d"\s+(\d{3})`|
|Malicious URLs|`https?://[a-z0-9.-]+.(ru|
|Credit Card (PCI DSS)|`\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b`|
|Suspicious PowerShell|`-enc[oded]*\s+[A-Za-z0-9+/=]+`|

---

## Verwendete Tools

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Verwendete Tools**|Regex101.com|Online-Testumgebung zum Erstellen, Testen und Verstehen von Regular Expressions|
||Python re-Modul|Eingebautes Python-Modul zur Verwendung von Regex in Skripten|
||Webbrowser|Zum Zugriff auf Online-Regex-Tester (Chrome, Firefox, Edge für Windows 11)|
||Text-Editor mit Regex-Support|Editoren wie VS Code, Notepad++ (Windows 11) zur Textverarbeitung mit Regex|
||grep (Command Line)|Unix/Linux-Tool zum Durchsuchen von Dateien mit Regex-Mustern|
||sed (Stream Editor)|Tool zur Textmanipulation mit Regex-Mustern|

---

## Technische Fachbegriffe

|**Kategorie**|**Begriff**|**Bedeutung**|
|---|---|---|
|**Technische Fachbegriffe**|Regular Expression (Regex/Regexp)|Zeichenfolge, die ein Suchmuster für Textverarbeitung definiert|
||Pattern (Muster)|Die Definition dessen, wonach in einem Text gesucht werden soll|
||Metacharacter (Metazeichen)|Sonderzeichen mit spezieller Bedeutung in Regex (z.B. ., *, +, ?)|
||Literal Character|Zeichen, das sich selbst repräsentiert (z.B. 'a' findet 'a')|
||Anchor (Anker)|Position im Text (Anfang/Ende), nicht tatsächliche Zeichen (^, $, \b)|
||Character Class (Zeichenklasse)|Set von Zeichen, von denen eines gematcht werden soll (z.B. [aeiou])|
||Predefined Character Class|Vordefinierte Abkürzungen (\d, \w, \s, \D, \W, \S)|
||Quantifier (Quantifizierer)|Gibt an, wie oft ein Element vorkommen muss (*, +, ?, {n}, {n,m})|
||Greedy Matching|Quantifizierer matcht so viel Text wie möglich|
||Non-Greedy/Lazy Matching|Quantifizierer matcht so wenig Text wie möglich (mit ? nach Quantifizierer)|
||Capturing Group|Gruppierung mit Klammern (), die gematchten Text extrahiert|
||Non-Capturing Group|Gruppierung (?:...) ohne Extraktion, nur für Logik|
||Alternation (Oder-Verknüpfung)|Pipe-Symbol \| für "oder" Logik (z.B. cat\|dog)|
||Escaping|Backslash \ vor Metazeichen, um sie literal zu matchen|
||Word Boundary|Position zwischen Wortzeichen und Nicht-Wortzeichen (\b)|
||Regex Flavor|Variante der Regex-Syntax (PCRE, POSIX BRE/ERE, Python)|
||Match|Erfolgreiche Übereinstimmung eines Musters mit Text|
||PCRE (Perl Compatible RE)|Weit verbreitete Regex-Syntax, ähnlich zu Python|
||Raw String (Python)|String mit r"" Präfix, behandelt Backslashes literal|
|**Wichtige Vokabeln**|Pattern matching|Musterabgleich, Finden von Textmustern|
||Search pattern|Suchmuster zur Textfindung|
||Text processing|Textverarbeitung und -manipulation|
||Data extraction|Extraktion spezifischer Daten aus Text|
||Log analysis|Analyse von Log-Dateien|
||Intrusion Detection/Prevention (IDS/IPS)|Systeme zum Erkennen/Verhindern von Angriffen|
||Data validation|Überprüfung der Eingaberichtigkeit|
||Digital forensics|Digitale Forensik zur Beweissicherung|
||Malware analysis|Analyse von Schadsoftware|
||Signature|Erkennungsmuster für Malware oder Angriffe|
||Whitespace|Leerzeichen, Tabs, Zeilenumbrüche|
||Newline|Zeilenumbruch (\n)|
||Alphanumeric|Buchstaben und Zahlen|
||Delimiter|Trennzeichen|
||Token|Einzelnes Element in einem Muster|
||Modifier/Flag|Optionen zur Verhaltensänderung (z.B. case-insensitive)|
||Non-overlapping|Nicht-überlappende Matches|
||Iterator|Objekt zur schrittweisen Verarbeitung von Matches|