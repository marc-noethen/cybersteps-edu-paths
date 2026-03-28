Firewall Logs provide records of what traffic was allowed or denied. Firewall-Protokolle liefern Aufzeichnungen darüber, welcher Datenverkehr zugelassen oder verweigert wurde.

Excellent for identifying unauthorized connection attempts. Hervorragend geeignet zur Identifizierung unbefugter Verbindungsversuche.

A log might look like DENY TCP one dot two dot three dot four colon five six seven eight to one nine two dot one six eight dot one dot one zero zero colon two two. Ein Protokolleintrag könnte so aussehen: DENY TCP eins punkt zwei punkt drei punkt vier Doppelpunkt fünf sechs sieben acht zu eins neun zwei punkt eins sechs acht punkt eins punkt eins null null Doppelpunkt zwei zwei.

Intrusion Detection and Prevention System, IDS and IPS Logs, these systems contain alerts for specific, recognized attack patterns, such as ET SCAN Nmap Scripting Engine User Agent Detected. Intrusion Detection und Prevention System, IDS und IPS Protokolle: Diese Systeme enthalten Alarme für spezifische, erkannte Angriffsmuster, wie zum Beispiel ET SCAN Nmap Scripting Engine Benutzer-Agent erkannt.

Proxy Logs, a detailed history of every website visited by users, including the full URL, the user, and the result. Proxy-Protokolle: Eine detaillierte Historie jeder von Benutzern besuchten Webseite, einschließlich der vollständigen URL, des Benutzers und des Ergebnisses.

DNS Logs, every domain name lookup. DNS-Protokolle: Jede Domänennamen-Abfrage.

These can reveal connections to malicious command and control, or C2, servers. Diese können Verbindungen zu bösartigen Command-and-Control- oder C2-Servern aufdecken.

Think about it. Denken Sie darüber nach.

If you only have NetFlow data for an incident, you could likely identify a large data transfer to an unusual external IP address, potential data exfiltration, or a host connecting to thousands of other hosts on a specific port, a network scan. Wenn Sie nur NetFlow-Daten für einen Vorfall haben, könnten Sie wahrscheinlich eine große Datenübertragung zu einer ungewöhnlichen externen IP-Adresse identifizieren, potenzielle Datenexfiltration, oder einen Host, der sich mit Tausenden von anderen Hosts auf einem bestimmten Port verbindet, ein Netzwerk-Scan.

However, you would miss the specifics, such as what file was exfiltrated or whether a login attempt used the correct password. Allerdings würden Sie die Details verpassen, wie zum Beispiel welche Datei herausgeschleust wurde oder ob ein Anmeldeversuch das richtige Passwort verwendet hat.

Core Network Forensics Tools. Grundlegende Netzwerk-Forensik-Werkzeuge.

While many tools exist, two are fundamental to nearly every network forensics investigation. Während viele Werkzeuge existieren, sind zwei grundlegend für nahezu jede Netzwerk-Forensik-Untersuchung.

Both are pre installed on Kali Linux. Beide sind auf Kali Linux vorinstalliert.

Wireshark, the world's foremost network protocol analyzer. Wireshark: Der weltweit führende Netzwerkprotokoll-Analysator.

It allows for deep, interactive inspection of PCAP files. Er ermöglicht eine tiefgehende, interaktive Untersuchung von PCAP-Dateien.

Key Features, its power lies in its vast library of protocol dissectors that decode thousands of protocols, and its robust display filtering engine. Hauptmerkmale: Seine Stärke liegt in seiner umfangreichen Bibliothek von Protokoll-Dissektoren, die Tausende von Protokollen dekodieren, und seiner robusten Anzeige-Filterungs-Engine.

A crucial feature is Follow TCP Stream, which reconstructs a conversation and displays the application layer data in a human readable format, stripping away the packet headers. Eine entscheidende Funktion ist Follow TCP Stream, die ein Gespräch rekonstruiert und die Anwendungsschichtdaten in einem menschenlesbaren Format anzeigt, wobei die Paket-Header entfernt werden.

The Interface, Wireshark has three main panes: the Packet List, a summary of each packet, Packet Details, a collapsible, deep dive into the selected packet's headers, and Packet Bytes, the raw data of the packet in hexadecimal. Die Benutzeroberfläche: Wireshark hat drei Hauptbereiche: die Paketliste, eine Zusammenfassung jedes Pakets, Paketdetails, ein einklappbarer, tiefer Einblick in die Header des ausgewählten Pakets, und Paket-Bytes, die Rohdaten des Pakets in hexadezimaler Form.

Tshark, the command line equivalent of Wireshark. Tshark: Das Kommandozeilen-Äquivalent von Wireshark.

While it lacks a graphical interface, it is incredibly powerful for automating analysis and extracting specific fields from large captures. Obwohl es keine grafische Benutzeroberfläche hat, ist es unglaublich leistungsfähig für die Automatisierung von Analysen und das Extrahieren spezifischer Felder aus großen Erfassungen.

You can use it in scripts to process huge amounts of data in a fraction of the time it would take in the graphical user interface. Sie können es in Skripten verwenden, um riesige Datenmengen in einem Bruchteil der Zeit zu verarbeiten, die es in der grafischen Benutzeroberfläche dauern würde.

For example, to pull all requested hostnames from HTTP traffic in a PCAP, you could use a command like tshark minus r file dot pcap minus Y quote http dot request quote minus T fields minus e http dot host. Um zum Beispiel alle angeforderten Hostnamen aus HTTP-Verkehr in einem PCAP zu extrahieren, könnten Sie einen Befehl wie tshark minus r file punkt pcap minus Y Anführungszeichen http punkt request Anführungszeichen minus T fields minus e http punkt host verwenden.

The Network Forensics Process. Der Netzwerk-Forensik-Prozess.

A typical investigation follows a structured process. Eine typische Untersuchung folgt einem strukturierten Prozess.

Acquisition, capturing the network traffic, typically using a network TAP or a switch's SPAN port. Erfassung: Das Erfassen des Netzwerkverkehrs, typischerweise unter Verwendung eines Netzwerk-TAP oder eines SPAN-Ports eines Switches.

Analysis, using tools like Wireshark and Tshark to examine the captured data, looking for anomalies, indicators of compromise, or IOCs, and evidence of the attacker's actions. Analyse: Verwendung von Werkzeugen wie Wireshark und Tshark zur Untersuchung der erfassten Daten, Suche nach Anomalien, Indikatoren für Kompromittierung oder IOCs und Beweisen für die Handlungen des Angreifers.

Correlation, the final and most crucial step. Korrelation: Der letzte und entscheidendste Schritt.

Network evidence is rarely sufficient on its own. Netzwerkbeweise sind selten für sich allein ausreichend.

An analyst must correlate events seen on the network with evidence from other sources, such as host based logs, for example Windows Event Logs, memory analysis, and disk forensics, to build a comprehensive timeline. Ein Analyst muss Ereignisse, die im Netzwerk gesehen werden, mit Beweisen aus anderen Quellen korrelieren, wie zum Beispiel hostbasierten Protokollen, zum Beispiel Windows-Ereignisprotokolle, Speicheranalyse und Festplatten-Forensik, um eine umfassende Zeitlinie zu erstellen.

A Model for Investigation: The Diamond Model. Ein Modell für die Untersuchung: Das Diamant-Modell.

To help structure an investigation, analysts often use conceptual frameworks. Um eine Untersuchung zu strukturieren, verwenden Analysten oft konzeptionelle Rahmenwerke.

The Diamond Model of Intrusion Analysis is a popular one. Das Diamant-Modell der Intrusions-Analyse ist ein beliebtes.

It states that every intrusion event consists of four interconnected vertices. Es besagt, dass jedes Intrusions-Ereignis aus vier miteinander verbundenen Eckpunkten besteht.

Adversary, the attacker who is responsible for the event. Gegner: Der Angreifer, der für das Ereignis verantwortlich ist.

Capability, the tools and or techniques used by the adversary. Fähigkeit: Die Werkzeuge und oder Techniken, die vom Gegner verwendet werden.

Infrastructure, the physical or logical communication structures the adversary uses, for example their C2 server IP address, a malicious domain name. Infrastruktur: Die physischen oder logischen Kommunikationsstrukturen, die der Gegner verwendet, zum Beispiel ihre C2-Server-IP-Adresse, ein bösartiger Domänenname.

Victim, the target of the attack. Opfer: Das Ziel des Angriffs.

By trying to identify and link these four elements, an analyst can organize their findings and better understand the overall incident. Indem man versucht, diese vier Elemente zu identifizieren und zu verknüpfen, kann ein Analyst seine Erkenntnisse organisieren und den Gesamtvorfall besser verstehen.

Try it yourself. Probieren Sie es selbst aus.

Download a real malware pcap from the malware traffic analysis website. Laden Sie einen echten Malware-PCAP von der Malware-Traffic-Analyse-Webseite herunter.

Open the file in Wireshark. Öffnen Sie die Datei in Wireshark.

Perform an initial triage, what endpoints are involved in the PCAP, what protocols, any domains you can find, any files transferred? Führen Sie eine erste Sichtung durch: Welche Endpunkte sind im PCAP beteiligt, welche Protokolle, welche Domänen können Sie finden, wurden Dateien übertragen?

The slides for the live session can be viewed at the provided link. Die Folien für die Live-Sitzung können unter dem bereitgestellten Link angesehen werden.

Try not to peek before class, spoilers inside. Versuchen Sie nicht, vor dem Unterricht hineinzuschauen, Spoiler enthalten.