# Beitragen zu InsightLog

Vielen Dank für dein Interesse an InsightLog! Dies ist ein Solo-Entwicklungsprojekt zu Bildungszwecken. Dieses Dokument beschreibt den Entwicklungs-Workflow und die Standards.

---

## 🚀 Erste Schritte

### Voraussetzungen
- Python 3.8+
- Git
- Grundverständnis von Log-Analyse
- Erfahrung mit Python-Entwicklung

### Entwicklungsumgebung einrichten

```bash
# Repository klonen
git clone https://github.com/dein-benutzername/InsightLog.git
cd InsightLog

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Im Entwicklungsmodus installieren
pip install -e .
```

---

## 📝 Entwicklungs-Workflow

### 1. Branch-Strategie

```bash
main                    # Stabil, produktionsreif
├── develop            # Integrationsbranch
├── feature/xxx        # Neue Features
├── bugfix/xxx         # Bug-Fixes
└── hotfix/xxx         # Dringende Fixes
```

### 2. Neues Feature erstellen

```bash
# Main-Branch aktualisieren
git checkout main
git pull origin main

# Feature-Branch erstellen
git checkout -b feature/dein-feature-name

# Änderungen vornehmen
# ... code, test, commit ...

# Zum Repository pushen
git push origin feature/dein-feature-name
```

### 3. Commit-Nachrichten

Folge der [Conventional Commits](https://www.conventionalcommits.org/) Spezifikation:

```
<typ>(<bereich>): <betreff>

<text>

<fußzeile>
```

**Typen:**
- `feat`: Neues Feature
- `fix`: Bug-Fix
- `docs`: Dokumentations-Änderungen
- `style`: Code-Stil-Änderungen (Formatierung)
- `refactor`: Code-Refactoring
- `test`: Tests hinzufügen oder aktualisieren
- `chore`: Wartungsaufgaben

**Beispiele:**
```bash
feat(parser): JSON Log-Format-Unterstützung hinzugefügt
fix(analyzer): IP-Extraktion Regex-Muster korrigiert
docs(readme): Installations-Anleitung aktualisiert
test(parser): Unit-Tests für Edge-Cases hinzugefügt
refactor(utils): Hilfsfunktionen vereinfacht
```

---

## 🧪 Testing

### Tests ausführen

```bash
# Alle Tests ausführen
pytest

# Mit Coverage
pytest --cov=insightlog --cov-report=html

# Spezifische Test-Datei
pytest tests/test_analyzer.py

# Spezifischer Test
pytest tests/test_analyzer.py::test_ip_extraction
```

### Tests schreiben

```python
# tests/test_feature.py
import pytest
from insightlog import Analyzer

def test_feature_basis():
    """Teste Basis-Funktionalität."""
    analyzer = Analyzer()
    ergebnis = analyzer.analysieren("test.log")
    assert ergebnis is not None

def test_feature_edge_case():
    """Teste Edge-Case-Behandlung."""
    analyzer = Analyzer()
    ergebnis = analyzer.analysieren("")
    assert ergebnis == []
```

---

## 📊 Code-Qualität

### Code-Formatierung

```bash
# Mit black formatieren
black insightlog/

# Formatierung prüfen
black --check insightlog/
```

### Linting

```bash
# pylint ausführen
pylint insightlog/

# Mit spezifischer Config
pylint --rcfile=.pylintrc insightlog/
```

### Typ-Überprüfung

```bash
# mypy ausführen
mypy insightlog/
```

---

## 📚 Dokumentation

### Docstring-Format

Verwende Google-Style Docstrings:

```python
def log_analysieren(dateipfad: str, muster: str = None) -> dict:
    """Analysiere eine Log-Datei und extrahiere relevante Informationen.
    
    Args:
        dateipfad: Pfad zur zu analysierenden Log-Datei
        muster: Optionales Regex-Muster zur Suche
        
    Returns:
        Dictionary mit Analyse-Ergebnissen:
        - 'ips': Liste extrahierter IP-Adressen
        - 'fehler': Liste von Fehlermeldungen
        - 'treffer': Muster-Treffer falls muster angegeben
        
    Raises:
        FileNotFoundError: Wenn Log-Datei nicht existiert
        ValueError: Wenn Muster ungültiges Regex ist
        
    Example:
        >>> ergebnisse = log_analysieren('access.log', muster='ERROR')
        >>> print(ergebnisse['fehler'])
        ['Error 404', 'Error 500']
    """
    pass
```

---

## 🐛 Bug-Reports

Beim Melden von Bugs, bitte folgendes angeben:

1. **Beschreibung**: Klare Beschreibung des Problems
2. **Schritte zum Reproduzieren**: Detaillierte Schritte
3. **Erwartetes Verhalten**: Was sollte passieren
4. **Tatsächliches Verhalten**: Was passiert tatsächlich
5. **Umgebung**: OS, Python-Version, etc.
6. **Log-Dateien**: Beispiel-Log falls relevant (anonymisiert)

---

## 💡 Feature-Anfragen

Feature-Anfragen sind willkommen! Bitte beschreibe:

- **Feature-Beschreibung**: Klare Beschreibung
- **Use-Case**: Warum wird dieses Feature benötigt?
- **Vorgeschlagene Lösung**: Wie sollte es funktionieren?
- **Alternativen**: Andere mögliche Lösungen

---

## 📖 Ressourcen

### Lern-Ressourcen
- [Python Best Practices](https://docs.python-guide.org/)
- [Testing mit pytest](https://docs.pytest.org/)
- [Type Hints Guide](https://docs.python.org/3/library/typing.html)

### Tools
- [Black](https://black.readthedocs.io/) - Code-Formatter
- [Pylint](https://pylint.org/) - Code-Linter
- [mypy](http://mypy-lang.org/) - Typ-Checker
- [pytest](https://docs.pytest.org/) - Testing-Framework

---

**Vielen Dank fürs Mitwirken!**
