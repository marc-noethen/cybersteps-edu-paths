# 🐍 Reverse Words - Wörter umkehren

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Kehre jedes Wort in einem Satz um, behalte die Reihenfolge der Wörter.

**Anforderungen:**
- Input: Satz (mit Prompt)
- Verarbeitung: Jedes Wort einzeln umkehren
- Output: Umgekehrte Wörter, durch Leerzeichen getrennt

---

## Lösung

```python
# Satz einlesen
sentence = input("Enter a sentence: ")

# Wörter trennen, umkehren, wieder zusammenfügen
words = sentence.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)

# Ausgabe
print(result)
```

**Kompakte Alternative:**
```python
sentence = input("Enter a sentence: ")
print(" ".join(word[::-1] for word in sentence.split()))
```

---

## Tests

| Input | Output | ✓ |
|-------|--------|---|
| `Hello World` | `olleH dlroW` | ✅ |
| `Python is fun` | `nohtyP si nuf` | ✅ |
| `A` | `A` | ✅ |

---

## Notizen

- **`[::-1]`:** Slice-Notation zum Umkehren eines Strings
- **`.split()`:** Trennt String an Leerzeichen → Liste
- **`" ".join(liste)`:** Verbindet Liste mit Leerzeichen
- **List Comprehension:** `[ausdruck for item in liste]`
