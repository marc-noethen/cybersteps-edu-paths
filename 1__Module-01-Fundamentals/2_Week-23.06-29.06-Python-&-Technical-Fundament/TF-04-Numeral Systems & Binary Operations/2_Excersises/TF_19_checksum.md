# 🖥️ Broken Record - XOR Checksum Validation

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 25.06.2025

---

## Aufgabe

**Ziel:** Multi-Byte Datenrecords analysieren, XOR-Checksummen berechnen und validieren, Python-Implementation erstellen

**Aufgabenstellung:**
- Record-Struktur: `[Record ID] [Data Bytes...] [Checksum]`
- Checksum-Regel: XOR aller Data Bytes (ohne Record ID)
- **Record A:** `1A 01 F0 AC 33 55 9B DD`
- **Record B:** `1B 22 4D 6F 81 B9 07 F5`
- Tasks: Validieren, korrekte Checksummen berechnen, Python-Funktion implementieren

---

## Lösung

### Umgebung
```
Methode: Manuelle XOR-Berechnung + Python Implementation
Tools: Hex-Binary Konvertierung, XOR-Operation, Python 3.x
```

### Durchführung

---

## Record A: Manual Validation

**Record A:** `1A 01 F0 AC 33 55 9B DD`
- Record ID: `1A` (nicht in Checksum)
- Data Bytes: `01 F0 AC 33 55 9B`
- Provided Checksum: `DD`

**Schritt 1:** Konvertierung zu Binary
```
01 = 00000001
F0 = 11110000
AC = 10101100
33 = 00110011
55 = 01010101
9B = 10011011
```

**Schritt 2:** XOR aller Data Bytes
```
     00000001  (01)
XOR  11110000  (F0)
    ---------
     11110001

XOR  10101100  (AC)
    ---------
     01011101

XOR  00110011  (33)
    ---------
     01101110

XOR  01010101  (55)
    ---------
     00111011

XOR  10011011  (9B)
    ---------
     10100000 = 0xA0
```

**Ergebnis:** Berechnete Checksum = `0xA0`

**Validation:** Provided `DD` ≠ Calculated `A0` → **INVALID**

**Correct Checksum:** `0xA0`

---

## Record B: Manual Validation

**Record B:** `1B 22 4D 6F 81 B9 07 F5`
- Record ID: `1B` (nicht in Checksum)
- Data Bytes: `22 4D 6F 81 B9 07`
- Provided Checksum: `F5`

**Schritt 1:** Konvertierung zu Binary
```
22 = 00100010
4D = 01001101
6F = 01101111
81 = 10000001
B9 = 10111001
07 = 00000111
```

**Schritt 2:** XOR aller Data Bytes
```
     00100010  (22)
XOR  01001101  (4D)
    ---------
     01101111

XOR  01101111  (6F)
    ---------
     00000000

XOR  10000001  (81)
    ---------
     10000001

XOR  10111001  (B9)
    ---------
     00111000

XOR  00000111  (07)
    ---------
     00111111 = 0x3F
```

**Ergebnis:** Berechnete Checksum = `0x3F`

**Validation:** Provided `F5` ≠ Calculated `3F` → **INVALID**

**Correct Checksum:** `0x3F`

---

## Part 3: Python Implementation

```python
def calculate_xor_checksum(data_bytes):
    """
    Berechnet XOR-Checksum für eine Liste von Datenbytes.
    
    Args:
        data_bytes: Liste von Integers (0-255), z.B. [0x01, 0xF0, 0xAC]
    
    Returns:
        XOR-Checksum als Integer (0-255)
    """
    # Startwert für XOR ist 0 (neutral element)
    checksum = 0
    
    # XOR alle Bytes nacheinander
    for byte in data_bytes:
        checksum ^= byte
    
    return checksum


# Tests mit Record A
record_a_data = [0x01, 0xF0, 0xAC, 0x33, 0x55, 0x9B]
result_a = calculate_xor_checksum(record_a_data)
print(f"Record A Checksum: 0x{result_a:02X}")  # 0xA0

# Tests mit Record B
record_b_data = [0x22, 0x4D, 0x6F, 0x81, 0xB9, 0x07]
result_b = calculate_xor_checksum(record_b_data)
print(f"Record B Checksum: 0x{result_b:02X}")  # 0x3F

# Test mit Beispiel aus Aufgabe
test_data = [0x3F, 0x8A, 0x1C]
result_test = calculate_xor_checksum(test_data)
print(f"Test Checksum: 0x{result_test:02X}")  # 0xA9
print(f"Test Checksum (decimal): {result_test}")  # 169
```

---

## Ergebnisse

### Manual Validation

| Record | Data Bytes | Provided Checksum | Calculated Checksum | Status | Correct Checksum |
|--------|------------|-------------------|---------------------|--------|------------------|
| **A** | `01 F0 AC 33 55 9B` | `DD` | `A0` | ❌ **Invalid** | **0xA0** |
| **B** | `22 4D 6F 81 B9 07` | `F5` | `3F` | ❌ **Invalid** | **0x3F** |

### Python Implementation

```python
def calculate_xor_checksum(data_bytes):
    checksum = 0
    for byte in data_bytes:
        checksum ^= byte
    return checksum
```

**Verification:**
- Record A: `calculate_xor_checksum([0x01, 0xF0, 0xAC, 0x33, 0x55, 0x9B])` → `0xA0` ✅
- Record B: `calculate_xor_checksum([0x22, 0x4D, 0x6F, 0x81, 0xB9, 0x07])` → `0x3F` ✅
- Example: `calculate_xor_checksum([0x3F, 0x8A, 0x1C])` → `0xA9` (169 decimal) ✅

---

## Notizen

- **Gelernt:** XOR-Checksum für Fehlerkennung, mehrstufige XOR-Berechnung
- **XOR-Eigenschaften:**
  - Neutral Element: `A XOR 0 = A`
  - Kommutativ: `A XOR B = B XOR A`
  - Assoziativ: `(A XOR B) XOR C = A XOR (B XOR C)`
- **Checksum-Zweck:** Erkennung von Datenkorruption, nicht für Sicherheit (kein Hash!)
- **Limitation:** XOR-Checksum ist schwach (collisions möglich), besser: CRC, SHA
- **Record-Struktur:** ID nicht in Checksum → nur Nutzdaten schützen
- **Python-Trick:** `^=` Operator für akkumulierende XOR-Operation
- **Alternative:** `from functools import reduce; reduce(lambda a,b: a^b, data_bytes, 0)`
- **Format-String:** `f"0x{value:02X}"` → 2-stelliger Hex mit führender 0