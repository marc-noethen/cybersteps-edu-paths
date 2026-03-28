## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Was ist Server-Side Development?

Server-Side Code läuft auf einem Webserver (nicht im Browser) und kann auf Datenbanken und Server-Ressourcen zugreifen. Er generiert dynamische HTML-Inhalte basierend auf Nutzeranfragen.

### Flask Grundlagen

**Flask** ist ein Python-Framework für Webentwicklung. Es ist leichtgewichtig, flexibel und einfach zu erlernen.

**Installation (Windows 11):**

```bash
pip install Flask
```

**Minimale Flask-Anwendung:**

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hallo Welt!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Die 3 Kernkonzepte:

1. **Routing** - URLs werden mit `@app.route('/pfad')` auf Python-Funktionen gemappt
2. **View Functions** - Funktionen, die Requests verarbeiten und Responses zurückgeben
3. **Templates** - HTML-Dateien mit Platzhaltern `{{ variable }}`) für dynamische Inhalte

### Request-Response Zyklus:

1. Browser sendet HTTP-Request an Server
2. Flask findet passende Route
3. View Function wird ausgeführt
4. Response (meist HTML) wird an Browser zurückgesendet
5. Browser rendert die Seite

### Wichtige Parameter:

- `debug=True` - Automatisches Neuladen + Fehleranzeige (nur in Entwicklung!)
- `host='0.0.0.0'` - Server von überall im Netzwerk erreichbar
- `port=5000` - Standard-Port für Flask

**Praktischer Tipp:** Mit `render_template()` können Sie HTML-Templates mit dynamischen Daten befüllen, statt HTML-Code direkt in Python zu schreiben.

---

## Übersichtstabelle

|Kategorie|Inhalt|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Flask|Micro-Webframework für Python zur Entwicklung von Webanwendungen|
||pip / pip3|Paketmanager für Python zur Installation von Bibliotheken|
||Python|Programmiersprache für die Server-seitige Entwicklung|
||Jinja2|Template-Engine für dynamische HTML-Generierung|
||Werkzeug|WSGI-Bibliothek (wird von Flask intern verwendet)|
||Terminal / Eingabeaufforderung|Kommandozeilen-Tool zur Ausführung von Befehlen (Windows: CMD oder PowerShell)|
|**Technische Fachbegriffe**|Client-Side|Code, der im Webbrowser des Nutzers ausgeführt wird (HTML, CSS, JavaScript)|
||Server-Side|Code, der auf einem Webserver ausgeführt wird (z.B. Python mit Flask)|
||HTTP Request|Anfrage vom Browser an den Server|
||HTTP Response|Antwort vom Server an den Browser|
||Routing|Zuordnung von URLs zu spezifischen Python-Funktionen|
||View Function|Funktion, die eine Route verarbeitet und eine Antwort zurückgibt|
||Decorator `@app.route()`)|Python-Syntax zur Definition von Routen|
||Template|HTML-Datei mit Platzhaltern für dynamische Inhalte|
||Rendering|Prozess der Umwandlung eines Templates in fertiges HTML|
||Debug Mode|Entwicklungsmodus mit automatischem Neuladen und Fehleranzeige|
||Port|Netzwerk-Endpunkt für die Kommunikation (Standard: 5000)|
||localhost / 127.0.0.1|Lokale IP-Adresse des eigenen Computers|
|**Wichtige Vokabeln**|Web Framework|Sammlung von Tools und Bibliotheken zur vereinfachten Web-Entwicklung|
||Micro Framework|Schlankes Framework mit minimalem Kern, aber erweiterbar|
||Request-Response Cycle|Ablauf von Anfrage bis Antwort zwischen Browser und Server|
||Dynamic Content|Inhalte, die zur Laufzeit generiert werden (z.B. personalisierte Seiten)|
||Extension|Zusatzmodul zur Erweiterung von Flask-Funktionalität|
||Development Server|Integrierter Testserver für die Entwicklung (nicht für Produktion)|
||Production Environment|Live-Umgebung für echte Nutzer (hier kein Debug-Modus!)|