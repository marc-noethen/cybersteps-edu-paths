#!/usr/bin/env python3
"""
InsightLog Projektstruktur Setup-Script

Dieses Script erstellt die komplette Verzeichnisstruktur für das InsightLog-Projekt.
Führe dieses Script im Projekt-Root-Verzeichnis aus.

Verwendung:
    python setup_struktur.py
"""

import os
from pathlib import Path


def erstelle_verzeichnis(pfad: Path, beschreibung: str = ""):
    """Erstelle ein Verzeichnis falls es nicht existiert."""
    if not pfad.exists():
        pfad.mkdir(parents=True)
        print(f"✅ Erstellt: {pfad}" + (f" - {beschreibung}" if beschreibung else ""))
    else:
        print(f"⚠️  Existiert: {pfad}")


def erstelle_datei(pfad: Path, inhalt: str = "", beschreibung: str = ""):
    """Erstelle eine Datei mit optionalem Inhalt."""
    if not pfad.exists():
        pfad.parent.mkdir(parents=True, exist_ok=True)
        pfad.write_text(inhalt, encoding='utf-8')
        print(f"✅ Erstellt: {pfad}" + (f" - {beschreibung}" if beschreibung else ""))
    else:
        print(f"⚠️  Existiert: {pfad}")


def setup_projektstruktur():
    """Erstelle die komplette InsightLog-Projektstruktur."""
    
    print("\n🚀 Richte InsightLog-Projektstruktur ein...\n")
    
    # Root-Verzeichnis
    root = Path(".")
    
    # Haupt-Package-Verzeichnis
    erstelle_verzeichnis(root / "insightlog", "Haupt-Package")
    erstelle_datei(
        root / "insightlog" / "__init__.py",
        '"""InsightLog - Log-Analyse-Tool"""\n\n__version__ = "0.2.0"\n',
        "Package-Init"
    )
    
    erstelle_datei(
        root / "insightlog" / "analyzer.py",
        '"""Kern-Analyse-Logik"""\n\nclass Analyzer:\n    pass\n',
        "Analyse-Modul"
    )
    
    erstelle_datei(
        root / "insightlog" / "parser.py",
        '"""Log-Parsing-Funktionalität"""\n\nclass Parser:\n    pass\n',
        "Parser-Modul"
    )
    
    erstelle_datei(
        root / "insightlog" / "patterns.py",
        '"""Regex-Muster für Log-Analyse"""\n\n# Häufige Muster\nIP_PATTERN = r"\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}"\n',
        "Muster-Definitionen"
    )
    
    erstelle_datei(
        root / "insightlog" / "utils.py",
        '"""Hilfsfunktionen"""\n\ndef datei_lesen(dateipfad):\n    pass\n',
        "Hilfsfunktionen"
    )
    
    # Tests-Verzeichnis
    erstelle_verzeichnis(root / "tests", "Unit-Tests")
    erstelle_datei(
        root / "tests" / "__init__.py",
        "",
        "Tests-Init"
    )
    
    erstelle_datei(
        root / "tests" / "test_analyzer.py",
        '"""Tests für Analyzer-Modul"""\n\nimport pytest\nfrom insightlog.analyzer import Analyzer\n\ndef test_basis():\n    pass\n',
        "Analyzer-Tests"
    )
    
    erstelle_datei(
        root / "tests" / "test_parser.py",
        '"""Tests für Parser-Modul"""\n\nimport pytest\nfrom insightlog.parser import Parser\n\ndef test_basis():\n    pass\n',
        "Parser-Tests"
    )
    
    # Test-Daten
    erstelle_verzeichnis(root / "tests" / "test_daten", "Beispiel-Test-Logs")
    erstelle_datei(
        root / "tests" / "test_daten" / "beispiel.log",
        "2026-01-21 10:00:00 INFO Anwendung gestartet\n2026-01-21 10:00:01 ERROR Verbindung fehlgeschlagen\n",
        "Beispiel-Log-Datei"
    )
    
    # Dokumentation
    erstelle_verzeichnis(root / "docs", "Dokumentation")
    erstelle_datei(
        root / "docs" / "API.md",
        "# API-Dokumentation\n\nKommt bald...\n",
        "API-Docs"
    )
    
    # Beispiele
    erstelle_verzeichnis(root / "beispiele", "Verwendungsbeispiele")
    erstelle_datei(
        root / "beispiele" / "basis_nutzung.py",
        '#!/usr/bin/env python3\n"""Basis-Verwendungsbeispiel"""\n\nfrom insightlog import Analyzer\n\nif __name__ == "__main__":\n    print("Basis-Verwendungsbeispiel")\n',
        "Basis-Beispiel"
    )
    
    erstelle_verzeichnis(root / "beispiele" / "beispiel_logs", "Beispiel-Log-Dateien")
    erstelle_datei(
        root / "beispiele" / "beispiel_logs" / "access.log",
        "192.168.1.1 - - [21/Jan/2026:10:00:00] GET /index.html 200\n",
        "Beispiel-Access-Log"
    )
    
    # Scripts
    erstelle_verzeichnis(root / "scripts", "Utility-Scripts")
    erstelle_datei(
        root / "scripts" / "benchmark.py",
        '#!/usr/bin/env python3\n"""Performance-Benchmarking"""\n\nif __name__ == "__main__":\n    print("Benchmark-Script")\n',
        "Benchmark-Script"
    )
    
    # Screenshots-Verzeichnis (für Dokumentation)
    erstelle_verzeichnis(root / "screenshots", "Screenshots für Dokumentation")
    erstelle_datei(
        root / "screenshots" / "README.md",
        "# Screenshots\n\nPlatziere Screenshots hier für die Dokumentation.\n",
        "Screenshots-Readme"
    )
    
    # Konfigurations-Dateien
    erstelle_datei(
        root / ".gitignore",
        """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Projektspezifisch
*.log
test_output/
""",
        "Git-Ignore-Datei"
    )
    
    erstelle_datei(
        root / "requirements.txt",
        """# Kern-Abhängigkeiten
requests>=2.31.0
python-dateutil>=2.8.2

# Optionale Abhängigkeiten
# pandas>=2.0.0  # Für erweiterte Daten-Analyse
# matplotlib>=3.7.0  # Für Visualisierung
""",
        "Projekt-Abhängigkeiten"
    )
    
    erstelle_datei(
        root / "requirements-dev.txt",
        """# Entwicklungs-Abhängigkeiten
pytest>=7.4.0
pytest-cov>=4.1.0
black>=23.7.0
pylint>=2.17.0
mypy>=1.4.0
""",
        "Dev-Abhängigkeiten"
    )
    
    erstelle_datei(
        root / "setup.py",
        """from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="insightlog",
    version="0.2.0",
    author="Dein Name",
    author_email="deine.email@beispiel.de",
    description="Fortgeschrittenes Log-Analyse-Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dein-benutzername/InsightLog",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "insightlog=insightlog.cli:main",
        ],
    },
)
""",
        "Setup-Script"
    )
    
    erstelle_datei(
        root / "pytest.ini",
        """[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --strict-markers
    --cov=insightlog
    --cov-report=term-missing
    --cov-report=html
""",
        "Pytest-Config"
    )
    
    erstelle_datei(
        root / ".pylintrc",
        """[MASTER]
jobs=1

[MESSAGES CONTROL]
disable=
    missing-module-docstring,
    missing-class-docstring,
    too-few-public-methods

[FORMAT]
max-line-length=100
""",
        "Pylint-Config"
    )
    
    erstelle_datei(
        root / "LICENSE",
        """MIT Lizenz

Copyright (c) 2026 [Dein Name]

Hiermit wird unentgeltlich jeder Person, die eine Kopie der Software und der 
zugehörigen Dokumentationen (die "Software") erhält, die Erlaubnis erteilt, 
sie uneingeschränkt zu nutzen, inklusive und ohne Ausnahme mit dem Recht, sie 
zu verwenden, zu kopieren, zu ändern, zusammenzufügen, zu veröffentlichen, zu 
verbreiten, zu unterlizenzieren und/oder zu verkaufen, und Personen, denen diese 
Software überlassen wird, diese Rechte zu verschaffen, unter den folgenden 
Bedingungen:

Der obige Urheberrechtsvermerk und dieser Erlaubnisvermerk sind in allen Kopien 
oder Teilkopien der Software beizulegen.

DIE SOFTWARE WIRD OHNE JEDE AUSDRÜCKLICHE ODER IMPLIZIERTE GARANTIE 
BEREITGESTELLT, EINSCHLIEẞLICH DER GARANTIE ZUR BENUTZUNG FÜR DEN VORGESEHENEN 
ODER EINEM BESTIMMTEN ZWECK SOWIE JEGLICHER RECHTSVERLETZUNG, JEDOCH NICHT 
DARAUF BESCHRÄNKT. IN KEINEM FALL SIND DIE AUTOREN ODER COPYRIGHTINHABER FÜR 
JEGLICHEN SCHADEN ODER SONSTIGE ANSPRÜCHE HAFTBAR ZU MACHEN, OB INFOLGE DER 
ERFÜLLUNG EINES VERTRAGES, EINES DELIKTES ODER ANDERS IM ZUSAMMENHANG MIT DER 
SOFTWARE ODER SONSTIGER VERWENDUNG DER SOFTWARE ENTSTANDEN.
""",
        "MIT-Lizenz"
    )
    
    print("\n✅ Projektstruktur-Setup abgeschlossen!\n")
    print("Nächste Schritte:")
    print("1. Generierte Dateien überprüfen und anpassen")
    print("2. Abhängigkeiten installieren: pip install -r requirements.txt")
    print("3. Dev-Abhängigkeiten installieren: pip install -r requirements-dev.txt")
    print("4. Tests ausführen: pytest")
    print("5. Mit Entwicklung beginnen!\n")


if __name__ == "__main__":
    setup_projektstruktur()
