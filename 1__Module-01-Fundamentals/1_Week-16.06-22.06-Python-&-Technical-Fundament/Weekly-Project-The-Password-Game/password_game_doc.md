# 🐍 Password Game - Team Project

**Kurs:** Cyber Security Analyst - Project 1 | **Datum:** 20.06.2025

---

## Aufgabe

**Ziel:** Entwicklung eines interaktiven "Password Game" nach dem Vorbild von neal.fun/password-game, bei dem Benutzer eine Reihe von zunehmend komplexen Passwortregeln erfüllen müssen.

**Anforderungen:**
- Interaktives Spiel mit mindestens 10 Passwortregeln
- Verwendung von: `input()`, `print()`, Variablen, Bedingungen, Schleifen
- Validierung jeder Eingabe mit Fehlermeldungen
- Möglichkeit, mehrere Passwörter zu erstellen
- Finales Passwort wird aus allen Teilpasswörtern zusammengesetzt

**Implementierte Regeln:**
1. Mindestens 5 Buchstaben (nur Buchstaben)
2. Genau eine Ziffer
3. Ein Sonderzeichen
4. Ein Großbuchstabe
5. Ein Monatsname (mit Geburtstag)
6. Name des ersten Haustiers (aus Liste)
7. Lieblingsfarbe (aus Liste)
8. Zwei Zahlen, die zusammen 30 ergeben
9. Markenauswahl (Nike, Adidas, Puma)
10. Zufallszahl aus drei generierten Zahlen wählen

---

## Lösung

```python
import random

answer = input("Input (yes/no):\n").lower()

while True:
    # Password 1: at least 5 letters
    while True:
        pw1 = input("1. Enter at least 5 letters:\n")
        if pw1.isalpha() and len(pw1) >= 5:
            break
        else:
            print("Error: Letters only and at least 5 characters!")

    # Password 2: exactly 1 digit
    while True:
        pw2 = input("2. Enter exactly one digit:\n")
        if pw2.isdigit() and len(pw2) == 1:
            break
        else:
            print("Error: Must be exactly one digit!")

    # Password 3: exactly 1 special character
    special_chars = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
        '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]

    while True:
        pw3 = input("3. Enter a special character:\n")
        if pw3 in special_chars:
            break
        else:
            print("Error: Only special characters allowed!")

    # Password 4: one uppercase letter
    while True:
        pw4 = input("4. Enter one uppercase letter:\n")
        if pw4.isupper() and len(pw4) == 1:
            break
        else:
            print("Error: Only one uppercase letter!")

    # Password 5: a valid month
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        pw5 = input("5. Enter a month someone has a birthday in:\n").capitalize()
        if pw5 in months:
            break
        else:
            print("Error: Please enter a valid month!")

    # Password 6: first pet
    pets = [
        "Dog", "Cat", "Guinea pig", "Hamster", "Rabbit", "Budgie",
        "Parrot", "Fish", "Rat", "Mouse", "Chinchilla", "Hedgehog",
        "Ferret", "Turtle", "Iguana", "Snake", "Spider"
    ]

    while True:
        print(pets)
        pw6 = input("6. Enter your first pet:\n").capitalize()
        if pw6 in pets:
            break
        else:
            print("Error: Please enter a valid pet!")

    # Password 7: favorite color
    favorite_colors = [
        "Blue", "Red", "Green", "Yellow", "Purple", "Orange", "Black",
        "White", "Pink", "Turquoise", "Brown", "Gray", "Beige", "Violet", "Gold", "Silver"
    ]

    while True:
        print(favorite_colors)
        pw7 = input("7. Enter your favorite color:\n").capitalize()
        if pw7 in favorite_colors:
            break
        else:
            print("Error: Please enter a valid color!")

    # Password 8: two numbers that add up to 30
    while True:
        try:
            pw8_1 = int(input("8. Enter two numbers that add up to 30.\nFirst number:\n"))
            pw8_2 = int(input("Second number:\n"))
        except ValueError:
            print("Error: Numbers only!")
            continue

        if pw8_1 + pw8_2 == 30:
            break
        else:
            print("Error: The numbers must add up to 30!")

    # Password 9: brand
    brands = ["nike", "adidas", "puma"]
    while True:
        pw9 = input("9. Which of these brands fits you best? (nike, adidas, puma):\n").lower()
        if pw9 in brands:
            break
        else:
            print("Error: Only one of the 3 brands!")

    # Password 10: pick a random number
    while True:
        numbers = [random.randint(1, 100) for _ in range(3)]
        try:
            pw10 = int(input(f"10. Choose one of these random numbers: {numbers}\n"))
        except ValueError:
            print("Error: Numbers only!")
            continue

        if pw10 in numbers:
            break
        else:
            print("Error: Please choose one of the shown numbers!")

    # Final password output
    print(f"\n✅ Your final password: {pw1}{pw2}{pw3}{pw4}{pw5}{pw6}{pw7}{pw8_1}{pw8_2}{pw9}{pw10}")
    print("🎉 Password game completed!\n")

    # Play again?
    answer = input("Do you want to create another password? (yes/no):\n").lower()
    if answer != "yes":
        print("Program ended.")
        break
```

---

## Tests

| Test-Szenario | Input-Beispiel | Erwartet | Ergebnis | ✓ |
|---------------|----------------|----------|----------|---|
| **Regel 1** | `"hello"` | Akzeptiert | ✅ | ✅ |
| **Regel 1** | `"hi"` | Error (< 5) | Error | ✅ |
| **Regel 1** | `"hello5"` | Error (keine Zahlen) | Error | ✅ |
| **Regel 2** | `"7"` | Akzeptiert | ✅ | ✅ |
| **Regel 2** | `"12"` | Error (genau 1) | Error | ✅ |
| **Regel 3** | `"@"` | Akzeptiert | ✅ | ✅ |
| **Regel 3** | `"a"` | Error (kein Sonderzeichen) | Error | ✅ |
| **Regel 4** | `"A"` | Akzeptiert | ✅ | ✅ |
| **Regel 4** | `"AB"` | Error (nur 1 Buchstabe) | Error | ✅ |
| **Regel 5** | `"january"` | Akzeptiert (capitalized) | ✅ | ✅ |
| **Regel 5** | `"Smarch"` | Error (ungültiger Monat) | Error | ✅ |
| **Regel 8** | `15, 15` | Akzeptiert (30) | ✅ | ✅ |
| **Regel 8** | `10, 15` | Error (≠ 30) | Error | ✅ |
| **Regel 10** | Zahl aus Liste | Akzeptiert | ✅ | ✅ |
| **Regel 10** | `999` (nicht in Liste) | Error | Error | ✅ |
| **Wiederholen** | `"yes"` | Neues Spiel | Neues Spiel | ✅ |
| **Beenden** | `"no"` | Programm endet | "Program ended." | ✅ |

---

## Notizen

### **Verwendete Python-Konzepte:**

**Grundkonzepte (aus dem Unterricht):**
- `input()` und `print()` für Benutzerinteraktion
- `while`-Schleifen für Wiederholungen und Validierung
- `if/else`-Bedingungen für Logik
- Variablen für Datenspeicherung
- Listen für vordefinierte Optionen

**Fortgeschrittene Features (selbst recherchiert):**

1. **String-Methoden:**
   - `.isalpha()` – prüft, ob String nur Buchstaben enthält
   - `.isdigit()` – prüft, ob String nur Ziffern enthält
   - `.isupper()` – prüft, ob Zeichen Großbuchstabe ist
   - `.lower()` / `.capitalize()` – Normalisierung von Eingaben

2. **Exception Handling:**
   - `try/except ValueError` – fängt Fehler bei `int()`-Konvertierung ab
   - Verhindert Programmabsturz bei ungültigen Eingaben

3. **Random-Modul:**
   - `import random` – importiert Zufallszahlen-Funktionalität
   - `random.randint(1, 100)` – generiert Zufallszahl
   - List Comprehension: `[random.randint(1, 100) for _ in range(3)]`

4. **F-Strings:**
   - `f"Text {variable}"` – moderne String-Formatierung
   - Bessere Lesbarkeit als `.format()` oder `+`-Konkatenation

5. **List Comprehension:**
   - `[expression for item in iterable]` – kompakte Listenerstellung
   - Verwendet für Zufallszahlen-Generierung

### **Design-Entscheidungen:**

- **Verschachtelte Loops:** Jede Regel hat eine eigene `while`-Schleife für Validierung bis korrekte Eingabe erfolgt
- **Normalisierung:** `.capitalize()` und `.lower()` machen Eingaben case-insensitive
- **Benutzerfreundlichkeit:** Listen werden angezeigt (Regeln 6, 7), damit Benutzer wissen, was gültig ist
- **Wiederholbarkeit:** Äußere Schleife ermöglicht mehrere Passwörter ohne Neustart

### **Herausforderungen & Lösungen:**

- **Problem:** Benutzer könnten Buchstaben statt Zahlen eingeben
  - **Lösung:** `try/except` bei numerischen Eingaben (Regeln 8, 10)
  
- **Problem:** Case-Sensitivity bei Monaten/Farben/Haustieren
  - **Lösung:** `.capitalize()` normalisiert erste Buchstaben

- **Problem:** Unklare Anforderungen für Benutzer
  - **Lösung:** Klare Fehlermeldungen und Listen-Anzeige

### **Erweiterungsmöglichkeiten:**

- Schwierigkeitsgrade (Easy/Medium/Hard)
- Dynamisches Hinzufügen von Regeln während des Spiels
- Score-System basierend auf Anzahl der Versuche
- Passwort-Stärke-Anzeige
- GUI mit Tkinter
- Zeitlimit pro Regel