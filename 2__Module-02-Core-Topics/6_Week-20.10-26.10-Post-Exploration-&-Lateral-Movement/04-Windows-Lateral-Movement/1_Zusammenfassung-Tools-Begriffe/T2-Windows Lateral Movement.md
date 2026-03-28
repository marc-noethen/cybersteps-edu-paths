
Part Two:

PsExec.
PsExec.

PsExec is a legitimate command-line tool from the Windows Sysinternals suite that allows an administrator to execute processes on other systems.
PsExec ist ein legitimes Kommandozeilen-Tool aus der Windows Sysinternals-Suite, das einem Administrator ermöglicht, Prozesse auf anderen Systemen auszuführen.

It's designed for remote administration, but its functionality makes it a favorite among attackers.
Es ist für die remote Administration konzipiert, aber seine Funktionalität macht es zu einem Favoriten unter Angreifern.

It works by combining two core Windows networking protocols.
Es funktioniert, indem es zwei Kern-Netzwerkprotokolle von Windows kombiniert.

SMB, Server Message Block: The protocol used for file sharing.
SMB, Server Message Block: Das Protokoll, das für Dateifreigaben verwendet wird.

PsExec uses it to connect to a hidden administrative share on the target machine called ADMIN$, which points to C:\Windows.
PsExec verwendet es, um sich mit einer versteckten administrativen Freigabe auf der Zielmaschine zu verbinden, die ADMIN$ genannt wird und auf C:\Windows zeigt.

RPC, Remote Procedure Call: A protocol that allows a program on one computer to request a service from a program on another computer.
RPC, Remote Procedure Call: Ein Protokoll, das einem Programm auf einem Computer ermöglicht, einen Dienst von einem Programm auf einem anderen Computer anzufordern.

Here’s how it typically works.
So funktioniert es typischerweise.

Authenticates to the target machine's ADMIN$ share using SMB, Port 445.
Authentifiziert sich an der ADMIN$-Freigabe der Zielmaschine mit SMB, Port 445.

Uploads a service executable, PSEXESVC.exe, to the target's C:\Windows directory via SMB.
Lädt eine Service-Executable, PSEXESVC.exe, in das C:\Windows-Verzeichnis der Zielmaschine via SMB hoch.

Uses RPC to remotely command the target's Service Control Manager to create and start the PSEXESVC service.
Verwendet RPC, um remote den Service Control Manager der Zielmaschine anzuweisen, den PSEXESVC-Service zu erstellen und zu starten.

Establishes a named pipe connection to the service for input/output, effectively giving the attacker a command shell.
Stellt eine Named-Pipe-Verbindung zum Service für Input/Output her, was dem Angreifer effektiv eine Command-Shell gibt.

When the session ends, it uses RPC again to stop and delete the service.
Wenn die Session endet, verwendet es RPC erneut, um den Service zu stoppen und zu löschen.

Because PsExec is a legitimate, signed Microsoft tool, its presence on a network doesn't automatically trigger alerts.
Weil PsExec ein legitimes, signiertes Microsoft-Tool ist, löst seine Präsenz im Netzwerk nicht automatisch Alarme aus.

Windows Management Instrumentation.
Windows Management Instrumentation.

Windows Management Instrumentation is the infrastructure for management data and operations on Windows-based operating systems.
Windows Management Instrumentation ist die Infrastruktur für Management-Daten und -Operationen auf Windows-basierten Betriebssystemen.

System administrators use it for everything: querying hardware, installing software, and running scripts across hundreds of machines at once.
Systemadministratoren verwenden es für alles: Abfragen von Hardware, Installieren von Software und Ausführen von Skripten auf Hunderten von Maschinen gleichzeitig.

It's an incredibly powerful, built-in tool.
Es ist ein unglaublich mächtiges, integriertes Tool.

Attackers can abuse Windows Management Instrumentation to execute commands on remote machines, often with a single command line.
Angreifer können Windows Management Instrumentation missbrauchen, um Befehle auf remote Maschinen auszuführen, oft mit einer einzigen Kommandozeile.

wmic /node:TARGET_IP /user:USERNAME /password:PASSWORD process call create cmd.exe /c some_command
wmic /node:TARGET_IP /user:USERNAME /password:PASSWORD process call create cmd.exe /c some_command

The key advantage of using Windows Management Instrumentation for an attacker is that it's often considered fileless.
Der entscheidende Vorteil der Verwendung von Windows Management Instrumentation für einen Angreifer ist, dass es oft als fileless betrachtet wird.

Unlike PsExec, it doesn't need to drop a binary like PSEXESVC.exe onto the target system's disk.
Im Gegensatz zu PsExec muss es kein Binary wie PSEXESVC.exe auf die Festplatte des Zielsystems ablegen.

It uses existing, legitimate Windows components, wmic.exe on the attacker's side, and the Windows Management Instrumentation service on the victim's side, to run the command, making it much stealthier and less likely to be detected by simple antivirus solutions.
Es verwendet existierende, legitime Windows-Komponenten, wmic.exe auf der Seite des Angreifers und den Windows Management Instrumentation-Service auf der Seite des Opfers, um den Befehl auszuführen, was es viel stealthier macht und weniger wahrscheinlich von einfachen Antivirus-Lösungen erkannt wird.

Remote Desktop Protocol.
Remote Desktop Protocol.

The simplest method of all.
Die einfachste Methode von allen.

If an attacker has valid credentials for a user who is allowed to log in remotely, they can simply open an RDP client, enter the target machine's IP address and the credentials, and get a full interactive desktop session.
Wenn ein Angreifer gültige Anmeldeinformationen für einen Benutzer hat, der remote Anmeldung erlaubt ist, kann er einfach einen RDP-Client öffnen, die IP-Adresse der Zielmaschine und die Anmeldeinformationen eingeben und eine vollständige interaktive Desktop-Session erhalten.

While effective, it is also noisy.
Obwohl effektiv, ist es auch noisy.

A successful RDP login, Event ID 4624, creates a very clear log in the Windows Security Event Log, and if a user is already logged in, they may see their session get kicked.
Eine erfolgreiche RDP-Anmeldung, Event ID 4624, erzeugt einen sehr klaren Log im Windows Security Event Log, und wenn ein Benutzer bereits angemeldet ist, könnte er sehen, dass seine Session gekickt wird.

However, on a server with no active user, it can go unnoticed for some time.
Allerdings kann es auf einem Server ohne aktiven Benutzer eine Weile unbemerkt bleiben.

Try it yourself.
Probieren Sie es selbst aus.

These commands target your own machine to safely demonstrate the tools.
Diese Befehle zielen auf Ihre eigene Maschine ab, um die Tools sicher zu demonstrieren.

Windows Management Instrumentation can be used to manage and execute processes.
Windows Management Instrumentation kann verwendet werden, um Prozesse zu managen und auszuführen.

List Running Processes: See what wmic can query.
Running Processes auflisten: Sehen Sie, was wmic abfragen kann.

wmic process get name, processid
wmic process get name, processid

Execute a Program: Use wmic to launch Notepad.
Ein Programm ausführen: Verwenden Sie wmic, um Notepad zu starten.

This demonstrates the core of WMI-based remote execution.
Das demonstriert den Kern der WMI-basierten remote Ausführung.

wmic process call create notepad.exe
wmic process call create notepad.exe

SMB, Server Message Block, is the protocol for file sharing.
SMB, Server Message Block, ist das Protokoll für Dateifreigaben.

Attackers use it to move tools onto a target.
Angreifer verwenden es, um Tools auf ein Ziel zu bewegen.

List Local Shares: See your machine's default administrative shares, C$, ADMIN$.
Lokale Shares auflisten: Sehen Sie die standardmäßigen administrativen Shares Ihrer Maschine, C$, ADMIN$.

net share
net share

Access Your Own Admin Share: Use the dir command to view your C: drive through its share, simulating how an attacker would access a remote file system.
Auf Ihren eigenen Admin-Share zugreifen: Verwenden Sie den dir-Befehl, um Ihr C:-Laufwerk durch seine Share zu betrachten, was simuliert, wie ein Angreifer auf ein remote Dateisystem zugreifen würde.

dir \\127.0.0.1\C$
dir \\127.0.0.1\C$

Combining SMB and WMI, Local Simulation.
SMB und WMI kombinieren, lokale Simulation.

This two-step process simulates an attacker's actions: staging a file and then running it.
Dieser Zwei-Schritt-Prozess simuliert die Aktionen eines Angreifers: Ein File zu stagen und es dann auszuführen.

Step A: Stage a Payload.
Schritt A: Ein Payload stagen.

Create a simple batch file in a temporary directory.
Erstellen Sie eine einfache Batch-Datei in einem temporären Verzeichnis.

This mimics an attacker copying a tool over an SMB share.
Das simuliert einen Angreifer, der ein Tool über eine SMB-Share kopiert.

echo calc.exe > C:\Windows\Temp\payload.bat
echo calc.exe > C:\Windows\Temp\payload.bat

Step B: Execute the Payload.
Schritt B: Das Payload ausführen.

Use WMI to run the batch file you just created.
Verwenden Sie WMI, um die Batch-Datei auszuführen, die Sie gerade erstellt haben.

wmic process call create C:\Windows\Temp\payload.bat
wmic process call create C:\Windows\Temp\payload.bat

The Calculator application will open.
Die Calculator-Anwendung wird geöffnet.

You have just simulated placing a file and then executing it remotely.
Sie haben gerade das Platzieren einer Datei und dann das remote Ausführen simuliert.

Cleanup, Optional.
Cleanup, optional.

del C:\Windows\Temp\payload.bat
del C:\Windows\Temp\payload.bat