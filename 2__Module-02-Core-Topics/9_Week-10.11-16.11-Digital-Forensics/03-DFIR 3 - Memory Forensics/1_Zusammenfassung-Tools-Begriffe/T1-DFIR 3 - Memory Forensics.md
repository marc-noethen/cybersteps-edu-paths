Welcome to Memory Forensics. Willkommen zur Speicherforensik.

Before our live session, this document will guide you through the foundational concepts of analyzing a computer's volatile memory. Vor unserer Live-Sitzung wird dieses Dokument Sie durch die grundlegenden Konzepte der Analyse des flüchtigen Speichers eines Computers führen.

Our goal is to understand what memory forensics is, why it's a game changer in modern cybersecurity investigations, and to get our primary tool, Volatility, set up and ready for analysis. Unser Ziel ist es zu verstehen, was Speicherforensik ist, warum sie ein Wendepunkt in modernen Cybersicherheitsuntersuchungen ist und unser Hauptwerkzeug, Volatility, einzurichten und für die Analyse bereitzumachen.

What is Memory Forensics? Was ist Speicherforensik?

Imagine a detective arriving at a crime scene. Stellen Sie sich einen Detektiv vor, der an einem Tatort ankommt.

The physical evidence, a dropped wallet, a footprint in the mud, is crucial. Die physischen Beweise, eine fallen gelassene Brieftasche, ein Fußabdruck im Schlamm, sind entscheidend.

This is like disk forensics, the analysis of data stored permanently on hard drives and SSDs. Dies ist wie Festplattenforensik, die Analyse von Daten, die dauerhaft auf Festplatten und SSDs gespeichert sind.

It tells us what was left behind. Sie sagt uns, was zurückgelassen wurde.

But what about the things that are gone moments later? Aber was ist mit den Dingen, die Momente später verschwunden sind?

The smell of gunpowder, the lingering warmth of a car engine, a whispered conversation. Der Geruch von Schießpulver, die anhaltende Wärme eines Automotors, eine geflüsterte Unterhaltung.

This is memory forensics. Dies ist Speicherforensik.

It's the art of capturing and analyzing a computer's volatile memory, RAM, which is the system's temporary workspace. Es ist die Kunst, den flüchtigen Speicher eines Computers, RAM, zu erfassen und zu analysieren, der der temporäre Arbeitsbereich des Systems ist.

RAM is where a computer holds everything it's actively working on: running programs, open files, network connections, and user actions. RAM ist der Ort, an dem ein Computer alles speichert, woran er aktiv arbeitet: laufende Programme, offene Dateien, Netzwerkverbindungen und Benutzeraktionen.

Unlike a hard drive, RAM is volatile, its contents are wiped clean the moment the computer loses power. Anders als eine Festplatte ist RAM flüchtig, sein Inhalt wird in dem Moment gelöscht, in dem der Computer die Stromversorgung verliert.

Memory forensics gives us a snapshot of this bustling workspace at a specific moment in time, revealing evidence that may never have been written to the disk and would otherwise be lost forever. Speicherforensik gibt uns einen Schnappschuss dieses geschäftigen Arbeitsbereichs zu einem bestimmten Zeitpunkt und enthüllt Beweise, die möglicherweise nie auf die Festplatte geschrieben wurden und sonst für immer verloren wären.

The Order of Volatility. Die Reihenfolge der Flüchtigkeit.

As we've discussed in previous lessons, the Order of Volatility is a fundamental principle in digital forensics. Wie wir in früheren Lektionen besprochen haben, ist die Reihenfolge der Flüchtigkeit ein grundlegendes Prinzip in der digitalen Forensik.

It reminds us to collect evidence from the most transient sources first. Sie erinnert uns daran, zuerst Beweise aus den flüchtigsten Quellen zu sammeln.

Because data in RAM is lost the moment a computer is shut down, it is one of the most volatile and time sensitive forms of evidence. Da Daten im RAM in dem Moment verloren gehen, in dem ein Computer heruntergefahren wird, ist dies eine der flüchtigsten und zeitkritischsten Formen von Beweisen.

This is why securing a memory dump from a live system is a critical first step in many incident response scenarios. Deshalb ist die Sicherung eines Speicherabbilds von einem laufenden System ein kritischer erster Schritt in vielen Incident-Response-Szenarien.

Why is Memory Forensics So Important? Warum ist Speicherforensik so wichtig?

Cyber attackers are intelligent and adaptive. Cyberangreifer sind intelligent und anpassungsfähig.

They know investigators traditionally focus on files stored on the hard drive. Sie wissen, dass Ermittler sich traditionell auf Dateien konzentrieren, die auf der Festplatte gespeichert sind.

To evade detection, they've developed techniques to live off the land, using legitimate system tools and running their malicious code exclusively in memory. Um einer Entdeckung zu entgehen, haben sie Techniken entwickelt, um mit Bordmitteln zu arbeiten, legitime Systemwerkzeuge zu verwenden und ihren bösartigen Code ausschließlich im Speicher auszuführen.

This is the essence of fileless malware. Dies ist die Essenz von dateiloser Malware.

If an investigator only performs disk forensics, they might conclude the system is clean, while the attacker's malware is still actively running in RAM. Wenn ein Ermittler nur Festplattenforensik durchführt, könnte er zu dem Schluss kommen, dass das System sauber ist, während die Malware des Angreifers noch aktiv im RAM läuft.

Memory forensics allows us to answer critical investigative questions by uncovering evidence that only exists in this volatile space. Speicherforensik ermöglicht es uns, kritische Ermittlungsfragen zu beantworten, indem wir Beweise aufdecken, die nur in diesem flüchtigen Bereich existieren.

What was the system doing? Was hat das System gemacht?

By examining the list of running processes, we can spot malicious programs, even those disguised as legitimate ones, for example, svchost dot exe. Durch die Untersuchung der Liste laufender Prozesse können wir bösartige Programme erkennen, selbst solche, die als legitime getarnt sind, zum Beispiel svchost punkt exe.

We can see which user account launched them and when. Wir können sehen, welches Benutzerkonto sie gestartet hat und wann.

Who was the system talking to? Mit wem hat das System kommuniziert?

A list of network connections can reveal communications with a malicious command and control server, data being exfiltrated to an attacker's machine, or attempts to spread to other computers on the network. Eine Liste von Netzwerkverbindungen kann Kommunikationen mit einem bösartigen Command-and-Control-Server, Daten, die zur Maschine eines Angreifers exfiltriert werden, oder Versuche, sich auf andere Computer im Netzwerk auszubreiten, offenbaren.

How did the attacker get in and what did they do? Wie ist der Angreifer hereingekommen und was hat er getan?

We can often find executed commands, showing us exactly what the attacker typed into a command prompt or PowerShell window. Wir können oft ausgeführte Befehle finden, die uns genau zeigen, was der Angreifer in eine Eingabeaufforderung oder ein PowerShell-Fenster eingegeben hat.

This provides a direct log of their activity. Dies liefert ein direktes Protokoll ihrer Aktivität.

What secrets did the attacker steal? Welche Geheimnisse hat der Angreifer gestohlen?

Attackers need to steal credentials to move around a network. Angreifer müssen Anmeldeinformationen stehlen, um sich in einem Netzwerk zu bewegen.

We can often extract passwords, usernames, and cryptographic keys directly from memory where they were being used by the operating system or applications. Wir können oft Passwörter, Benutzernamen und kryptografische Schlüssel direkt aus dem Speicher extrahieren, wo sie vom Betriebssystem oder von Anwendungen verwendet wurden.

How does the malware work? Wie funktioniert die Malware?

By analyzing malware artifacts, we can see how a malicious program has hooked into the operating system, injected code into legitimate processes, or is trying to hide its presence. Durch die Analyse von Malware-Artefakten können wir sehen, wie sich ein bösartiges Programm in das Betriebssystem eingehakt hat, Code in legitime Prozesse injiziert hat oder versucht, seine Präsenz zu verbergen.

Think about it. Denken Sie darüber nach.

If you were a malware author, what steps might you take to make your memory resident malware harder for a forensics investigator to find or analyze? Wenn Sie ein Malware-Autor wären, welche Schritte würden Sie unternehmen, um Ihre speicherresidente Malware für einen forensischen Ermittler schwerer zu finden oder zu analysieren?

This is known as an anti forensics technique. Dies ist als Anti-Forensik-Technik bekannt.

The Process: Acquisition and Analysis. Der Prozess: Erfassung und Analyse.

Memory forensics involves two distinct phases: acquiring the data and then analyzing it. Speicherforensik umfasst zwei unterschiedliche Phasen: die Erfassung der Daten und dann deren Analyse.

Number one, Acquisition: Getting the Memory Dump. Nummer eins, Erfassung: Das Speicherabbild erhalten.

First, we must create a bit for bit copy of the entire contents of RAM and save it to a single file. Zuerst müssen wir eine Bit-für-Bit-Kopie des gesamten Inhalts des RAM erstellen und in einer einzigen Datei speichern.

This file is called a memory dump, memory image, or capture. Diese Datei wird als Speicherabbild, Speicher-Image oder Erfassung bezeichnet.

This step is delicate. Dieser Schritt ist heikel.

The very act of running an acquisition tool on a live system uses memory and CPU, which slightly alters the state of the system we're trying to preserve, this is the observer effect. Die bloße Handlung, ein Erfassungswerkzeug auf einem laufenden System auszuführen, verwendet Speicher und CPU, was den Zustand des Systems, das wir zu bewahren versuchen, leicht verändert, dies ist der Beobachtereffekt.

Therefore, acquisition tools are designed to be as lightweight as possible. Daher sind Erfassungswerkzeuge so leichtgewichtig wie möglich konzipiert.

