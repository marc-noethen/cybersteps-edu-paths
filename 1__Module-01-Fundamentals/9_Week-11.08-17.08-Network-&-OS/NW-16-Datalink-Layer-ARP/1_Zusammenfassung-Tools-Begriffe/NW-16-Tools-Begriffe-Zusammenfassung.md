# Kategorisierung ARP (Address Resolution Protocol)

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **Terminal/Eingabeaufforderung**: ARP-Cache anzeigen (macOS: `arp -a`; Windows: `arp -a` oder `arp /a`)<br>• **PowerShell**: `Get-NetNeighbor` (zeigt ARP-Cache in Windows)<br>• **arp**: ARP-Tabelle verwalten (beide Systeme: `arp -a`, `arp -d`, `arp -s`)<br>• **Wireshark**: ARP-Pakete analysieren und aufzeichnen<br>• **tcpdump**: ARP-Traffic mitschneiden (macOS: `tcpdump arp`; Windows: WinDump)<br>• **arping**: ARP-Anfragen manuell senden (Linux/macOS; Windows: über Tools)<br>• **ping**: Kommunikation initiieren (löst ARP aus)<br>• **netsh**: Netzwerk-Konfiguration (Windows: `netsh interface ipv4 show neighbors`)<br>• **System Settings/Einstellungen**: Netzwerkeinstellungen prüfen<br>• **Network Monitor**: Erweiterte Netzwerkanalyse (Windows)<br>• **arpwatch**: ARP-Monitoring-Tool (Unix/Linux)<br>• **Packet Tracer**: ARP-Simulation in Cisco-Umgebungen|
|**Technische Fachbegriffe**|• **ARP** (Address Resolution Protocol): Adressauflösungsprotokoll<br>• **IP Address**: Internet Protocol-Adresse (Layer 3)<br>• **MAC Address**: Media Access Control-Adresse (Layer 2)<br>• **Layer 2**: Datenverbindungsschicht (Data Link Layer)<br>• **Layer 3**: Netzwerkschicht (Network Layer)<br>• **Address Resolution**: Adressauflösung (IP → MAC)<br>• **ARP Request**: ARP-Anfrage (Broadcast)<br>• **ARP Reply**: ARP-Antwort (Unicast)<br>• **ARP Cache/Table**: ARP-Cache/Tabelle (temporärer Speicher)<br>• **Broadcast**: Rundsendung an alle Geräte<br>• **Unicast**: Einzelsendung an ein spezifisches Gerät<br>• **Broadcast MAC Address**: FF:FF:FF:FF:FF:FF<br>• **Local Network Segment**: Lokales Netzwerksegment<br>• **Broadcast Domain**: Broadcast-Bereich<br>• **Ethernet Frame**: Ethernet-Rahmen<br>• **NIC** (Network Interface Card): Netzwerkkarte<br>• **Default Gateway**: Standard-Gateway (Router)<br>• **Dynamic Entry**: Dynamischer Eintrag (zeitlich begrenzt)<br>• **Static Entry**: Statischer Eintrag (permanent)<br>• **Timeout/TTL**: Ablaufzeit/Gültigkeitsdauer<br>• **Opcode**: Operations-Code (1=Request, 2=Reply)<br>• **Hardware Type**: Hardware-Typ (z.B. Ethernet)<br>• **Protocol Type**: Protokoll-Typ (z.B. IPv4)<br>• **Sender MAC/IP**: Absender-MAC/IP-Adresse<br>• **Target MAC/IP**: Ziel-MAC/IP-Adresse<br>• **ARP Spoofing/Poisoning**: ARP-Täuschungsangriff<br>• **MITM** (Man-in-the-Middle): Angriff durch ARP-Manipulation<br>• **Gratuitous ARP**: Unaufgefordertes ARP (IP-Konfliktprüfung)<br>• **Proxy ARP**: ARP-Proxy (Router antwortet für andere Netze)<br>• **Reverse ARP (RARP)**: Umgekehrtes ARP (MAC → IP, veraltet)<br>• **IPv6 Neighbor Discovery**: IPv6-Nachbarschaftserkennung (ersetzt ARP)|
|**Wichtige Vokabeln**|• **Adressauflösung**: Übersetzung von IP zu MAC<br>• **Lokales Netzwerksegment**: Direktverbundener Netzwerkbereich<br>• **Physikalische Adresse**: Hardware-Adresse (MAC)<br>• **Logische Adresse**: Netzwerkadresse (IP)<br>• **Nachschlagen**: Suche nach Zuordnung<br>• **Zuordnung**: Mapping/Verknüpfung IP ↔ MAC<br>• **Zwischenspeicher**: Temporärer Cache<br>• **Kürzlich gelernt**: Dynamisch erfasste Einträge<br>• **Ablaufzeit**: Timeout-Periode<br>• **Veraltete Information**: Stale/überholte Daten<br>• **Grenzbereich**: Boundary zwischen Layern<br>• **Statuslos**: Stateless (keine persistente Verbindung)<br>• **Anfrage-Antwort**: Request-Response-Mechanismus<br>• **Fluten**: Flooding (Broadcast auf allen Ports)<br>• **Still verwerfen**: Silently discard (ohne Benachrichtigung)<br>• **Einkapseln**: Encapsulation (in Ethernet-Frame)<br>• **Weiterleiten**: Forwarding<br>• **Eingebrannt**: Burned-in (fest in Hardware)<br>• **Endgültige Zustellung**: Final delivery<br>• **Gemeinsam genutzt**: Shared (gemeinsames Segment)<br>• **Überbrückung**: Bridge (zwischen Layern)<br>• **Verifizierung**: Überprüfung der Identität<br>• **Missbrauch**: Abuse (Sicherheitsverletzung)<br>• **Vertrauen**: Trust (in ARP-System)<br>• **Gefälschte Antwort**: Spoofed reply<br>• **Kompromittierung**: Compromise (Sicherheitsbruch)|

---

## 80/20-Zusammenfassung: Die wichtigsten 20% zum Verständnis von 80% von ARP

### **Das Problem: IP kennen, aber MAC brauchen**

**Szenario**: Computer A will Daten an Computer B im **selben lokalen Netzwerk** senden

```
Computer A kennt:
- Eigene IP: 192.168.1.10
- Eigene MAC: AA:AA:AA:AA:AA:AA
- Ziel-IP: 192.168.1.20

Computer A kennt NICHT:
- Ziel-MAC: ??? (braucht aber MAC für Ethernet-Frame!)
```

**Warum ist das ein Problem?**

**Layer 3 (IP)**: Routing zwischen Netzwerken → IP-Adressen **Layer 2 (Ethernet)**: Zustellung im lokalen Netz → MAC-Adressen

```
┌──────────────────────────────────────────┐
│  IP-Paket (Layer 3)                      │
│  Quell-IP: 192.168.1.10                  │
│  Ziel-IP:  192.168.1.20                  │
└──────────────────────────────────────────┘
           ↓ Muss eingekapselt werden
┌──────────────────────────────────────────┐
│  Ethernet-Frame (Layer 2)                │
│  Quell-MAC: AA:AA:AA:AA:AA:AA            │
│  Ziel-MAC:  ??? (UNBEKANNT!)             │
│  Payload: [IP-Paket]                     │
└──────────────────────────────────────────┘
```

**Frage**: Wie findet Computer A die MAC-Adresse von Computer B?

**Antwort**: **ARP (Address Resolution Protocol)**! 🔍

### **Was ist ARP? Der IP-zu-MAC-Übersetzer**

**ARP (Address Resolution Protocol)** = Protokoll zur **Auflösung von IP-Adressen zu MAC-Adressen** im lokalen Netzwerk

**Funktion**: Dynamisches Nachschlagewerk für IP ↔ MAC Zuordnung

**Eigenschaften**:

- ⚙️ Arbeitet zwischen Layer 2 und Layer 3
- 📡 Nur im **lokalen Netzwerksegment** (nicht über Router hinweg)
- 🔄 **Statuslos** (keine persistente Verbindung)
- 📋 **Request-Response-Mechanismus**

**Analogie**: ARP ist wie ein **Telefonbuch für das lokale Netzwerk** – du kennst den Namen (IP), suchst die Telefonnummer (MAC)

### **Wie ARP funktioniert: Der 5-Schritte-Prozess**

#### **Schritt 1: ARP-Cache prüfen** 🗂️

```
Computer A: "Will an 192.168.1.20 senden..."
          ↓
Computer A prüft ARP-Cache:
"Habe ich die MAC für 192.168.1.20 schon?"

Fall A: JA → Direkt senden (kein ARP nötig)
Fall B: NEIN → ARP-Anfrage starten
```

**ARP-Cache** = Temporärer Speicher für IP↔MAC-Zuordnungen

#### **Schritt 2: ARP Request senden (Broadcast) 📢**

```
Computer A erstellt ARP Request:
"Wer hat IP 192.168.1.20? Bitte antworten an 192.168.1.10!"

Ethernet-Frame:
┌────────────────────────────────────────┐
│ Quell-MAC:  AA:AA:AA:AA:AA:AA (A)      │
│ Ziel-MAC:   FF:FF:FF:FF:FF:FF (Broadcast!) │
│ Typ: ARP                               │
│ ──────────────────────────────────────│
│ ARP Request:                           │
│  - Opcode: 1 (Request)                 │
│  - Sender MAC: AA:AA:AA:AA:AA:AA       │
│  - Sender IP:  192.168.1.10            │
│  - Target MAC: 00:00:00:00:00:00 (?)   │
│  - Target IP:  192.168.1.20            │
└────────────────────────────────────────┘

Frame wird an ALLE Geräte im lokalen Netz gesendet!
```

**Wichtig**: **Broadcast-MAC** = `FF:FF:FF:FF:FF:FF` → Switch flutet an alle Ports

#### **Schritt 3: ARP Request verarbeiten** 🎯

```
Alle Geräte im Netzwerk empfangen Broadcast:

Computer B (192.168.1.20):
"Hey, das ist meine IP! Ich antworte!"
→ Speichert auch: A's IP (192.168.1.10) ↔ MAC (AA:AA:AA:AA:AA:AA)

Computer C (192.168.1.30):
"Nicht meine IP, ignorieren."
→ Still verwerfen

Computer D (192.168.1.40):
"Auch nicht meine IP, ignorieren."
→ Still verwerfen
```

**Nur das Zielgerät antwortet!**

#### **Schritt 4: ARP Reply senden (Unicast) 📬**

```
Computer B erstellt ARP Reply:
"Ich habe IP 192.168.1.20, meine MAC ist BB:BB:BB:BB:BB:BB!"

Ethernet-Frame:
┌────────────────────────────────────────┐
│ Quell-MAC:  BB:BB:BB:BB:BB:BB (B)      │
│ Ziel-MAC:   AA:AA:AA:AA:AA:AA (A, Unicast!) │
│ Typ: ARP                               │
│ ──────────────────────────────────────│
│ ARP Reply:                             │
│  - Opcode: 2 (Reply)                   │
│  - Sender MAC: BB:BB:BB:BB:BB:BB       │
│  - Sender IP:  192.168.1.20            │
│  - Target MAC: AA:AA:AA:AA:AA:AA       │
│  - Target IP:  192.168.1.10            │
└────────────────────────────────────────┘

Frame wird DIREKT an Computer A gesendet (kein Broadcast)
```

#### **Schritt 5: ARP-Cache aktualisieren & Daten senden** ✅

```
Computer A empfängt ARP Reply:
"Super! 192.168.1.20 hat MAC BB:BB:BB:BB:BB:BB"

Computer A speichert in ARP-Cache:
192.168.1.20 → BB:BB:BB:BB:BB:BB

Jetzt kann A endlich senden:
┌────────────────────────────────────────┐
│ Ethernet-Frame:                        │
│ Quell-MAC:  AA:AA:AA:AA:AA:AA          │
│ Ziel-MAC:   BB:BB:BB:BB:BB:BB (JETZT BEKANNT!) │
│ Payload: [Original IP-Paket]          │
└────────────────────────────────────────┘

Daten werden zugestellt! 🎉
```

### **Visueller Ablauf**

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│ Computer A  │         │   Switch    │         │ Computer B  │
│ 192.168.1.10│         │             │         │ 192.168.1.20│
│ AA:AA:...:AA│         │             │         │ BB:BB:...:BB│
└─────────────┘         └─────────────┘         └─────────────┘
      │                        │                        │
      │  1. ARP Request        │                        │
      │  "Wer hat .20?"        │                        │
      │ ──────────────────────>│                        │
      │  (Broadcast)            │  2. Flooding          │
      │                        │ ──────────────────────>│
      │                        │                        │
      │                        │  3. "Das bin ich!"     │
      │                        │ <──────────────────────│
      │  4. ARP Reply          │                        │
      │  "Meine MAC: BB..."    │                        │
      │ <──────────────────────│                        │
      │  (Unicast)              │                        │
      │                        │                        │
      │  5. Datenpaket         │                        │
      │  mit korrekter MAC     │                        │
      │ ──────────────────────>│ ──────────────────────>│
      │                        │                        │
```

### **Der ARP-Cache: Effizienz durch Speicherung**

**Problem**: ARP-Request für **jedes** Paket wäre ineffizient

**Lösung**: **ARP-Cache** speichert gelernte Zuordnungen

**Eigenschaften**:

**Dynamische Einträge**:

- Automatisch durch ARP-Prozess gelernt
- **Zeitlich begrenzt** (Timeout: oft 1-20 Minuten, OS-abhängig)
- Nach Ablauf: Eintrag gelöscht, bei Bedarf neu auflösen

**Statische Einträge**:

- Manuell hinzugefügt (selten)
- **Permanent** (bis manuelles Löschen)
- Für spezielle Netzwerk-Konfigurationen

**Warum Timeout?**

- IP-Adressen können sich ändern (DHCP)
- Geräte können Netzwerk verlassen
- Verhindert veraltete/falsche Zuordnungen

### **ARP-Cache anzeigen (Windows 11)**

**Methode 1: Kommandozeile**

```cmd
arp -a
```

**Beispiel-Ausgabe**:

```
Schnittstelle: 192.168.1.10 --- 0x4
  Internetadresse       Physische Adresse     Typ
  192.168.1.1           1c-2d-3e-4f-5a-6b     dynamisch
  192.168.1.20          bb-bb-bb-bb-bb-bb     dynamisch
  192.168.1.255         ff-ff-ff-ff-ff-ff     statisch
  224.0.0.22            01-00-5e-00-00-16     statisch
```

**Erklärung**:

- **Internetadresse**: IP-Adresse
- **Physische Adresse**: MAC-Adresse (mit `-` statt `:`)
- **Typ**: dynamisch (zeitlich begrenzt) oder statisch (permanent)

**Methode 2: PowerShell**

```powershell
Get-NetNeighbor -AddressFamily IPv4
```

**Weitere ARP-Befehle**:

**Einzelnen Eintrag löschen**:

```cmd
arp -d 192.168.1.20
```

**Gesamten Cache löschen**:

```cmd
arp -d *
```

**Statischen Eintrag hinzufügen**:

```cmd
arp -s 192.168.1.20 BB-BB-BB-BB-BB-BB
```

### **Praktischer Test**

**1. Cache vor Ping prüfen**:

```cmd
arp -a | findstr "192.168.1.1"
```

(Möglicherweise kein Eintrag)

**2. Gerät anpingen**:

```cmd
ping 192.168.1.1
```

**3. Cache nach Ping prüfen**:

```cmd
arp -a | findstr "192.168.1.1"
```

(Jetzt sollte Eintrag vorhanden sein!)

**Ergebnis**: Der Ping hat ARP-Auflösung ausgelöst → Eintrag im Cache

### **ARP-Nachrichtenformat**

**Wichtige Felder** (vereinfacht):

```
┌─────────────────────────────────────┐
│ Hardware Type: Ethernet (1)         │
│ Protocol Type: IPv4 (0x0800)        │
│ Hardware Addr Length: 6 Bytes       │
│ Protocol Addr Length: 4 Bytes       │
│ Opcode: 1=Request, 2=Reply         │
├─────────────────────────────────────┤
│ Sender MAC Address (6 Bytes)        │
│ Sender IP Address (4 Bytes)         │
│ Target MAC Address (6 Bytes)        │
│   - Request: 00:00:00:00:00:00      │
│   - Reply: bekannte MAC             │
│ Target IP Address (4 Bytes)         │
└─────────────────────────────────────┘
```

**Opcode-Werte**:

- **1**: ARP Request
- **2**: ARP Reply

### **Besonderheiten: Gateway-Kommunikation**

**Was passiert bei Zielen außerhalb des lokalen Netzes?**

```
Computer A (192.168.1.10) will zu Google (8.8.8.8)

8.8.8.8 ist NICHT im lokalen Netz!

Computer A:
1. "8.8.8.8 ist nicht lokal (andere Subnetzmaske)"
2. "Muss an Standard-Gateway senden"
3. ARP-Anfrage für Gateway-IP (z.B. 192.168.1.1)
4. Frame mit Gateway-MAC senden, aber IP-Paket für 8.8.8.8

Router/Gateway:
- Empfängt Frame (seine MAC)
- Öffnet IP-Paket (Ziel: 8.8.8.8)
- Leitet ins Internet weiter
```

**Wichtig**: Computer A braucht **nicht** die MAC von Google, sondern die **MAC des Gateways**!

### **ARP-Sicherheitsprobleme**

⚠️ **ARP Spoofing/Poisoning** (Hauptproblem)

**Problem**: ARP **vertraut blindlings** – keine Authentifizierung!

**Angriff**:

```
Angreifer sendet gefälschte ARP Reply:
"Ich bin 192.168.1.1 (Gateway), meine MAC ist ANGREIFER-MAC!"

Opfer aktualisiert ARP-Cache:
192.168.1.1 → ANGREIFER-MAC (FALSCH!)

Jetzt:
Opfer → sendet Internet-Traffic an Angreifer
Angreifer → fängt Daten ab, leitet (optional) weiter
```

**Resultat**: **Man-in-the-Middle (MITM) Angriff** 🕵️

**Beispiel**:

```
Normal:
PC → Router → Internet

Mit ARP Spoofing:
PC → Angreifer → Router → Internet
     ↑
 Liest alles mit!
```

**Weitere ARP-Angriffe**:

- **ARP Flooding**: Massenhaft falsche ARP-Nachrichten → Switch-Überlastung
- **Gratuitous ARP Abuse**: Unaufgefordertes ARP zum Überschreiben von Caches

### **ARP-Sicherheitsmaßnahmen**

✅ **Static ARP Entries** (für kritische Geräte):

```cmd
arp -s 192.168.1.1 AA-BB-CC-DD-EE-FF
```

Nachteil: Manuelle Verwaltung aufwendig

✅ **Dynamic ARP Inspection (DAI)** (Managed Switches):

- Switch validiert ARP-Nachrichten
- Nur autorisierte Geräte dürfen ARP-Antworten senden

✅ **Port Security** (Switches):

- Limitiert MAC-Adressen pro Port

✅ **ARP Monitoring Tools**:

- `arpwatch` (Linux)
- Warnung bei ungewöhnlichen ARP-Änderungen

✅ **Netzwerksegmentierung** (VLANs):

- Begrenzt Broadcast-Domänen
- Reduziert Angriffsfläche

### **Warum nicht nur IP-Adressen nutzen?**

**Frage**: Warum Layer-2-Adressen (MAC), wenn wir Layer-3 (IP) haben?

**Antworten**:

**1. Layer-Trennung** 🏗️:

- **Layer 2 (Ethernet)**: Wurde für lokale Zustellung mit MACs entwickelt
- **Layer 3 (IP)**: Für globales Routing entwickelt
- Jede Schicht hat ihre Aufgabe!

**2. Switches arbeiten auf Layer 2** 🔀:

- Switches lesen **nur** MAC-Adressen
- Switches inspizieren **keine** IP-Pakete
- Ethernet-Frames brauchen MACs für Weiterleitung

**3. Flexibilität** 🔄:

- IP kann sich ändern (DHCP)
- MAC bleibt (meist) gleich
- Layer-2 unabhängig von Layer-3-Protokoll

**4. Historische Gründe** 📜:

- Ethernet existierte vor IP
- MACs waren der ursprüngliche Mechanismus

**Analogie**:

- **MAC-Adresse** = Hausnummer in der Straße (lokal)
- **IP-Adresse** = Komplette Postadresse mit Stadt (global)
- Du brauchst **beides** für die Zustellung!

### **Gratuitous ARP (Unaufgefordertes ARP)**

**Was ist das?** ARP-Request/-Reply **ohne vorherige Anfrage**

**Zwecke**:

**1. IP-Konfliktprüfung** 🔍:

```
Gerät bekommt neue IP (z.B. via DHCP)
Sendet Gratuitous ARP: "Hat jemand diese IP schon?"
Falls Antwort: IP-Konflikt!
```

**2. Cache-Update** 🔄:

```
Gerät ändert MAC-Adresse (z.B. Failover)
Sendet Gratuitous ARP: "Meine IP hat jetzt neue MAC!"
Alle Geräte aktualisieren Cache
```

**3. Schnellere Kommunikation** ⚡:

```
Gerät teilt proaktiv seine IP↔MAC mit
Andere Geräte müssen nicht erst anfragen
```

### **IPv6 und Neighbor Discovery**

**Wichtig**: ARP ist **IPv4-spezifisch**!

**IPv6** nutzt **Neighbor Discovery Protocol (NDP)**:

- Teil von ICMPv6
- Ähnliche Funktion wie ARP
- Zusätzliche Features (Router Discovery, Redirect, etc.)

**Neighbor Solicitation** = IPv6-Äquivalent zu ARP Request **Neighbor Advertisement** = IPv6-Äquivalent zu ARP Reply

### **Kernbotschaft**

**ARP** ist der **unsichtbare Helfer**, der IP-Adressen zu MAC-Adressen auflöst:

**Problem**:

- Layer 3 nutzt IP-Adressen
- Layer 2 (Ethernet) braucht MAC-Adressen
- **Gap zwischen Layern**

**Lösung**:

- **ARP Request** (Broadcast): "Wer hat diese IP?"
- **ARP Reply** (Unicast): "Ich! Hier ist meine MAC"
- **ARP-Cache**: Speichert Zuordnungen für Effizienz

**Der Prozess**:

```
1. Cache prüfen → Falls vorhanden: direkt senden
2. Falls nicht: ARP Request (Broadcast) an alle
3. Zielgerät antwortet: ARP Reply (Unicast)
4. Cache aktualisieren
5. Daten mit korrekter MAC senden
```

**Sicherheit**: ⚠️ ARP ist **nicht authentifiziert** → anfällig für Spoofing/Poisoning 🛡️ Schutzmaßnahmen: DAI, Port Security, Monitoring, VLANs

**Analogie finale**: ARP ist wie ein **lokales Telefonbuch-Service** – du rufst an (Broadcast), fragst nach der Nummer (MAC) zu einem Namen (IP), und der Besitzer meldet sich zurück. Alle anderen hören zwar den Anruf, antworten aber nicht, weil sie nicht gemeint sind! 📞📋🔍