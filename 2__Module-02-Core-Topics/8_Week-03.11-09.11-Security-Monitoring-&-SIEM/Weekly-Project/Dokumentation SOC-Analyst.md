1. **Vorbereitung**
	1. Die Vorbereitungsphase bezieht sich auf die Bereitschaft einer Organisation gegenüber einem Angriff. Das bedeutet, die *Anforderungen zu dokumentieren*, die *Richtlinien zu definieren*, die *Sicherheitskontrollen zur Überwachung einzubinden* wie EDR / SIEM / IDS / IPS usw. Es beinhaltet auch die *Anstellung/Weiterbildung des Personals*
	
2. **Erkennung** und **Analyse**
	1. Die Erkennungsphase umfasst alles, was mit der *Erkennung eines Vorfalls und dessen Analyse zusammenhängt*. Diese Phase umfasst das *Erhalten von Warnmeldungen von Sicherheitskontrollen* wie SIEM/EDR und die *Untersuchung der Warnmeldung*, um die Ursache zu finden. Diese Phase umfasst auch die *Suche nach unbekannten Bedrohungen* innerhalb des Unternehmens.
	
3. **Isolation, Beseitigung** und **Wiederherstellung**
	1. Diese Phase umfasst die *Maßnahmen*, die erforderlich sind, um eine *Ausbreitung* des Vorfalls zu *verhindern* und das Netzwerk zu *sichern*. Dazu gehören Schritte, um eine Ausbreitung des Angriffs im Netzwerk zu verhindern, den infizierten Host zu *isolieren*, das Netzwerk von den Spuren der *Infektion zu befreien* und die *Kontrolle* über den Angriff *zurückzugewinnen*.
	
4. Aktivitäten nach dem Vorfall / **Gewonnene Erkenntnisse**
	1. In dieser Phase werden die *Sicherheitslücken in der Organisation identifiziert*, die zu einem Eindringen geführt haben, und Verbesserungen vorgenommen, damit sich der Angriff nicht wiederholt. Dazu gehören die *Identifizierung der Schwachstellen*, die zum Angriff geführt haben, das *Hinzufügen von Erkennungsregeln*, damit sich ähnliche Verstöße *nicht wiederholen*, und vor allem die *Schulung der Mitarbeiter*, falls erforderlich.

# Cyber Kill Chain
- Unsere Aufgabe als Sicherheitsanalyst wäre es, diesen Cyber-Angriff zu untersuchen und die Aktivitäten des Angreifers in alle 7 Phasen der Cyber Kill Chain zu kartieren. 
- Wir folgen dem Cyber Kill Chain Modell und kartieren die Aktivitäten des Angreifers in jeder Phase während dieser Untersuchung. 
- Wenn erforderlich, werden wir auch Open Source Intelligence (OSINT) und andere Fundstellen nutzen, um Lücken in der Kill Chain zu füllen. 
- Es ist nicht notwendig, diese Reihenfolge der Phasen während der Untersuchung zu befolgen.
	1. Reconnaissance  *Anerkennung*
	2. Weaponize  *Waffeneinsatz*
	3. Delivery  *Lieferung*
	4. Exploitation  *Ausbeutung*
	5. Installation 
	6. Command & Control  *Befehl und Kontrolle*
	7. Actions on Objectives  *Maßnahmen zu den Zielen*

---
### Detection and Analysis phase
**Splunk**
- Während unserer Untersuchung werden wir `Splunk` als unsere SIEM-Lösung verwenden
- Logs werden von Webserver/Firewall/Suricata/Sysmon usw. eingelesen

------------
	[->] Start VM und VPN 
		**$ cd Downloads**
		**$ sudo openvpn marcjannis89.ovpn**  
		**ping [IP]**
		
----
									 **Important**

| Log-Quelle     | Details                                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| wineventlog    | Enthält Windows-Event-Logs                                                                                                                                                                     |
| winRegistry    | Enthält die Logs im Zusammenhang mit der Erstellung/Änderung/Löschung der Registrierung usw.                                                                                                   |
| XmlWinEventLog | Enthält die Sysmon-Event-Logs. Es ist eine sehr wichtige Logquelle aus einer Untersuchungsperspektive.                                                                                         |
| fortigate_utm  | Enthält Fortinet-Firewall-Protokolle                                                                                                                                                           |
| iis            | Enthält IIS-Webserver-Protokolle                                                                                                                                                               |
| Nessus:scan    | Enthält die Ergebnisse des Nessus-Sicherheitsscanners                                                                                                                                          |
| Suricata       | Enthält die Details der Alarme aus der Suricata-IDS. Diese Logquelle zeigt, welcher Alarm ausgelöst wurde und was den Alarm ausgelöst hat — eine sehr wichtige Logquelle für die Untersuchung. |
| stream:http    | Enthält den Netzwerkfluss im Zusammenhang mit HTTP-Verkehr                                                                                                                                     |
| stream:DNS     | Enthält den Netzwerkfluss im Zusammenhang mit DNS-Verkehr                                                                                                                                      |
| stream:icmp    | Enthält den Netzwerkfluss im Zusammenhang mit ICMP-Verkehr                                                                                                                                     |
- **Hinweis**: Alle Ereignisprotokolle, die wir untersuchen werden, sind in `index=botsv1` vorhanden.
-  IP-Adresse zugewiesen: `10.10.252.28`

---
### Rekonnaissance-Phase
- Recherche ist ein Versuch, Informationen über ein Ziel zu entdecken und zu sammeln. Es kann Wissen über das verwendete System, die Webanwendung, die Mitarbeiter oder den Standort usw. umfassen.

1. Aus einer Analystenperspektive, wo müssen wir zuerst suchen?
	- Wenn wir die verfügbaren Protokolldatenquellen betrachten, finden wir  eingehenden Kommunikationen die zu unserem Webserver in der Protokolldatenquelle eingetragen werden, die den Webverkehr enthält.
	- [ ] Ich habe das Suchwort `imreallynotbatman.com` im Index `botsv1` durchsucht
	- [ ] Ich Stelle sicher das, `All Time` im Time Range Picker ausgewählt ist sowie der Verbose Mode
	- [ ] Im Feld `sourcetype`habe ich die folgenden Protokolldatenquellen die Spuren dieses Suchworts enthalten gefunden
		- *Suricata*
			- Enthält die Details der Alarme aus der Suricata-IDS. Diese Logquelle zeigt, welcher Alarm ausgelöst wurde und was den Alarm ausgelöst hat — eine sehr wichtige Logquelle für die Untersuchung.
		- *stream:http*
			- Enthält den Netzwerkfluss im Zusammenhang mit HTTP-Verkehr
		- *fortigate_utm*
			- Enthält Fortinet-Firewall-Protokolle
		- *iis*
			- Enthält IIS-Webserver-Protokolle
	
 2. Unsere erste Aufgabe ist es, die IP-Adresse zu identifizieren, die versucht, Reconnaissance-Aktivitäten auf unserem Webserver durchzuführen. Es wäre naheliegend, den Webverkehr zu betrachten, der in das Netzwerk kommt
	 - Wir beginnen mit der Untersuchung des Log-Quellstroms `http` , der die HTTP-Traffic-Logs enthält
	 - [ ] **Suchanfrage:** ``index=botsv1 imreallynotbatman.com sourcetype="stream:http"
	
	-  Das Feld ``src_ip`` enthält die Quell-IP-Adresse, die es in den Logs findet.
	
3. Überprüfe die IP-Adresse, die gescannt wird.
	-  Also, was müssen wir tun, um den Scan versuch zu validieren? 
	-  Einfach, tiefer in die Weblogs graben.
	- [ ] **Suchanfrage:** ``index=botsv1 imreallynotbatman.com src=40.80.148.42 sourcetype=suricata`

		- *Abfrageerklärung* Diese Anfrage zeigt die Logs aus der Suricata-Logquelle, die von der Quell-IP 40.80.248.42 detektiert/erzeugt wurden.

----

### Exploitation Phase 
- In dieser Aufgabe werden wir den potenziellen Exploitversuch des Angreifers gegen unseren Webserver untersuchen und sehen, ob der Angreifer erfolgreich beim Ausnutzen war.

Um unsere Untersuchung zu beginnen, notieren wir uns die Informationen, die wir bisher haben:
1. Wir haben zwei IP-Adressen aus der Reconnaissance-Phase gefunden, die Anfragen an unseren Server gesendet haben.
	1. IP `40.80.148.42` wurde beobachtet, wie sie versuchte, den Server mit der IP 192.168.250.70 zu scannen.
	2. Der Angreifer nutzte den Web-Scanner Acunetix für die Scanversuche
2. 
	- [ ] **Suchanfrage: **`index=botsv1 imreallynotbatman.com sourcetype=stream* | stats count(src_ip) as Requests by src_ip | sort - Requests`

		- *Abfrageerklärung:* Diese Abfrage verwendet die stats-Funktion, um die Anzahl der IP-Adressen im Feld ``src_ip`` anzuzeigen.

3. Jetzt werden wir die Ergebnisse auf Anfragen eingrenzen, die an unseren Webserver mit der IP `192.168.250.70` gesendet wurden

	- [ ] **Suchanfrage: **`index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70"`
	
		- *Abfrageerklärung:* Diese Abfrage sucht nach allen eingehenden Datenverkehr zu der IP-Adresse 192.168.250.70.
		- [40.80.148.42]
		- [23.22.63.114]
		- [192.168.2.50]

4. Ein weiterer interessanter Bereich, http_method wird uns Informationen darüber geben, welche HTTP-Methoden während dieser HTTP-Kommunikationen beobachtet wurden.
	- [POST] 70.408%
	- [GET] 29.552%

	- [ ] **Suchanfrage:**`index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST`
	
- Der Begriff Joomla ist mit dem Webserver assoziiert, der in mehreren Feldern wie url, url_path, http_referrer usw. zu finden ist. 
- Dies bedeutet, dass unser Webserver das Joomla CMS (Content Management Service) im Backend verwendet.
- Eine kleine Suche im Internet nach der Admin-Login-Seite des Joomla CMS wird zeigen als -> `/joomla/administrator/index.php`
- Referenz: https://www.joomla.org/administrator/index.php
- Es ist wichtig, denn diese URL enthält die Login-Seite, um auf das Webportal zuzugreifen, daher werden wir den Verkehr, der auf dieses Admin-Panel eintritt, auf potenzielle Brute-Force-Angriffe untersuchen.

	- [ ] **Suchanfrage:** ``index=botsv1 imreallynotbatman.com sourcetype=stream:http dest_ip="192.168.250.70"  uri="/joomla/administrator/index.php"``
		- *Abfrageerklärung:* Wir werden `url="/joomla/administrator/index.php"` in die Suchanfrage einfügen, um den Verkehr, der auf diese URI eintritt, anzuzeigen.
		- *form_data* -> Selected Field
			- Das Feld enthält die Anfragen, die über das Formular auf der Admin-Panel-Seite gesendet wurden, die eine Login-Seite hat. 
			
	- [ ] **Suchanfrage:** ``index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST uri="/joomla/administrator/index.php" | table _time uri src_ip dest_ip form_data``

		- *Abfrageerklärung:* Wir fügen dies hinzu -> `| table _time uri src_ip dest_ip form_data` , um eine Tabelle mit wichtigen Feldern zu erstellen, wie unten gezeigt:

5. Extrahieren von Username- und Passwd-Feldern mit Regex
	- Bei der Durchsicht der Protokolle sehen wir, dass diese Felder nicht korrekt geparst werden. Lassen Sie uns Regex in der Suche verwenden, um nur diese beiden Felder und ihre Werte aus den Protokollen zu extrahieren und anzuzeigen.

		- [ ] **Suchanfrage:** `index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST uri="/joomla/administrator/index.php" form_data=*username*passwd* | table _time uri src_ip dest_ip form_data`

	- Lass uns Regex verwenden. `rex field=form_data "passwd=(?<creds>\w+)"` , um nur die Passwortwerte zu extrahieren. Dies wird das Feld form_data auswählen und alle Werte extrahieren, die mit dem Feld gefunden wurden. `creds` .
	
		- [ ] **Suchanfrage:**`index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST form_data=*username*passwd* | rex field=form_data "passwd=(?<creds>\w+)"  | table src_ip creds`
	
		- **Values** [Python-urllib/2.7] -> Python Skript
		- **Values** [Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko] -> Direkte Browser Anfrage
	
	Aber eine Anfrage kam von einem Mozilla-Browser. WARUM?
	- Lassen uns eine Tabelle erstellen, um Schlüsselfelder und Werte anzuzeigen, indem wir -> `| table _time src_ip uri http_user_agent creds` in der Suchanfrage anhängen, wie unten gezeigt.
	
		- [ ] **Suchanfrage:** `index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST form_data=*username*passwd* | rex field=form_data "passwd=(?<creds>\w+)" |table _time src_ip uri http_user_agent creds`
		- *Value*
			- 2016-08-10 21:48:05.858
			- 40.80.148.42
			- /joomla/administrator/index.php
			- Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
			- batman
		
Wichtige Informationen Zusammengefasst: 
1. Was war der URI, der mehrere Brute-Force-Versuche erhielt?
	1. /joomla/administrator/index.php
2. Gegen welches Benutzername wurde der Brute-Force-Versuch durchgeführt?
	1. admin
3. Was war das richtige Passwort für den Administratorzugriff auf das Content-Management-System, das imreallynotbatman.com läuft?
	1. batman
4. Wie viele eindeutige Passwörter wurden im Brute-Force-Angriff versucht?
	1. 412
5. Welche IP-Adresse versucht wahrscheinlich eine Brute-Force-Password-Angriff gegen imreallynotbatman.com?
	1. 40.80.148.42

-----
### Installation Phase
Sobald der Angreifer die Sicherheit eines Systems erfolgreich ausgenutzt hat, wird er versuchen, eine Hintertür oder eine Anwendung zu installieren, um sich dauerhaft Zugang zu verschaffen oder mehr Kontrolle über das System zu erlangen. Diese Aktivität fällt unter die Installationsphase.

In der vorherigen Ausnutzungsphase haben wir Hinweise darauf gefunden, dass der Webserver iamreallynotbatman.com durch eine Brute-Force-Attacke kompromittiert wurde, bei der der Angreifer ein Python-Skript einsetzte, um das richtige Passwort automatisch zu ermitteln. Der Angreifer nutzte die IP-Adresse für den Angriff und die IP-Adresse, um sich beim Server anzumelden. In dieser Phase werden alle Payloads/Schadprogramme untersucht, die von den IP-Adressen der Angreifer auf den Server hochgeladen und auf dem kompromittierten Server installiert wurden.

1. Um eine Untersuchung zu beginnen, würden wir zunächst alle eingehenden http-Verkehr zu unserem Server 192.168.250.70 einschränken, der den Begriff ".exe." enthält.

- [ ] **Suchanfrage**: `index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" *.exe`

	- *Ausgewähltes Feld:* part_filename{ }

1. Als nächstes müssen wir herausfinden, ob einer dieser Dateien von den IP-Adressen stammt, die bereits früher mit dem Angriff in Verbindung gebracht wurden.
- [ ] **Suchanfrage**: ``index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" "part_filename{}"="3791.exe"'`` 