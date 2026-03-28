## 📊 Zusammenfassung nach dem 80/20-Prinzip

**Was ist HTTP?** HTTP (Hypertext Transfer Protocol) ist das grundlegende Kommunikationsprotokoll des Internets. Es definiert, wie Webbrowser (Clients) Webseiten von Servern anfordern und wie Server darauf antworten.

**Grundprinzipien:**

1. **Client-Server-Modell**: Ihr Browser sendet eine Anfrage (Request), der Server antwortet (Response)
2. **Zustandslosigkeit**: Jede Anfrage ist unabhängig – der Server "erinnert sich" nicht an vorherige Anfragen
3. **Ressourcen & URLs**: Alles im Web (Webseiten, Bilder, Daten) ist über URLs identifizierbar

**Die wichtigsten HTTP-Methoden:**

- **GET**: Webseite oder Daten abrufen (nur lesend)
- **POST**: Daten senden (z.B. Formulare absenden)

**Die wichtigsten Statuscodes:**

- **200 OK**: Alles hat funktioniert
- **404 Not Found**: Seite existiert nicht
- **500 Internal Server Error**: Server-Problem

**HTTP vs. HTTPS:**

- **HTTP**: Unverschlüsselte Übertragung – unsicher
- **HTTPS**: Verschlüsselte Übertragung mit TLS/SSL – sicher und mittlerweile Standard

**Praktischer Nutzen:** Mit den Browser Developer Tools (F12 bzw. Rechtsklick → "Untersuchen" → Network-Tab) können Sie alle HTTP-Anfragen live beobachten und analysieren – perfekt zum Lernen und Debuggen.

**Wichtigste Erkenntnis:** HTTP ist textbasiert und folgt einem einfachen Anfrage-Antwort-Muster. Jede Webinteraktion läuft über diesen Zyklus: Browser fragt → Server antwortet → Browser zeigt Ergebnis an.

---

## Kategorisierung

|Kategorie|Begriff|Bedeutung|
|---|---|---|
|**Verwendete Tools**|Browser Developer Tools|Entwicklerwerkzeuge in modernen Browsern (Chrome, Firefox) zur Inspektion des Netzwerkverkehrs|
||Network Tab|Registerkarte in den Developer Tools zur Anzeige aller HTTP-Anfragen|
||curl|Kommandozeilen-Tool zum Senden von HTTP-Anfragen|
||Apache / Nginx / IIS|Webserver-Software zum Hosten und Bereitstellen von Webressourcen|
|**Technische Fachbegriffe**|HTTP (Hypertext Transfer Protocol)|Regelwerk für die Kommunikation zwischen Webbrowser und Webserver|
||HTTPS (HTTP Secure)|Verschlüsselte Version von HTTP mit TLS/SSL-Verschlüsselung|
||Client-Server-Modell|Architektur, bei der der Client Anfragen stellt und der Server antwortet|
||Request-Response-Zyklus|Der Ablauf von Anfrage (Request) und Antwort (Response) bei HTTP|
||Statelessness (Zustandslosigkeit)|Jede HTTP-Anfrage wird unabhängig behandelt, ohne Speicherung vorheriger Anfragen|
||URL (Uniform Resource Locator)|Adresse zur Identifizierung einer Webressource (z.B. Webseite, Bild)|
||DNS (Domain Name System)|System zur Auflösung von Domainnamen in IP-Adressen|
||TCP|Transport-Protokoll, auf dem HTTP aufbaut (Port 80 für HTTP, Port 443 für HTTPS)|
||Application Layer (Anwendungsschicht)|Oberste Schicht im 5-Schichten-Netzwerkmodell|
||Headers (Kopfzeilen)|Metadaten in HTTP-Nachrichten (Name-Wert-Paare)|
||Message Body (Nachrichtenrumpf)|Eigentlicher Dateninhalt einer HTTP-Nachricht|
||TLS/SSL|Verschlüsselungsprotokolle für sichere Datenübertragung|
||Idempotent|Eigenschaft einer Operation, die bei mehrfacher Ausführung dasselbe Ergebnis liefert|
||CRLF|Carriage Return Line Feed - Zeilenumbruch in HTTP-Nachrichten|
|**HTTP-Methoden**|GET|Abrufen einer Ressource (nur lesend, keine Zustandsänderung)|
||POST|Senden von Daten zur Verarbeitung (z.B. Formularübermittlung)|
||PUT|Ersetzen einer Ressource durch neue Daten|
||DELETE|Löschen einer angegebenen Ressource|
||HEAD|Abrufen nur der Header ohne Body (zur Metadatenprüfung)|
||OPTIONS|Abfragen verfügbarer Kommunikationsoptionen|
||PATCH|Teilweise Änderung einer Ressource|
|**HTTP-Statuscodes**|1xx|Informativ - Anfrage empfangen, Verarbeitung läuft|
||2xx|Erfolg (z.B. 200 OK, 201 Created, 204 No Content)|
||3xx|Umleitung (z.B. 301 Moved Permanently, 302 Found)|
||4xx|Client-Fehler (z.B. 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)|
||5xx|Server-Fehler (z.B. 500 Internal Server Error, 503 Service Unavailable)|
|**URL-Komponenten**|Scheme (Schema)|Protokoll-Bezeichnung (http:// oder https://)|
||Host (Domain)|Domainname oder IP-Adresse des Servers|
||Path (Pfad)|Speicherort der Ressource auf dem Server|
||Query String|Parameter zur Datenübergabe (beginnt mit ?)|
||Fragment|Abschnittskennung innerhalb der Ressource (beginnt mit #)|
|**Wichtige Header**|Host|Zieldomain des Servers (erforderlich in HTTP/1.1)|
||User-Agent|Identifikation der Client-Software|
||Accept|Vom Client bevorzugte Inhaltstypen|
||Content-Type|Typ des übertragenen Inhalts|
||Content-Length|Größe des Message Body in Bytes|
||Location|Neue URL bei Weiterleitungen|
|**Sicherheitskonzepte**|Confidentiality (Vertraulichkeit)|Schutz vor unbefugtem Mitlesen durch Verschlüsselung|
||Integrity (Integrität)|Sicherstellung, dass Daten nicht manipuliert wurden|
||Authentication (Authentifizierung)|Überprüfung der Server-Identität mittels Zertifikaten|
||Man-in-the-Middle-Attack|Angriff durch Abfangen und Manipulieren der Kommunikation|