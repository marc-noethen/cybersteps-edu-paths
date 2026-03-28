# 🌐 ISP Spotter

**Kurs:** Netzwerktechnik | **Datum:** 31.01.2026

---

## Aufgabe

**Ziel:** Unterschied zwischen lokaler und öffentlicher IP-Adresse verstehen und die Rolle des ISPs in IP-Registrierungen erkennen.

---

## Umgebung

```
Lokale IP:      192.168.0.92 (aus Aufgabe 1)
Öffentliche IP: 92.206.120.5
Tool:           https://whatismyipaddress.com/
Whois-Tool:     IP Lookup Service
```

---

## Durchführung

**Schritt 1 - Öffentliche IP ermitteln:**
- **Service:** whatismyipaddress.com
- **Ergebnis IPv4:** 92.206.120.5
- **Ergebnis IPv6:** 2001:4860:7:610::ec

**Schritt 2 - Whois Lookup:**
```
IP:             92.206.120.5
Country:        Germany
Country ISO:    DE
State:          Sachsen-Anhalt
City:           Halberstadt
Postal Code:    38820
Latitude:       51.8956
Longitude:      11.0562
Organization:   Tele Columbus AG
ISP:            Tele Columbus AG
```

---

## Analyse

### IP-Adress-Vergleich

| Typ | IP-Adresse | Gültigkeitsbereich | Zweck |
|-----|------------|--------------------|-------|
| Lokal (privat) | 192.168.0.92 | Heimnetzwerk | Kommunikation zwischen Geräten im lokalen Netz |
| Öffentlich | 92.206.120.5 | Internet (global) | Kommunikation mit dem Internet |

### ISP-Informationen

| Parameter | Wert |
|-----------|------|
| Organisation | Tele Columbus AG |
| ISP | Tele Columbus AG |
| Land | Deutschland (DE) |
| Bundesland | Sachsen-Anhalt |
| Stadt | Halberstadt |

---

## Antworten

**Frage:** Erkläre den Unterschied zwischen lokaler und öffentlicher IP-Adresse und beschreibe die Rolle von ISP und Router.

**Antwort:**

**Lokale IP-Adresse (192.168.0.92):**
- Wird vom Router im Heimnetzwerk vergeben
- Nur innerhalb des eigenen Netzwerks gültig
- Ermöglicht Kommunikation zwischen Geräten im selben Netzwerk (z.B. Laptop ↔ Smartphone ↔ Drucker)
- Nicht im Internet routbar
- Privater Adressbereich (RFC 1918)

**Öffentliche IP-Adresse (92.206.120.5):**
- Vom ISP (Tele Columbus AG) zugewiesen
- Global eindeutig im Internet
- Identifiziert den Router/Anschluss nach außen
- Ermöglicht Kommunikation mit dem Rest der Welt
- Wird für alle Geräte im Heimnetzwerk gemeinsam genutzt

**Rolle des Routers:**
- Übersetzt zwischen lokalen und öffentlichen IP-Adressen (NAT - Network Address Translation)
- Verwaltet das lokale Netzwerk (DHCP)
- Leitet Anfragen aus dem Heimnetzwerk ins Internet weiter
- Empfängt Antworten aus dem Internet und leitet sie an das richtige lokale Gerät

**Rolle des ISPs:**
- Stellt die Internetverbindung bereit
- Weist die öffentliche IP-Adresse zu (dynamisch oder statisch)
- Routet den Datenverkehr zwischen dem Heimnetzwerk und dem Internet
- Verwaltet IP-Adressblöcke (hier: 92.206.120.x Bereich)

**Kommunikationsweg:**
```
Laptop (192.168.0.92) → Router (192.168.0.1 lokal / 92.206.120.5 öffentlich) 
    → ISP (Tele Columbus) → Internet → Zielserver → ISP → Router → Laptop
```

---

## Notizen

- NAT (Network Address Translation) ermöglicht es mehreren Geräten, eine öffentliche IP zu teilen
- Private IP-Bereiche: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- Die öffentliche IP kann sich ändern (dynamische IP), wenn der ISP sie neu zuweist
- IPv6 ermöglicht jedem Gerät eine eigene öffentliche Adresse (hier: 2001:4860:7:610::ec)
