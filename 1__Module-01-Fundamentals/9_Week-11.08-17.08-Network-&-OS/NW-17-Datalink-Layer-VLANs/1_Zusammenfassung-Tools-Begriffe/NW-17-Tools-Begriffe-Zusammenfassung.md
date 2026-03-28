# Kategorisierung VLANs (Virtual Local Area Networks)

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **Managed Switch**: VLAN-fähiger Switch (z.B. Cisco Catalyst, HP ProCurve, Netgear)<br>• **Switch-Webinterface**: VLAN-Konfiguration über Browser<br>• **Cisco IOS CLI**: Kommandozeilen-Interface für Cisco-Switches<br>• **Packet Tracer**: Cisco-Netzwerksimulator für VLAN-Übungen (Windows & macOS)<br>• **GNS3**: Netzwerk-Emulator mit VLAN-Unterstützung<br>• **Wireshark**: 802.1Q-VLAN-Tags analysieren<br>• **VLAN-Management-Software**: Herstellerspezifische Tools<br>• **Network Diagram Tools**: Visio, draw.io, Lucidchart (VLAN-Topologien zeichnen)<br>• **SNMP-Tools**: VLAN-Monitoring (z.B. PRTG, SolarWinds)<br>• **Terminal/SSH-Client**: CLI-Zugriff auf Switches (PuTTY für Windows)<br>• **PowerShell**: Netzwerk-VLAN-Konfiguration (Windows Server Hyper-V VLANs)<br>• **Linux VLANs**: `vconfig`, `ip link` für VLAN-Interfaces|
|**Technische Fachbegriffe**|• **VLAN** (Virtual Local Area Network): Virtuelles lokales Netzwerk<br>• **LAN** (Local Area Network): Lokales Netzwerk<br>• **Broadcast Domain**: Broadcast-Bereich<br>• **Network Segmentation**: Netzwerksegmentierung<br>• **IEEE 802.1Q**: VLAN-Tagging-Standard<br>• **VLAN Tagging**: VLAN-Markierung in Ethernet-Frames<br>• **VLAN ID (VID)**: VLAN-Identifikationsnummer (1-4094)<br>• **Access Port**: Zugangs-Port (gehört zu einem VLAN)<br>• **Trunk Port**: Trunk-Port (trägt mehrere VLANs)<br>• **Native VLAN**: Standard-VLAN für unmarkierten Traffic auf Trunk<br>• **Untagged Traffic**: Nicht markierter Datenverkehr<br>• **Tagged Traffic**: Markierter Datenverkehr (mit 802.1Q-Tag)<br>• **Inter-VLAN Routing**: Routing zwischen VLANs<br>• **Layer 2 Segmentation**: Segmentierung auf Schicht 2<br>• **Layer 3 Switch**: Switch mit Routing-Fähigkeiten<br>• **VLAN Trunking Protocol (VTP)**: Cisco-Protokoll zur VLAN-Verwaltung<br>• **Private VLAN**: Isolierte VLAN-Segmente innerhalb eines VLANs<br>• **Voice VLAN**: Spezielles VLAN für VoIP-Telefone<br>• **Management VLAN**: VLAN für Switch-Verwaltung<br>• **Default VLAN**: Standard-VLAN (meist VLAN 1)<br>• **VLAN Hopping**: Angriff zum Überspringen von VLAN-Grenzen<br>• **Dynamic VLAN**: Dynamische VLAN-Zuweisung (z.B. über RADIUS)<br>• **Static VLAN**: Statische Port-zu-VLAN-Zuordnung<br>• **SVI** (Switch Virtual Interface): Virtuelles Interface für VLAN<br>• **EtherChannel/Port Channel**: Gebündelte Trunk-Verbindungen|
|**Wichtige Vokabeln**|• **Logische Segmentierung**: Virtuelle Aufteilung ohne physische Trennung<br>• **Broadcast-Traffic**: Rundsendungen an alle Geräte<br>• **Physikalische Infrastruktur**: Hardware-Netzwerk (Kabel, Switches)<br>• **Unabhängige Bereiche**: Getrennte Netzwerksegmente<br>• **Isolierung**: Trennung von Netzwerkverkehr<br>• **Übermäßiger Verkehr**: Zu viel Netzwerk-Traffic<br>• **Flache Netzwerke**: Nicht segmentierte Netzwerke<br>• **Abteilungsbasiert**: Nach Abteilungen organisiert<br>• **Sicherheitsanforderungen**: Datenschutz- und Schutzvorschriften<br>• **Physische Neuverkabelung**: Manuelle Kabelumsteckung<br>• **Kostenersparnis**: Finanzielle Einsparungen<br>• **Skalierbarkeit**: Erweiterungsfähigkeit<br>• **Verwaltungsvereinfachung**: Einfachere Administration<br>• **Flexibilität**: Anpassungsfähigkeit<br>• **Mini-Switches**: Virtuelle Switch-Segmente<br>• **Tag einfügen**: VLAN-Markierung hinzufügen<br>• **Tag entfernen**: VLAN-Markierung löschen<br>• **VLAN-bewusst**: VLAN-fähig (VLAN-aware)<br>• **Unbewusst**: Nicht VLAN-fähig (unaware)<br>• **Durchlaufen**: Traffic passiert (traverse)<br>• **Beibehalten**: Tag bleibt erhalten (retain)<br>• **Inter-Switch-Verbindung**: Verbindung zwischen Switches<br>• **Bandbreitenverbrauch**: Netzwerk-Traffic-Nutzung<br>• **Leistungseinbuße**: Performance-Verlust<br>• **Unbefugter Zugriff**: Zugriff ohne Berechtigung<br>• **Kompromittierte Geräte**: Infizierte/gehackte Geräte<br>• **Malware-Verbreitung**: Ausbreitung schädlicher Software|

---

## 80/20-Zusammenfassung: Die wichtigsten 20% zum Verständnis von 80% von VLANs

### **Was ist ein LAN? Wiederholung**

**LAN (Local Area Network)** = Lokales Netzwerk in begrenztem geografischem Bereich

**Traditionelles LAN**:

```
┌──────────────────────────────────────┐
│  EINE Broadcast-Domäne               │
│                                      │
│  [PC1] [PC2] [PC3] [Drucker] [Server]│
│         Alle im selben Switch        │
│                                      │
│  Broadcast von PC1 → ALLE empfangen  │
└──────────────────────────────────────┘
```

**Eigenschaft**: Alle Geräte = eine Broadcast-Domäne = alle hören alle Broadcasts

### **Das Problem: Große LANs werden unhandlich**

**4 Hauptprobleme großer, flacher LANs**:

#### **1. Sicherheitsrisiken** 🔓

```
Gast-WLAN + Finanz-Server im SELBEN Netzwerk?

Gast-Laptop (kompromittiert)
    ↓
Kann auf Finanz-Server zugreifen
    ↓
Datenleck! 💀
```

#### **2. Performance-Probleme** 🐌

```
1000 Geräte im selben LAN
    ↓
Jedes Broadcast geht an ALLE 1000 Geräte
    ↓
Bandbreite verschwendet, CPU-Last auf allen Geräten
```

#### **3. Verwaltungschaos** 😵

```
Sales, Engineering, HR, Gäste - alle durcheinander
→ Schwer zu verwalten
→ Schwer Richtlinien durchzusetzen
```

#### **4. Fehlende Flexibilität** 🔌

```
Mitarbeiter wechselt Abteilung
→ Physisch Kabel umstecken?
→ Ineffizient und teuer!
```

**Lösung**: **Netzwerksegmentierung** durch **VLANs**!

### **Was sind VLANs? Virtuelle Mini-Netzwerke**

**VLAN (Virtual Local Area Network)** = **Virtuelle** Unterteilung eines **physikalischen** LANs in **mehrere logisch getrennte** Netzwerke

**Kernidee**:

```
EIN physikalischer Switch
     ↓
Wird logisch aufgeteilt in mehrere "virtuelle Switches"
     ↓
Jedes VLAN = eigene Broadcast-Domäne
```

**Analogie**: Ein Bürogebäude mit offenen Räumen → VLANs sind wie **unsichtbare Trennwände**, die Abteilungen isolieren, obwohl sie im selben Gebäude (Switch) sind

### **VLAN-Beispiel: Vorher vs. Nachher**

#### **OHNE VLANs (traditionell)**:

```
Physische Trennung nötig:

┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Switch 1    │      │  Switch 2    │      │  Switch 3    │
│  (Sales)     │      │  (Engineering)│     │  (HR)        │
├──────────────┤      ├──────────────┤      ├──────────────┤
│ PC1  PC2  PC3│      │ PC4  PC5  PC6│      │ PC7  PC8  PC9│
└──────────────┘      └──────────────┘      └──────────────┘

Braucht: 3 Switches, viel Verkabelung, teuer!
```

#### **MIT VLANs (modern)**:

```
Logische Trennung auf EINEM Switch:

┌─────────────────────────────────────────────────────┐
│           EIN physikalischer Switch                 │
├─────────────────────────────────────────────────────┤
│  VLAN 10 (Sales)  │ VLAN 20 (Eng)  │ VLAN 30 (HR)  │
│  ┌──┬──┬──┐       │ ┌──┬──┬──┐     │ ┌──┬──┬──┐   │
│  │P1│P2│P3│       │ │P4│P5│P6│     │ │P7│P8│P9│   │
│  └──┴──┴──┘       │ └──┴──┴──┘     │ └──┴──┴──┘   │
└─────────────────────────────────────────────────────┘

Braucht: 1 VLAN-fähiger Switch (Managed Switch)
Vorteile: Günstiger, flexibler, einfacher!
```

**Wichtig**: Geräte in **VLAN 10** können **NICHT** direkt mit Geräten in **VLAN 20** kommunizieren (ohne Router/Layer-3-Switch)!

### **Wie VLANs funktionieren: VLAN-Tagging (802.1Q)**

**Problem**: Wie weiß ein Switch, zu welchem VLAN ein Frame gehört?

**Lösung**: **VLAN-Tag** im Ethernet-Frame

**IEEE 802.1Q Standard**:

```
Normaler Ethernet-Frame:
┌────────┬────────┬──────────┬─────────┬─────┐
│Ziel-MAC│Quell-MAC│ EtherType│ Payload │ FCS │
└────────┴────────┴──────────┴─────────┴─────┘

Mit 802.1Q VLAN-Tag:
┌────────┬────────┬──────────┬──────────┬─────────┬─────┐
│Ziel-MAC│Quell-MAC│ 802.1Q   │ EtherType│ Payload │ FCS │
│        │        │ VLAN-Tag │          │         │     │
│        │        │ (4 Bytes)│          │         │     │
└────────┴────────┴──────────┴──────────┴─────────┴─────┘
                      ↑
                VLAN ID (VID): z.B. 10
```

**VLAN-Tag enthält**:

- **VLAN ID (VID)**: Nummer 1-4094 (identifiziert VLAN)
- **Priority**: QoS-Priorität
- **Tag Protocol Identifier (TPID)**: 0x8100 (kennzeichnet 802.1Q)

### **Access Ports vs. Trunk Ports: Die zwei Port-Typen**

#### **Access Port (Zugangs-Port)** 🚪

**Eigenschaften**:

- Gehört zu **EINEM VLAN**
- Für **Endgeräte** (PCs, Drucker, Telefone)
- Geräte sind **VLAN-unbewusst** (wissen nichts von VLANs)
- Switch **fügt** VLAN-Tag hinzu beim Senden (zu Trunk)
- Switch **entfernt** VLAN-Tag beim Empfangen (von Trunk)

**Beispiel**:

```
PC1 (VLAN 10) → Access Port 1
PC2 (VLAN 20) → Access Port 2

PC1 sendet normalen Frame (ohne Tag)
    ↓
Switch Port 1 (Access, VLAN 10):
"Das ist VLAN 10-Traffic"
    ↓
Fügt Tag "VLAN 10" hinzu (falls zu Trunk)
```

**Konfiguration** (Cisco-Beispiel):

```
interface FastEthernet0/1
  switchport mode access
  switchport access vlan 10
```

#### **Trunk Port (Trunk-Port)** 📦

**Eigenschaften**:

- Trägt Traffic für **MEHRERE VLANs**
- Für **Inter-Switch-Verbindungen** oder **Router-Verbindungen**
- Frames behalten **VLAN-Tag** (802.1Q)
- Empfänger kann anhand Tag VLAN identifizieren

**Beispiel**:

```
┌────────────┐                    ┌────────────┐
│  Switch A  │                    │  Switch B  │
│            │                    │            │
│ VLAN 10 ──┐│ Trunk (trägt alle) │┌── VLAN 10 │
│ VLAN 20 ──┼┼────────────────────┼┼── VLAN 20 │
│ VLAN 30 ──┘│  VLANs 10, 20, 30  │└── VLAN 30 │
└────────────┘                    └────────────┘

Über Trunk fließen Frames mit Tags:
[VLAN 10] [VLAN 20] [VLAN 10] [VLAN 30]...
```

**Konfiguration** (Cisco-Beispiel):

```
interface GigabitEthernet0/1
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30
```

### **Access vs. Trunk: Vergleichstabelle**

|Merkmal|Access Port|Trunk Port|
|---|---|---|
|**VLANs**|EIN VLAN|MEHRERE VLANs|
|**Verbindet**|Endgeräte|Switches, Router|
|**VLAN-Tag**|Entfernt/Hinzugefügt|Bleibt erhalten|
|**Geräte-Bewusstsein**|VLAN-unbewusst|VLAN-bewusst|
|**Verwendung**|PC, Drucker, Telefone|Inter-Switch-Links|
|**Beispiel**|PC an Port 5|Switch-zu-Switch|

### **Native VLAN: Der Sonderfall**

**Native VLAN** = VLAN für **ungetaggten** Traffic auf Trunk-Ports

**Standard**: VLAN 1 (Default VLAN)

**Funktionsweise**:

```
Trunk empfängt Frame OHNE Tag
    ↓
"Das muss Native VLAN sein!"
    ↓
Zuordnung zu Native VLAN (z.B. VLAN 1)
```

**Warum wichtig?**

- Abwärtskompatibilität mit nicht-802.1Q-Geräten
- Management-Traffic (CDP, VTP) oft im Native VLAN

**Sicherheitshinweis**: Native VLAN **sollte geändert werden** (nicht VLAN 1 nutzen) → verhindert VLAN-Hopping-Angriffe

### **Praktisches VLAN-Beispiel**

**Szenario**: Firma mit 3 Abteilungen auf einem Switch

```
┌───────────────────────────────────────────────────┐
│           Managed Switch                          │
├───────────────────────────────────────────────────┤
│ Port 1-5: VLAN 10 (Sales)       - Access Ports   │
│ Port 6-10: VLAN 20 (Engineering) - Access Ports  │
│ Port 11-15: VLAN 30 (Guest)      - Access Ports  │
│ Port 24: Trunk zu Router         - Trunk Port    │
└───────────────────────────────────────────────────┘
```

**Kommunikation**:

**Innerhalb eines VLANs** (z.B. VLAN 10):

```
PC1 (Port 1, VLAN 10) → PC2 (Port 3, VLAN 10)
    ✅ Funktioniert direkt (gleiche Broadcast-Domäne)
```

**Zwischen VLANs** (z.B. VLAN 10 → VLAN 20):

```
PC1 (VLAN 10) → PC6 (VLAN 20)
    ❌ Funktioniert NICHT direkt!
    ✅ Braucht Router (Inter-VLAN-Routing)

Ablauf mit Router:
1. PC1 → Switch (VLAN 10)
2. Switch → Router (über Trunk, Tag: VLAN 10)
3. Router: Routing-Entscheidung
4. Router → Switch (über Trunk, Tag: VLAN 20)
5. Switch → PC6 (VLAN 20)
```

### **Inter-VLAN-Routing: Kommunikation zwischen VLANs**

**Problem**: VLANs sind **isoliert** → keine direkte Kommunikation

**Lösung**: **Router** oder **Layer-3-Switch**

**Methode 1: Router-on-a-Stick**

```
┌────────────┐
│   Router   │
│  (1 Port)  │
└──────┬─────┘
       │ Trunk (Sub-Interfaces)
       │ - VLAN 10: 192.168.10.1/24
       │ - VLAN 20: 192.168.20.1/24
       │ - VLAN 30: 192.168.30.1/24
       │
┌──────┴─────────────────────────┐
│    Managed Switch               │
│  VLANs 10, 20, 30              │
└────────────────────────────────┘
```

**Methode 2: Layer-3-Switch** (moderner):

```
Layer-3-Switch mit Routing:
- Kann direkt zwischen VLANs routen
- Schneller als externe Router
- SVIs (Switch Virtual Interfaces) für jedes VLAN
```

### **Vorteile von VLANs: Die 5 Hauptbenefits**

#### **1. Verbesserte Sicherheit** 🔒

```
VLAN 10 (Employees) → Zugriff auf interne Ressourcen
VLAN 99 (Guests)    → Nur Internet-Zugriff

Gäste können Firmen-Server NICHT erreichen!
```

#### **2. Reduzierter Broadcast-Traffic** 📉

```
Ohne VLANs:
Broadcast → 500 Geräte empfangen

Mit VLANs (5 VLANs à 100 Geräte):
Broadcast in VLAN 10 → nur 100 Geräte empfangen
75% weniger Broadcast-Traffic!
```

#### **3. Kostenersparnis** 💰

```
Ohne VLANs: 5 physikalische Switches nötig
Mit VLANs: 1 Managed Switch reicht

Einsparung: Hardware, Verkabelung, Strom, Wartung
```

#### **4. Flexibilität** 🔄

```
Mitarbeiter wechselt von Sales zu Engineering:

Ohne VLANs: Kabel physisch umstecken
Mit VLANs: Port-Konfiguration ändern (30 Sekunden!)

switchport access vlan 20  (statt vlan 10)
```

#### **5. Vereinfachte Verwaltung** 🎯

```
Logische Gruppierung nach Funktion, nicht nach Ort:

Accounting-VLAN (VLAN 50):
- Alle Buchhaltungs-PCs
- Egal ob 1. Stock, 3. Stock, oder Zweigstelle
- Gleiche Sicherheitsrichtlinien für alle
```

### **VLAN-Sicherheit: Angriffe und Schutz**

⚠️ **VLAN Hopping** (Hauptangriff)

**Angriff 1: Double Tagging**

```
Angreifer in VLAN 10 sendet Frame:
[Outer Tag: VLAN 10] [Inner Tag: VLAN 20] [Payload]

Switch 1: Entfernt Outer Tag (VLAN 10)
    ↓
Frame hat jetzt nur noch Inner Tag (VLAN 20)
    ↓
Switch 2: "Das ist VLAN 20!" → Leitet an VLAN 20 weiter

Angreifer umgeht VLAN-Isolation! 💀
```

**Angriff 2: Switch Spoofing**

```
Angreifer sendet DTP-Pakete (Dynamic Trunking Protocol)
    ↓
Täuscht Switch: "Ich bin ein anderer Switch!"
    ↓
Port wird zum Trunk
    ↓
Angreifer empfängt Traffic aller VLANs
```

**Schutzmaßnahmen**:

✅ **Native VLAN ändern** (nicht VLAN 1):

```
switchport trunk native vlan 999
```

✅ **DTP deaktivieren** (kein Auto-Trunking):

```
switchport mode access
switchport nonegotiate
```

✅ **Nicht genutzte Ports deaktivieren**:

```
interface range FastEthernet0/10-24
  shutdown
  switchport access vlan 999  (unused VLAN)
```

✅ **Port Security**:

```
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
```

### **VLAN-Best-Practices**

1. **Nicht VLAN 1 nutzen** → Sicherheitsrisiko, weil Default
2. **Native VLAN ändern** → Verhindert Double-Tagging
3. **Management VLAN separieren** → Switch-Verwaltung isolieren
4. **Voice VLANs für VoIP** → QoS für Telefone
5. **Dokumentation** → Welches VLAN wofür?
6. **VLAN-Naming** → Aussagekräftige Namen (nicht nur Nummern)
7. **Least Privilege** → Nur nötige VLANs auf Trunks erlauben

### **VLAN-Konfiguration (Cisco-Beispiel)**

**VLAN erstellen**:

```
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name Engineering
Switch(config-vlan)# exit
```

**Access Port konfigurieren**:

```
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

**Trunk Port konfigurieren**:

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# switchport trunk native vlan 99
Switch(config-if)# exit
```

**VLANs anzeigen**:

```
Switch# show vlan brief
Switch# show interfaces trunk
```

### **Kernbotschaft**

**VLANs** ermöglichen **logische Netzwerksegmentierung** auf **einem physikalischen Switch**:

**Problem**:

- Große, flache LANs = unsicher, langsam, unflexibel, schwer zu verwalten

**Lösung**:

- **VLANs** teilen ein physisches LAN in **mehrere virtuelle LANs**
- Jedes VLAN = **eigene Broadcast-Domäne**
- Geräte in verschiedenen VLANs **isoliert** voneinander

**Technologie**:

- **IEEE 802.1Q**: VLAN-Tagging-Standard
- **Access Ports**: Ein VLAN, für Endgeräte
- **Trunk Ports**: Mehrere VLANs, für Inter-Switch-Links

**Vorteile**:

- ✅ **Sicherheit** (Isolation)
- ✅ **Performance** (weniger Broadcasts)
- ✅ **Flexibilität** (logische Zuordnung)
- ✅ **Kostenersparnis** (weniger Hardware)
- ✅ **Vereinfachte Verwaltung** (zentrale Konfiguration)

**Inter-VLAN-Kommunikation**: Braucht **Router** oder **Layer-3-Switch**

**Analogie finale**: VLANs sind wie **unsichtbare Trennwände in einem Großraumbüro** – physisch ein Raum (Switch), aber logisch mehrere getrennte Bereiche (VLANs). Jede Abteilung (VLAN) hat ihren eigenen Bereich und kann die anderen nicht stören, obwohl alle im selben Gebäude (Switch) sind! 🏢🔀🛡️