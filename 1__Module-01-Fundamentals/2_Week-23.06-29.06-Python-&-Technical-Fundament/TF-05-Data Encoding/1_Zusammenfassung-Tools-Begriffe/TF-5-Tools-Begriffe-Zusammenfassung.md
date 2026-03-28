## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Das Grundproblem: Computer verstehen nur Zahlen

**Computer = Binärmaschinen**: Alles (Texte, Bilder, Videos, Programme) muss als 0en und 1en gespeichert werden.

**Kodierung = Übersetzungsregel**: Wie wandeln wir Buchstaben in Zahlen um?

**Beispiel:**

- Buchstabe 'A' → Zahl 65 → Binär 01000001
- Ohne Standard: Chaos! (Computer A sagt 65='A', Computer B sagt 65='Z')

### Die 3 wichtigsten Kodierungen

#### 1. **ASCII - Der Urahn (1963)**

**Was es ist:**

- Standard für englische Zeichen
- Nutzt **7 Bits** = 2⁷ = **128 Zeichen** (0-127)
- Definiert Zuordnung: Zahl ↔ Zeichen

**Was es enthält:**

- Großbuchstaben: A-Z (65-90)
- Kleinbuchstaben: a-z (97-122)
- Ziffern: 0-9 (48-57)
- Satzzeichen: !, @, #, $, etc.
- Steuerzeichen: Newline, Tab, Backspace (unsichtbar)

**Wichtigste ASCII-Werte auswendig:**

```
'A' = 65    'a' = 97    '0' = 48
'Z' = 90    'z' = 122   '9' = 57
Space = 32  Newline = 10  Tab = 9
```

**Merksatz:** Kleinbuchstaben = Großbuchstaben + 32

- 'A' (65) + 32 = 'a' (97)
- 'B' (66) + 32 = 'b' (98)

**Limitation:** Nur Englisch! Keine ä, é, ñ, 猫, 😀

#### 2. **Unicode & UTF-8 - Die moderne Lösung**

**Unicode:**

- Universelles System mit über 149.000 Zeichen
- Jedes Zeichen = eindeutige Nummer (Codepoint)
- Beispiel: 'A' = U+0041, '猫' = U+732B, '😀' = U+1F600

**UTF-8 (die wichtigste Unicode-Kodierung):**

- **Variable Breite**: 1-4 Bytes pro Zeichen

|Zeichen-Typ|Bytes|Beispiele|
|---|---|---|
|ASCII (0-127)|1 Byte|A, B, 5, !, Space|
|Erweitert Latein|2 Bytes|ä, ö, ü, é, ñ|
|Asiatisch/Symbole|3 Bytes|猫, €, ™|
|Emojis/Selten|4 Bytes|😀, 🚀, 🎉|

**Killer-Feature: ASCII-Kompatibilität**

- ASCII-Zeichen (0-127) sind in UTF-8 **identisch**
- Alte ASCII-Dateien = gültige UTF-8-Dateien
- Sanfter Übergang ohne Breaking Changes

**Warum UTF-8 dominiert:**

1. Unterstützt ALLE Sprachen weltweit
2. 100% rückwärtskompatibel mit ASCII
3. Effizient: Englisch braucht nur 1 Byte/Zeichen
4. Web-Standard (>98% aller Webseiten)

#### 3. **Base64 - Binärdaten als Text**

**Problem:**

- E-Mail-Systeme erwarten nur Text (ASCII)
- Bilder/PDFs sind Binärdaten (enthält alle 256 Byte-Werte)
- Binärdaten könnten Steuerzeichen enthalten → Korruption!

**Lösung: Base64**

- Wandelt **beliebige Binärdaten** in **druckbare ASCII-Zeichen** um
- Nutzt nur 64 "sichere" Zeichen: `A-Z`, `a-z`, `0-9`, `+`, `/`

**Funktionsweise (vereinfacht):**

```
Input:  3 Bytes (24 Bits) Binärdaten
↓
Aufteilen: 4 × 6-Bit-Blöcke
↓
Mapping: Jeder 6-Bit-Block → ein Base64-Zeichen (0-63)
↓
Output: 4 ASCII-Zeichen
```

**Beispiel: "Man" kodieren**

```
Text:    M        a        n
ASCII:   77       97       110
Binär:   01001101 01100001 01101110  (24 Bits)

Gruppiere 6 Bits:
         010011   010110   000101   101110
Dezimal: 19       22       5        46
Base64:  T        W        F        u

Ergebnis: "TWFu"
```

**Padding-Regel:**

- Wenn Input nicht Vielfaches von 3 Bytes → mit `=` auffüllen
- Beispiel: "A" → `QQ==` (2× Padding)

**KRITISCH: Base64 ist KEINE Verschlüsselung!**

- ❌ Bietet NULL Sicherheit
- ❌ Jeder kann es dekodieren
- ✅ Nur für sichere Übertragung, nicht Geheimhaltung
- Vergleich: Wie aus Deutsch nach Englisch übersetzen (kein Geheimnis)

**Wo du Base64 siehst:**

- E-Mail-Anhänge (MIME)
- Bilder in HTML: `<img src="data:image/png;base64,iVBORw0K...">`
- JWT-Tokens (Authentifizierung)
- SSL-Zertifikate (.pem Dateien)
- API-Keys

### ASCII vs UTF-8 vs Base64: Wann was?

||ASCII|UTF-8|Base64|
|---|---|---|---|
|**Zweck**|Englische Zeichen|Alle Sprachen|Binärdaten als Text|
|**Zeichen**|128 (0-127)|149.000+|Nicht für Zeichen|
|**Bytes/Zeichen**|1|1-4|1.33× Input|
|**Enthält**|A-Z, 0-9, Basic|A-Z + ä,é,猫,😀|Nur A-Z,a-z,0-9,+,/|
|**Nutzung**|Legacy-Systeme|Moderne Texte|E-Mail, Daten-URLs|
|**Kompatibel mit**|-|ASCII (0-127)|ASCII-Output|

### Häufige Probleme & Lösungen

#### **Problem 1: Mojibake (Zeichensalat)**

```
Datei enthält: "Hällö" (UTF-8)
Gelesen als:   "HÃ¤llÃ¶" (ASCII/Latin-1)
```

**Ursache:** Falsche Kodierung beim Öffnen **Lösung:** Richtige Kodierung angeben (UTF-8 ist Standard)

#### **Problem 2: Base64 als Verschlüsselung verwechselt**

```
Geheimes Passwort: "admin123"
Base64:            "YWRtaW4xMjM="
```

**FALSCH:** "Jetzt ist es sicher!" ❌ **RICHTIG:** Jeder kann es mit `base64 -d` dekodieren!

#### **Problem 3: Binärdaten direkt senden**

```
Bild-Datei → E-Mail → Korrupt!
```

**Ursache:** E-Mail-System interpretiert Bytes als Text **Lösung:** Base64-kodieren vor dem Senden

### Windows-Tools: Schnell-Referenz

**Zeichentabelle:**

1. `Windows-Taste` → "charmap"
2. Zeichen suchen → Codepoint anzeigen
3. Kopieren → Einfügen

**PowerShell für ASCII:**

```powershell
# Zeichen → Code
[int][char]'A'      # → 65

# Code → Zeichen  
[char]65            # → A

# String → Bytes
[System.Text.Encoding]::UTF8.GetBytes("Hello")
```

**Python (wenn installiert):**

```python
# Starten: python in CMD
ord('A')                # ASCII-Wert
chr(65)                 # Zeichen
'Hello'.encode('utf-8') # UTF-8 Bytes

# Base64
import base64
base64.b64encode(b'Hello World!')
```

### Praktische Übungen

**Übung 1: ASCII erkunden**

```
Finde den ASCII-Wert für:
1. Dein Initial (z.B. 'J')
2. Das $-Symbol
3. Die Ziffer 0 (nicht Null-Byte!)

Rechne: 'J' (74) + 32 = ? → 'j' (106)
```

**Übung 2: Base64 dekodieren**

```
Gegeben: "SGVsbG8gV29ybGQh"
Tool: https://www.base64decode.org/
Ergebnis: ?
```

**Übung 3: Mojibake verstehen**

```
Text: "café"
UTF-8 Hex: 63 61 66 C3 A9
Als ASCII: c a f ? ?  (� �)
```

### Die 5 wichtigsten Erkenntnisse

1. **ASCII ist tot, lang lebe UTF-8!**
    
    - ASCII nur für Legacy
    - UTF-8 ist der moderne Standard
    - Immer UTF-8 wählen bei neuen Projekten
2. **Base64 ≠ Verschlüsselung**
    
    - Nur Kodierung, keine Sicherheit
    - In Cybersecurity: Angreifer dekodieren Base64 sofort
    - Niemals Geheimnisse nur mit Base64 "schützen"
3. **Kodierungs-Mismatch = Zeichensalat**
    
    - Sender: UTF-8, Empfänger: ASCII → Mojibake
    - Immer gleiche Kodierung abstimmen
    - UTF-8 ist sicherste Wahl (universell)
4. **1 Hex-Ziffer = 1 Zeichen in Base64? NEIN!**
    
    - Base64: 3 Bytes → 4 Zeichen
    - Vergrößerung um ~33%
    - Hex: 1 Byte → 2 Zeichen (Vergrößerung 100%)
5. **Binär → Text: Nutze Base64**
    
    - Bilder, PDFs, Archive in E-Mail
    - Daten in JSON/XML
    - API-Kommunikation

### Kernbotschaft

**Die Kodierungs-Pyramide:**

```
     Anwendung
         ↓
    UTF-8 (Text)
         ↓
   Base64 (Transport)
         ↓
    Binär (0 & 1)
         ↓
     Hardware
```

**Eselsbrücken:**

- **ASCII** = Altes System Comes from International Institute (nur Englisch)
- **UTF-8** = Universal Text Format - 8 bits (aber variabel!)
- **Base64** = Basis mit 64 Zeichen (A-Z, a-z, 0-9, +, /)

**Praktischer Tipp für Cybersecurity:**

- Base64 in verdächtigen Skripten? → Sofort dekodieren!
- Oft verstecken Angreifer Malware in Base64
- Tools: `base64 -d` (Linux/Mac) oder CyberChef (Web)

---

## Verwendete Tools, Technische Fachbegriffe und Wichtige Vokabeln

|Begriff|Bedeutung|
|---|---|
|**Verwendete Tools (macOS → Windows)**||
|`man ascii` (Terminal)|ASCII-Tabelle im Terminal anzeigen (Windows CMD: nicht verfügbar, nutze Online-ASCII-Tabelle oder PowerShell: `[char]65` zeigt 'A')|
|Terminal / Command Prompt|Kommandozeile zum Anzeigen von Zeichentabellen (Windows: CMD oder PowerShell)|
|Online Base64 Encoder/Decoder|Web-Tools zur Base64-Kodierung/Dekodierung (plattformunabhängig)|
|Text Editor (Plain Text Mode)|Einfacher Texteditor zur Anzeige von Kodierungen (Windows: Notepad, Notepad++)|
|Character Map|Zeichentabelle-Tool (Windows: `charmap.exe` über Start-Suche)|
|Python|Programmiersprache für Kodierungs-Experimente (`encode()`, `decode()`) - identisch auf Windows|
|**Grundkonzepte**||
|Data Encoding|Datenkodierung - Umwandlung von Information in ein bestimmtes Format (meist binär)|
|Decoding|Dekodierung - Rückumwandlung in lesbare/nutzbare Form|
|Character Encoding|Zeichenkodierung - Zuordnung von Zeichen zu Binärzahlen|
|Binary Data|Binärdaten - Rohdaten in 0en und 1en (z.B. Bilder, Programme)|
|Text Data|Textdaten - menschenlesbare Zeichen und Symbole|
|Bit|Binary Digit - kleinste Dateneinheit (0 oder 1)|
|Byte|8 Bits zusammen - Standard-Speichereinheit|
|Pattern|Muster - spezifische Bit-Anordnung zur Darstellung von Information|
|**ASCII (American Standard Code for Information Interchange)**||
|ASCII|Ältester Standard zur Zeichenkodierung (7 Bit = 128 Zeichen)|
|7-bit Encoding|7-Bit-Kodierung - 2⁷ = 128 verschiedene Zeichen möglich|
|ASCII Table|ASCII-Tabelle - Zuordnung von Zahlen (0-127) zu Zeichen|
|Code Point|Zahlenwert eines Zeichens in einer Kodierung|
|Control Characters|Steuerzeichen - nicht sichtbar, steuern Textverarbeitung (Newline, Tab, Backspace)|
|Printable Characters|Druckbare Zeichen - sichtbare Zeichen (Buchstaben, Zahlen, Symbole)|
|Uppercase Letters|Großbuchstaben A-Z (ASCII 65-90)|
|Lowercase Letters|Kleinbuchstaben a-z (ASCII 97-122)|
|Digits|Ziffern 0-9 (ASCII 48-57)|
|Punctuation|Satzzeichen und Symbole (!, @, #, $, etc.)|
|**ASCII-Beispiele**||
|'A' = 65 = 0x41 = 01000001|Großbuchstabe A|
|'a' = 97 = 0x61 = 01100001|Kleinbuchstabe a|
|'0' = 48 = 0x30 = 00110000|Ziffer Null (nicht Null-Byte!)|
|Space = 32 = 0x20 = 00100000|Leerzeichen|
|'!' = 33 = 0x21 = 00100001|Ausrufezeichen|
|Newline (LF) = 10 = 0x0A|Zeilenumbruch (Line Feed)|
|Tab = 9 = 0x09|Tabulatorzeichen|
|**ASCII-Limitierungen**||
|English-Only|Nur englisches Alphabet - keine Umlaute, Akzente, andere Alphabete|
|No Accents|Keine Akzentzeichen (é, à, ñ, etc.)|
|No Umlauts|Keine deutschen Umlaute (ä, ö, ü, ß)|
|No International Characters|Keine internationalen Zeichen (Kyrillisch, Griechisch, Chinesisch, etc.)|
|**Unicode & UTF-8**||
|Unicode|Universeller Zeichensatz - über 149.000 Zeichen aus allen Sprachen + Emojis|
|Code Point|Unicode-Codepoint - eindeutige Nummer für jedes Zeichen (z.B. U+0041 für 'A')|
|Character Set|Zeichensatz - Sammlung aller definierten Zeichen|
|UTF-8|Unicode Transformation Format 8-bit - häufigste Unicode-Kodierung|
|Variable-Width Encoding|Variable Breite - nutzt 1-4 Bytes pro Zeichen je nach Bedarf|
|Backward Compatible|Rückwärtskompatibel - ASCII-Zeichen (0-127) sind identisch in UTF-8|
|Multi-Byte Character|Mehrbyte-Zeichen - Zeichen außerhalb ASCII benötigen 2-4 Bytes|
|**UTF-8 Byte-Struktur**||
|1 Byte (ASCII range)|ASCII-kompatibel: 0-127 (0xxxxxxx)|
|2 Bytes|Erweiterte lateinische, griechische, kyrillische Zeichen (110xxxxx 10xxxxxx)|
|3 Bytes|Asiatische Zeichen, Symbole (1110xxxx 10xxxxxx 10xxxxxx)|
|4 Bytes|Seltene Zeichen, Emojis (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)|
|**Unicode-Beispiele**||
|'€' (Euro)|U+20AC - 3 Bytes in UTF-8|
|'ä' (Umlaut)|U+00E4 - 2 Bytes in UTF-8|
|'猫' (Katze, Chinesisch)|U+732B - 3 Bytes in UTF-8|
|'😀' (Emoji)|U+1F600 - 4 Bytes in UTF-8|
|**Base64 Encoding**||
|Base64|Kodierung von Binärdaten als druckbare ASCII-Zeichen (64 verschiedene)|
|Binary-to-Text Encoding|Binär-zu-Text-Kodierung - macht Binärdaten text-sicher|
|6-bit Chunks|6-Bit-Blöcke - Base64 arbeitet mit 6-Bit-Gruppen|
|Padding|Auffüllung - `=` Zeichen am Ende bei unvollständigen Gruppen|
|Base64 Alphabet|64 Zeichen: A-Z, a-z, 0-9, +, /|
|**Base64-Struktur**||
|Input: 3 Bytes (24 Bits)|Eingabe wird in 3-Byte-Blöcken verarbeitet|
|Output: 4 Characters|Ausgabe sind 4 druckbare Zeichen|
|Expansion|Vergrößerung um ~33% (3 Bytes → 4 Zeichen)|
|Reversible|Umkehrbar - einfach dekodierbar|
|NOT Encryption|KEINE Verschlüsselung - bietet keine Sicherheit!|
|**Base64 Padding-Regeln**||
|No padding|Eingabe ist Vielfaches von 3 Bytes → kein `=`|
|One `=`|2 Bytes übrig → ein `=` am Ende|
|Two `==`|1 Byte übrig → zwei `==` am Ende|
|**Anwendungsfälle**||
|Email Attachments|E-Mail-Anhänge - Base64 für binäre Dateien in E-Mails (MIME)|
|Data URLs|Eingebettete Bilder in HTML/CSS (`data:image/png;base64,...`)|
|Authentication Tokens|API-Keys, JWT-Tokens oft in Base64|
|Binary in JSON/XML|Binärdaten in text-basierten Formaten|
|Certificate Files|SSL/TLS-Zertifikate (.pem, .crt Dateien)|
|**Encoding vs Encryption**||
|Encoding|Kodierung - Format-Umwandlung, kein Geheimnis (umkehrbar für jeden)|
|Encryption|Verschlüsselung - Geheimhaltung, benötigt Schlüssel zum Entschlüsseln|
|Obfuscation|Verschleierung - schwerer lesbar machen, aber nicht sicher|
|**Probleme & Fehler**||
|Mojibake|Zeichensalat - falsche Dekodierung (z.B. UTF-8 als ASCII gelesen)|
|Character Corruption|Zeichenverfälschung durch falsche Kodierung|
|Data Corruption|Datenverfälschung - Binärdaten durch Text-System beschädigt|
|Encoding Mismatch|Kodierungs-Konflikt - Sender und Empfänger nutzen verschiedene Kodierungen|
|**Wichtige Befehle/Syntax**||
|Python: `str.encode('utf-8')`|String zu Bytes mit UTF-8 kodieren|
|Python: `bytes.decode('utf-8')`|Bytes zu String mit UTF-8 dekodieren|
|Python: `base64.b64encode()`|Base64-Kodierung|
|Python: `base64.b64decode()`|Base64-Dekodierung|
|Python: `ord('A')`|Gibt ASCII/Unicode-Codepoint zurück (65)|
|Python: `chr(65)`|Wandelt Codepoint zu Zeichen ('A')|

---

## Windows 11: Zeichenkodierung erkunden

|Funktion|Anleitung|
|---|---|
|**Zeichentabelle öffnen**|`Windows-Taste` → "charmap" eingeben → Enter (zeigt alle Unicode-Zeichen)|
|**ASCII-Werte anzeigen**|In Zeichentabelle: Zeichen auswählen → unten rechts steht "U+0041" (Hex-Codepoint)|
|**PowerShell: Zeichen → Code**|`[int][char]'A'` gibt `65` zurück|
|**PowerShell: Code → Zeichen**|`[char]65` gibt `A` zurück|
|**Notepad Kodierung**|Speichern unter → Dropdown "Kodierung": UTF-8, ANSI, Unicode (UTF-16)|
|**Python für Kodierung**|Python installieren → in CMD/PowerShell: `python`|

**Python-Beispiele (Windows CMD/PowerShell):**

```python
# Python starten
python

# ASCII/Unicode-Werte
ord('A')           # → 65
chr(65)            # → 'A'
ord('€')           # → 8364 (U+20AC)

# UTF-8 Kodierung
'Hello'.encode('utf-8')      # → b'Hello'
'Hällö'.encode('utf-8')      # → b'H\xc3\xa4ll\xc3\xb6'

# Base64
import base64
base64.b64encode(b'Hello World!')  # → b'SGVsbG8gV29ybGQh'
base64.b64decode(b'SGVsbG8gV29ybGQh')  # → b'Hello World!'
```