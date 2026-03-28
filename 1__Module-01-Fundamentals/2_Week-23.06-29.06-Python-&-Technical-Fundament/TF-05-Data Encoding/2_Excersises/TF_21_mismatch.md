# 🖥️ Mismatch Mayhem - Encoding Errors

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 26.06.2025

---

## Aufgabe

**Ziel:** Character Encoding Mismatches demonstrieren und Fehlerbehandlung mit Python implementieren

---

## Lösung

### Umgebung
```
Sprache: Python 3.x
Konzept: String encoding/decoding, Exception Handling
```

### Durchführung

**Python Script: encoding_mismatch.py**

```python
# Schritt 1: Test String definieren
test_string = "München Price: 10€"
print(f"Original String: {test_string}")
print()

# Schritt 2: Korrekt zu UTF-8 Bytes encodieren
utf8_bytes = test_string.encode('utf-8')
print(f"UTF-8 Encoded Bytes: {utf8_bytes}")
print(f"Hex Representation: {utf8_bytes.hex()}")
print()

# Schritt 3: Falsche Dekodierung mit ASCII (try-except)
print("Attempting to decode UTF-8 bytes as ASCII...")
try:
    # Versuch mit falschem Codec
    wrong_decode = utf8_bytes.decode('ascii')
    print(f"Decoded String: {wrong_decode}")
    
except UnicodeDecodeError as e:
    print(f"❌ Decoding FAILED!")
    print(f"Error: {e}")
    print(f"Reason: ASCII codec cannot decode bytes outside 0x00-0x7F range.")
    print()

# Schritt 4: Korrekte Dekodierung mit UTF-8
print("Attempting to decode UTF-8 bytes as UTF-8...")
correct_decode = utf8_bytes.decode('utf-8')
print(f"✅ Decoded String: {correct_decode}")
print(f"Match with original: {correct_decode == test_string}")
print()

# Schritt 5: Erklärung
print("=" * 60)
print("EXPLANATION: Why UnicodeDecodeError occurred")
print("=" * 60)
print("""
When we encode 'München Price: 10€' to UTF-8, characters like
'ü' and '€' are represented using multiple bytes with values > 127.

Example breakdown:
- 'ü' → UTF-8: 0xC3 0xBC (2 bytes)
- '€' → UTF-8: 0xE2 0x82 0xAC (3 bytes)

The ASCII codec only recognizes single-byte values 0-127 (0x00-0x7F).
When it encounters byte 0xC3 (195 in decimal), which is > 127,
it raises a UnicodeDecodeError because this byte is invalid in ASCII.

Fundamental Conflict:
- ASCII: 7-bit encoding, supports only 128 characters (0-127)
- UTF-8: Variable-length encoding, uses bytes 128-255 for multi-byte
  sequences to represent characters beyond basic ASCII

Solution: Always decode with the same encoding that was used to encode!
""")
```

**Ausführung:**
```bash
python3 encoding_mismatch.py
```

---

## Ergebnisse

**Console Output:**
```
Original String: München Price: 10€

UTF-8 Encoded Bytes: b'M\xc3\xbcnchen Price: 10\xe2\x82\xac'
Hex Representation: 4dc3bc6e6368656e2050726963653a2031309e282ac

Attempting to decode UTF-8 bytes as ASCII...
❌ Decoding FAILED!
Error: 'ascii' codec can't decode byte 0xc3 in position 1: ordinal not in range(128)
Reason: ASCII codec cannot decode bytes outside 0x00-0x7F range.

Attempting to decode UTF-8 bytes as UTF-8...
✅ Decoded String: München Price: 10€
Match with original: True
```

---

## Notizen

- **Gelernt:** Encoding Mismatches, Try-Except Exception Handling, UTF-8 vs ASCII
- **UnicodeDecodeError Ursachen:**
  1. ASCII ist 7-bit Encoding (nur Werte 0-127 gültig)
  2. UTF-8 Multi-Byte Sequenzen verwenden Bytes ≥ 128 (0x80-0xFF)
  3. ASCII-Decoder stoppt bei Byte > 127 mit Fehler
- **Beispiel-Breakdown:**
  - 'M' → ASCII/UTF-8: `0x4D` ✅ (beide gleich)
  - 'ü' → UTF-8: `0xC3 0xBC` ❌ (ASCII kann 0xC3 nicht decodieren)
  - '€' → UTF-8: `0xE2 0x82 0xAC` ❌ (drei Bytes alle > 127)
- **Best Practice:** Immer mit gleichem Encoding en-/decodieren
- **Error Handling:** `try-except UnicodeDecodeError` für robuste Programme
- **Common Mistake:** "Mojibake" (文字化け) = falsche Encoding-Interpretation
  - Beispiel: UTF-8 Bytes als Latin-1 gelesen → "MÃ¼nchen" statt "München"
- **Python Bytes:** Prefix `b'...'` zeigt Bytes-Objekt
- **Hex Method:** `.hex()` konvertiert Bytes zu Hex-String