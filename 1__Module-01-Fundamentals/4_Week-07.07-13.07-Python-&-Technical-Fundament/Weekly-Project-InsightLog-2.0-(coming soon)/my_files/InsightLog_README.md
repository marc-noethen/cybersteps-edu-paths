# 🔍 InsightLog - Erweiterte Version

> Fortgeschrittenes Python-Tool zur Log-Analyse und Sicherheitsüberwachung

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Lizenz](https://img.shields.io/badge/Lizenz-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-In%20Entwicklung-yellow.svg)]()

---

## 📋 Projekt-Übersicht

**InsightLog** ist ein umfassendes Python-basiertes Log-Analyse-Tool, entwickelt für Cybersecurity-Profis und Systemadministratoren. Es extrahiert und analysiert kritische Informationen aus rohen Log-Dateien, einschließlich IP-Adressen, Fehlermustern, verdächtigen Aktivitäten und benutzerdefinierten Suchmustern.

**Original Repository:** [CyberstepsDE/InsightLog](https://github.com/CyberstepsDE/InsightLog)

### 🎯 Projektziele

Diese erweiterte Version zielt darauf ab:
- Bestehende Bugs zu beheben und TODOs abzuschließen
- Code-Qualität und Architektur zu verbessern
- Neue Features für bessere Nutzbarkeit hinzuzufügen
- Dokumentation und Tests zu erweitern
- Performance zu optimieren

---

## ✨ Features

### Aktuelle Features
- ✅ IP-Adressen-Extraktion aus Logs
- ✅ Fehlermuster-Erkennung
- ✅ Flexible regex-basierte Suchmuster
- ✅ Unterstützung mehrerer Log-Formate

### 🚧 Geplante Verbesserungen
- [ ] Erweiterte Fehlerbehandlung
- [ ] Performance-Optimierung für große Dateien
- [ ] Zusätzliche Ausgabeformate (JSON, CSV)
- [ ] Automatische Report-Generierung
- [ ] Echtzeit-Log-Überwachung
- [ ] Statistisches Analyse-Dashboard

---

## 🚀 Schnellstart

### Voraussetzungen
```bash
Python 3.8 oder höher
pip (Python Package Manager)
```

### Installation

```bash
# Repository klonen
git clone https://github.com/[dein-benutzername]/InsightLog.git
cd InsightLog

# Abhängigkeiten installieren
pip install -r requirements.txt

# Basis-Analyse durchführen
python insightlog.py --file beispiel.log
```

### Grundlegende Verwendung

```bash
# Log-Datei analysieren
python insightlog.py --file /pfad/zur/logdatei.log

# Nach spezifischem Muster suchen
python insightlog.py --file access.log --pattern "ERROR"

# IP-Adressen extrahieren
python insightlog.py --file access.log --extract-ips

# Report generieren
python insightlog.py --file access.log --output bericht.txt
```

---

## 📂 Projektstruktur

```
InsightLog/
├── README.md              # Diese Datei
├── requirements.txt       # Python-Abhängigkeiten
├── setup.py              # Installations-Script
│
├── insightlog/           # Haupt-Package
│   ├── __init__.py
│   ├── analyzer.py       # Kern-Analyse-Logik
│   ├── parser.py         # Log-Parsing
│   ├── patterns.py       # Regex-Muster
│   └── utils.py          # Hilfsfunktionen
│
├── tests/                # Unit-Tests
│   ├── test_analyzer.py
│   ├── test_parser.py
│   └── test_daten/       # Beispiel-Logs für Tests
│
├── docs/                 # Dokumentation
│   ├── API.md           # API-Dokumentation
│   ├── CONTRIBUTING.md  # Beitrags-Richtlinien
│   └── CHANGELOG.md     # Versions-Historie
│
├── beispiele/            # Verwendungsbeispiele
│   ├── basis_nutzung.py
│   ├── erweiterte_muster.py
│   └── beispiel_logs/   # Beispiel-Log-Dateien
│
└── scripts/             # Utility-Scripts
    ├── benchmark.py     # Performance-Tests
    └── report_erstellen.py
```

---

## 🔧 Entwicklung

### Entwicklungsumgebung einrichten

```bash
# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Im Entwicklungsmodus installieren
pip install -e .

# Dev-Abhängigkeiten installieren
pip install -r requirements-dev.txt
```

### Tests ausführen

```bash
# Alle Tests ausführen
pytest

# Mit Coverage
pytest --cov=insightlog

# Spezifischen Test ausführen
pytest tests/test_analyzer.py
```

### Code-Qualität

```bash
# Code formatieren
black insightlog/

# Code-Linting
pylint insightlog/

# Typ-Überprüfung
mypy insightlog/
```

---

## 📝 Entwicklungsfortschritt

### Aktueller Sprint
**Fokus:** Bug-Fixes und Kern-Verbesserungen

#### Abgeschlossen ✅
- [x] Initiales Repository-Setup
- [x] Projektstruktur reorganisiert
- [x] Dokumentations-Framework

#### In Arbeit 🔄
- [ ] IP-Extraktion Edge-Cases beheben
- [ ] Fehlerbehandlung verbessern
- [ ] Unit-Test-Coverage erhöhen
- [ ] Performance-Profiling

#### Backlog 📋
- [ ] JSON-Ausgabeformat
- [ ] Echtzeit-Monitoring-Feature
- [ ] Web-Dashboard
- [ ] Konfigurations-Datei-Support

---

## 🐛 Bekannte Probleme & TODOs

### Hohe Priorität
- [ ] **Bug:** Memory-Leak bei großen Log-Dateien (>1GB)
- [ ] **Bug:** Fehlerhafte Zeitzone in Timestamps
- [ ] **TODO:** Logging-Konfiguration hinzufügen
- [ ] **TODO:** Kommandozeilen-Argument-Validierung

### Mittlere Priorität
- [ ] **Verbesserung:** Support für komprimierte Logs (.gz)
- [ ] **Verbesserung:** Multi-Threading für Performance
- [ ] **TODO:** Konfigurations-Datei-Support

### Niedrige Priorität
- [ ] **Verbesserung:** Farbcodierte Terminal-Ausgabe
- [ ] **TODO:** Installer-Script erstellen

---

## 📊 Änderungsprotokoll

### Version 0.2.0 (Aktuell)
- Projektstruktur reorganisiert
- Dokumentation erweitert
- Unit-Testing-Framework hinzugefügt
- Fehlerbehandlung verbessert

### Version 0.1.0 (Original)
- Basis-Log-Parsing-Funktionalität
- IP-Adressen-Extraktion
- Muster-Matching

Siehe [CHANGELOG.md](docs/CHANGELOG.md) für detaillierte Versions-Historie.

---

## 🤝 Mitwirken

Dies ist ein Solo-Entwicklungsprojekt, aber Vorschläge und Feedback sind willkommen!

### Entwicklungs-Workflow

```bash
# Feature-Branch erstellen
git checkout -b feature/dein-feature-name

# Änderungen vornehmen und committen
git add .
git commit -m "feat: Beschreibung deiner Änderungen"

# Zum Repository pushen
git push origin feature/dein-feature-name
```

### Commit-Nachrichten-Konvention

```
feat: neues Feature
fix: Bug-Fix
docs: Dokumentations-Änderungen
test: Tests hinzufügen
refactor: Code-Refactoring
perf: Performance-Verbesserung
```

---

## 📚 Ressourcen

### Dokumentation
- [Python Logging Guide](https://docs.python.org/3/library/logging.html)
- [Regex Tutorial](https://docs.python.org/3/library/re.html)
- [Beispiel-Log-Dateien](https://github.com/logpai/loghub)

### Verwandte Projekte
- [Logstash](https://www.elastic.co/logstash/)
- [Graylog](https://www.graylog.org/)
- [Splunk](https://www.splunk.com/)

---

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](0__Workspace/0__Karriere/Projekte-Cybersteps/cybersteps-security-meeting-distributor-to-googlecalender/DE/meetup-calendar-sync/venv/Lib/site-packages/pip/_vendor/idna/LICENSE.md) Datei für Details.

---

## 📧 Kontakt

**Entwickler:** [Dein Name]  
**E-Mail:** [deine.email@beispiel.de]  
**GitHub:** [@dein-benutzername](https://github.com/dein-benutzername)

---

## 🙏 Danksagungen

- Original-Projekt von [CyberstepsDE](https://github.com/CyberstepsDE)
- Kurs-Dozenten und Mentoren
- Python-Community für exzellente Bibliotheken

---

**Zuletzt aktualisiert:** Januar 2026  
**Version:** 0.2.0  
**Status:** In aktiver Entwicklung
