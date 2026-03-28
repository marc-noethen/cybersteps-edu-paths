Welcome to the pre-class material for our session on Windows Lateral Movement.
Willkommen zum Vorbereitungsmaterial für unsere Session über Windows Lateral Movement.

In our last sessions, we focused on gaining initial access to a machine and elevating our privileges on that single host.
In unseren letzten Sessions haben wir uns darauf konzentriert, den initialen Zugriff auf eine Maschine zu erlangen und unsere Privilegien auf diesem einzelnen Host zu erhöhen.

Now, we'll explore the next logical step in an attack: moving from that initial foothold to other machines across the network.
Nun erkunden wir den nächsten logischen Schritt in einem Angriff: Das Bewegen vom initialen Fußhalt zu anderen Maschinen im gesamten Netzwerk.

This process is known as lateral movement.
Dieser Prozess ist als Lateral Movement bekannt.

The goal of this pre-class reading is to introduce the core concepts, terminology, and tools used to pivot through a Windows environment.
Das Ziel dieser Vorbereitungslektüre ist es, die Kernkonzepte, Terminologie und Tools vorzustellen, die verwendet werden, um durch eine Windows-Umgebung zu pivotieren.

Understanding this material is crucial for the hands-on demonstrations in our upcoming live session.
Das Verständnis dieses Materials ist entscheidend für die praktischen Demonstrationen in unserer bevorstehenden Live-Session.

The Beachhead and The Goal.
Der Beachhead und das Ziel.

In a real-world attack, gaining access to a single user's workstation is just the beginning.
In einem realen Angriff ist der Zugriff auf die Workstation eines einzelnen Benutzers nur der Anfang.

This first compromised machine is the beachhead.
Diese erste kompromittierte Maschine ist der Beachhead.

It's a starting point, but rarely the final target.
Es ist ein Ausgangspunkt, aber selten das endgültige Ziel.

An attacker's objective is almost never to just control one random computer.
Das Ziel eines Angreifers ist fast nie, nur einen zufälligen Computer zu kontrollieren.

The ultimate goal is usually to find and exfiltrate sensitive data, deploy ransomware, or gain persistent control over the entire network.
Das ultimative Ziel ist normalerweise, sensible Daten zu finden und zu exfiltrieren, Ransomware bereitzustellen oder persistente Kontrolle über das gesamte Netzwerk zu erlangen.

To do this, an attacker must move from the beachhead to more valuable targets, such as file servers, database servers, or the ultimate prize: a Domain Controller.
Um das zu tun, muss ein Angreifer vom Beachhead zu wertvolleren Zielen wechseln, wie Dateiservern, Datenbankservern oder dem ultimativen Preis: einem Domain Controller.

Lateral movement is the set of techniques attackers use to pivot from machine to machine.
Lateral Movement ist die Menge an Techniken, die Angreifer verwenden, um von Maschine zu Maschine zu pivotieren.

It leverages the credentials and access gained from the initial host to authenticate to and execute code on other systems within the same network.
Es nutzt die Anmeldeinformationen und den Zugriff aus, die vom initialen Host gewonnen wurden, um sich an anderen Systemen im selben Netzwerk zu authentifizieren und Code auszuführen.

This phase is tracked in the MITRE ATT&CK framework as Tactic TA0008.
Diese Phase wird im MITRE ATT&CK-Framework als Tactic TA0008 verfolgt.

Abusing Legitimate Authentication.
Missbrauch legitimer Authentifizierung.

At its core, lateral movement in a Windows environment is about the abuse of legitimate authentication mechanisms.
Im Kern geht es beim Lateral Movement in einer Windows-Umgebung um den Missbrauch legitimer Authentifizierungsmechanismen.

Attackers don't need to invent a new way to log into a remote computer; they can simply use the very protocols and tools that system administrators rely on every day to keep the network running.
Angreifer müssen keinen neuen Weg erfinden, um sich an einem remote Computer anzumelden; sie können einfach die Protokolle und Tools verwenden, auf die Systemadministratoren täglich angewiesen sind, um das Netzwerk am Laufen zu halten.

You've already learned how to acquire user credentials, passwords and hashes.
Sie haben bereits gelernt, wie man Benutzeranmeldeinformationen erlangt, Passwörter und Hashes.

Now, let's see how to use them.
Nun schauen wir, wie man sie verwendet.

Pass-the-Hash.
Pass-the-Hash.

This is one of the most fundamental lateral movement techniques in Windows networks.
Das ist eine der fundamentalsten Lateral-Movement-Techniken in Windows-Netzwerken.

To understand it, you first need to remember that Windows doesn't store your plaintext password.
Um es zu verstehen, müssen Sie sich zuerst erinnern, dass Windows Ihr Klartext-Passwort nicht speichert.

Instead, it stores and uses password hashes, primarily NTLM hashes.
Stattdessen speichert und verwendet es Passwort-Hashes, hauptsächlich NTLM-Hashes.

An NTLM hash is a one-way cryptographic function of your password.
Ein NTLM-Hash ist eine einweg-kryptografische Funktion Ihres Passworts.

You can't reverse the hash to get the password back.
Sie können den Hash nicht umkehren, um das Passwort zurückzubekommen.

When you try to access a resource on another Windows machine that isn't using Kerberos, your computer proves it knows your password using a challenge-response protocol.
Wenn Sie versuchen, auf eine Ressource auf einer anderen Windows-Maschine zuzugreifen, die Kerberos nicht verwendet, beweist Ihr Computer, dass er Ihr Passwort kennt, mit einem Challenge-Response-Protokoll.

The key detail is that your actual password never crosses the network.
Das entscheidende Detail ist, dass Ihr tatsächliches Passwort nie das Netzwerk überquert.

Only the hash is used in this process.
Nur der Hash wird in diesem Prozess verwendet.

The remote server effectively says, If you have the correct hash, I'll let you in.
Der remote Server sagt effektiv: Wenn Sie den richtigen Hash haben, lasse ich Sie herein.

A Pass-the-Hash attack exploits this.
Ein Pass-the-Hash-Angriff nutzt das aus.

An attacker who has compromised a machine can use a tool like Mimikatz to dump the NTLM hashes of all users who have logged into that box from the computer's memory.
Ein Angreifer, der eine Maschine kompromittiert hat, kann ein Tool wie Mimikatz verwenden, um die NTLM-Hashes aller Benutzer, die sich an dieser Box angemeldet haben, aus dem Speicher des Computers zu dumpen.

They can then take a user's NTLM hash and pass it directly to the remote server to authenticate.
Sie können dann den NTLM-Hash eines Benutzers nehmen und ihn direkt an den remote Server weitergeben, um sich zu authentifizieren.

No password cracking is required.
Kein Passwort-Cracking ist erforderlich.

Analogy: Think of the NTLM hash as a master keycard.
Analogie: Stellen Sie sich den NTLM-Hash als eine Master-Keycard vor.

The password is the complex PIN you used to generate the keycard.
Das Passwort ist der komplexe PIN, den Sie verwendet haben, um die Keycard zu generieren.

For most doors, you don't need to enter the PIN again; you just swipe the card.
Für die meisten Türen müssen Sie den PIN nicht erneut eingeben; Sie wischen einfach die Karte.

If an attacker steals your keycard, they can open all the same doors you can, without ever knowing your original PIN.
Wenn ein Angreifer Ihre Keycard stiehlt, kann er alle dieselben Türen öffnen, die Sie können, ohne je Ihren originalen PIN zu kennen.

Pass-the-Ticket.
Pass-the-Ticket.

This technique is the Kerberos equivalent of Pass-the-Hash.
Diese Technik ist das Kerberos-Äquivalent zu Pass-the-Hash.

Kerberos is the default, and more secure, authentication protocol used in modern Active Directory environments.
Kerberos ist das Standard- und sicherere Authentifizierungsprotokoll, das in modernen Active Directory-Umgebungen verwendet wird.

When you log into a domain, you authenticate once to a central server called the Key Distribution Center.
Wenn Sie sich in einer Domäne anmelden, authentifizieren Sie sich einmal an einem zentralen Server, der Key Distribution Center genannt wird.

The Key Distribution Center gives you a special credential called a Ticket-Granting Ticket.
Das Key Distribution Center gibt Ihnen eine spezielle Anmeldeinformation, die Ticket-Granting Ticket genannt wird.

This Ticket-Granting Ticket is stored in your computer's memory and acts as proof of your identity for your entire login session.
Dieses Ticket-Granting Ticket wird im Speicher Ihres Computers gespeichert und dient als Beweis Ihrer Identität für Ihre gesamte Anmeldesession.

When you want to access a specific service, like a file share, your computer presents the Ticket-Granting Ticket to the Key Distribution Center and requests a service ticket for that specific share.
Wenn Sie auf einen spezifischen Dienst zugreifen möchten, wie eine Dateifreigabe, präsentiert Ihr Computer das Ticket-Granting Ticket dem Key Distribution Center und fordert ein Service-Ticket für diese spezifische Freigabe an.

It then presents the service ticket to the file server to gain access.
Es präsentiert dann das Service-Ticket dem Dateiserver, um Zugriff zu erhalten.

In a Pass-the-Ticket attack, an attacker on a compromised machine dumps the contents of memory to find and steal these Kerberos tickets, both Ticket-Granting Tickets and service tickets.
In einem Pass-the-Ticket-Angriff dump ein Angreifer auf einer kompromittierten Maschine den Inhalt des Speichers, um diese Kerberos-Tickets zu finden und zu stehlen, sowohl Ticket-Granting Tickets als auch Service-Tickets.

They can then inject these tickets into their own session and use them to access network resources just as the legitimate user would.
Sie können diese Tickets dann in ihre eigene Session injizieren und sie verwenden, um auf Netzwerkressourcen zuzugreifen, genau wie der legitime Benutzer es tun würde.

Like Pass-the-Hash, this bypasses the need for a plaintext password.
Wie bei Pass-the-Hash umgeht das die Notwendigkeit eines Klartext-Passworts.

Analogy: Think of a large music festival.
Analogie: Stellen Sie sich ein großes Musikfestival vor.

The Key Distribution Center is the main gate where you show your ID, password, once.
Das Key Distribution Center ist das Haupttor, wo Sie Ihren Ausweis, Passwort, einmal vorzeigen.

They give you a wristband, the Ticket-Granting Ticket.
Sie geben Ihnen ein Armband, das Ticket-Granting Ticket.

For every stage or food stall you want to enter, a service, you flash your wristband to a security guard who gives you a small paper token, the service ticket, for that specific area.
Für jede Bühne oder Imbissstand, den Sie betreten möchten, einen Dienst, zeigen Sie Ihr Armband einem Sicherheitsmann, der Ihnen ein kleines Papier-Token, das Service-Ticket, für diesen spezifischen Bereich gibt.

An attacker performing Pass-the-Ticket is like someone who steals your wristband.
Ein Angreifer, der Pass-the-Ticket ausführt, ist wie jemand, der Ihr Armband stiehlt.

They can now go get tokens for any stage you were allowed to visit.
Sie können nun Tokens für jede Bühne holen, die Sie besuchen durften.

Think about it.
Denken Sie darüber nach.

Why is it so common for highly privileged credentials, like a Domain Admin's hash or ticket, to be found on a regular, low-security employee workstation?
Warum ist es so üblich, dass hochprivilegierte Anmeldeinformationen, wie der Hash oder das Ticket eines Domain Admins, auf einer regulären, niedrig gesicherten Mitarbeiter-Workstation gefunden werden?

What kind of everyday IT tasks might lead to this situation?
Welche Art von alltäglichen IT-Aufgaben könnte zu dieser Situation führen?

Common Tools and Techniques for Execution.
Gängige Tools und Techniken für die Ausführung.

Once an attacker has the necessary credentials, a hash or a ticket, they need a way to use them to execute commands on a remote system.
Sobald ein Angreifer die notwendigen Anmeldeinformationen hat, einen Hash oder ein Ticket, braucht er einen Weg, sie zu verwenden, um Befehle auf einem remote System auszuführen.
