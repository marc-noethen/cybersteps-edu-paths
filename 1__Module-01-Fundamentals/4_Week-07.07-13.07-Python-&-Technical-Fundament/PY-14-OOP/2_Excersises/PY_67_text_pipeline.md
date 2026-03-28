# 🐍 Text Processing Pipeline - Chain of Responsibility

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 10.07.2025

---

## Aufgabe

**Ziel:** Implementierung einer Pipeline zur sequenziellen Textverarbeitung

**Anforderungen:**
- Basisklasse: `TextProcessor` mit abstrakter `process(text)` Methode
- Subklasse: `UpperCaseProcessor` - Konvertiert Text zu Großbuchstaben
- Subklasse: `RemovePunctuationProcessor` - Entfernt Satzzeichen (.,!?)
- Klasse: `Pipeline` - Verkettet mehrere Prozessoren
  - `add_processor(processor_object)`: Fügt Prozessor hinzu
  - `run(initial_text)`: Führt alle Prozessoren sequenziell aus
- Rückgabe: String (verarbeiteter Text)
- Edge Cases: Basis-Methode wirft NotImplementedError

---

## Lösung

```python
class TextProcessor:
    """Basisklasse für Textverarbeitungs-Prozessoren."""
    
    def __init__(self):
        """Initialisierung (optional)."""
        pass
    
    def process(self, text):
        """Muss von Subklassen implementiert werden."""
        raise NotImplementedError("Subclass must implement this method")


class UpperCaseProcessor(TextProcessor):
    """Konvertiert Text zu Großbuchstaben."""
    
    def process(self, text):
        """Gibt Text in Großbuchstaben zurück."""
        return text.upper()


class RemovePunctuationProcessor(TextProcessor):
    """Entfernt gängige Satzzeichen aus Text."""
    
    def process(self, text):
        """Entfernt Satzzeichen (.,!?) aus dem Text."""
        translator = str.maketrans('', '', '.,!?')
        return text.translate(translator)


class Pipeline:
    """Verkettet mehrere TextProcessor-Objekte zu einer Pipeline."""
    
    def __init__(self):
        """Initialisiert leere Prozessor-Liste."""
        self.processors = []
    
    def add_processor(self, processor_object):
        """Fügt einen TextProcessor zur Pipeline hinzu."""
        self.processors.append(processor_object)
    
    def run(self, initial_text):
        """Führt alle Prozessoren sequenziell aus und gibt Ergebnis zurück."""
        current_text = initial_text
        for processor in self.processors:
            current_text = processor.process(current_text)
        return current_text
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `pipeline = Pipeline(); pipeline.add_processor(UpperCaseProcessor()); pipeline.add_processor(RemovePunctuationProcessor()); pipeline.run("Hello, World! How are you?")` | "HELLO WORLD HOW ARE YOU" | HELLO WORLD HOW ARE YOU | ✅ |
| `pipeline2 = Pipeline(); pipeline2.add_processor(RemovePunctuationProcessor()); pipeline2.run("Test!")` | "Test" | Test | ✅ |

---

## Notizen

- **Konzept:** Chain of Responsibility Pattern & Strategy Pattern
- **str.maketrans():** Erstellt Translation Table für `translate()`
- **translate():** Effiziente Methode zum Entfernen/Ersetzen von Zeichen
- **Sequential Processing:** Ausgabe eines Prozessors ist Eingabe des nächsten
- **Polymorphismus:** Pipeline arbeitet mit beliebigen TextProcessor-Subklassen
- **Alternative:** `text.replace('.', '').replace(',', '')...` für Satzzeichen-Entfernung
- **Erweiterbarkeit:** Neue Prozessoren können leicht hinzugefügt werden
