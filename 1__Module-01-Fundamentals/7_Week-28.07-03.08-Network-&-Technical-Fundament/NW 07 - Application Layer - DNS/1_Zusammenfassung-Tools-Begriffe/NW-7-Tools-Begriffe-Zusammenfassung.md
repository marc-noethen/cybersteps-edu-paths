## 📊 Zusammenfassung nach dem 80/20-Prinzip

### **Was ist DNS? Das Internet-Telefonbuch**

DNS (Domain Name System) übersetzt **menschenlesbare Domainnamen** (wie `google.com`) in **maschinenlesbare IP-Adressen** (wie `142.250.180.142`). Ohne DNS müssten wir uns alle IP-Adressen merken – praktisch unmöglich!

**Analogie**: DNS ist wie ein Telefonbuch – du suchst nach einem Namen und erhältst die Telefonnummer (IP-Adresse).

### **Die DNS-Hierarchie: Ein umgekehrter Baum**

DNS ist hierarchisch organisiert, von oben nach unten:

1. **Root Zone (.)** – Die Wurzel des Systems (hunderte Server weltweit)
2. **TLDs (Top-Level Domains)** – Endungen wie `.com`, `.org`, `.de`
3. **SLDs (Second-Level Domains)** – Deine registrierte Domain wie `google` in `google.com`
4. **Subdomains** – Weitere Unterteilungen wie `mail.google.com`

**Beispiel**: `www.google.com.` = Subdomain (www) + SLD (google) + TLD (com) + Root (.)

**Wichtig**: Diese Struktur macht DNS skalierbar – keine einzelne Instanz muss alles wissen!

### **Wie funktioniert eine DNS-Abfrage? Der 8-Schritte-Prozess**

Wenn du `www.example.com` eingibst:

1. **Lokaler Cache** – Computer prüft eigenen Speicher
2. **Recursive Resolver** – Dein ISP oder öffentlicher DNS (8.8.8.8, 1.1.1.1) übernimmt
3. **Root Server** – "Wo finde ich .com?"
4. **TLD Server** – ".com Server weiß wo example.com ist"
5. **Authoritative Server** – "example.com's Server kennt www.example.com"
6. **Finale Antwort** – IP-Adresse wird zurückgesendet
7. **Caching** – Ergebnis wird gespeichert (TTL beachten)
8. **Verbindung** – Browser verbindet sich mit der IP-Adresse

**Zeitaufwand**: Normalerweise nur Millisekunden!

### **Die wichtigsten DNS-Record-Typen**

|Record-Typ|Bedeutung|Beispiel|
|---|---|---|
|**A**|IPv4-Adresse|`google.com` → `142.250.180.142`|
|**AAAA**|IPv6-Adresse|`google.com` → `2a00:1450:4005:80a::200e`|
|**CNAME**|Alias/Verweis|`www.example.com` → `example.com`|
|**MX**|Mail-Server|E-Mail-Zustellung mit Priorität|
|**NS**|Name-Server|Delegierung an zuständige Server|
|**TXT**|Textinformation|Domain-Verifizierung, E-Mail-Sicherheit|

**Merke**: **A** und **AAAA** sind die Grundpfeiler – sie liefern die eigentlichen IP-Adressen!

### **DNS-Caching und TTL: Geschwindigkeit vs. Aktualität**

**Caching** speichert DNS-Antworten temporär (im Browser, Betriebssystem, Resolver), um wiederholte Anfragen zu beschleunigen.

**TTL (Time-To-Live)** bestimmt, wie lange ein Eintrag gecacht werden darf:

- **Kurze TTL** (60-300 Sek.) → Änderungen schnell sichtbar, aber mehr Server-Last
- **Lange TTL** (86400 Sek. = 24h) → Weniger Last, aber Änderungen brauchen länger

**Balance finden**: Stabile Domains → lange TTL; häufige Änderungen → kurze TTL

### **Praktischer Test (Windows-Anpassung)**

Öffne die **Eingabeaufforderung** oder **PowerShell**:

```cmd
ping -n 1 google.com
```

→ Zeigt die aufgelöste IP-Adresse

```cmd
ping -n 1 heise.de
```

→ Andere Domain, andere IP

```cmd
ping -n 1 non-existent-domain-12345.com
```

→ Fehler: "Ping-Anforderung konnte Host nicht finden" = DNS-Auflösung fehlgeschlagen

**Zusätzliche Tools für Windows**:

```cmd
nslookup google.com
```

→ Zeigt detaillierte DNS-Informationen

### **Öffentliche DNS-Resolver: Alternative zu ISP-DNS**

Statt des DNS-Servers deines Internetanbieters kannst du öffentliche Resolver nutzen:

- **Google**: `8.8.8.8` und `8.8.4.4`
- **Cloudflare**: `1.1.1.1` und `1.0.0.1`

**Vorteile**: Oft schneller, mehr Privatsphäre, zuverlässiger

**Nachteile**: Externer Anbieter sieht deine DNS-Anfragen

### **Kernbotschaft**

DNS ist das **unsichtbare Rückgrat des Internets** – ein verteiltes, hierarchisches System, das in Millisekunden menschenfreundliche Namen in maschinenlesbare Adressen übersetzt. Ohne DNS wäre das moderne Internet praktisch unbrauchbar!

**Rekursiv** (dein Resolver macht die Arbeit) und **iterativ** (Resolver fragt Schritt für Schritt) arbeiten zusammen, um jede Anfrage in Sekundenbruchteilen zu beantworten.

---

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **Terminal**: Kommandozeilen-Tool (macOS: Terminal; Windows: Eingabeaufforderung, PowerShell, Windows Terminal)<br>• **ping**: Netzwerkdiagnose-Tool zum Testen von Verbindungen (auf beiden Systemen verfügbar)<br>• **nslookup**: DNS-Abfrage-Tool (Windows & macOS)<br>• **dig**: Erweiterte DNS-Abfrage (macOS vorinstalliert; Windows: über BIND-Installation)<br>• **hosts-Datei**: Lokale Namensauflösung (macOS: `/etc/hosts`; Windows: `C:\Windows\System32\drivers\etc\hosts`)<br>• **Spotlight**: Suchfunktion (macOS: Cmd+Space; Windows: Windows-Taste für Suche)<br>• **Öffentliche DNS-Resolver**: Google DNS (8.8.8.8), Cloudflare (1.1.1.1)|
|**Technische Fachbegriffe**|• **DNS** (Domain Name System): Internet-Namensauflösungssystem<br>• **IP-Adresse**: Numerische Netzwerkadresse (IPv4: z.B. 142.250.180.142; IPv6: z.B. 2a00:1450:4005:80a::200e)<br>• **Root Zone**: Oberste Ebene der DNS-Hierarchie<br>• **TLD** (Top-Level Domain): Domainendungen wie .com, .org, .de<br>• **SLD** (Second-Level Domain): Registrierte Domain wie "google" in google.com<br>• **Subdomain**: Unterbereich einer Domain (z.B. mail.google.com)<br>• **FQDN** (Fully Qualified Domain Name): Vollständiger Domainname mit abschließendem Punkt<br>• **Recursive Resolver**: DNS-Server der vollständige Anfragen bearbeitet<br>• **Authoritative Name Server**: DNS-Server mit offiziellen Domain-Informationen<br>• **Recursive Query**: Anfrage, bei der der Resolver die vollständige Auflösung übernimmt<br>• **Iterative Query**: Schrittweise Anfrage durch verschiedene DNS-Server-Ebenen<br>• **DNS Cache**: Temporärer Speicher für DNS-Abfragen<br>• **TTL** (Time-To-Live): Gültigkeitsdauer von DNS-Einträgen in Sekunden<br>• **DNS Records**: Datensätze in DNS-Servern<br>• **Reverse DNS Lookup**: Rückwärts-Auflösung von IP zu Hostname|
|**Wichtige Vokabeln**|• **Namensauflösung**: Übersetzung von Domain-Namen zu IP-Adressen<br>• **Hierarchie**: Baumstruktur des DNS-Systems<br>• **Delegierung**: Weitergabe von Zuständigkeit an untergeordnete Server<br>• **Skalierbarkeit**: Fähigkeit des Systems zu wachsen<br>• **Resilienz**: Ausfallsicherheit und Robustheit<br>• **Propagierung**: Verbreitung von DNS-Änderungen im Internet<br>• **A Record**: IPv4-Adresszuordnung<br>• **AAAA Record** (Quad-A): IPv6-Adresszuordnung<br>• **CNAME Record**: Alias-Name für eine Domain<br>• **MX Record**: Mail-Server-Zuordnung<br>• **NS Record**: Name-Server-Delegierung<br>• **TXT Record**: Textinformationen (SPF, DKIM, DMARC)<br>• **PTR Record**: Pointer für Reverse-DNS<br>• **ISP** (Internet Service Provider): Internetanbieter<br>• **Millisekunden**: Zeiteinheit für DNS-Abfragen<br>• **Prioritätswert**: Reihenfolge bei MX-Records<br>• **Domain-Registrierung**: Anmeldung einer Domain<br>• **Hosts-Datei**: Lokale manuelle Namensauflösung|