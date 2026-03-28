## 📊 Zusammenfassung nach dem 80/20-Prinzip

### **Die Netzwerkschicht: Der Postdienst des Internets**

Die **Netzwerkschicht (Layer 3)** ist wie der Postdienst, der herausfindet, **wohin** ein Paket muss und **welchen Weg** es nehmen soll – auch über tausende Kilometer hinweg.

**Drei Hauptaufgaben**:

1. **Logische Adressierung**: Eindeutige IP-Adressen für Geräte vergeben
2. **Routing**: Besten Pfad für Pakete bestimmen
3. **Paketvermittlung**: Pakete von Router zu Router senden

**Analogie**: IP-Adresse = Postadresse | Router = Postverteilzentren | Routing = Wegfindung

### **IP (Internet Protocol): Das Arbeitspferd**

**Zwei Schlüsseleigenschaften**:

**1. Verbindungslos (Connectionless)**:

- Kein Verbindungsaufbau vor dem Senden
- Jedes Paket wird unabhängig behandelt
- Wie wenn du jede Seite eines Briefs in eigenem Umschlag verschickst

**2. Best-Effort Delivery**:

- IP versucht sein Bestes, **garantiert aber nichts**
- Pakete können verloren gehen, dupliziert werden, falsch sortiert ankommen
- Zuverlässigkeit ist Aufgabe höherer Schichten (z.B. TCP)

### **IPv4-Adressen: Das 32-Bit-System**

**Format**: 32-Bit-Zahl in **punktierter Dezimalschreibweise**

**Beispiel**: `192.168.1.100`

- Vier **Oktette** (8-Bit-Gruppen)
- Jedes Oktett: Wert von 0 bis 255
- Total: 4,3 Milliarden mögliche Adressen (zu wenig für heutige Welt!)

### **Subnetting: Netzwerke aufteilen**

Eine IP-Adresse besteht aus **zwei Teilen**:

**Subnetzmaske** zeigt die Trennung:

```
IP-Adresse:     192.168.1.100
Subnetzmaske:   255.255.255.0
                ─────────── ───
                Netzwerkteil Host-Teil
```

- **Netzwerkteil**: Identifiziert das Netzwerk (hier: `192.168.1`)
- **Host-Teil**: Identifiziert das Gerät (hier: `.100`)

**CIDR-Notation**: Kürzere Schreibweise

- `255.255.255.0` = `/24` (24 Bits für Netzwerk)
- `192.168.1.100/24` definiert IP und Subnetz

**Warum Subnetting?**

- ✅ **Organisation**: Übersichtliche Struktur
- ✅ **Sicherheit**: Isolation von Netzwerkbereichen
- ✅ **Performance**: Weniger Broadcast-Verkehr
- ✅ **Effizienz**: Bessere Adressnutzung

### **Spezielle IPv4-Adressen**

|Adresstyp|Beispiel|Bedeutung|
|---|---|---|
|**Netzwerkadresse**|192.168.1.0|Repräsentiert das gesamte Netzwerk (alle Host-Bits = 0)|
|**Broadcast-Adresse**|192.168.1.255|Sendet an alle Geräte im Netzwerk (alle Host-Bits = 1)|
|**Loopback**|127.0.0.1|Paket an sich selbst (Netzwerk-Stack-Test)|

### **Öffentliche vs. Private IP-Adressen**

**Öffentliche IP-Adressen**:

- ✅ Weltweit eindeutig
- ✅ Im Internet routbar
- ✅ Von ISP zugewiesen
- Beispiel: Dein Heimrouter bekommt eine vom Provider

**Private IP-Adressbereiche**:

- `10.0.0.0/8` (10.0.0.0 bis 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 bis 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 bis 192.168.255.255)

**Eigenschaften privater IPs**:

- ❌ Nicht im Internet routbar
- ✅ Für interne Netzwerke (Heim, Büro)
- ✅ Können mehrfach verwendet werden (in verschiedenen Netzen)

**NAT (Network Address Translation)**:

- Router übersetzt private → öffentliche IP
- Viele Geräte teilen sich eine öffentliche IP
- Lösung für IPv4-Adressknappheit

### **Praktische Befehle (Windows-Anpassung)**

**Netzwerkkonfiguration anzeigen**:

```cmd
ipconfig
```

(Zeigt IP-Adresse, Subnetzmaske, Standard-Gateway)

**Detaillierte Informationen**:

```powershell
ipconfig /all
```

**Sich selbst anpingen (Loopback-Test)**:

```cmd
ping 127.0.0.1
```

**Gateway anpingen**:

```cmd
ping [Gateway-IP]
```

**Routing-Tabelle anzeigen**:

```cmd
netstat -rn
```

oder

```cmd
route print
```

**IPv6-Adresse anzeigen**:

```powershell
ipconfig | findstr IPv6
```

**IPv6-Ping**:

```cmd
ping -6 2001:4860:4860::8888
```

(Google DNS über IPv6)

### **IPv6: Die Zukunft**

**Problem mit IPv4**: Nur ~4,3 Milliarden Adressen → **Adresserschöpfung**

**IPv6-Lösung**:

- **128-Bit-Adressen** (vs. 32-Bit bei IPv4)
- **3,4 × 10³⁸ Adressen** (praktisch unerschöpflich!)

**Format**: Acht Gruppen hexadezimaler Ziffern

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

**Abkürzungsregeln**:

1. Führende Nullen weglassen: `0db8` → `db8`
    
2. Folge von Nullen durch `::` ersetzen (nur einmal!):
    
    ```
    2001:0db8:0000:0000:0000:0000:0000:0001→ 2001:db8::1
    ```
    

**IPv6-Vorteile**:

- ✅ Riesiger Adressraum
- ✅ Vereinfachter Header (effizientere Verarbeitung)
- ✅ Kein NAT nötig (End-to-End-Konnektivität)
- ✅ Eingebaute IPSec-Unterstützung (Sicherheit)

**Dual-Stack**: Viele Netzwerke betreiben IPv4 und IPv6 parallel

### **Routing: Den Weg finden**

**Router**: Spezialgeräte, die Pakete zwischen Netzwerken vermitteln

**Routing-Tabelle** enthält:

- **Zielnetz**: Wohin soll das Paket?
- **Next Hop**: IP des nächsten Routers
- **Interface**: Welche Schnittstelle verwenden?
- **Metrik**: "Kosten" der Route (Hops, Geschwindigkeit)

**Routing-Prozess**:

1. Router empfängt Paket
2. Prüft Ziel-IP im Paket-Header
3. Sucht beste Übereinstimmung in Routing-Tabelle
4. Leitet Paket an Next Hop weiter

**Zwei Routing-Arten**:

|Statisches Routing|Dynamisches Routing|
|---|---|
|✏️ Manuell konfiguriert|🤖 Automatisch angepasst|
|✅ Einfach für kleine Netze|✅ Skalierbar für große Netze|
|❌ Nicht flexibel|✅ Passt sich Änderungen an|
|Beispiel: Heimnetzwerk|Beispiel: Internet, Firmennetzwerke|

**Routing-Protokolle** (dynamisch):

- **OSPF** (Open Shortest Path First)
- **BGP** (Border Gateway Protocol) – Internet-Backbone
- **RIP** (Routing Information Protocol)
- **EIGRP** (Enhanced Interior Gateway Routing Protocol)

### **Standard-Gateway: Der Ausgang zum Internet**

**Was ist das?**

- Router in deinem lokalen Netzwerk
- Kennt den Weg zu externen Netzwerken (Internet)
- Endgeräte senden alle externen Anfragen dorthin

**Regel**:

- **Ziel im lokalen Netz?** → Direkt senden
- **Ziel außerhalb?** → An Standard-Gateway senden

**Analogie**: Der Gateway ist wie der Ausgang aus deiner Nachbarschaft – ohne ihn kommst du nicht aus dem Viertel raus!

### **Subnetz-Beispiel: Durchrechnen**

**Gegeben**:

- IP: `10.0.1.50`
- Subnetzmaske: `255.255.0.0` (= `/16`)

**Analyse**:

```
IP:          10 . 0  . 1  . 50
Maske:      255 .255 . 0  . 0
            ──────── ────────
            Netzwerk Host-Teil
```

**Ergebnis**:

- **Netzwerkadresse**: `10.0.0.0` (alle Host-Bits auf 0)
- **Broadcast-Adresse**: `10.0.255.255` (alle Host-Bits auf 1)
- **Verfügbare Hosts**: 10.0.0.1 bis 10.0.255.254 (65.534 Geräte!)

### **Cisco Packet Tracer: Netzwerk-Simulation**

**Tool zum**:

- Virtuelle Netzwerke aufbauen
- Router und Switches konfigurieren
- Netzwerk-Szenarien testen
- Fehler beheben lernen

**Installation** (Windows):

1. NetAcad-Konto erstellen: [netacad.com](https://www.netacad.com/)
2. Packet Tracer für Windows herunterladen
3. `.exe` installieren
4. Mit NetAcad-Login anmelden

**Tipp**: Schriftgröße erhöhen (Options → Preferences → Font → CLI auf 18)

### **Kernbotschaft**

Die **Netzwerkschicht** ist das Fundament der Internet-Kommunikation:

**IP-Adressen** = Eindeutige Identifikation von Geräten **Subnetting** = Organisierte Netzwerkaufteilung **Routing** = Intelligente Pfadfindung für Pakete

**IPv4** löst das "Wohin?", ist aber am Limit → **IPv6** bietet praktisch unbegrenzte Adressen

**Router** sind die intelligenten Postverteiler, die mit **Routing-Tabellen** den besten Weg für jedes Paket finden.

**Unterschied zu höheren Schichten**:

- Layer 3 (Netzwerk): **Wo** ist das Ziel? **Wie** komme ich hin?
- Layer 4 (Transport): **Welche Anwendung** bekommt die Daten?
- Layer 7 (Anwendung): **Was** bedeuten die Daten?

Ohne Netzwerkschicht gäbe es kein Internet – sie ist der Klebstoff, der alle Netzwerke weltweit verbindet! 🌐📬🗺️

---

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **Terminal/Eingabeaufforderung**: Netzwerkbefehle ausführen (macOS: Terminal; Windows: CMD, PowerShell)<br>• **ifconfig**: Netzwerkschnittstellen anzeigen (macOS; Windows: `ipconfig`)<br>• **ip address**: Moderne Alternative zu ifconfig (macOS: `ip a`; Windows: `Get-NetIPAddress` in PowerShell)<br>• **ping**: Netzwerkverbindung testen (beide Systeme: `ping`)<br>• **ping6**: IPv6-Ping (macOS: `ping6`; Windows: `ping -6`)<br>• **netstat**: Routing-Tabellen und Netzwerkstatistiken (beide Systeme: `netstat -rn` bzw. `netstat -nr`)<br>• **traceroute/tracert**: Paketverfolgung (macOS: `traceroute`; Windows: `tracert`)<br>• **Cisco Packet Tracer**: Netzwerksimulations- und Konfigurationstool (Windows & macOS)<br>• **Wireshark**: Paketanalyse-Tool für IP-Pakete<br>• **nslookup**: DNS-Abfragen<br>• **arp**: ARP-Tabelle anzeigen (beide Systeme)<br>• **route**: Routing-Tabelle manipulieren (Windows: `route print`, `route add`)<br>• **Get-NetRoute**: PowerShell-Cmdlet für Routing (Windows)|
|**Technische Fachbegriffe**|• **Network Layer**: Netzwerkschicht (Schicht 3 im OSI-Modell)<br>• **IP** (Internet Protocol): Hauptprotokoll der Netzwerkschicht<br>• **IPv4**: Internet Protocol Version 4 (32-Bit-Adressen)<br>• **IPv6**: Internet Protocol Version 6 (128-Bit-Adressen)<br>• **IP-Adresse**: Eindeutige numerische Kennung für Netzwerkgeräte<br>• **Dotted Decimal Notation**: Punktierte Dezimalschreibweise (z.B. 192.168.1.100)<br>• **Octet**: 8-Bit-Gruppe in IPv4-Adresse (Wert 0-255)<br>• **Hexadecimal**: Hexadezimalschreibweise (IPv6)<br>• **Subnet/Subnetz**: Logische Unterteilung eines IP-Netzwerks<br>• **Subnetting**: Prozess der Netzwerkaufteilung<br>• **Subnet Mask/Subnetzmaske**: Trennung von Netzwerk- und Host-Teil<br>• **CIDR** (Classless Inter-Domain Routing): Notation mit Schrägstrich (z.B. /24)<br>• **Network Portion**: Netzwerkteil der IP-Adresse<br>• **Host Portion**: Host-Teil der IP-Adresse<br>• **Network Address**: Netzwerkadresse (alle Host-Bits = 0)<br>• **Broadcast Address**: Broadcast-Adresse (alle Host-Bits = 1)<br>• **Loopback Address**: Rückschleifenadresse (127.0.0.1)<br>• **Public IP Address**: Öffentliche IP-Adresse (weltweit eindeutig)<br>• **Private IP Address**: Private IP-Adresse (nicht im Internet routbar)<br>• **NAT** (Network Address Translation): Netzwerkadressübersetzung<br>• **Router**: Vermittlungsgerät zwischen Netzwerken<br>• **Routing**: Pfadauswahl für Pakete<br>• **Routing Table**: Routing-Tabelle<br>• **Default Gateway/Standard-Gateway**: Router für externe Verbindungen<br>• **Next Hop**: Nächster Router auf dem Weg<br>• **Metric**: Kostenwert einer Route<br>• **Static Routing**: Statisches Routing (manuelle Konfiguration)<br>• **Dynamic Routing**: Dynamisches Routing (automatische Anpassung)<br>• **Routing Protocol**: Routing-Protokoll (OSPF, BGP, RIP, EIGRP)<br>• **Connectionless**: Verbindungslos<br>• **Best-Effort Delivery**: Bemühte Zustellung ohne Garantie<br>• **Packet**: Datenpaket<br>• **Packet Forwarding**: Paketvermittlung<br>• **Interface/Schnittstelle**: Netzwerkschnittstelle (z.B. en0, eth0)<br>• **Dual-Stack**: Gleichzeitiger Betrieb von IPv4 und IPv6<br>• **IPSec**: Internet Protocol Security<br>• **Address Exhaustion**: Adresserschöpfung (IPv4)<br>• **Logical Addressing**: Logische Adressierung|
|**Wichtige Vokabeln**|• **Schicht 3**: Netzwerkschicht im OSI-Modell<br>• **Postdienst-Analogie**: Netzwerkschicht wie Postdienst für Briefsendungen<br>• **Eindeutige Adresse**: Unverwechselbare Identifikation<br>• **Netzübergreifend**: Über verschiedene Netzwerke hinweg<br>• **Bester Pfad**: Optimale Route für Pakete<br>• **Paketvermittlung**: Weiterleitung von Paketen<br>• **32-Bit-Zahl**: IPv4-Adressenlänge<br>• **128-Bit-Zahl**: IPv6-Adressenlänge<br>• **Punktierte Dezimalschreibweise**: Format wie 192.168.1.1<br>• **Oktett**: 8-Bit-Segment (0-255)<br>• **Netzwerkaufteilung**: Unterteilung in Subnetze<br>• **Organisationsstruktur**: Logische Gliederung<br>• **Sicherheitsisolierung**: Trennung von Netzwerkbereichen<br>• **Broadcast-Domäne**: Bereich für Broadcast-Verkehr<br>• **Adressverwaltung**: Effiziente Nutzung von IP-Adressen<br>• **Binäre Einsen**: 1-Bits in Subnetzmaske (Netzwerkteil)<br>• **Binäre Nullen**: 0-Bits in Subnetzmaske (Host-Teil)<br>• **Schrägstrich-Notation**: /24, /16 usw.<br>• **Netzwerkrepräsentation**: Darstellung des gesamten Netzwerks<br>• **Alle Geräte**: Broadcast an alle Hosts<br>• **Selbst-Adressierung**: Loopback für interne Tests<br>• **Weltweit eindeutig**: Öffentliche IPs im Internet<br>• **Nicht routbar**: Private IPs nur lokal gültig<br>• **Adressübersetzung**: NAT-Mechanismus<br>• **Gemeinsame öffentliche IP**: Mehrere Geräte nutzen eine IP<br>• **Routerfunktion**: Paketvermittlung zwischen Netzen<br>• **Pfadauswahl**: Entscheidung für beste Route<br>• **Nächster Sprung**: Next Hop zum Ziel<br>• **Kosten einer Route**: Metrik (Hops, Geschwindigkeit)<br>• **Manuelle Konfiguration**: Statisches Routing<br>• **Automatische Anpassung**: Dynamisches Routing<br>• **Externe Verbindungen**: Zugang zu anderen Netzwerken<br>• **Lokales Netzwerk**: Direkt verbundene Geräte<br>• **Hexadezimale Schreibweise**: IPv6-Format<br>• **Astronomische Anzahl**: Riesiger IPv6-Adressraum<br>• **End-to-End-Konnektivität**: Direkte Verbindung ohne NAT<br>• **Vereinfachter Header**: Effizientere Verarbeitung|