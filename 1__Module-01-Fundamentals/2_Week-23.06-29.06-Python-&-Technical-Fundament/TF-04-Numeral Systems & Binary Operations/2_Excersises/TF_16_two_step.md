![[template_tf]]# 🖥️ Two-Step Transformation - Bit Manipulation

**Kurs:** Technische Fundamentals | **Datum:** [DD.MM.YYYY]

---

## Aufgabe

**Ziel:** Bit-Manipulation durch XOR-Operation und gezieltes Bit-Flipping praktizieren

**Aufgabenstellung:**
- Eingabe: 4 Bytes (Hex): `B1`, `A1`, `D1`, `C1`
- Operation 1: Bitwise XOR mit Key `0xAA`
- Operation 2: 4. Bit von rechts flippen (2³ = 8er-Stelle)
- Ausgabe: Resultierende 4-Byte-Sequenz in Hex

---

## Lösung

### Umgebung
```
Methode: Manuelle Berechnung mit binärer Arithmetik
Tools: Hex-Binary Konvertierung, XOR-Tabelle, Bit-Manipulation
```

### Durchführung

**Byte 1: 0xB1**

**Schritt 1:** XOR mit 0xAA
```
B1 (hex) = 10110001 (binary)
AA (hex) = 10101010 (binary)

XOR (1 wenn unterschiedlich, 0 wenn gleich):
  1 0 1 1 0 0 0 1
  1 0 1 0 1 0 1 0
  ---------------
  0 0 0 1 1 0 1 1 = 0x1B
```

**Schritt 2:** Flip 4. Bit von rechts (2³ = Bit an Position 3)
```
0x1B = 00011011
Bit 3 (von rechts, 0-indexiert): Position 3 ist 1
Flip: 1 → 0

  0 0 0 1 1 0 1 1
        ↓ (flip)
  0 0 0 1 0 0 1 1 = 0x13
```
**Ergebnis Byte 1:** `0x13`

---

**Byte 2: 0xA1**

**Schritt 1:** XOR mit 0xAA
```
A1 (hex) = 10100001 (binary)
AA (hex) = 10101010 (binary)

XOR:
  1 0 1 0 0 0 0 1
  1 0 1 0 1 0 1 0
  ---------------
  0 0 0 0 1 0 1 1 = 0x0B
```

**Schritt 2:** Flip 4. Bit von rechts
```
0x0B = 00001011
Bit 3: Position 3 ist 1
Flip: 1 → 0

  0 0 0 0 1 0 1 1
        ↓ (flip)
  0 0 0 0 0 0 1 1 = 0x03
```
**Ergebnis Byte 2:** `0x03`

---

**Byte 3: 0xD1**

**Schritt 1:** XOR mit 0xAA
```
D1 (hex) = 11010001 (binary)
AA (hex) = 10101010 (binary)

XOR:
  1 1 0 1 0 0 0 1
  1 0 1 0 1 0 1 0
  ---------------
  0 1 1 1 1 0 1 1 = 0x7B
```

**Schritt 2:** Flip 4. Bit von rechts
```
0x7B = 01111011
Bit 3: Position 3 ist 1
Flip: 1 → 0

  0 1 1 1 1 0 1 1
        ↓ (flip)
  0 1 1 1 0 0 1 1 = 0x73
```
**Ergebnis Byte 3:** `0x73`

---

**Byte 4: 0xC1**

**Schritt 1:** XOR mit 0xAA
```
C1 (hex) = 11000001 (binary)
AA (hex) = 10101010 (binary)

XOR:
  1 1 0 0 0 0 0 1
  1 0 1 0 1 0 1 0
  ---------------
  0 1 1 0 1 0 1 1 = 0x6B
```

**Schritt 2:** Flip 4. Bit von rechts
```
0x6B = 01101011
Bit 3: Position 3 ist 1
Flip: 1 → 0

  0 1 1 0 1 0 1 1
        ↓ (flip)
  0 1 1 0 0 0 1 1 = 0x63
```
**Ergebnis Byte 4:** `0x63`

---

## Ergebnisse

| Byte | Original | Nach XOR 0xAA | Nach Bit-Flip | Final |
|------|----------|---------------|---------------|-------|
| 1 | 0xB1 | 0x1B | Bit 3: 1→0 | **0x13** |
| 2 | 0xA1 | 0x0B | Bit 3: 1→0 | **0x03** |
| 3 | 0xD1 | 0x7B | Bit 3: 1→0 | **0x73** |
| 4 | 0xC1 | 0x6B | Bit 3: 1→0 | **0x63** |

**Finale 4-Byte-Sequenz:** `13 03 73 63`

---

## Notizen

- **Gelernt:** XOR-Operation, gezieltes Bit-Flipping, mehrstufige Transformationen
- **XOR-Eigenschaften:** A XOR B: Bits unterschiedlich → 1, gleich → 0
- **Bit-Nummerierung:** Rechtester Bit = Bit 0 (LSB), 4. Bit von rechts = Bit 3 (2³ = 8)
- **Bit-Flip:** Toggle eines einzelnen Bits mittels XOR mit Maske (z.B. `XOR 00001000` für Bit 3)
- **Alternative Flip-Methode:** `result XOR 0x08` (0x08 = 00001000) flippt Bit 3
- **Tipp:** Python-Verifikation: `(0xB1 ^ 0xAA) ^ 0x08`