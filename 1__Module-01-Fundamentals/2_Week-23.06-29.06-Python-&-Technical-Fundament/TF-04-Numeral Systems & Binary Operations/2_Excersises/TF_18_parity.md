# 🖥️ Not Pair! - Parity Checking

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 25.06.2025

---

## Aufgabe

**Ziel:** Parity Checking für Fehlererkennung verstehen und implementieren

**Aufgabenstellung:**
- **Part 1:** Manuelle Verifikation von 4 Paketen mit Even Parity
- **Part 2:** Python-Funktion `has_even_parity()` schreiben
- **Part 3:** Python-Funktion `generate_even_parity_bit()` schreiben

**Konzept:** Even Parity = Gesamtanzahl der 1en ist gerade (inkl. Parity Bit)

---

## Lösung

### Umgebung
```
Methode: Manuelle Zählung + Python Implementation
Tools: Binär-Zählung, Python 3.x
```

### Durchführung

---

## Part 1: Manual Verification

**Packet 1: `11010110`**
```
Zähle die 1en: 1,1,0,1,0,1,1,0
Anzahl: 1+1+0+1+0+1+1+0 = 5
5 ist ungerade → Even Parity INCORRECT
```
**Status:** ❌ **Incorrect**

---

**Packet 2: `00111001`**
```
Zähle die 1en: 0,0,1,1,1,0,0,1
Anzahl: 0+0+1+1+1+0+0+1 = 4
4 ist gerade → Even Parity CORRECT
```
**Status:** ✅ **Correct**

---

**Packet 3: `10101011`**
```
Zähle die 1en: 1,0,1,0,1,0,1,1
Anzahl: 1+0+1+0+1+0+1+1 = 5
5 ist ungerade → Even Parity INCORRECT
```
**Status:** ❌ **Incorrect**

---

**Packet 4: `01100011`**
```
Zähle die 1en: 0,1,1,0,0,0,1,1
Anzahl: 0+1+1+0+0+0+1+1 = 4
4 ist gerade → Even Parity CORRECT
```
**Status:** ✅ **Correct**

---

## Part 2: Python - Parity Checker

**Funktion:** Prüft ob ein 8-bit Paket Even Parity hat

```python
def has_even_parity(packet_string):
    """
    Prüft ob ein binärer String Even Parity hat.
    
    Args:
        packet_string: 8-bit binärer String (z.B. "11010110")
    
    Returns:
        True wenn Anzahl der 1en gerade ist, sonst False
    """
    # Zähle die Anzahl der '1'en im String
    count_ones = packet_string.count('1')
    
    # Prüfe ob gerade (Modulo 2 ergibt 0)
    return count_ones % 2 == 0


# Tests
print(has_even_parity("11010110"))  # False (5 Einsen)
print(has_even_parity("00111001"))  # True  (4 Einsen)
print(has_even_parity("10101011"))  # False (5 Einsen)
print(has_even_parity("01100011"))  # True  (4 Einsen)
```

---

## Part 3: Python - Parity Bit Generator

**Funktion:** Generiert das Parity Bit für 7-bit Daten

```python
def generate_even_parity_bit(data_bits_string):
    """
    Generiert Even Parity Bit für 7-bit Daten.
    
    Args:
        data_bits_string: 7-bit binärer Daten-String (z.B. "1101011")
    
    Returns:
        Parity Bit als String: "0" oder "1"
    """
    # Zähle die Anzahl der '1'en in den Datenbits
    count_ones = data_bits_string.count('1')
    
    # Wenn Anzahl ungerade: Parity Bit = 1 (macht Gesamt gerade)
    # Wenn Anzahl gerade: Parity Bit = 0 (hält Gesamt gerade)
    if count_ones % 2 == 0:
        return "0"
    else:
        return "1"


# Tests
print(generate_even_parity_bit("1101011"))  # "0" (4 Einsen → gerade)
print(generate_even_parity_bit("0011100"))  # "1" (3 Einsen → ungerade)
print(generate_even_parity_bit("1010101"))  # "0" (4 Einsen → gerade)
print(generate_even_parity_bit("0000000"))  # "0" (0 Einsen → gerade)
```

---

## Ergebnisse

### Part 1: Manual Verification

| Packet | Binary | Anzahl 1en | Status |
|--------|--------|------------|--------|
| 1 | `11010110` | 5 (ungerade) | ❌ **Incorrect** |
| 2 | `00111001` | 4 (gerade) | ✅ **Correct** |
| 3 | `10101011` | 5 (ungerade) | ❌ **Incorrect** |
| 4 | `01100011` | 4 (gerade) | ✅ **Correct** |

### Part 2: Python Code
```python
def has_even_parity(packet_string):
    count_ones = packet_string.count('1')
    return count_ones % 2 == 0
```

### Part 3: Python Code
```python
def generate_even_parity_bit(data_bits_string):
    count_ones = data_bits_string.count('1')
    return "0" if count_ones % 2 == 0 else "1"
```

---

## Notizen

- **Gelernt:** Parity Checking für Fehlererkennung, Even vs Odd Parity
- **Even Parity:** Gesamtanzahl 1en muss gerade sein (0, 2, 4, 6, 8)
- **Odd Parity:** Gesamtanzahl 1en muss ungerade sein (1, 3, 5, 7)
- **Limitation:** Parity erkennt Single-Bit-Fehler, aber nicht wenn 2+ Bits flippen
- **Anwendung:** Serielle Kommunikation (UART), RAM (ECC), Datenübertragung
- **Modulo-Trick:** `count % 2 == 0` prüft auf gerade Zahl
- **Alternative:** XOR aller Bits ergibt Parity Bit (XOR-Kette)
- **Tipp:** `str.count('1')` ist effizient für Parity-Berechnung in Python