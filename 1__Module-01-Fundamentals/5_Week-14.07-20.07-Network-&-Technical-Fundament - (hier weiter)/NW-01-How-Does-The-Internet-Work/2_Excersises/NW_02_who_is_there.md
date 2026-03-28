# 🌐 Who Is There

**Kurs:** Netzwerktechnik | **Datum:** 31.01.2026

---

## Aufgabe

**Ziel:** Verbindung zu einem öffentlichen Server testen, die Organisation des IP-Blocks identifizieren und mit einer nicht routbaren Adresse vergleichen.

---

## Umgebung

```
Tool:           ping (Windows Command Prompt)
Ziel-IP 1:      1.1.1.1 (Cloudflare DNS)
Ziel-IP 2:      192.0.2.1 (Dokumentations-IP)
Whois-Tool:     Online IP Whois Lookup
```

---

## Durchführung

**Test 1 - Erreichbare IP:**
```bash
ping -n 5 1.1.1.1
```

**Ausgabe:**
```
Ping wird ausgeführt für 1.1.1.1 mit 32 Bytes Daten:
Antwort von 1.1.1.1: Bytes=32 Zeit=15ms TTL=54
Ping-Statistik für 1.1.1.1:
    Pakete: Gesendet = 5, Empfangen = 5, Verloren = 0
    (0% Verlust),
Ca. Zeitangaben in Millisek.:
    Minimum = 14ms, Maximum = 23ms, Mittelwert = 16ms
```

**Test 2 - Nicht routbare IP:**
```bash
ping 192.0.2.1
```

**Ausgabe:**
```
Ping wird ausgeführt für 192.0.2.1 mit 32 Bytes Daten:
Zeitüberschreitung der Anforderung.
Ping-Statistik für 192.0.2.1:
    Pakete: Gesendet = 4, Empfangen = 0, Verloren = 4
    (100% Verlust),
```

---

## Analyse

### Ping-Vergleich

| IP-Adresse | Typ | Pakete gesendet | Empfangen | Verloren | Durchschnitt | Verhalten |
|------------|-----|-----------------|-----------|----------|--------------|-----------|
| 1.1.1.1 | Öffentlicher DNS | 5 | 5 | 0 (0%) | 16ms | Erfolgreich |
| 192.0.2.1 | Dokumentations-IP | 4 | 0 | 4 (100%) | - | Zeitüberschreitung |

### Whois-Ergebnis für 1.1.1.1

```
org-name: APNIC Research and Development
```

---

## Antworten

**Frage 4:** Organisation des IP-Blocks 1.1.1.1
- **Antwort:** APNIC Research and Development
- **Hinweis:** Cloudflare nutzt diesen IP-Block für ihren öffentlichen DNS-Service

**Frage 5:** Unterschied im Verhalten zwischen 1.1.1.1 und 192.0.2.1

**Antwort:**
- **1.1.1.1:** Alle 5 Pakete wurden erfolgreich empfangen mit durchschnittlich 16ms Latenz
- **192.0.2.1:** Alle 4 Pakete gingen verloren (100% Paketverlust) mit "Zeitüberschreitung der Anforderung"

**Erklärung:**
- 192.0.2.1 ist eine Dokumentations-IP-Adresse (TEST-NET-1, RFC 5737) und nicht routbar im Internet
- Diese IP-Adresse ist ausschließlich für Dokumentationszwecke reserviert
- Keine Router im Internet leiten Pakete an diese Adresse weiter

---

## Notizen

- Der `-n 5` Parameter bei Windows entspricht `-c 5` bei Linux/macOS
- 1.1.1.1 ist Cloudflares öffentlicher DNS-Server (schnell und zuverlässig)
- TTL=54 zeigt, dass das Paket 54 Hops übrig hat (ursprünglich wahrscheinlich 64)
- Dokumentations-IPs (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) sollten niemals im Internet geroutet werden
