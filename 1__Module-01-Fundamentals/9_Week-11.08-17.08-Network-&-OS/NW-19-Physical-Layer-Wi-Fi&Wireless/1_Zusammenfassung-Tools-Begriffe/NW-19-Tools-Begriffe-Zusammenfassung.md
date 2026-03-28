# Kategorisierung Wi-Fi & Drahtlose Kommunikation

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **Wi-Fi-Einstellungen**: Netzwerkverbindungen verwalten (macOS: Wi-Fi-Symbol + Option-Taste; Windows: Einstellungen → Netzwerk und Internet → WLAN)<br>• **Command Prompt/PowerShell**: WLAN-Befehle (Windows: `netsh wlan show interfaces`, `netsh wlan show networks`)<br>• **Wi-Fi Analyzer Apps**: inSSIDer, NetSpot, WiFi Analyzer (Windows & Android)<br>• **Wireshark**: WLAN-Paketanalyse (beide Systeme, Monitor-Mode-Adapter nötig)<br>• **Aircrack-ng**: WLAN-Security-Testing (Linux, über WSL in Windows)<br>• **Network Utility/Resource Monitor**: Verbindungsdetails (macOS: veraltet; Windows: Ressourcenmonitor)<br>• **System Information**: Netzwerkadapter-Details (Windows: `msinfo32`)<br>• **Router-Webinterface**: WLAN-Konfiguration (Browser: meist 192.168.1.1 oder 192.168.0.1)<br>• **Speedtest Apps**: Ookla Speedtest, Fast.com (Durchsatzmessung)<br>• **WiFi Explorer**: macOS-Tool für WLAN-Analyse<br>• **Acrylic WiFi**: Windows-Tool für WLAN-Scanning<br>• **Wireless Diagnostics**: macOS-integriertes WLAN-Diagnose-Tool|
|**Technische Fachbegriffe**|• **Wireless Communication**: Drahtlose Kommunikation<br>• **Wi-Fi**: Wireless Fidelity (WLAN-Technologie)<br>• **Radio Waves**: Radiowellen/Funkwellen<br>• **Electromagnetic Waves**: Elektromagnetische Wellen<br>• **Frequency**: Frequenz (Schwingungen pro Sekunde)<br>• **Hertz (Hz)**: Maßeinheit für Frequenz<br>• **GHz** (Gigahertz): Milliarden Schwingungen pro Sekunde<br>• **2.4 GHz Band**: 2,4-Gigahertz-Frequenzband<br>• **5 GHz Band**: 5-Gigahertz-Frequenzband<br>• **6 GHz Band**: 6-Gigahertz-Frequenzband (Wi-Fi 6E)<br>• **Radio Spectrum**: Funkfrequenz-Spektrum<br>• **Channel**: Kanal (Unterteilung des Frequenzbands)<br>• **Interference**: Störung/Interferenz<br>• **IEEE 802.11**: Wi-Fi-Standardfamilie<br>• **802.11b/a/g/n/ac/ax**: Verschiedene Wi-Fi-Generationen<br>• **Wi-Fi 6 (802.11ax)**: Sechste Wi-Fi-Generation<br>• **Wi-Fi 6E**: Wi-Fi 6 Extended (mit 6 GHz)<br>• **MIMO** (Multiple Input Multiple Output): Mehrfach-Antennen-Technologie<br>• **OFDMA** (Orthogonal Frequency-Division Multiple Access): Effizienzverbesserung bei Wi-Fi 6<br>• **WAP/AP** (Wireless Access Point): WLAN-Zugangspunkt<br>• **WNIC** (Wireless Network Interface Card): WLAN-Netzwerkkarte<br>• **SSID** (Service Set Identifier): WLAN-Netzwerkname<br>• **Hidden SSID**: Nicht-ausgestrahlter Netzwerkname<br>• **Broadcast**: Ausstrahlung des SSIDs<br>• **Authentication**: Authentifizierung/Anmeldung<br>• **Encryption**: Verschlüsselung<br>• **WEP** (Wired Equivalent Privacy): Veraltete Verschlüsselung (UNSICHER!)<br>• **WPA** (Wi-Fi Protected Access): Erste sichere Verschlüsselung<br>• **WPA2**: Zweite Generation (AES-basiert, Standard)<br>• **WPA3**: Dritte Generation (neuester Standard, verbesserte Sicherheit)<br>• **PSK** (Pre-Shared Key): Vorher geteilter Schlüssel (Passwort)<br>• **TKIP** (Temporal Key Integrity Protocol): Alter Verschlüsselungsalgorithmus (verwundbar)<br>• **AES** (Advanced Encryption Standard): Moderner Verschlüsselungsalgorithmus<br>• **CCMP**: AES-basiertes Protokoll für WPA2<br>• **RSSI** (Received Signal Strength Indicator): Empfangene Signalstärke<br>• **dBm** (Decibel-Milliwatt): Maßeinheit für Signalstärke<br>• **Tx Rate** (Transmit Rate): Übertragungsrate<br>• **PHY Mode**: Physikalischer Modus (verwendeter 802.11-Standard)<br>• **Rogue Access Point**: Betrügerischer/gefälschter Access Point<br>• **Evil Twin**: Gefälschtes WLAN mit gleichem Namen<br>• **Packet Sniffing**: Paketmitschnitt aus der Luft<br>• **DoS** (Denial of Service): Dienstblockade<br>• **Deauthentication Attack**: Zwangs-Abmeldung von WLAN|
|**Wichtige Vokabeln**|• **Drahtlos**: Ohne Kabel<br>• **Elektromagnetische Strahlung**: Funkwellen<br>• **Wellenlänge**: Distanz zwischen Wellenbergen<br>• **Oszillieren**: Schwingen/Wiederholen<br>• **Zyklus**: Schwingung<br>• **Spektrum**: Frequenzbereich<br>• **Zugewiesen**: Für bestimmten Zweck reserviert<br>• **Überlappend**: Sich überschneidend<br>• **Unterbrechung**: Störung<br>• **Schwächung**: Signal wird schwächer<br>• **Mikrowellenherd**: Störungsquelle für 2,4 GHz<br>• **Dicke Wände**: Physikalische Hindernisse<br>• **Metallobjekte**: Signalblockierung<br>• **Abwärtskompatibel**: Mit älteren Standards kompatibel<br>• **Theoretische Maximalgeschwindigkeit**: Ideale Geschwindigkeit<br>• **Dichte Umgebungen**: Viele WLAN-Geräte<br>• **Brücke**: Verbindung zwischen drahtlos und kabelgebunden<br>• **Transceiver**: Sender-Empfänger<br>• **Sichtbare externe Antennen**: Antennen außerhalb des Geräts<br>• **Interne Antennen**: Versteckte Antennen<br>• **Ausrichtung**: Positioning der Antennen<br>• **Ausstrahlung**: Broadcasting<br>• **Scannen**: Suche nach Netzwerken<br>• **Berechtigung**: Zugriffsgenehmigung<br>• **Abhören**: Eavesdropping<br>• **Unbefugter Zugriff**: Zugriff ohne Erlaubnis<br>• **Bandbreitennutzung**: Internetverbrauch<br>• **Geteilte Dateien**: Freigegebene Ressourcen<br>• **Vortäuschen**: Mimicking/Spoofing<br>• **Abfangen**: Intercepting<br>• **Legitim**: Echt/authentisch<br>• **Eindringen**: Intrusion<br>• **Abschwächung**: Mitigation<br>• **Reichweite**: Coverage/Range<br>• **Mobilität**: Bewegungsfreiheit<br>• **Gebunden**: Tethered (durch Kabel)<br>• **Empfänglich**: Susceptible<br>• **Hindernisse**: Obstructions<br>• **Atmosphärische Bedingungen**: Wetterbedingungen|

---

## 80/20-Zusammenfassung: Die wichtigsten 20% zum Verständnis von 80% von Wi-Fi & Drahtloser Kommunikation

### **Was ist drahtlose Kommunikation?**

**Wireless Communication** = Informationsübertragung **ohne physische Kabel** durch **elektromagnetische Wellen** (Funkwellen, Infrarot, Licht)

**Beispiele**:

- 📺 TV-Fernbedienung (Infrarot)
- 📱 Smartphone-Internet (Wi-Fi, Mobilfunk)
- 📻 Autoradio (FM/AM)
- 🎮 Bluetooth-Controller

**Im Netzwerk-Kontext**: **Wi-Fi** = WLAN (Wireless Local Area Network)

### **Wi-Fi vs. Kabelgebundene Netzwerke**

|Merkmal|**Wi-Fi (Drahtlos)**|**Ethernet (Kabelgebunden)**|
|---|---|---|
|**Medium**|Luft (Funkwellen)|Kabel (Kupfer, Glasfaser)|
|**Mobilität**|✅ Hoch (überall im Bereich)|❌ Niedrig (an Kabel gebunden)|
|**Geschwindigkeit**|Bis ~10 Gbps (Wi-Fi 6E)|Bis 100+ Gbps (Glasfaser)|
|**Stabilität**|⚠️ Variabel (Störungen)|✅ Sehr stabil|
|**Sicherheit**|⚠️ Anfälliger (Luft)|✅ Sicherer (physisch begrenzt)|
|**Reichweite**|🏠 ~30-50m (innen), abhängig von Hindernissen|🔌 100m (UTP), km (Glasfaser)|
|**Interferenz**|⚠️ Hoch (andere Geräte)|✅ Niedrig (geschirmt)|
|**Setup**|✅ Einfach|⚠️ Verkabelung nötig|

### **Funkwellen: Die Grundlage von Wi-Fi**

**Funkwellen** = Elektromagnetische Wellen mit langen Wellenlängen

#### **Frequenz** – Die Anzahl der Schwingungen

**Frequenz** = Schwingungen pro Sekunde (Hertz, Hz)

```
1 Hz  = 1 Schwingung/Sekunde
1 MHz = 1 Million Schwingungen/Sekunde
1 GHz = 1 Milliarde Schwingungen/Sekunde
```

**Wi-Fi-Frequenzbänder**:

|Band|Frequenz|Eigenschaften|
|---|---|---|
|**2.4 GHz**|2,4 Milliarden Schwingungen/s|✅ Größere Reichweite<br>✅ Bessere Durchdringung (Wände)<br>❌ Langsamer<br>❌ Viel Interferenz (viele Geräte)|
|**5 GHz**|5 Milliarden Schwingungen/s|✅ Schneller<br>✅ Weniger Interferenz<br>❌ Kürzere Reichweite<br>❌ Schlechtere Durchdringung|
|**6 GHz**|6 Milliarden Schwingungen/s (Wi-Fi 6E)|✅ Sehr schnell<br>✅ Kaum Interferenz (neu)<br>❌ Noch kürzere Reichweite<br>❌ Sehr schlechte Durchdringung|

**Faustregel**:

- **2.4 GHz**: Für große Häuser, durch viele Wände
- **5 GHz**: Für Geschwindigkeit, weniger Reichweite
- **6 GHz**: Für höchste Geschwindigkeit, gleiches Zimmer

#### **Kanäle** – Unterteilung des Spektrums

**Problem**: Alle Geräte auf derselben Frequenz → Interferenz!

**Lösung**: **Kanäle** (Unterteilungen innerhalb des Bands)

**2.4 GHz**:

- 11-14 Kanäle (je nach Land)
- **Nur 3 überlappungsfrei**: Kanal 1, 6, 11
- **Viele Geräte** = Stau!

**5 GHz**:

- ~24 Kanäle
- **Mehr nicht-überlappende** Kanäle
- **Weniger Stau**

**6 GHz** (Wi-Fi 6E):

- ~59 Kanäle
- **Komplett frei** (neu, kaum Geräte)

**Best Practice**: Router auf Kanal mit **geringster Nutzung** (Auto-Wahl oder manuell)

#### **Interferenz** – Störquellen

**Was stört Wi-Fi?**

**Im 2.4 GHz Band**:

- 🍴 Mikrowellenherde (~2,45 GHz!)
- 🎧 Bluetooth-Geräte
- 📞 Schnurlose Telefone
- 🏠 Nachbar-WLANs (gleicher Kanal)

**Physikalische Hindernisse**:

- 🧱 Dicke Wände (Beton, Ziegel)
- 🔩 Metall (Türen, Schränke, Alufolie)
- 💧 Wasser (Aquarien, Menschen = ~70% Wasser!)
- 🌳 Pflanzen (in großen Mengen)

### **Wi-Fi-Standards (IEEE 802.11-Familie)**

**IEEE 802.11** = Offizielle Wi-Fi-Standards

|Standard|Marketing-Name|Jahr|Frequenz|Max. Speed|Besonderheit|
|---|---|---|---|---|---|
|**802.11b**|-|1999|2.4 GHz|11 Mbps|Veraltet|
|**802.11a**|-|1999|5 GHz|54 Mbps|Erste 5 GHz|
|**802.11g**|-|2003|2.4 GHz|54 Mbps|Abwärtskompatibel zu b|
|**802.11n**|**Wi-Fi 4**|2009|2.4/5 GHz|600 Mbps|MIMO (mehrere Antennen)|
|**802.11ac**|**Wi-Fi 5**|2013|5 GHz|1,3+ Gbps|"Gigabit Wi-Fi"|
|**802.11ax**|**Wi-Fi 6/6E**|2019|2.4/5/6 GHz|9,6+ Gbps|OFDMA, besser in dichten Umgebungen|

**Trend**:

- Immer schneller
- Effizientere Nutzung des Spektrums
- Bessere Performance bei vielen Geräten

**Heute Standard**: Wi-Fi 5 (802.11ac) oder Wi-Fi 6 (802.11ax)

### **Wi-Fi-Komponenten: Die Hardware**

#### **1. Wireless Access Point (WAP/AP)** 📡

**Funktion**: Sendet und empfängt Wi-Fi-Signale

**Arten**:

- **Standalone AP**: Nur WLAN-Funktion
- **Wireless Router**: AP + Router + Switch kombiniert (typisch für Heimnetzwerke)

**Aufgabe**:

- Broadcast des SSIDs
- Authentifizierung von Clients
- Brücke zwischen WLAN und kabelgebundenem Netzwerk

#### **2. Wireless NIC (WNIC)** 📶

**Funktion**: WLAN-Adapter im Gerät

**Formen**:

- **Integriert**: In Laptop/Smartphone
- **USB-Adapter**: Extern ansteckbar
- **PCIe-Karte**: Intern in Desktop

**Aufgabe**: Senden/Empfangen von Funkwellen

#### **3. Antennen** 📻

**Typen**:

- **Extern**: Sichtbar (oft bei Routern)
- **Intern**: Versteckt (meiste moderne Geräte)

**Ausrichtung wichtig**:

- Vertikal für horizontale Ausbreitung
- Horizontal für vertikale Ausbreitung

### **SSID: Der Netzwerkname**

**SSID (Service Set Identifier)** = Name des WLAN-Netzwerks

**Beispiele**: "MyHomeWiFi", "Starbucks_WiFi", "FRITZ!Box 7590"

**Broadcast**:

- **Standard**: SSID wird **ausgestrahlt** (in Geräteliste sichtbar)
- **Hidden SSID**: SSID wird **nicht** ausgestrahlt

**Hidden SSID = Sicherheit?**

```
❌ NEIN! Nur "Security durch Obscurity"
⚠️ SSID trotzdem erkennbar (mit Tools wie Wireshark)
✅ Echte Sicherheit: Starkes Passwort + WPA2/WPA3
```

### **Wi-Fi-Verbindungsprozess**

```
┌──────────┐                      ┌──────────────┐
│  Gerät   │                      │ Access Point │
└────┬─────┘                      └──────┬───────┘
     │                                   │
     │  1. Scan (Suche Netzwerke)        │
     │ ──────────────────────────────────>│
     │                                   │
     │  2. SSID-Broadcast                │
     │ <──────────────────────────────────│
     │                                   │
     │  3. Authentifizierung (Passwort)  │
     │ ──────────────────────────────────>│
     │                                   │
     │  4. Authentication Success        │
     │ <──────────────────────────────────│
     │                                   │
     │  5. Verbindung                    │
     │ ──────────────────────────────────>│
     │                                   │
     │  6. Connection Confirmed          │
     │ <──────────────────────────────────│
     │                                   │
     │  ╔════════════════════════════╗   │
     │  ║ Daten jetzt verschlüsselt! ║   │
     │  ╚════════════════════════════╝   │
     │ <──────────────────────────────────>│
```

### **Wi-Fi-Sicherheit: Authentifizierung & Verschlüsselung**

#### **Sicherheitsstandards (Evolution)**

|Standard|Jahr|Verschlüsselung|Sicherheit|Empfehlung|
|---|---|---|---|---|
|**Open**|-|❌ Keine|❌❌❌|**NIE nutzen!**|
|**WEP**|1997|RC4 (schwach)|❌|**NIE nutzen!** (in Minuten hackbar)|
|**WPA**|2003|TKIP|⚠️|Veraltet|
|**WPA2**|2004|AES (CCMP)|✅✅✅|**Standard heute**|
|**WPA3**|2018|AES (SAE)|✅✅✅✅|**Bester Standard**|

**Verschlüsselungsalgorithmen**:

- **TKIP**: Temporal Key Integrity Protocol (veraltet, Schwachstellen)
- **AES**: Advanced Encryption Standard (stark, moderner Standard)
- **SAE**: Simultaneous Authentication of Equals (WPA3, noch stärker)

#### **WPA2/WPA3 Modi**

**Personal (PSK - Pre-Shared Key)**:

- Ein gemeinsames Passwort für alle
- Für Heimnetzwerke, kleine Büros
- **Setup**: Passwort im Router → alle nutzen gleiches Passwort

**Enterprise (802.1X/RADIUS)**:

- Individuelle Anmeldung pro Benutzer
- Für Unternehmen, Universitäten
- **Setup**: Zentraler Authentifizierungsserver (RADIUS)

**Empfehlung für Heimnetzwerke**:

```
✅ WPA2-Personal (AES) oder WPA3-Personal
✅ Starkes Passwort (min. 12 Zeichen, gemischt)
❌ NIEMALS WEP oder Open
```

### **Wi-Fi-Sicherheitsbedrohungen**

#### **1. Unbefugter Zugriff** 🚪

**Szenario**: Schwaches/kein Passwort

**Folgen**:

- Bandbreitennutzung (dein Internet wird langsamer)
- Zugriff auf Netzwerk-Ressourcen (Drucker, NAS)
- Rechtliche Probleme (falls Angreifer illegale Aktivitäten über deine IP)

**Schutz**:

- ✅ Starkes WPA2/WPA3-Passwort
- ✅ Gast-Netzwerk für Besucher (isoliert vom Hauptnetzwerk)

#### **2. Eavesdropping (Abhören)** 👂

**Szenario**: Angreifer fängt Funkwellen ab

**Ohne Verschlüsselung**:

```
Angreifer mit Wireshark:
→ Sieht alle Passwörter, E-Mails, Chatverläufe im Klartext!
```

**Mit WPA2/WPA3**:

```
Angreifer sieht nur:
→ Verschlüsselten "Datensalat" (AES)
→ Praktisch nicht zu entschlüsseln
```

**Zusätzlicher Schutz**:

- ✅ HTTPS für Websites (Ende-zu-Ende)
- ✅ VPN in öffentlichen WLANs

#### **3. Rogue Access Point (Gefälschter AP)** 🎣

**Szenario**: "Evil Twin" – Angreifer setzt gefälschten AP auf

**Ablauf**:

```
Echter AP:  "Starbucks_WiFi"
Fake AP:    "Starbucks_WiFi" (gleicher Name!)

User verbindet sich mit Fake
    ↓
Angreifer = Man-in-the-Middle
    ↓
Liest ALLEN Traffic mit
```

**Schutz**:

- ⚠️ Vorsicht bei offenen WLANs
- ✅ VPN nutzen (verschlüsselt gesamten Traffic)
- ✅ Nur bekannte/vertrauenswürdige Netzwerke
- ✅ Zertifikatswarnungen ernst nehmen

#### **4. Deauthentication Attack (DoS)** 💥

**Szenario**: Angreifer sendet "Deauth"-Pakete

**Ablauf**:

```
Angreifer → Deauth-Paket an Client
    ↓
Client denkt: "AP wirft mich raus"
    ↓
Verbindung wird getrennt
    ↓
Wiederholte Angriffe = DoS (Dienstverweigerung)
```

**Schutz**:

- ✅ WPA3 (Management Frame Protection - MFP)
- ✅ 802.11w (Protected Management Frames) aktivieren

### **Wi-Fi-Verbindungsdetails anzeigen (Windows 11)**

**Methode 1: GUI (Einstellungen)**

1. **Einstellungen** → **Netzwerk und Internet** → **WLAN**
2. Verbundenes Netzwerk anklicken → **Eigenschaften**
3. Anzeige:
    - SSID
    - Sicherheitstyp (WPA2, WPA3)
    - Frequenzband (2,4 GHz, 5 GHz)
    - Link-Geschwindigkeit

**Methode 2: Command Prompt**

```cmd
netsh wlan show interfaces
```

**Ausgabe**:

```
Name                   : Wi-Fi
Beschreibung           : Intel(R) Wi-Fi 6 AX201 160MHz
SSID                   : MyHomeWiFi
BSSID                  : aa:bb:cc:dd:ee:ff
Netzwerktyp            : Infrastruktur
Funktyp                : 802.11ax
Authentifizierung      : WPA2-Personal
Verschlüsselung        : CCMP
Kanal                  : 36
Empfang                : 95%
Übertragung            : 100%
Signalstärke           : 92%
```

**Methode 3: PowerShell (detailliert)**

```powershell
Get-NetAdapter | Where-Object {$_.Name -like "*Wi-Fi*"} | Get-NetAdapterStatistics
```

**Verfügbare Netzwerke scannen**:

```cmd
netsh wlan show networks mode=bssid
```

### **RSSI: Signalstärke verstehen**

**RSSI (Received Signal Strength Indicator)** = Empfangene Signalstärke

**Einheit**: **dBm** (Decibel-Milliwatt)

**Skala** (negativer Wert!):

```
-30 dBm  ════════════  Exzellent (direkt neben AP)
-40 dBm  ═══════════
-50 dBm  ══════════   Sehr gut
-60 dBm  ════════     Gut
-70 dBm  ═════        OK (nutzbar)
-80 dBm  ══           Schwach
-90 dBm  ═            Sehr schwach (kaum nutzbar)
-100 dBm              Kein Signal
```

**Faustregel**:

- **-30 bis -50 dBm**: ✅ Hervorragend
- **-50 bis -70 dBm**: ✅ Gut bis Okay
- **-70 bis -80 dBm**: ⚠️ Schwach (langsam)
- **< -80 dBm**: ❌ Sehr schwach (Verbindungsabbrüche)

**Näher an 0 = besser!** (weniger negativ)

### **Wi-Fi-Best-Practices**

✅ **Sicherheit**:

- WPA2-Personal (AES) oder WPA3-Personal
- Starkes Passwort (min. 12 Zeichen)
- Standard-Admin-Passwort ändern
- Firmware aktuell halten

✅ **Performance**:

- 5 GHz für Geschwindigkeit (kurze Distanz)
- 2,4 GHz für Reichweite (lange Distanz)
- AP zentral platzieren (erhöht)
- Kanal mit geringster Nutzung wählen

✅ **Netzwerk-Organisation**:

- Gast-WLAN für Besucher (isoliert)
- IoT-Geräte in separatem VLAN
- SSID-Broadcast an (verstecken bringt wenig Sicherheit)

❌ **Vermeiden**:

- Offene Netzwerke (ohne Passwort)
- WEP (komplett unsicher)
- Schwache Passwörter ("12345678")
- AP in Ecke/Keller (schlechte Abdeckung)

### **Kernbotschaft**

**Wi-Fi** ermöglicht **drahtlose Netzwerkkommunikation** durch **Funkwellen**:

**Frequenzbänder**:

- **2,4 GHz**: Weiter, durchdringender, langsamer, voll
- **5 GHz**: Schneller, weniger weit, weniger voll
- **6 GHz**: Sehr schnell, sehr kurz, leer (Wi-Fi 6E)

**Standards**: 802.11n/ac/ax (Wi-Fi 4/5/6) – immer schneller und effizienter

**Komponenten**: Access Point (sendet) + Wireless NIC (empfängt) + Antennen

**Sicherheit**:

- **WPA2/WPA3** = Standard (AES-Verschlüsselung)
- **WEP/Open** = Katastrophe (niemals nutzen!)
- **Starkes Passwort** = Pflicht

**Bedrohungen**: Unbefugter Zugriff, Abhören, Rogue APs, DoS

**Analogie finale**: Wi-Fi ist wie ein **unsichtbares Kabel aus Funkwellen** – flexibel und praktisch, aber anfällig für "Lauscher in der Luft". Verschlüsselung (WPA2/WPA3) ist wie ein **verschlossener Tunnel** durch diese Luft – nur du hast den Schlüssel! 📡🔐🌊