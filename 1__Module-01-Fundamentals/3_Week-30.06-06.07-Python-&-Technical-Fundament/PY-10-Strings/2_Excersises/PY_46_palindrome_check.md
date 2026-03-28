# 🐍 Palindrome Check - Palindrom-Prüfung

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Prüfe ob ein Text ein Palindrom ist (ignoriere Groß-/Kleinschreibung, Leerzeichen, Sonderzeichen).

**Anforderungen:**
- Input: Text (mit Prompt)
- Verarbeitung: Nur alphanumerische Zeichen, case-insensitive
- Output: `"Palindrome"` oder `"Not a palindrome"`

---

## Lösung

```python
# Text einlesen
text = input("Enter text: ")

# Nur alphanumerische Zeichen, lowercase
cleaned = ""
for char in text.lower():
    if char.isalnum():
        cleaned += char

# Palindrom-Check
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

**Kompakte Alternative:**
```python
text = input("Enter text: ")
cleaned = "".join(c for c in text.lower() if c.isalnum())
print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")
```

---

## Tests

| Input | Output | ✓ |
|-------|--------|---|
| `Racecar` | `Palindrome` | ✅ |
| `A man, a plan, a canal: Panama` | `Palindrome` | ✅ |
| `Hello World` | `Not a palindrome` | ✅ |
| `Was it a car or a cat I saw?` | `Palindrome` | ✅ |

---

## Notizen

- **`.isalnum()`:** `True` wenn Buchstabe oder Ziffer
- **`.lower()`:** Konvertiert zu Kleinbuchstaben
- **Palindrom:** Liest sich vorwärts und rückwärts gleich
- **`[::-1]`:** String umkehren
