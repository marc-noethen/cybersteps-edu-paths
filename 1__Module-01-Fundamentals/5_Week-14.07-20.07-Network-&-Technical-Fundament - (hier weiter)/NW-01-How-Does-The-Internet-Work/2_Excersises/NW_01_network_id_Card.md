# 🌐 Network ID Card

**Kurs:** Netzwerktechnik | **Datum:** 31.01.2026

---

## Aufgabe

**Ziel:** IPv4-Adresse des eigenen Computers mittels `ipconfig` (Windows) bzw. `ifconfig` (macOS/Linux) identifizieren und den Befehl zur Erreichbarkeitsprüfung angeben.

---

## Umgebung

```
Interface:   WLAN (Drahtlos-LAN-Adapter)
Lokale IP:   192.168.0.92
Router IP:   192.168.0.1
Tool:        ipconfig (Windows Command Prompt)
DNS-Suffix:  utopia.net
Subnetzmaske: 255.255.255.0
```

---

## Durchführung

**Befehl ausgeführt:**
```bash
ipconfig
```

**Ausgabe:**
```
Drahtlos-LAN-Adapter WLAN:
   Verbindungsspezifisches DNS-Suffix: utopia.net
   IPv4-Adresse  . . . . . . . . . . : 192.168.0.92
   Subnetzmaske  . . . . . . . . . . : 255.255.255.0
   Standardgateway . . . . . . . . . : 192.168.0.1
```

---

## Analyse

### Netzwerkkonfiguration

| Parameter | Wert |
|-----------|------|
| Aktives Interface | WLAN (Drahtlos-LAN-Adapter) |
| IPv4-Adresse | 192.168.0.92 |
| Subnetzmaske | 255.255.255.0 |
| Standardgateway | 192.168.0.1 |
| DNS-Suffix | utopia.net |

### Verbindungstest

**Befehl für Erreichbarkeitsprüfung:**
```bash
ping www.google.com
```

---

## Antworten

**Aufgabe 1-4:** IPv4-Adresse identifizieren
- **Antwort:** `192.168.0.92`
- **Interface:** Drahtlos-LAN-Adapter WLAN (status: active)

**Aufgabe 5:** Befehl zur Verbindungsprüfung
- **Antwort:** `ping www.google.com`

---

## Notizen

- Die IPv4-Adresse 192.168.0.92 ist eine private IP-Adresse (Class C)
- Das aktive Interface ist der WLAN-Adapter
- Der Standardgateway (Router) hat die IP 192.168.0.1
- Der `ping` Befehl sendet ICMP Echo Request Pakete zur Erreichbarkeitsprüfung
