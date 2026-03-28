## 📊 Zusammenfassung nach dem 80/20-Prinzip

**Das Problem:** HTTP ist zustandslos – jede Anfrage ist unabhängig, der Server "vergisst" vorherige Interaktionen. Moderne Webanwendungen müssen sich aber an Nutzer erinnern (Login, Warenkorb, Einstellungen).

**Die Lösung: Cookies** – Der Server schickt kleine Datenpakete (`Set-Cookie` Header) an den Browser, der diese speichert und bei jeder weiteren Anfrage zurücksendet (`Cookie` Header). So erkennt der Server den Nutzer wieder.

**Zwei Cookie-Typen:**

- **Session Cookies:** Temporär, werden beim Schließen des Browsers gelöscht
- **Persistent Cookies:** Dauerhaft mit Ablaufdatum, überleben Browser-Neustarts

**Kritische Sicherheitsattribute:**

- `HttpOnly` – schützt vor JavaScript-Zugriff (XSS-Schutz)
- `Secure` – nur über HTTPS übertragen
- `SameSite` – verhindert ungewollte Cross-Site-Anfragen (CSRF-Schutz)

**Best Practice: Server-Side Sessions** – Statt alle Daten im Cookie zu speichern, speichert der Server die Daten und sendet nur eine Session-ID als Cookie. Sicherer und flexibler.

**Hauptrisiken:** Session Hijacking (gestohlene Cookies), XSS-Angriffe, CSRF-Attacken und Tracking durch Drittanbieter-Cookies.

**Praktisch lernen:** Mit Browser Developer Tools (F12 → Application/Storage Tab) können Sie alle Cookies einer Website inspizieren und deren Attribute einsehen.

---

## Tabelle 1: Verwendete Tools

|Verwendete Tools|Bedeutung|
|---|---|
|Browser Developer Tools (F12)|Entwicklerwerkzeuge zum Inspizieren von Cookies und HTTP-Verkehr|
|Application/Storage Tab|Bereich in den Developer Tools zum Anzeigen gespeicherter Daten (Cookies, LocalStorage etc.)|
|Network Tab|Bereich zum Überwachen von HTTP-Requests und -Responses inklusive Cookie-Headers|
|Rechtsklick → "Untersuchen"|Alternative Methode zum Öffnen der Developer Tools|

**Windows 11 Anpassung:** Die Tastenkombination `F12` oder `Strg+Umschalt+I` funktioniert identisch unter Windows 11 (statt `Cmd+Opt+I` auf macOS).

---

## Tabelle 2: Technische Fachbegriffe

|Technische Fachbegriffe|Bedeutung|
|---|---|
|HTTP (Hypertext Transfer Protocol)|Zustandsloses Protokoll für Datenkommunikation im Web|
|Stateless Protocol|Protokoll, bei dem jede Anfrage unabhängig behandelt wird – keine automatische Erinnerung an vorherige Anfragen|
|State Management|Verwaltung von Zustandsinformationen über mehrere Anfragen hinweg|
|Cookie|Kleine Datenmenge, die vom Server im Browser gespeichert wird|
|Session Cookie|Temporärer Cookie ohne Ablaufdatum, wird beim Schließen des Browsers gelöscht|
|Persistent Cookie|Dauerhafter Cookie mit festgelegtem Ablaufdatum|
|Set-Cookie Header|HTTP-Response-Header, mit dem Server Cookies im Browser setzen|
|Cookie Header|HTTP-Request-Header, mit dem Browser Cookies an Server zurücksendet|
|Session ID|Eindeutige Kennung für eine Benutzersitzung|
|Server-Side Sessions|Sessiondaten werden auf dem Server gespeichert, nur die Session-ID wird im Cookie übertragen|
|Third-Party Cookies|Cookies von Drittanbietern (z.B. Werbenetzwerke), die Nutzerverhalten über mehrere Websites tracken|
|Session Hijacking|Angriff, bei dem ein Angreifer den Session-Cookie eines Nutzers stiehlt|
|XSS (Cross-Site Scripting)|Sicherheitslücke, bei der Angreifer Schadcode in Webseiten einschleusen|
|CSRF (Cross-Site Request Forgery)|Angriff, bei dem Nutzer ungewollt schädliche Anfragen an authentifizierte Websites senden|

---

## Tabelle 3: Wichtige Cookie-Attribute (Vokabeln)

|Wichtige Vokabeln|Bedeutung|
|---|---|
|`Expires=<date>`|Ablaufdatum des Cookies (Datum und Uhrzeit)|
|`Max-Age=<seconds>`|Lebensdauer des Cookies in Sekunden (hat Vorrang vor Expires)|
|`Domain=<domain-name>`|Gibt an, für welche Domain(s) der Cookie gültig ist|
|`Path=<path>`|URL-Pfad, für den der Cookie gültig ist|
|`Secure`|Cookie wird nur über verschlüsselte HTTPS-Verbindungen übertragen|
|`HttpOnly`|Cookie kann nicht per JavaScript zugegriffen werden (Schutz vor XSS)|
|`SameSite=Strict`|Cookie wird nur bei Anfragen von derselben Website gesendet|
|`SameSite=Lax`|Cookie bei Same-Site-Anfragen und Top-Level-Navigation (Standard)|
|`SameSite=None`|Cookie wird bei allen Anfragen gesendet (erfordert `Secure`)|