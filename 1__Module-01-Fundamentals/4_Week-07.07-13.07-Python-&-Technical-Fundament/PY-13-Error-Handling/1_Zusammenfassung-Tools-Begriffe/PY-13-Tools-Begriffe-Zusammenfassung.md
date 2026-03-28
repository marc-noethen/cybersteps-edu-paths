## 📊 Zusammenfassung nach dem 80/20-Prinzip
## **TEIL 1: WAS SIND FEHLER?**

### **1. Die zwei Hauptkategorien**

**1. Syntaxfehler (Syntax Errors)**

- **Wann:** Vor Programmausführung erkannt
- **Ursache:** Fehler in Code-Grammatik
- **Python sagt:** "Ich verstehe diesen Code nicht"

```python
# ❌ Syntaxfehler: Vergessener Doppelpunkt
if x > 5
    print("Groß")
# SyntaxError: invalid syntax

# ❌ Syntaxfehler: Falsch geschriebenes Keyword
whlie count < 10:
    print(count)
# SyntaxError: invalid syntax

# ❌ Syntaxfehler: Ungleiche Klammern
print("Hallo"
# SyntaxError: unexpected EOF
```

**Lösung:** Code korrigieren, dann läuft Programm

---

**2. Exceptions (Laufzeitfehler)**

- **Wann:** Während Programmausführung
- **Ursache:** Unerwartete Situation zur Laufzeit
- **Python sagt:** "Code ist korrekt, aber ich kann diese Aktion nicht ausführen"

```python
# ✅ Syntax korrekt, aber...

# ❌ TypeError zur Laufzeit
result = "Hallo" + 5
# TypeError: can only concatenate str (not "int") to str

# ❌ ZeroDivisionError zur Laufzeit
result = 10 / 0
# ZeroDivisionError: division by zero

# ❌ IndexError zur Laufzeit
liste = [1, 2, 3]
print(liste[10])
# IndexError: list index out of range
```

**Diese Lektion fokussiert sich auf Exceptions!**

---

### **2. Was passiert ohne Error-Handling?**

```python
# Programm startet
print("Programm gestartet")

# Fehler tritt auf
result = 10 / 0  # ZeroDivisionError!

# Programm stoppt hier (Crash)
print("Diese Zeile wird NIE erreicht")
```

**Output:**

```
Programm gestartet
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

**Problem:** Programm stürzt ab, Benutzer sieht kryptische Fehlermeldung

---

## **TEIL 2: WARUM ERROR-HANDLING?**

### **3. Die 5 Hauptgründe**

**1. Abstürze verhindern**

```python
# ❌ Ohne Handling: Crash
alter = int(input("Alter: "))  # User gibt "abc" ein → Crash!

# ✅ Mit Handling: Kein Crash
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Bitte Zahl eingeben!")
    alter = 0
```

**2. Benutzerfreundliche Meldungen**

```python
# ❌ Ohne Handling
with open("config.txt", "r") as file:
    config = file.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'config.txt'
# → Benutzer versteht nichts!

# ✅ Mit Handling
try:
    with open("config.txt", "r") as file:
        config = file.read()
except FileNotFoundError:
    print("Konfigurationsdatei nicht gefunden. Verwende Standardeinstellungen.")
    config = "default"
```

**3. Ressourcen aufräumen**

```python
try:
    datei = open("daten.txt", "w")
    datei.write("Wichtige Daten")
    # ... Fehler hier ...
finally:
    datei.close()  # Wird IMMER ausgeführt
```

**4. Wiederherstellung ermöglichen**

```python
try:
    verbindung_zu_server()
except ConnectionError:
    print("Verbindung fehlgeschlagen, versuche Backup-Server...")
    verbindung_zu_backup_server()
```

**5. Fehler protokollieren**

```python
try:
    kritische_operation()
except Exception as e:
    log_error(f"Fehler in kritischer Operation: {e}")
```

---

## **TEIL 3: DIE TRY-EXCEPT-STRUKTUR**

### **4. Grundstruktur**

```python
try:
    # Code, der Fehler verursachen könnte
    riskante_operation()
except ExceptionType:
    # Code, der ausgeführt wird, wenn Fehler auftritt
    fehlerbehandlung()
```

---

### **5. Einfaches Beispiel: Division**

```python
# Ohne Error-Handling
zahl1 = 10
zahl2 = 0
ergebnis = zahl1 / zahl2  # Crash!
print(ergebnis)

# Mit Error-Handling
zahl1 = 10
zahl2 = 0

try:
    ergebnis = zahl1 / zahl2
    print(f"Ergebnis: {ergebnis}")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt!")
    ergebnis = None

print("Programm läuft weiter...")
```

**Output:**

```
Fehler: Division durch Null ist nicht erlaubt!
Programm läuft weiter...
```

---

### **6. Mehrere Exception-Typen abfangen**

```python
def verarbeite_eingabe(eingabe):
    try:
        # Könnte ValueError verursachen (bei "abc")
        zahl = int(eingabe)
        
        # Könnte ZeroDivisionError verursachen (bei 0)
        ergebnis = 100 / zahl
        
        print(f"Ergebnis: {ergebnis}")
        
    except ValueError:
        print("Fehler: Bitte gültige Zahl eingeben!")
        
    except ZeroDivisionError:
        print("Fehler: Division durch Null!")
        
    print("Funktion abgeschlossen.")

# Tests
verarbeite_eingabe("20")    # Funktioniert
verarbeite_eingabe("abc")   # ValueError
verarbeite_eingabe("0")     # ZeroDivisionError
```

**Output:**

```
Ergebnis: 5.0
Funktion abgeschlossen.
Fehler: Bitte gültige Zahl eingeben!
Funktion abgeschlossen.
Fehler: Division durch Null!
Funktion abgeschlossen.
```

---

### **7. Exception-Objekt zugreifen mit `as`**

```python
try:
    datei = open("nicht_vorhanden.txt", "r")
except FileNotFoundError as fehler:
    print(f"Datei-Fehler aufgetreten: {fehler}")
    print(f"Fehlertyp: {type(fehler).__name__}")

# Output:
# Datei-Fehler aufgetreten: [Errno 2] No such file or directory: 'nicht_vorhanden.txt'
# Fehlertyp: FileNotFoundError
```

**Vorteil:** Zugriff auf Fehlerdetails für Logging/Debugging

---

## **TEIL 4: DAS `finally`-STATEMENT**

### **8. Was ist `finally`?**

**`finally` = Code, der IMMER ausgeführt wird**

- Egal ob Fehler auftritt oder nicht
- Egal ob Exception abgefangen wird oder nicht
- Perfekt für Cleanup (Dateien schließen, Verbindungen trennen)

---

### **9. Beispiel: Datei-Cleanup**

```python
datei = None
try:
    print("1. Öffne Datei...")
    datei = open("daten.txt", "w")
    
    print("2. Schreibe Daten...")
    datei.write("Wichtige Informationen")
    
    # Simuliere Fehler
    print("3. Führe riskante Operation aus...")
    x = 1 / 0  # ZeroDivisionError!
    
    print("4. Diese Zeile wird nie erreicht")
    
except ZeroDivisionError:
    print("5. Fehler abgefangen!")
    
finally:
    print("6. Cleanup: Schließe Datei...")
    if datei:
        datei.close()
    print("7. Datei geschlossen!")

print("8. Programm läuft weiter")
```

**Output:**

```
1. Öffne Datei...
2. Schreibe Daten...
3. Führe riskante Operation aus...
4. Fehler abgefangen!
5. Cleanup: Schließe Datei...
6. Datei geschlossen!
7. Programm läuft weiter
```

**Wichtig:** Zeile 4 wird übersprungen, aber `finally` läuft trotzdem!

---

### **10. `finally` ohne `except`**

```python
try:
    print("Versuche Operation...")
    risky_operation()
finally:
    print("Cleanup wird immer ausgeführt")
    cleanup()
# Exception wird nach finally weitergegeben (wenn nicht abgefangen)
```

**Verwendung:** Wenn Cleanup wichtig ist, aber Exception nicht behandelt werden soll

---

## **TEIL 5: HÄUFIGE EXCEPTIONS**

### **11. Die 10 wichtigsten Exception-Typen**

**1. `TypeError` – Falsche Datentyp-Operation**

```python
try:
    result = "Text" + 5
except TypeError:
    print("Fehler: Kann String und Integer nicht addieren")
```

**2. `ValueError` – Falscher Wert**

```python
try:
    alter = int("nicht-eine-zahl")
except ValueError:
    print("Fehler: Keine gültige Zahl")
```

**3. `ZeroDivisionError` – Division durch Null**

```python
try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Fehler: Division durch Null")
```

**4. `IndexError` – Index außerhalb Bereich**

```python
try:
    liste = [1, 2, 3]
    print(liste[10])
except IndexError:
    print("Fehler: Index existiert nicht")
```

**5. `KeyError` – Dictionary-Key nicht gefunden**

```python
try:
    person = {"name": "Alice"}
    print(person["alter"])
except KeyError:
    print("Fehler: Key 'alter' nicht gefunden")
```

**6. `FileNotFoundError` – Datei nicht gefunden**

```python
try:
    with open("nicht_da.txt", "r") as file:
        inhalt = file.read()
except FileNotFoundError:
    print("Fehler: Datei existiert nicht")
```

**7. `NameError` – Variable nicht definiert**

```python
try:
    print(undefinierte_variable)
except NameError:
    print("Fehler: Variable existiert nicht")
```

**8. `AttributeError` – Attribut/Methode existiert nicht**

```python
try:
    liste = [1, 2, 3]
    liste.appeend(4)  # Tippfehler
except AttributeError:
    print("Fehler: Methode existiert nicht")
```

**9. `ImportError` – Modul nicht gefunden**

```python
try:
    import nicht_existierendes_modul
except ImportError:
    print("Fehler: Modul kann nicht importiert werden")
```

**10. `Exception` – Allgemeine Exception (Basisklasse)**

```python
try:
    irgendwas_riskantes()
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
```

---

## **TEIL 6: BEST PRACTICES**

### **12. Spezifisch statt allgemein**

```python
# ❌ Zu allgemein (fängt ALLES ab)
try:
    datei = open("config.txt", "r")
    alter = int(eingabe)
    ergebnis = 10 / zahl
except:  # Fängt auch Syntax-Errors, Keyboard-Interrupts, etc.!
    print("Irgendein Fehler")

# ✅ Spezifisch (nur erwartete Fehler)
try:
    datei = open("config.txt", "r")
    alter = int(eingabe)
    ergebnis = 10 / zahl
except FileNotFoundError:
    print("Datei nicht gefunden")
except ValueError:
    print("Ungültige Zahl")
except ZeroDivisionError:
    print("Division durch Null")
```

**Warum?**

- Unerwartete Fehler werden nicht versehentlich "verschluckt"
- Besseres Debugging
- Klarerer Code

---

### **13. Generic Exception als Fallback**

```python
try:
    komplexe_operation()
except ValueError:
    print("Wert-Fehler")
except TypeError:
    print("Typ-Fehler")
except Exception as e:  # Fängt alle anderen Exceptions
    print(f"Unerwarteter Fehler: {e}")
```

**Regel:** Spezifische Exceptions zuerst, dann `Exception` als Fallback

---

### **14. Mehrere Exceptions gleichzeitig**

```python
# Methode 1: Tuple von Exceptions
try:
    risiko()
except (ValueError, TypeError) as e:
    print(f"Eingabe-Fehler: {e}")

# Methode 2: Separate except-Blöcke (wenn unterschiedliche Behandlung)
try:
    risiko()
except ValueError:
    print("Wert ist falsch")
except TypeError:
    print("Typ ist falsch")
```

---

## **TEIL 7: LBYL VS. EAFP**

### **15. Zwei Philosophien**

**LBYL (Look Before You Leap) – "Erst prüfen, dann springen"**

```python
# Prüfe vorher
if 'key' in mein_dict:
    wert = mein_dict['key']
else:
    wert = 'standard'

# Prüfe Dateityp
if isinstance(alter, int):
    print(alter)
```

**Vorteile:**

- Explizit und vorhersehbar
- Gut wenn Prüfung billig ist

**Nachteile:**

- Mehr Code
- Race Conditions möglich
- Nicht immer möglich zu prüfen

---

**EAFP (Easier to Ask Forgiveness than Permission) – "Erst machen, dann entschuldigen"**

```python
# Versuche es einfach
try:
    wert = mein_dict['key']
except KeyError:
    wert = 'standard'

# Versuche Konvertierung
try:
    zahl = int(eingabe)
except ValueError:
    zahl = 0
```

**Vorteile:**

- Pythonic (idiomatisch)
- Effizienter (bei seltenen Fehlern)
- Funktioniert bei unvorhersehbaren Situationen

**Nachteile:**

- Kann Performance kosten (bei häufigen Fehlern)

---

### **16. Wann was verwenden?**

|Situation|Methode|Beispiel|
|---|---|---|
|Prüfung ist billig und klar|LBYL|`if x != 0: y = 10/x`|
|Fehler ist selten|EAFP|`try: value = dict[key]`|
|Kann nicht vorher prüfen|EAFP|Import-Fehler, Netzwerk-Fehler|
|Performance-kritisch (viele Fehler)|LBYL|Loop über viele Items|

**Python-Präferenz:** EAFP ist idiomatischer

---

## **PRAKTISCHE BEISPIELE**

### **17. Beispiel 1: Sichere Benutzereingabe**

```python
def hole_positive_zahl():
    """Fordert Benutzer zur Eingabe positiver Zahl auf."""
    while True:
        try:
            eingabe = input("Gib positive Zahl ein: ")
            zahl = float(eingabe)
            
            if zahl <= 0:
                print("Fehler: Zahl muss positiv sein!")
                continue
            
            return zahl
            
        except ValueError:
            print("Fehler: Bitte gültige Zahl eingeben!")
        except KeyboardInterrupt:
            print("\nProgramm abgebrochen")
            return None

# Verwendung
zahl = hole_positive_zahl()
if zahl:
    print(f"Danke! Du hast {zahl} eingegeben.")
```

---

### **18. Beispiel 2: Konfigurations-Datei laden**

```python
def lade_config(dateiname="config.txt"):
    """Lädt Konfiguration, verwendet Defaults bei Fehler."""
    default_config = {
        "theme": "light",
        "font_size": 12,
        "language": "de"
    }
    
    try:
        with open(dateiname, "r") as file:
            # Angenommen: Jede Zeile ist "key=value"
            config = {}
            for zeile in file:
                zeile = zeile.strip()
                if '=' in zeile:
                    key, value = zeile.split('=', 1)
                    config[key] = value
            
            print(f"Konfiguration geladen aus {dateiname}")
            return config
            
    except FileNotFoundError:
        print(f"Warnung: {dateiname} nicht gefunden. Verwende Standardwerte.")
        return default_config
        
    except Exception as e:
        print(f"Fehler beim Laden: {e}. Verwende Standardwerte.")
        return default_config

# Verwendung
config = lade_config()
print(f"Theme: {config.get('theme', 'light')}")
```

---

### **19. Beispiel 3: Datenbank-Operation mit Cleanup**

```python
def speichere_in_datenbank(daten):
    """Simuliert Datenbank-Operation mit Cleanup."""
    verbindung = None
    try:
        print("1. Verbinde mit Datenbank...")
        verbindung = verbinde_datenbank()
        
        print("2. Beginne Transaktion...")
        verbindung.start_transaktion()
        
        print("3. Speichere Daten...")
        verbindung.speichern(daten)
        
        print("4. Commit Transaktion...")
        verbindung.commit()
        
        print("Erfolgreich gespeichert!")
        return True
        
    except VerbindungsFehler:
        print("Fehler: Keine Verbindung zur Datenbank")
        if verbindung:
            verbindung.rollback()
        return False
        
    except DatenFehler as e:
        print(f"Fehler: Ungültige Daten - {e}")
        if verbindung:
            verbindung.rollback()
        return False
        
    finally:
        print("5. Cleanup: Schließe Verbindung...")
        if verbindung:
            verbindung.schliessen()
        print("Verbindung geschlossen")
```

---

## **SCHNELLREFERENZ**

### **Try-Except-Finally Cheatsheet:**

```python
# Einfaches try-except
try:
    risiko()
except ValueError:
    behandlung()

# Mehrere Exceptions
try:
    risiko()
except ValueError:
    print("Wert-Fehler")
except TypeError:
    print("Typ-Fehler")

# Exception-Objekt zugreifen
try:
    risiko()
except Exception as e:
    print(f"Fehler: {e}")

# Mit finally
try:
    risiko()
except Exception:
    behandlung()
finally:
    cleanup()

# Mehrere Exceptions zusammen
try:
    risiko()
except (ValueError, TypeError):
    behandlung()

# Generic Fallback
try:
    risiko()
except ValueError:
    spezifisch()
except Exception as e:
    allgemein(e)
```

---

## **HÄUFIGE FEHLER UND LÖSUNGEN**

### **20. Fehler 1: Zu allgemeines `except:`**

```python
# ❌ Fängt ALLES ab (auch Ctrl+C!)
try:
    operation()
except:
    print("Fehler")

# ✅ Spezifisch
try:
    operation()
except ValueError:
    print("Wert-Fehler")
except Exception as e:
    print(f"Anderer Fehler: {e}")
```

---

### **21. Fehler 2: Vergessenes `finally` für Cleanup**

```python
# ❌ Datei wird nicht geschlossen bei Fehler
try:
    file = open("data.txt", "w")
    file.write(risky_data())
    file.close()  # Wird bei Fehler nicht erreicht!
except Exception:
    print("Fehler")

# ✅ Mit finally
try:
    file = open("data.txt", "w")
    file.write(risky_data())
except Exception:
    print("Fehler")
finally:
    file.close()  # Wird IMMER ausgeführt

# ✅✅ Oder besser: mit 'with'
try:
    with open("data.txt", "w") as file:
        file.write(risky_data())
except Exception:
    print("Fehler")
```

---

### **22. Fehler 3: Falsche Reihenfolge**

```python
# ❌ Generic Exception zuerst (fängt alles ab!)
try:
    operation()
except Exception:  # Fängt auch ValueError!
    print("Allgemein")
except ValueError:  # Wird NIE erreicht!
    print("Wert-Fehler")

# ✅ Spezifisch zuerst, generic zuletzt
try:
    operation()
except ValueError:
    print("Wert-Fehler")
except Exception:
    print("Allgemein")
```

---

## **ÜBUNGSAUFGABEN**

**Aufgabe 1:** Schreibe Funktion `sichere_division(a, b)`, die Division durchführt und alle möglichen Fehler abfängt.

**Aufgabe 2:** Erstelle Programm, das Benutzer nach Dateinamen fragt, Datei öffnet, Zeilen zählt. Behandle FileNotFoundError.

**Aufgabe 3:** Schreibe Funktion, die Liste von Strings in Integers konvertiert. Überspringe ungültige Werte.

**Aufgabe 4:** Simuliere Netzwerk-Request mit zufälligen Fehlern. Verwende try-except-finally für Cleanup.

---

### **Merksätze:**

🎯 **Exceptions = Laufzeitfehler, Syntax-Errors = Vor-Laufzeit-Fehler**  
🎯 **`try` = versuche, `except` = wenn Fehler, `finally` = immer**  
🎯 **`finally` läuft IMMER (perfekt für Cleanup!)**  
🎯 **Spezifische Exceptions zuerst, `Exception` als Fallback zuletzt**  
🎯 **EAFP = Pythonic, LBYL = explizit (beides hat seinen Platz)**  
🎯 **Nie `except:` ohne Exception-Typ (fängt zu viel ab!)**  
🎯 **Error-Handling = Abstürze verhindern + Benutzerfreundlichkeit**

---

## Verwendete Tools

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Python Interpreter|Zum Testen von Exception-Handling|
||VS Code|Editor zum Schreiben von Python-Skripten mit Error-Handling|
||Traceback|Fehlerbericht von Python mit Details zum Fehlerursprung|
||`try` Statement|Block für potenziell fehleranfälligen Code|
||`except` Statement|Block zur Behandlung von Exceptions|
||`finally` Statement|Block, der immer ausgeführt wird (für Cleanup)|

---

## Technische Fachbegriffe

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Technische Fachbegriffe**|Error (Fehler)|Situation, in der Code nicht wie erwartet ausgeführt werden kann|
||Exception (Ausnahme)|Laufzeitfehler, der während der Programmausführung auftritt|
||Syntax Error (Syntaxfehler)|Fehler in Code-Struktur/Grammatik (vor Ausführung erkannt)|
||Runtime Error (Laufzeitfehler)|Fehler während Programmausführung (= Exception)|
||Exception Handling (Ausnahmebehandlung)|Mechanismus zum Abfangen und Verarbeiten von Fehlern|
||Traceback|Fehlerprotokoll mit Aufruf-Historie und Fehlerposition|
||Crash (Absturz)|Programm stoppt abrupt wegen unbehandeltem Fehler|
||Graceful Handling (Elegante Behandlung)|Fehler abfangen ohne Programmabsturz|
||Cleanup (Aufräumen)|Freigeben von Ressourcen (Dateien, Verbindungen)|
||Recovery (Wiederherstellung)|Fehler korrigieren oder Alternative versuchen|
||Logging (Protokollierung)|Fehler für Debugging aufzeichnen|
||User Feedback|Benutzerfreundliche Fehlermeldung|
||Unhandled Exception|Nicht abgefangene Exception (führt zu Crash)|
||Re-raise (Erneut auslösen)|Exception weitergeben an äußeren try-Block|
||Matching (Übereinstimmung)|Passendes `except` für Exception-Typ finden|
||Base Class (Basisklasse)|Oberklasse, von der andere Exceptions erben|
||LBYL|"Look Before You Leap" - Vor Aktion prüfen|
||EAFP|"Easier to Ask Forgiveness than Permission" - Erst versuchen, dann Fehler behandeln|
|**Wichtige Vokabeln**|`try:`|Startet Block mit potenziell fehleranfälligem Code|
||`except ExceptionType:`|Fängt spezifischen Exception-Typ ab|
||`except Exception as e:`|Fängt Exception ab und speichert in Variable `e`|
||`finally:`|Block, der immer ausgeführt wird (Cleanup)|
||`Exception`|Basisklasse für die meisten Exceptions|
||`SyntaxError`|Fehler in Code-Syntax (nicht durch try-except abfangbar)|
||`TypeError`|Falsche Datentyp-Operation (z.B. `"text" + 5`)|
||`ValueError`|Richtiger Typ, falscher Wert (z.B. `int("abc")`)|
||`NameError`|Variable nicht definiert|
||`IndexError`|Index außerhalb Liste/Sequenz|
||`KeyError`|Dictionary-Key nicht gefunden|
||`FileNotFoundError`|Datei existiert nicht|
||`ZeroDivisionError`|Division durch Null|
||`ImportError`|Modul kann nicht importiert werden|
||`AttributeError`|Attribut/Methode existiert nicht (z.B. Tippfehler)|
||`IOError`|Ein-/Ausgabe-Fehler|
||`raise`|Manuelles Auslösen einer Exception (nicht im Detail behandelt)|