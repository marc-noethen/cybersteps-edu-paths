# 🖥️ Base(ic) Training - Number System Conversions

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 25.06.2025

---

## Aufgabe

**Ziel:** Grundlegende Zahlensystem-Konvertierungen und binäre Operationen demonstrieren

**Aufgabenstellung:**
1. Decimal 99 → 8-bit Binary
2. Hexadecimal 0xE4 → Decimal
3. Binary 10100101 → Hexadecimal
4. Binary Addition: 11010011 + 01011101
5. Bitwise AND: 11110000 AND 10101010

---

## Lösung

### Umgebung
```
Methode: Manuelle Berechnung / Python (optional zur Verifikation)
Tools: Rechner, Konvertierungstabellen
```

### Durchführung

**Aufgabe 1:** Decimal 99 → 8-bit Binary

```
Methode: Wiederholte Division durch 2
99 ÷ 2 = 49 Rest 1  (LSB)
49 ÷ 2 = 24 Rest 1
24 ÷ 2 = 12 Rest 0
12 ÷ 2 = 6  Rest 0
6  ÷ 2 = 3  Rest 0
3  ÷ 2 = 1  Rest 1
1  ÷ 2 = 0  Rest 1  (MSB)

Von unten nach oben lesen: 1100011
Mit führender 0 für 8-bit: 01100011
```
**Ergebnis:** `01100011`

---

**Aufgabe 2:** Hexadecimal 0xE4 → Decimal

```
Methode: Positionswertmethode
0xE4 = E × 16¹ + 4 × 16⁰
     = 14 × 16 + 4 × 1
     = 224 + 4
     = 228
```
**Ergebnis:** `228`

---

**Aufgabe 3:** Binary 10100101 → Hexadecimal

```
Methode: Gruppierung in 4-bit Nibbles
10100101 → 1010 | 0101
           
1010 (binary) = 10 (decimal) = A (hex)
0101 (binary) = 5  (decimal) = 5 (hex)

Zusammen: A5
```
**Ergebnis:** `0xA5`

---

**Aufgabe 4:** Binary Addition: 11010011 + 01011101

```
Methode: Spaltenweise Addition mit Übertrag

    1 1 1 1 1     (Überträge)
    1 1 0 1 0 0 1 1
  + 0 1 0 1 1 1 0 1
  -------------------
  1 0 0 1 1 0 0 0 0

Schritt für Schritt:
Position 0: 1 + 1 = 10₂ → 0, Übertrag 1
Position 1: 1 + 0 + 1 = 10₂ → 0, Übertrag 1
Position 2: 0 + 1 + 1 = 10₂ → 0, Übertrag 1
Position 3: 0 + 1 + 1 = 10₂ → 0, Übertrag 1
Position 4: 1 + 1 + 1 = 11₂ → 1, Übertrag 1
Position 5: 1 + 0 + 1 = 10₂ → 0, Übertrag 1
Position 6: 1 + 1 + 1 = 11₂ → 1, Übertrag 1
Position 7: 0 + 0 + 1 = 1₂ → 1, Übertrag 0
```
**Ergebnis:** `100110000` (9-bit) oder `00110000` (8-bit mit Overflow)

---

**Aufgabe 5:** Bitwise AND: 11110000 AND 10101010

```
Methode: Bit-für-Bit Vergleich (1 AND 1 = 1, sonst 0)

  1 1 1 1 0 0 0 0
  1 0 1 0 1 0 1 0
  ---------------
  1 0 1 0 0 0 0 0

Position für Position:
1 AND 1 = 1
1 AND 0 = 0
1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
```
**Ergebnis:** `10100000`

---

## Ergebnisse

| Aufgabe | Eingabe | Ergebnis |
|---------|---------|----------|
| 1. Decimal → Binary | 99 | `01100011` |
| 2. Hex → Decimal | 0xE4 | `228` |
| 3. Binary → Hex | 10100101 | `0xA5` |
| 4. Binary Addition | 11010011 + 01011101 | `100110000` |
| 5. Bitwise AND | 11110000 AND 10101010 | `10100000` |

---

## Notizen

- **Gelernt:** Zahlensystem-Konvertierungen, binäre Addition, bitweise Operationen
- **Decimal → Binary:** Wiederholte Division durch 2, Reste von unten nach oben lesen
- **Hex → Decimal:** E = 14, F = 15 im Hexadezimal-System
- **Binary → Hex:** Immer 4 Bits = 1 Hex-Ziffer (Nibble)
- **Binary Addition:** Überträge beachten! 1 + 1 = 10₂ (0 mit Übertrag 1)
- **AND-Operation:** Beide Bits müssen 1 sein für Ergebnis 1
- **Tipp:** Python zur Verifikation: `bin(99)`, `int('E4', 16)`, `hex(0b10100101)`