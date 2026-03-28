## 📊 Zusammenfassung nach dem 80/20-Prinzip

### Was ist eine API?

Eine **API (Application Programming Interface)** ist eine Schnittstelle, die es verschiedenen Softwaresystemen ermöglicht, miteinander zu kommunizieren. Sie funktioniert wie ein Kellner im Restaurant: Der Kunde (Client) bestellt über den Kellner (API) beim Koch (Server), ohne selbst in die Küche zu gehen.

### Die wichtigsten 20% - REST-APIs

**REST** ist der am häufigsten verwendete Architekturstil für Web-APIs mit folgenden Kernprinzipien:

- **Ressourcen** werden durch URLs identifiziert (z.B. `/users/123`)
- **HTTP-Methoden** definieren Aktionen:
    - `GET` = Abrufen
    - `POST` = Erstellen
    - `PUT/PATCH` = Aktualisieren
    - `DELETE` = Löschen
- **JSON** ist das Standard-Datenformat für den Austausch
- **Zustandslosigkeit**: Jede Anfrage enthält alle nötigen Informationen

### Sicherheit: Authentifizierung vs. Autorisierung

**Authentifizierung** ("Wer bist du?") überprüft die Identität, **Autorisierung** ("Was darfst du?") prüft Berechtigungen.

**Die drei gängigsten Authentifizierungsmethoden:**

1. **API Keys**: Einfacher eindeutiger String, aber langlebig und unsicherer
2. **HTTP Basic Auth**: Benutzername:Passwort in Base64, nur mit HTTPS sicher
3. **Bearer Tokens** (OAuth 2.0/JWT): Moderner Standard mit kurzer Gültigkeit und spezifischen Berechtigungen

**Wichtigste Sicherheitsregel**: Immer HTTPS verwenden, damit Zugangsdaten nicht abgefangen werden können.

### Praktischer Nutzen von APIs

APIs ermöglichen **Modularität** (unabhängige Services), **Wiederverwendbarkeit** (gleiche Funktionalität für mehrere Apps), **Integration** (verschiedene Systeme verbinden) und **Abstraktion** (Komplexität wird verborgen).

**Beispiel aus dem Alltag**: Eine Wetter-App auf dem Smartphone ruft Temperaturdaten über eine Wetter-API ab, ohne selbst Wetterdaten zu sammeln.

---

## Verwendete Tools, Technische Fachbegriffe und Wichtige Vokabeln

|Begriff|Bedeutung|
|---|---|
|**Verwendete Tools**||
|HTTP-Protokoll|Übertragungsprotokoll für die Kommunikation zwischen Client und Server im Web|
|JSON (JavaScript Object Notation)|Leichtgewichtiges Datenformat für den Datenaustausch zwischen Systemen|
|Browser Developer Tools (F12)|Entwicklerwerkzeuge im Browser zur Analyse von Netzwerkanfragen und -antworten|
|Mermaid|Diagramm-Tool zur Visualisierung von Abläufen und Sequenzen|
|**Technische Fachbegriffe**||
|API (Application Programming Interface)|Schnittstelle, die die Kommunikation zwischen verschiedenen Softwareanwendungen ermöglicht|
|REST (Representational State Transfer)|Architekturstil für APIs, der HTTP-Standardmethoden verwendet|
|HTTP-Methoden (GET, POST, PUT, PATCH, DELETE)|Standardisierte Verben zur Durchführung von Operationen auf Ressourcen|
|Endpoint|Spezifische URL-Adresse, über die eine API-Ressource erreichbar ist|
|Request (Anfrage)|Nachricht vom Client an den Server mit URL, Methode, Headers und ggf. Body|
|Response (Antwort)|Nachricht vom Server an den Client mit Statuscode, Headers und ggf. Body|
|HTTP-Statuscode|Dreistellige Zahl, die das Ergebnis einer Anfrage anzeigt (z.B. 200, 404, 500)|
|Header|Zusätzliche Informationen in HTTP-Anfragen/-Antworten (z.B. Content-Type, Authorization)|
|Payload (Body)|Datenteil einer HTTP-Nachricht, meist in JSON-Format|
|Statelessness (Zustandslosigkeit)|Prinzip, bei dem jede Anfrage alle nötigen Informationen enthält, ohne serverseitigen Kontext|
|Resource (Ressource)|Datenelement in einer API (z.B. Benutzer, Produkt), identifiziert durch URL|
|Authentication (Authentifizierung)|Prozess zur Überprüfung der Identität eines Benutzers ("Wer bist du?")|
|Authorization (Autorisierung)|Prozess zur Prüfung von Zugriffsrechten ("Was darfst du tun?")|
|API Key (API-Schlüssel)|Eindeutiger String zur Identifizierung eines Client-Programms|
|HTTP Basic Authentication|Authentifizierungsmethode mit Base64-kodiertem Benutzername:Passwort|
|Bearer Token|Sicherheitstoken, das in der Authorization-Header übertragen wird|
|OAuth 2.0|Autorisierungs-Framework für kontrollierten Zugriff auf HTTP-Dienste|
|JWT (JSON Web Token)|Kompaktes, URL-sicheres Token-Format für Authentifizierung mit eingebetteten Claims|
|HTTPS|Verschlüsselte Version von HTTP zur sicheren Datenübertragung|
|Base64|Kodierungsverfahren zur Darstellung von Binärdaten als Text|
|**Wichtige Vokabeln**||
|Client|Anwendung oder System, das eine API nutzt (Konsument)|
|Server|System, das eine API bereitstellt (Anbieter)|
|Provider|Anbieter einer API oder eines Dienstes|
|Token|Digitaler Zugriffsnachweis mit begrenzter Gültigkeit|
|Credentials|Anmeldedaten (Benutzername, Passwort) zur Authentifizierung|
|Scope|Umfang der Berechtigungen, die ein Token gewährt|
|Claims|Informationsaussagen in einem JWT über Benutzer oder Token|
|Rate Limiting|Begrenzung der Anzahl von API-Anfragen pro Zeiteinheit|
|Revocation|Widerruf/Ungültigmachung eines Tokens oder Schlüssels|