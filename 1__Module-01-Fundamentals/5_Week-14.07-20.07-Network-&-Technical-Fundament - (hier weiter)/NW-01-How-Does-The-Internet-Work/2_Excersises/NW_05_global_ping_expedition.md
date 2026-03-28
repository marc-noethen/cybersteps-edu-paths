# 🌐 Global Ping Expedition

**Kurs:** Netzwerktechnik | **Datum:** 31.01.2026

---

## Aufgabe

**Ziel:** Zusammenhang zwischen geografischer Distanz, Anzahl der Netzwerk-Hops und Latenz durch Traceroute zu verschiedenen globalen Standorten untersuchen.

---

## Umgebung

```
Standort:       Deutschland (Halberstadt, Sachsen-Anhalt)
Tool:           tracert (Windows Command Prompt)
ISP:            Tele Columbus AG
Lokale IP:      192.168.0.92
```

---

## Durchführung

### Test 1: Europa - Großbritannien
**Ziel:** www.ox.ac.uk (University of Oxford)

```bash
tracert www.ox.ac.uk
```

**Ausgabe:**
```
Routenverfolgung zu www.ox.ac.uk.cdn.cloudflare.net [104.20.34.13]
über maximal 30 Hops:

  1     9 ms     2 ms     1 ms  192.168.0.1
  2     *        *        *     Zeitüberschreitung der Anforderung.
  3     9 ms     9 ms     9 ms  172.17.166.37
  4    15 ms     8 ms     9 ms  172.17.166.21
  5    18 ms     8 ms     9 ms  172.17.80.161
  6     9 ms     8 ms     8 ms  172.17.80.205
  7    11 ms     9 ms    10 ms  172.17.80.206
  8    22 ms    10 ms    10 ms  80.64.181.65
  9    22 ms    13 ms    14 ms  109.104.59.228
 10    24 ms    23 ms    34 ms  85.239.113.148
 11    14 ms    12 ms    21 ms  104.20.34.13
```

### Test 2: Europa - Frankreich
**Ziel:** www.bnf.fr (Bibliothèque nationale de France)

```bash
tracert www.bnf.fr
```

**Ausgabe (gekürzt):**
```
Routenverfolgung zu www.bnf.fr [194.199.8.10]
über maximal 30 Hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  8     9 ms     8 ms     8 ms  80.64.181.65
  9    32 ms    13 ms    25 ms  109.104.60.32
 10    17 ms    14 ms    29 ms  gw2.dus2.dogado.net [212.162.17.137]
 [...]
 15    29 ms    28 ms    28 ms  be12265.ccr41.par01.atlas.cogentco.com
 [...]
 22    43 ms    43 ms    45 ms  rap-vl165-te0-1-0-8-ren-nr-jussieu-rtr-091.noc.renater.fr
 23-30 *        *        *     Zeitüberschreitung (Ziel erreicht, antwortet nicht)
```

### Test 3: Nordamerika - USA
**Ziel:** www.mit.edu (Massachusetts Institute of Technology)

```bash
tracert www.mit.edu
```

**Ausgabe:**
```
Routenverfolgung zu e9566.dscb.akamaiedge.net [23.63.142.104]
über maximal 30 Hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    21 ms    13 ms    12 ms  109.104.61.181
 10     *        *        *     Zeitüberschreitung der Anforderung.
 11    14 ms    24 ms    14 ms  lo1.r02.stem01.ber01.fab.netarch.akamai.com
 12    12 ms    14 ms    13 ms  lo1.r02.spine02.ber01.fab.netarch.akamai.com
 13    14 ms    23 ms    14 ms  lo1.r02.leaf01.ber01.fab.netarch.akamai.com
 14    13 ms    14 ms    14 ms  vlan100.r11.tor01.ber01.fab.netarch.akamai.com
 15    13 ms    14 ms    14 ms  a23-63-142-104.deploy.static.akamaitechnologies.com
```

### Test 4: Ostasien - Japan
**Ziel:** www.u-tokyo.ac.jp (University of Tokyo)

```bash
tracert www.u-tokyo.ac.jp
```

**Ausgabe:**
```
Routenverfolgung zu www.u-tokyo.ac.jp [210.152.243.234]
über maximal 30 Hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    25 ms    20 ms    16 ms  85.232.3.243
 10    29 ms    15 ms    28 ms  gw2.dus2.dogado.net [212.162.17.137]
 11   260 ms   260 ms   259 ms  ae2.3601.edge1.Osaka1.level3.net
 12   243 ms   247 ms   242 ms  8.245.34.46
 13   252 ms   243 ms   248 ms  163.139.136.67
 14   243 ms   244 ms   243 ms  202.79.80.158
 15-16 *        *        *     Zeitüberschreitung der Anforderung.
 17   258 ms   259 ms   263 ms  158.205.121.24
```

### Test 5: Ostasien - Japan (Alternative)
**Ziel:** www.nii.ac.jp (National Institute of Informatics)

```bash
tracert www.nii.ac.jp
```

**Ausgabe:**
```
Routenverfolgung zu lb-nii-ssl-www-333134043.ap-northeast-1.elb.amazonaws.com [3.115.145.97]
über maximal 30 Hops:

  1    11 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    27 ms    18 ms    18 ms  BYMUC-MC01.hlkomm.net [109.104.60.129]
 10    20 ms    21 ms    20 ms  ae12-405.muc10.core-backbone.com
 11   177 ms   173 ms   173 ms  ae3-2090.sin10.core-backbone.com
```

---

## Analyse

### Zusammenfassung der Ergebnisse

| Server | Region | GeoIP-Standort | Hops | Finale Latenz | Besonderheiten |
|--------|--------|----------------|------|---------------|----------------|
| www.ox.ac.uk | Europa (UK) | Cloudflare CDN (104.20.34.13) | 11 | ~16 ms | Via Cloudflare CDN |
| www.bnf.fr | Europa (FR) | Paris (194.199.8.10) | 22 | ~44 ms | Via Renater (FR Academic Network) |
| www.mit.edu | Nordamerika | Berlin - Akamai CDN (23.63.142.104) | 15 | ~14 ms | Lokal in Berlin gecacht! |
| www.u-tokyo.ac.jp | Ostasien (JP) | Tokyo (210.152.243.234) | 17+ | ~260 ms | Echter Japan-Server |
| www.nii.ac.jp | Ostasien (JP) | Tokyo - AWS (3.115.145.97) | 11 | ~175 ms | Via Singapur zu AWS Tokyo |

### GeoIP-Verifizierung

**Oxford (www.ox.ac.uk):**
- **IP:** 104.20.34.13
- **Tatsächlicher Standort:** Cloudflare CDN - wahrscheinlich Deutschland/Europa
- **Erwartete Region:** UK ✗ (CDN hat lokalen Edge-Server)

**BnF (www.bnf.fr):**
- **IP:** 194.199.8.10
- **Tatsächlicher Standort:** Paris, Frankreich (Renater-Netzwerk)
- **Erwartete Region:** Frankreich ✓

**MIT (www.mit.edu):**
- **IP:** 23.63.142.104
- **Tatsächlicher Standort:** Berlin, Deutschland (Akamai CDN)
- **Erwartete Region:** USA ✗ (Akamai Edge in Berlin)

**U-Tokyo (www.u-tokyo.ac.jp):**
- **IP:** 210.152.243.234
- **Tatsächlicher Standort:** Tokyo, Japan (via Osaka Level3)
- **Erwartete Region:** Japan ✓

**NII (www.nii.ac.jp):**
- **IP:** 3.115.145.97
- **Tatsächlicher Standort:** Tokyo, Japan (AWS ap-northeast-1)
- **Erwartete Region:** Japan ✓

---

## Bericht: Analyse der Korrelationen

### 1. Latenz und geografische Distanz

**Beobachtungen:**
- **Innerhalb Europas (UK/FR via CDN):** 14-44 ms
- **Nordamerika (via lokales CDN):** 14 ms (!)
- **Ostasien (echter Server):** 175-260 ms

**Fazit:** 
Die Latenz steigt **nicht immer** mit geografischer Distanz. CDNs (Content Delivery Networks) wie Cloudflare und Akamai haben lokale Edge-Server in Deutschland, die Inhalte cachen. Dadurch können geografisch weit entfernte Websites (MIT in USA) schneller sein als nähere Standorte ohne CDN (BnF in Frankreich).

**Bei echten Servern ohne CDN** ist die Korrelation deutlich:
- Paris (BnF): ~800 km → ~44 ms
- Tokyo (U-Tokyo): ~9000 km → ~260 ms

**Lichtgeschwindigkeits-Limit:** 
Die theoretische Mindestlatenz für 9000 km beträgt ~30 ms (Hin- und Rückweg, 2/3 Lichtgeschwindigkeit in Glasfaser). Die tatsächlichen 260 ms zeigen, dass Routing-Delays und Verarbeitungszeit erheblich zur Gesamtlatenz beitragen.

### 2. Anzahl der Hops und Distanz

**Beobachtungen:**
- **Lokales CDN (MIT/Oxford):** 11-15 Hops, aber geringe Latenz
- **Paris ohne CDN (BnF):** 22 Hops, moderate Latenz  
- **Japan (echte Server):** 11-17 Hops, sehr hohe Latenz

**Fazit:**
Die Anzahl der Hops korreliert **nicht zwingend** mit der Distanz. Wichtiger ist die **Art der Hops**:
- Viele Hops in gut vernetzten Regionen (Europa) können schnell sein
- Wenige Hops über lange Unterwasser-Kabel (Deutschland → Japan) sind langsam

### 3. Stärkere Korrelation: Latenz vs. Hops oder Latenz vs. Distanz?

**Antwort: Es ist komplex und gemischt.**

**Hauptfaktoren für Latenz:**

1. **Physische Distanz** (bei echten Servern):
   - Japan: 9000 km → 260 ms
   - Paris: 800 km → 44 ms
   - Berlin (CDN): 200 km → 14 ms

2. **Netzwerk-Qualität der Hops:**
   - Hop 11 (U-Tokyo): Deutschland → Japan Sprung = +230 ms (!)
   - Hops 1-10: Nur ~30 ms kumulativ

3. **CDN-Präsenz:**
   - MIT (USA) über Berlin-CDN: 14 ms
   - BnF (Paris) ohne CDN: 44 ms

**Besonders auffällig bei U-Tokyo:**
```
Hop 10: 29 ms (Deutschland, dogado)
Hop 11: 260 ms (Osaka, Level3) → +231 ms für einen Hop!
```

Dieser eine Hop über das Unterwasser-Kabel nach Japan verursacht mehr Latenz als alle vorherigen Hops zusammen.

### 4. Delay-Verursacher im Netzwerkpfad

**Basierend auf den tracert-Ausgaben:**

**a) Physische Distanz / Kabel-Länge:**
- Größter Einzelfaktor bei interkontinentalen Verbindungen
- Beispiel: Deutschland → Japan Hop: +230 ms

**b) Router-Processing und Queuing:**
- Jeder Hop verarbeitet Pakete: 1-3 ms pro Hop typisch
- 15 Hops × 2 ms = 30 ms zusätzlich

**c) Backbone-Übergänge:**
- Peering-Points zwischen ISPs
- Beispiel: Tele Columbus → Level3 → Cogent → Renater (BnF)

**d) Congestion (Überlastung):**
- Sichtbar an schwankenden Zeiten
- Beispiel BnF Hop 9: 32 ms, 13 ms, 25 ms (Varianz!)

**e) Kontinental-Überquerungen:**
- Unterwasser-Kabel (Deutschland → Japan)
- Transatlantik wäre ähnlich (Deutschland → USA-Ostküste)

**f) Nicht-Antwortende Hops (`* * *`):**
- Verursachen keine zusätzliche Latenz für den Traffic
- ICMP wird nur nicht beantwortet (Firewall-Policy)

**Latenz-Budget Beispiel (U-Tokyo):**
- Lokale Hops 1-10: ~30 ms
- Deutschland → Japan Kabel: ~230 ms
- Processing in Japan: ~0 ms (bereits im Total)
- **Gesamt: ~260 ms**

---

## Antworten

**1. Steigt Latenz mit geografischer Distanz?**

Ja, bei echten Servern **ohne CDN** ist eine klare Korrelation sichtbar:
- Paris: ~800 km → ~44 ms
- Tokyo: ~9000 km → ~260 ms

**Aber:** CDNs brechen diese Regel, indem sie Inhalte lokal cachen (MIT in Berlin mit nur 14 ms trotz USA-Server).

**2. Steigt die Anzahl der Hops mit Distanz?**

**Nicht unbedingt.** Die Hop-Anzahl hängt eher von der Netzwerk-Topologie ab:
- Japan (9000 km): 11-17 Hops
- Paris (800 km): 22 Hops

Gut vernetzte Backbone-Provider (Level3, Cogent) ermöglichen wenige Hops über große Distanzen.

**3. Stärkere Korrelation: Hops oder Distanz?**

**Distanz** hat bei interkontinentalen Verbindungen den größeren Einfluss. Ein einzelner Hop (Deutschland → Japan) verursacht mehr Delay als 10 lokale Hops.

**Aber:** In regional gut vernetzten Gebieten (Europa) können viele Hops wenig Latenz bedeuten, wenn die Hops hochwertige Verbindungen nutzen.

**4. Was verursacht Delays?**

Rangfolge nach Auswirkung:
1. **Interkontinentale Kabel** (+200+ ms)
2. **Physische Distanz** (Lichtgeschwindigkeit: 3.3 µs/km in Glasfaser)
3. **Router-Processing** (1-3 ms pro Hop)
4. **Network Congestion** (variabel, sichtbar an Schwankungen)
5. **Peering-Points** (ISP-Übergänge)

---

## Notizen

### Wichtige Erkenntnisse:

- **CDNs verändern alles:** MIT (USA) ist schneller als BnF (Frankreich) durch lokales Caching
- **Unterwasser-Kabel sind langsam:** Ein Hop nach Japan = +230 ms
- **`* * *` bedeutet nicht "blockiert":** Pakete kommen durch, nur ICMP-Antworten werden gefiltert
- **Hop-Anzahl ≠ Distanz:** Netzwerk-Topologie ist wichtiger
- **Varianz zeigt Congestion:** Schwankende Zeiten (13 ms, 25 ms, 32 ms) deuten auf Überlastung hin

### Technische Details:

- **Level3** (jetzt Lumen/CenturyLink): Großer internationaler Backbone-Provider
- **Cogent:** Budget-Backbone mit dichtem Netz in Europa
- **Renater:** Französisches akademisches Netzwerk (wie DFN in Deutschland)
- **Akamai/Cloudflare:** CDN-Anbieter mit Edge-Servern weltweit

### Verbesserungsmöglichkeiten:

- Bei wiederholtem Timeout: Alternativen Server probieren
- GeoIP-Tools können ungenau sein bei Anycast-Netzwerken (CDNs)
- Mehrere Tests zu verschiedenen Tageszeiten zeigen Congestion-Muster
