# 🖥️ Encoding Essentials - ASCII, UTF-8 & Base64

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 26.06.2025

---

## Aufgabe

**Ziel:** ASCII/UTF-8 Representation und Base64 Encoding/Decoding mit Standard-Tools praktizieren

---

## Lösung

### Umgebung
```
OS: macOS / Ubuntu
Shell: zsh / bash
Tools: echo, xxd, base64
```

### Durchführung

**Schritt 1:** ASCII Decimal Value für 'A'
```bash
# ASCII Tabelle anzeigen
man ascii

# Oder direkter Weg
printf "%d\n" "'A"
```
**Ausgabe:** `65`

**Antwort:** Der ASCII decimal value für 'A' ist **65**

---

**Schritt 2:** UTF-8 Bytes für Euro-Symbol '€'
```bash
# Euro-Symbol in Hex-Bytes anzeigen
echo -n '€' | xxd -p
```
**Ausgabe:** `e282ac`

**Analyse:**
- Hex Bytes: `E2 82 AC`
- Anzahl Bytes: **3 Bytes**

**Warum kann 7-bit ASCII '€' nicht darstellen?**
- Standard ASCII verwendet nur 7 Bits (0-127 decimal, 0x00-0x7F hex)
- Das Euro-Symbol € hat den Unicode Codepoint U+20AC
- U+20AC liegt weit außerhalb des ASCII-Bereichs (20AC hex = 8364 decimal)
- UTF-8 benötigt 3 Bytes zur Codierung: `11100010 10000010 10101100`

---

**Schritt 3:** Base64 Encoding
```bash
# String "Cyber" encodieren
echo -n "Cyber" | base64
```
**Ausgabe:** `Q3liZXI=`

```bash
# String "Encoding is fun!" encodieren
echo -n "Encoding is fun!" | base64
```
**Ausgabe:** `RW5jb2RpbmcgaXMgZnVuIQ==`

---

**Schritt 4:** Base64 Decoding
```bash
# Base64 String dekodieren
echo "RGF0YSBFbmNvZGluZyBSb2NrcyE=" | base64 -d
```
**Ausgabe:** `Data Encoding Rocks!`

---

## Ergebnisse

| Frage | Antwort |
|-------|---------|
| ASCII decimal für 'A' | `65` |
| UTF-8 Hex Bytes für '€' | `E2 82 AC` |
| Anzahl Bytes für '€' | `3 Bytes` |
| Warum kein ASCII für '€'? | ASCII ist 7-bit (0-127), € liegt bei Unicode U+20AC (8364 decimal) - außerhalb ASCII-Bereich |
| Base64 von "Cyber" | `Q3liZXI=` |
| Base64 von "Encoding is fun!" | `RW5jb2RpbmcgaXMgZnVuIQ==` |
| Decoded "RGF0YSBFbmNvZGluZyBSb2NrcyE=" | `Data Encoding Rocks!` |

---

## Notizen

- **Gelernt:** ASCII vs UTF-8, Multi-Byte Encodings, Base64 Encoding/Decoding
- **ASCII:** 7-bit (128 Zeichen: 0-127), primär englische Zeichen
- **UTF-8:** Variable-Length Encoding (1-4 Bytes)
  - 1 Byte: ASCII-kompatibel (0x00-0x7F)
  - 2 Bytes: Latin, Griechisch, Kyrillisch
  - 3 Bytes: € und die meisten anderen Zeichen
  - 4 Bytes: Emojis, seltene Zeichen
- **Base64:** Binärdaten in ASCII-Text umwandeln (6 Bits → 1 ASCII-Zeichen)
  - Alphabet: A-Z, a-z, 0-9, +, /
  - Padding: `=` für Ausrichtung auf 4-Zeichen-Blöcke
  - Zweck: Sichere Übertragung von Binärdaten über Text-Protokolle
- **xxd:** Hex-Dump Tool, `-p` = plain hex output
- **echo -n:** `-n` verhindert newline am Ende