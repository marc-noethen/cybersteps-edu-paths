# 🖥️ URL Unraveling - Percent Encoding

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 26.06.2025

---

## Aufgabe

**Ziel:** URL Encoding (Percent-Encoding) verstehen und mit Python praktizieren

---

## Lösung

### Umgebung
```
Sprache: Python 3.x
Module: urllib.parse
Konzept: URL Encoding/Decoding
```

### Durchführung

**Schritt 1: Konzeptuelle Fragen - Warum URL Encoding?**

**Beispiel-URL:** `https://example.com/search?category=shoes&color=blue`

**Problem 1: Sonderzeichen mit spezieller Bedeutung**
```
Was wenn der Suchbegriff selbst ein '&' oder '?' enthält?

Beispiel ohne Encoding:
  URL: /search?query=shoes&boots?

Problem: Der Server interpretiert:
  - '&' als Separator zwischen Parametern
  - '?' als Start eines neuen Query-Strings
  
Resultat: Ambiguität! Server kann nicht unterscheiden zwischen:
  - Strukturellen Zeichen (Teil der URL-Syntax)
  - Daten-Zeichen (Teil des Suchbegriffs)

Lösung: Encoding!
  URL: /search?query=shoes%26boots%3F
  - %26 = '&' (encoded)
  - %3F = '?' (encoded)
```

**Problem 2: Leerzeichen in URLs**
```
Leerzeichen sind in URLs problematisch weil:
1. HTTP-Protokoll verwendet Leerzeichen als Trenner
   Beispiel: "GET /page.html HTTP/1.1"
   
2. Verschiedene Systeme interpretieren Leerzeichen unterschiedlich
   
3. URLs sollen "safe" für Copy-Paste sein

Lösung:
  - Leerzeichen → %20 (Percent-Encoding)
  - Leerzeichen → + (Plus-Encoding, häufig in Query Strings)
```

---

**Schritt 2: URL Parameter Decoding**

**Gegeben:** `https://example.com/search?query=M%C3%BCnchen+U-Bahn`

**Python Script:**
```python
from urllib.parse import unquote_plus

# Encoded Query Parameter
encoded_query = "M%C3%BCnchen+U-Bahn"

# Decodieren
decoded_query = unquote_plus(encoded_query)

print(f"Encoded: {encoded_query}")
print(f"Decoded: {decoded_query}")
```

**Ausgabe:**
```
Encoded: M%C3%BCnchen+U-Bahn
Decoded: München U-Bahn
```

**Erklärung der Sequenzen:**

1. **`%C3%BC`** = 'ü'
   ```
   - UTF-8 Bytes für 'ü': 0xC3 0xBC
   - URL Encoding: Jedes Byte → %XX
   - %C3 = erstes Byte (195 decimal)
   - %BC = zweites Byte (188 decimal)
   - Zusammen: UTF-8 codiertes 'ü'
   ```

2. **`+`** = Leerzeichen
   ```
   - In Query Strings: '+' repräsentiert Leerzeichen
   - Alternative: %20 (auch gültig für Leerzeichen)
   - Historischer Grund: Kompaktheit in Form-Daten
   ```

**Original Search Query:** `München U-Bahn`

---

**Schritt 3: String für URL Encoding**

**Gegeben:** `Preis: 10€`

**Python Script:**
```python
from urllib.parse import quote_plus

# Original String
original = "Preis: 10€"

# URL Encoding
encoded = quote_plus(original)

print(f"Original: {original}")
print(f"Encoded:  {encoded}")

# Byte-by-Byte Analyse
print("\nByte-by-Byte Breakdown:")
for char in original:
    encoded_char = quote_plus(char)
    print(f"  '{char}' → {encoded_char}")
```

**Ausgabe:**
```
Original: Preis: 10€
Encoded:  Preis%3A+10%E2%82%AC

Byte-by-Byte Breakdown:
  'P' → P
  'r' → r
  'e' → e
  'i' → i
  's' → s
  ':' → %3A
  ' ' → +
  '1' → 1
  '0' → 0
  '€' → %E2%82%AC
```

**URL-Encoded String:** `Preis%3A+10%E2%82%AC`

**Erklärung:**
- `P`, `r`, `e`, `i`, `s`, `1`, `0`: URL-safe → keine Änderung
- `:` → `%3A` (Doppelpunkt hat spezielle Bedeutung in URLs)
- ` ` → `+` (Leerzeichen)
- `€` → `%E2%82%AC` (UTF-8: E2 82 AC in Hex)

---

## Ergebnisse

| Frage | Antwort |
|-------|---------|
| **Konzeptuelle Fragen** | |
| Warum Encoding bei `&` und `?`? | Diese Zeichen haben strukturelle Bedeutung in URLs (Parameter-Separator, Query-Start). Ohne Encoding → Ambiguität zwischen Syntax und Daten. |
| Warum sind Leerzeichen problematisch? | 1) HTTP nutzt Leerzeichen als Trenner<br>2) Inkonsistente Interpretation<br>3) Nicht "safe" für Copy-Paste |
| **Decoding** | |
| Decoded Query | `München U-Bahn` |
| `%C3%BC` bedeutet | UTF-8 Bytes für 'ü' (0xC3 0xBC) |
| `+` bedeutet | Leerzeichen (in Query Strings) |
| **Encoding** | |
| Encoded String | `Preis%3A+10%E2%82%AC` |

---

## Notizen

- **Gelernt:** URL Encoding Notwendigkeit, Percent-Encoding, UTF-8 in URLs
- **URL-Safe Characters:** A-Z, a-z, 0-9, `-`, `_`, `.`, `~`
- **Reserved Characters:** `:`, `/`, `?`, `#`, `[`, `]`, `@`, `!`, `$`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `;`, `=`
- **Encoding-Methoden:**
  - `quote()`: Standardmäßiges Percent-Encoding
  - `quote_plus()`: Wie `quote()`, aber Leerzeichen → `+`
  - `unquote()`: Decodiert %XX Sequenzen
  - `unquote_plus()`: Decodiert %XX und `+` → Leerzeichen
- **UTF-8 in URLs:** Multi-Byte Zeichen → mehrere %XX Sequenzen
- **Historisch:** `+` für Leerzeichen aus `application/x-www-form-urlencoded`
- **Modern:** `%20` bevorzugt in Path, `+` OK in Query Strings
- **Security:** Immer user input encodieren vor URL-Konstruktion!