# 🖥️ The Payload - Base64 & Binary Data Analysis

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 26.06.2025

---

## Aufgabe

**Ziel:** Base64-codierten String decodieren, binäre Datenstruktur interpretieren und Checksum verifizieren

---

## Lösung

### Umgebung
```
Sprache: Python 3.x
Module: base64, struct
Konzept: Base64 Decoding, Binary Data Parsing, Checksum Verification
```

### Durchführung

**Gegeben:** Base64 String `ALsGSGVsbG8hAtY=`

**Datenstruktur (Big-Endian):**
- Payload Type: 16-bit unsigned int (2 bytes)
- Payload Length: 8-bit unsigned int (1 byte)
- Payload Data: ASCII string (variable Länge)
- Checksum: 16-bit unsigned int (2 bytes)

---

**Schritt 1: Base64 Decoding**

```python
import base64
import struct

# Base64 String
base64_string = "ALsGSGVsbG8hAtY="

# Decodieren
decoded_bytes = base64.decode(base64_string.encode('ascii'))

print(f"Base64 Input:  {base64_string}")
print(f"Decoded Bytes: {decoded_bytes.hex(' ').upper()}")
print(f"Decoded Bytes: {decoded_bytes}")
print(f"Total Length:  {len(decoded_bytes)} bytes")
print()
```

**Ausgabe:**
```
Base64 Input:  ALsGSGVsbG8hAtY=
Decoded Bytes: 00 BB 06 48 65 6C 6C 6F 21 02 D6
Decoded Bytes: b'\x00\xbb\x06Hello!\x02\xd6'
Total Length:  11 bytes
```

---

**Schritt 2: Binary Data Unpacking**

**Hex Breakdown:**
```
00 BB 06 48 65 6C 6C 6F 21 02 D6
│────│ │  │──────────────│ │────│
│    │ │  │              │ └────┴─ Checksum (2 bytes)
│    │ │  └──────────────┴──────── Payload Data (6 bytes)
│    │ └────────────────────────── Payload Length (1 byte)
└────┴──────────────────────────── Payload Type (2 bytes)
```

**Python Code:**

```python
# Payload Type: Bytes 0-1 (Big-Endian)
payload_type_bytes = decoded_bytes[0:2]
payload_type = struct.unpack('>H', payload_type_bytes)[0]
print(f"Payload Type (bytes): {payload_type_bytes.hex(' ').upper()}")
print(f"Payload Type (value): {payload_type}")
print()

# Payload Length: Byte 2
payload_length = decoded_bytes[2]
print(f"Payload Length (byte): {hex(payload_length).upper()}")
print(f"Payload Length (value): {payload_length}")
print()

# Payload Data: Bytes 3 bis (3 + payload_length)
start_idx = 3
end_idx = 3 + payload_length
payload_data_bytes = decoded_bytes[start_idx:end_idx]
payload_data = payload_data_bytes.decode('ascii')
print(f"Payload Data (bytes): {payload_data_bytes.hex(' ').upper()}")
print(f"Payload Data (string): '{payload_data}'")
print()

# Checksum: Letzte 2 Bytes (Big-Endian)
checksum_start = end_idx
checksum_bytes = decoded_bytes[checksum_start:checksum_start+2]
checksum_provided = struct.unpack('>H', checksum_bytes)[0]
print(f"Checksum (bytes): {checksum_bytes.hex(' ').upper()}")
print(f"Checksum (provided): {checksum_provided}")
print()
```

**Ausgabe:**
```
Payload Type (bytes): 00 BB
Payload Type (value): 187

Payload Length (byte): 0X6
Payload Length (value): 6

Payload Data (bytes): 48 65 6C 6C 6F 21
Payload Data (string): 'Hello!'

Checksum (bytes): 02 D6
Checksum (provided): 726
```

---

**Schritt 3: Checksum Verification**

**Checksum-Regel:** Summe aller Bytes von Payload Type + Payload Length + Payload Data

```python
# Bytes für Checksum-Berechnung extrahieren
checksum_fields_bytes = decoded_bytes[0:end_idx]
print(f"Bytes for checksum calculation: {checksum_fields_bytes.hex(' ').upper()}")
print(f"Individual bytes: {[f'{b:02X}' for b in checksum_fields_bytes]}")
print()

# Checksum berechnen (Summe aller Byte-Werte)
calculated_checksum = sum(checksum_fields_bytes)

print(f"Checksum Calculation:")
print(f"  Payload Type bytes:   {payload_type_bytes.hex(' ').upper()} → {sum(payload_type_bytes)}")
print(f"  Payload Length byte:  {hex(payload_length).upper()} → {payload_length}")
print(f"  Payload Data bytes:   {payload_data_bytes.hex(' ').upper()} → {sum(payload_data_bytes)}")
print()
print(f"  Total Sum: {sum(payload_type_bytes)} + {payload_length} + {sum(payload_data_bytes)}")
print(f"           = {calculated_checksum}")
print()

# Vergleich
print("=" * 60)
print("CHECKSUM VERIFICATION")
print("=" * 60)
print(f"Calculated Checksum: {calculated_checksum}")
print(f"Provided Checksum:   {checksum_provided}")
print(f"Match: {calculated_checksum == checksum_provided}")
if calculated_checksum == checksum_provided:
    print("✅ Checksum is VALID!")
else:
    print("❌ Checksum is INVALID!")
```

**Detaillierte Berechnung:**
```
Payload Type:   00 BB → 0 + 187 = 187
Payload Length: 06    → 6
Payload Data:   48 65 6C 6C 6F 21
                → 72 + 101 + 108 + 108 + 111 + 33 = 533

Total: 187 + 6 + 533 = 726
```

**Ausgabe:**
```
Checksum Calculation:
  Payload Type bytes:   00 BB → 187
  Payload Length byte:  0X6 → 6
  Payload Data bytes:   48 65 6C 6C 6F 21 → 533

  Total Sum: 187 + 6 + 533
           = 726

============================================================
CHECKSUM VERIFICATION
============================================================
Calculated Checksum: 726
Provided Checksum:   726
Match: True
✅ Checksum is VALID!
```

---

## Ergebnisse

| Feld | Bytes | Wert |
|------|-------|------|
| **Payload Type** | `00 BB` | **187** (decimal) |
| **Payload Length** | `06` | **6** (decimal) |
| **Payload Data** | `48 65 6C 6C 6F 21` | **"Hello!"** |
| **Checksum (provided)** | `02 D6` | **726** (decimal) |
| **Checksum (calculated)** | - | **726** (decimal) |
| **Checksums Match?** | - | ✅ **YES** |

**Zusammenfassung:**
- Base64 decodiert zu: `00 BB 06 48 65 6C 6C 6F 21 02 D6`
- Payload Type: 187
- Payload Length: 6
- Payload Data: "Hello!"
- Checksum: 726 (valid ✅)

---

## Notizen

- **Gelernt:** Base64 Decoding, Binary Protocol Parsing, Checksum Verification
- **Base64:** Binärdaten → Text (6 bits → 1 ASCII Zeichen)
  - Padding: `=` für Ausrichtung auf 4-Zeichen-Blöcke
  - Decode: `base64.b64decode()` oder `.decode()`
- **Binary Parsing:** `struct.unpack()` für strukturierte Daten
- **Checksum-Arten:**
  - **Simple Sum:** Summe aller Bytes (wie hier)
  - **XOR:** XOR aller Bytes
  - **CRC:** Cyclic Redundancy Check (robuster)
  - **Hash:** SHA, MD5 (kryptographisch)
- **Big-Endian in Netzwerk-Protokollen:** Standard (RFC)
- **Payload Structure:** Typ-Länge-Wert (TLV) Pattern
  - Type: Identifiziert Datentyp
  - Length: Länge des Datenfeldes
  - Value: Eigentliche Daten
- **Checksum-Zweck:** Integritätsprüfung (nicht Sicherheit!)
- **Python Tipps:**
  - `sum(bytes)` summiert alle Byte-Werte
  - `.decode('ascii')` für ASCII-Strings aus Bytes
  - `struct.unpack('>H', ...)` für 16-bit Big-Endian unsigned int