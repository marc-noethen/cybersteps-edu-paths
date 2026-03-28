Welcome to Network Forensics. Willkommen bei der Netzwerk-Forensik.

In the world of digital investigations, some evidence is static, like files on a hard drive. In der Welt der digitalen Ermittlungen sind manche Beweise statisch, wie Dateien auf einer Festplatte.

Network forensics is different. Netzwerk-Forensik ist anders.

It deals with data in motion, a fleeting, chaotic, and incredibly rich source of information. Sie befasst sich mit Daten in Bewegung, einer flüchtigen, chaotischen und unglaublich reichhaltigen Informationsquelle.

This is the art and science of capturing, recording, and analyzing network events to discover the source of security attacks, intrusions, or other problem incidents. Dies ist die Kunst und Wissenschaft des Erfassens, Aufzeichnens und Analysierens von Netzwerkereignissen, um die Quelle von Sicherheitsangriffen, Eindringversuchen oder anderen Problemvorfällen zu entdecken.

Think of yourself as a detective listening in on conversations to solve a crime, except the conversations are digital, and the crime could be anything from data theft to a full scale system compromise. Stellen Sie sich vor, Sie sind ein Detektiv, der Gespräche abhört, um ein Verbrechen aufzuklären, nur dass die Gespräche digital sind und das Verbrechen alles sein kann, von Datendiebstahl bis zur vollständigen Systemkompromittierung.

What is Network Forensics? Was ist Netzwerk-Forensik?

Network Forensics involves monitoring and analyzing network traffic for the purposes of information gathering, legal evidence, or intrusion detection. Netzwerk-Forensik umfasst die Überwachung und Analyse des Netzwerkverkehrs zum Zweck der Informationssammlung, der Beweiserhebung oder der Eindringlingserkennung.

When an incident occurs, the network is often the scene of the crime. Wenn ein Vorfall eintritt, ist das Netzwerk oft der Tatort.

By analyzing the traffic, we can reconstruct the sequence of events to understand exactly what an attacker did and what data they may have accessed or exfiltrated. Durch die Analyse des Datenverkehrs können wir die Abfolge der Ereignisse rekonstruieren, um genau zu verstehen, was ein Angreifer getan hat und auf welche Daten er möglicherweise zugegriffen oder die er herausgeschleust hat.

Key objectives include identifying the attacker, pinpointing the source IP address and correlating it with other information to uncover the adversary. Zu den Hauptzielen gehören die Identifizierung des Angreifers, das Aufspüren der Quell-IP-Adresse und deren Korrelation mit anderen Informationen, um den Gegner aufzudecken.

Determining the scope of the incident, answering questions like which systems were compromised, what data was accessed, was any data stolen or exfiltrated? Die Bestimmung des Umfangs des Vorfalls, die Beantwortung von Fragen wie: Welche Systeme wurden kompromittiert, auf welche Daten wurde zugegriffen, wurden Daten gestohlen oder herausgeschleust?

Understanding the attack methodology, reconstructing the steps the attacker took, from initial reconnaissance to final objectives. Das Verstehen der Angriffsmethodik, die Rekonstruktion der Schritte, die der Angreifer unternommen hat, von der ersten Aufklärung bis zu den endgültigen Zielen.

This is crucial for patching vulnerabilities and preventing future attacks. Dies ist entscheidend für das Schließen von Sicherheitslücken und die Verhinderung zukünftiger Angriffe.

The Challenges of Network Forensics. Die Herausforderungen der Netzwerk-Forensik.

Analyzing network traffic is not always straightforward. Die Analyse des Netzwerkverkehrs ist nicht immer einfach.

Investigators face several significant hurdles. Ermittler stehen vor mehreren erheblichen Hürden.

Volume, a busy network can generate terabytes of data per day. Volumen: Ein ausgelastetes Netzwerk kann täglich Terabytes an Daten erzeugen.

Finding a single malicious packet in this ocean of data is a true needle in a haystack problem. Ein einzelnes bösartiges Paket in diesem Datenmeer zu finden, ist ein echtes Problem wie die Suche nach der Nadel im Heuhaufen.

This is why filtering and automated analysis are so critical. Deshalb sind Filterung und automatisierte Analyse so entscheidend.

Volatility, network data is ephemeral. Flüchtigkeit: Netzwerkdaten sind vergänglich.

If you don't capture it as it passes, it's gone forever. Wenn Sie sie nicht erfassen, während sie vorbeifließen, sind sie für immer verloren.

This makes proactive monitoring and capture essential, as you can't go back in time to record traffic from a past incident. Dies macht proaktive Überwachung und Erfassung unerlässlich, da Sie nicht in der Zeit zurückreisen können, um den Verkehr eines vergangenen Vorfalls aufzuzeichnen.

Encryption, much of today's network traffic, for example HTTPS, SSH, VPNs, is encrypted. Verschlüsselung: Ein Großteil des heutigen Netzwerkverkehrs, zum Beispiel HTTPS, SSH, VPNs, ist verschlüsselt.

While you can see the metadata, who is talking to whom, the actual content of the conversation is unreadable without the decryption keys. Während Sie die Metadaten sehen können, wer mit wem spricht, ist der tatsächliche Inhalt des Gesprächs ohne die Entschlüsselungsschlüssel nicht lesbar.

This is a major obstacle, though sometimes analysis of the metadata alone can provide valuable clues. Dies ist ein großes Hindernis, obwohl manchmal die Analyse der Metadaten allein wertvolle Hinweise liefern kann.

Obfuscation, attackers often try to hide their activities by using non standard ports, tunneling protocols, or encoding data in ways that are not immediately obvious. Verschleierung: Angreifer versuchen oft, ihre Aktivitäten zu verbergen, indem sie nicht standardisierte Ports, Tunnelprotokolle oder Datenkodierungen verwenden, die nicht sofort offensichtlich sind.

Checkout the website which includes a collection of C2 frameworks that leverage legitimate services to evade detection. Schauen Sie sich die Webseite an, die eine Sammlung von Command and Control Frameworks enthält, die legitime Dienste nutzen, um der Erkennung zu entgehen.

Attackers are creative, we need to be as well. Angreifer sind kreativ, wir müssen es auch sein.

Sources of Network Evidence. Quellen für Netzwerkbeweise.

Network evidence comes in many forms, each with its own strengths and weaknesses. Netzwerkbeweise gibt es in vielen Formen, jede mit ihren eigenen Stärken und Schwächen.

An investigator rarely relies on a single source, instead, they correlate data from multiple sources to build a complete picture. Ein Ermittler verlässt sich selten auf eine einzige Quelle, stattdessen korreliert er Daten aus mehreren Quellen, um ein vollständiges Bild zu erstellen.

Full Packet Capture, or PCAP, this is the gold standard of network evidence. Vollständige Paketerfassung oder PCAP: Dies ist der Goldstandard der Netzwerkbeweise.

A full packet capture saves every single bit of data that travels across a network segment. Eine vollständige Paketerfassung speichert jedes einzelne Bit an Daten, das über ein Netzwerksegment fließt.

Each packet contains headers, like source and destination addresses and ports, and a payload, the actual data being sent. Jedes Paket enthält Header, wie Quell- und Zieladressen und Ports, sowie eine Nutzlast, die tatsächlich gesendeten Daten.

With a PCAP, you can reconstruct entire conversations, extract files, and see exactly what was exchanged. Mit einem PCAP können Sie ganze Gespräche rekonstruieren, Dateien extrahieren und genau sehen, was ausgetauscht wurde.

Strength, the most detailed evidence possible. Stärke: Der detaillierteste Beweis, der möglich ist.

Weakness, requires immense storage and processing power. Schwäche: Erfordert enormen Speicher- und Rechenleistungsbedarf.

NetFlow and IPFIX, NetFlow, a Cisco proprietary protocol, and IPFIX, its standardized successor, are technologies that collect metadata about network traffic. NetFlow und IPFIX: NetFlow, ein proprietäres Cisco-Protokoll, und IPFIX, sein standardisierter Nachfolger, sind Technologien, die Metadaten über Netzwerkverkehr sammeln.

Instead of capturing every packet, they record conversations, summarizing who talked to whom, when, for how long, and how much data was sent. Anstatt jedes Paket zu erfassen, zeichnen sie Gespräche auf und fassen zusammen, wer mit wem gesprochen hat, wann, wie lange und wie viele Daten gesendet wurden.

Think of it as a phone bill, you see the numbers called, the call duration, and the time, but you don't have a recording of the conversation itself. Stellen Sie es sich wie eine Telefonrechnung vor: Sie sehen die angerufenen Nummern, die Gesprächsdauer und die Zeit, aber Sie haben keine Aufzeichnung des Gesprächs selbst.

A typical NetFlow record contains the five tuple: Source IP, Destination IP, Source Port, Destination Port, and Protocol. Ein typischer NetFlow-Datensatz enthält das Fünf-Tupel: Quell-IP, Ziel-IP, Quellport, Zielport und Protokoll.

Strength, much less resource intensive, provides a high level overview of all network activity. Stärke: Wesentlich weniger ressourcenintensiv, bietet einen Überblick über alle Netzwerkaktivitäten auf hoher Ebene.

Weakness, lacks the granular detail of the payload, you know a conversation happened, but not what was said. Schwäche: Fehlt das detaillierte Detail der Nutzlast, Sie wissen, dass ein Gespräch stattgefunden hat, aber nicht, was gesagt wurde.

Logs from Network Devices. Protokolle von Netzwerkgeräten.

