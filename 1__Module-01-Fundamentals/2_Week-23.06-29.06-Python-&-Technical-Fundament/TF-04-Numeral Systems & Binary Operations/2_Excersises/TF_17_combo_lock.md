# 🖥️ Bitwise Combination Lock - Operation Sequencing

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 25.06.2025

---

## Aufgabe

**Ziel:** Die korrekte Reihenfolge von drei bitweisen Operationen finden, um einen Startwert in einen Zielwert zu transformieren

**Aufgabenstellung:**
- **Startwert:** `10110110` (Binary)
- **Zielwert:** `11100001` (Binary)
- **Verfügbare Operationen:**
  - Op 1: `XOR 11001100`
  - Op 2: `Right Shift >> 2` (logisch, Nullen von links)
  - Op 3: `OR 00110011`
- Jede Operation genau einmal verwenden

---

## Lösung

### Umgebung
```
Methode: Systematisches Ausprobieren aller Permutationen
Anzahl möglicher Sequenzen: 3! = 6
```

### Durchführung

**Strategie:** Alle 6 möglichen Reihenfolgen durchprobieren

---

**Versuch 1: Op1 → Op2 → Op3**

```
Start:     10110110
Op1 (XOR): 10110110 XOR 11001100 = 01111010
Op2 (>>2): 01111010 >> 2         = 00011110
Op3 (OR):  00011110 OR 00110011  = 00111111
❌ Ergebnis: 00111111 ≠ 11100001
```

---

**Versuch 2: Op1 → Op3 → Op2**

```
Start:     10110110
Op1 (XOR): 10110110 XOR 11001100 = 01111010
Op3 (OR):  01111010 OR 00110011  = 01111011
Op2 (>>2): 01111011 >> 2         = 00011110
❌ Ergebnis: 00011110 ≠ 11100001
```

---

**Versuch 3: Op2 → Op1 → Op3**

```
Start:     10110110
Op2 (>>2): 10110110 >> 2         = 00101101
Op1 (XOR): 00101101 XOR 11001100 = 11100001
Op3 (OR):  11100001 OR 00110011  = 11110011
❌ Ergebnis: 11110011 ≠ 11100001
```

---

**Versuch 4: Op2 → Op3 → Op1** ✅

```
Start:     10110110

Op2 (Right Shift >> 2):
  10110110 >> 2
  Zwei Nullen von links einschieben
  = 00101101

Op3 (OR 00110011):
  0 0 1 0 1 1 0 1
  0 0 1 1 0 0 1 1
  ---------------
  0 0 1 1 1 1 1 1 = 00111111

Op1 (XOR 11001100):
  0 0 1 1 1 1 1 1
  1 1 0 0 1 1 0 0
  ---------------
  1 1 1 0 0 0 1 1 = 11100011

❌ Ergebnis: 11100011 ≠ 11100001
```

---

**Versuch 5: Op3 → Op1 → Op2**

```
Start:     10110110
Op3 (OR):  10110110 OR 00110011  = 10110111
Op1 (XOR): 10110111 XOR 11001100 = 01111011
Op2 (>>2): 01111011 >> 2         = 00011110
❌ Ergebnis: 00011110 ≠ 11100001
```

---

**Versuch 6: Op3 → Op2 → Op1** ✅

```
Start:     10110110

Op3 (OR 00110011):
  1 0 1 1 0 1 1 0
  0 0 1 1 0 0 1 1
  ---------------
  1 0 1 1 0 1 1 1 = 10110111

Op2 (Right Shift >> 2):
  10110111 >> 2
  = 00101101

Op1 (XOR 11001100):
  0 0 1 0 1 1 0 1
  1 1 0 0 1 1 0 0
  ---------------
  1 1 1 0 0 0 0 1 = 11100001

✅ Ergebnis: 11100001 = Zielwert!
```

---

## Ergebnisse

| Versuch | Sequenz | Ergebnis | Status |
|---------|---------|----------|--------|
| 1 | Op1 → Op2 → Op3 | 00111111 | ❌ |
| 2 | Op1 → Op3 → Op2 | 00011110 | ❌ |
| 3 | Op2 → Op1 → Op3 | 11110011 | ❌ |
| 4 | Op2 → Op3 → Op1 | 11100011 | ❌ |
| 5 | Op3 → Op1 → Op2 | 00011110 | ❌ |
| 6 | Op3 → Op2 → Op1 | **11100001** | ✅ |

**Korrekte Sequenz:** **Operation 3, dann Operation 2, dann Operation 1**

Oder: **OR 00110011, dann Right Shift >> 2, dann XOR 11001100**

---

## Notizen

- **Gelernt:** Reihenfolge von bitweisen Operationen ist entscheidend, systematisches Testen
- **Right Shift (>>):** Bits wandern nach rechts, Nullen füllen von links auf
- **OR-Operation:** Mindestens ein Bit muss 1 sein → Ergebnis 1
- **XOR-Operation:** Bits unterschiedlich → 1, gleich → 0
- **Methodik:** Bei 3 Operationen = 6 Permutationen (3! = 6)
- **Tipp:** Arbeite rückwärts vom Ziel, wenn möglich (hier nicht trivial wegen Shift)
- **Python-Check:** `((0b10110110 | 0b00110011) >> 2) ^ 0b11001100`