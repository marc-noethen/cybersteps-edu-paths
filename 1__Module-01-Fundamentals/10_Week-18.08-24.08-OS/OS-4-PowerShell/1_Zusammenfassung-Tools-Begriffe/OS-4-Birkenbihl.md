Welcome to your introduction to PowerShell! This preparation material will provide you with the foundational knowledge needed for our upcoming lesson. PowerShell is a powerful tool for system administrators and cybersecurity professionals alike. Understanding its basics is a key step in mastering Windows environments.

Willkommen zu Ihrer Einführung in PowerShell! Dieses Vorbereitungsmaterial wird Ihnen das grundlegende Wissen vermitteln, das Sie für unsere kommende Lektion benötigen. PowerShell ist ein mächtiges Werkzeug sowohl für Systemadministratoren als auch für Cybersicherheitsexperten. Das Verständnis der Grundlagen ist ein wichtiger Schritt zur Beherrschung von Windows-Umgebungen.

What is PowerShell?

Was ist PowerShell?

PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. It was developed by Microsoft and was first released in 2006 for Windows.

PowerShell ist eine plattformübergreifende Lösung zur Aufgabenautomatisierung, die aus einer Befehlszeilenschnittstelle, einer Skriptsprache und einem Konfigurationsverwaltungs-Framework besteht. Es wurde von Microsoft entwickelt und erstmals 2006 für Windows veröffentlicht.

Unlike traditional command-line shells that work with text streams, like Command Prompt in Windows or Bash in Linux and macOS, PowerShell is built on the dot NET Framework and works with objects. This is a fundamental difference and a source of its power and flexibility.

Im Gegensatz zu traditionellen Befehlszeilenschnittstellen, die mit Textströmen arbeiten, wie die Eingabeaufforderung in Windows oder Bash in Linux und macOS, basiert PowerShell auf dem dot NET Framework und arbeitet mit Objekten. Dies ist ein grundlegender Unterschied und eine Quelle seiner Leistungsfähigkeit und Flexibilität.

Think of it this way. Traditional shells pass around strings of text. If you want to get a list of running processes and then sort them by memory usage, you'd typically get a block of text, then use other text-manipulation tools to parse that text, extract the memory usage, and then sort.

Stellen Sie es sich so vor. Traditionelle Shells übergeben Textzeichenfolgen. Wenn Sie eine Liste laufender Prozesse erhalten und diese dann nach Speichernutzung sortieren möchten, würden Sie normalerweise einen Textblock erhalten, dann andere Textmanipulationswerkzeuge verwenden, um diesen Text zu analysieren, die Speichernutzung zu extrahieren und dann zu sortieren.

PowerShell, on the other hand, gives you a list of process objects. Each object inherently knows its properties, like name, ID, CPU usage, and memory usage. You can then directly tell PowerShell to sort these objects by their memory property, without complex text parsing.

PowerShell hingegen gibt Ihnen eine Liste von Prozessobjekten. Jedes Objekt kennt von sich aus seine Eigenschaften, wie Name, ID, CPU-Nutzung und Speichernutzung. Sie können dann PowerShell direkt anweisen, diese Objekte nach ihrer Speichereigenschaft zu sortieren, ohne komplexe Textanalyse.

PowerShell is designed for automation, automating repetitive administrative tasks, configuration management, managing and maintaining the configuration of systems, and system interaction, interacting with various components of the operating system and applications.

PowerShell ist konzipiert für Automatisierung, die Automatisierung sich wiederholender administrativer Aufgaben, Konfigurationsverwaltung, die Verwaltung und Pflege der Konfiguration von Systemen und Systeminteraktion, die Interaktion mit verschiedenen Komponenten des Betriebssystems und Anwendungen.

Initially a Windows-only tool, PowerShell is now open-source and available on macOS and Linux, making it a versatile tool for diverse environments.

Ursprünglich ein reines Windows-Werkzeug, ist PowerShell jetzt Open-Source und verfügbar für macOS und Linux, was es zu einem vielseitigen Werkzeug für unterschiedliche Umgebungen macht.

What is PowerShell used for?

Wofür wird PowerShell verwendet?

PowerShell is an indispensable tool for IT professionals, including those in cybersecurity, for several reasons.

PowerShell ist ein unverzichtbares Werkzeug für IT-Experten, einschließlich derjenigen im Bereich Cybersicherheit, aus mehreren Gründen.

System administration and management. Many IT tasks involve interacting with and managing Windows systems. PowerShell provides deep access to system internals for configuration, maintenance, and troubleshooting.

Systemadministration und Verwaltung. Viele IT-Aufgaben beinhalten die Interaktion mit und Verwaltung von Windows-Systemen. PowerShell bietet tiefen Zugriff auf Systeminterna für Konfiguration, Wartung und Fehlerbehebung.

Incident response. During a security incident, PowerShell can be used to quickly gather information about a compromised system, identify malicious processes, check network connections, and collect forensic data.

Vorfallreaktion. Während eines Sicherheitsvorfalls kann PowerShell verwendet werden, um schnell Informationen über ein kompromittiertes System zu sammeln, bösartige Prozesse zu identifizieren, Netzwerkverbindungen zu überprüfen und forensische Daten zu sammeln.

Forensics. Its ability to access detailed system information, like event logs, registry entries, and running services, makes it valuable for digital forensics.

Forensik. Seine Fähigkeit, auf detaillierte Systeminformationen wie Ereignisprotokolle, Registrierungseinträge und laufende Dienste zuzugreifen, macht es wertvoll für die digitale Forensik.

Penetration testing and red teaming. Attackers, and penetration testers mimicking them, often use PowerShell for reconnaissance, exploitation, and post-exploitation activities due to its power and native presence on Windows systems. Understanding PowerShell helps defenders recognize and counter these techniques.

Penetrationstests und Red Teaming. Angreifer und Penetrationstester, die sie nachahmen, verwenden häufig PowerShell für Aufklärung, Ausnutzung und Aktivitäten nach der Ausnutzung aufgrund seiner Leistungsfähigkeit und nativen Präsenz auf Windows-Systemen. Das Verständnis von PowerShell hilft Verteidigern, diese Techniken zu erkennen und zu bekämpfen.

Log analysis. PowerShell can parse and analyze various log files, helping to identify suspicious activities or system errors.

Protokollanalyse. PowerShell kann verschiedene Protokolldateien analysieren und auswerten und hilft dabei, verdächtige Aktivitäten oder Systemfehler zu identifizieren.

Active Directory management. Active Directory is a core component of most enterprise networks. PowerShell is the primary tool for managing and querying Active Directory.

Active Directory Verwaltung. Active Directory ist eine Kernkomponente der meisten Unternehmensnetzwerke. PowerShell ist das primäre Werkzeug zur Verwaltung und Abfrage von Active Directory.

Automation of security and IT tasks. Security checks, compliance reporting, software deployment, user provisioning, and remediation actions can be scripted and automated.

Automatisierung von Sicherheits- und IT-Aufgaben. Sicherheitsüberprüfungen, Compliance-Berichte, Softwareverteilung, Benutzerbereitstellung und Behebungsmaßnahmen können skriptgesteuert und automatisiert werden.

Because PowerShell is installed by default on all modern Windows operating systems, it's a common tool for both administrators, or blue teams, and attackers, or red teams. Knowing PowerShell is crucial for both defending systems, managing them efficiently, and understanding potential attack vectors.

Da PowerShell standardmäßig auf allen modernen Windows-Betriebssystemen installiert ist, ist es ein gängiges Werkzeug sowohl für Administratoren, die Blue Teams, als auch für Angreifer, die Red Teams. PowerShell zu kennen ist entscheidend sowohl für die Verteidigung von Systemen, ihre effiziente Verwaltung als auch für das Verständnis potenzieller Angriffsvektoren.

Core PowerShell concepts. Let's dive into some of the fundamental building blocks of PowerShell.

Kern-Konzepte von PowerShell. Lassen Sie uns in einige der grundlegenden Bausteine von PowerShell eintauchen.

Cmdlets, or command-lets. Cmdlets are the heart of PowerShell. They are lightweight commands that implement a specific function. The name cmdlet is a contraction of command-let, like a small command.

Cmdlets. Cmdlets sind das Herzstück von PowerShell. Sie sind leichtgewichtige Befehle, die eine bestimmte Funktion implementieren. Der Name Cmdlet ist eine Kontraktion von Command-let, wie ein kleiner Befehl.

A key feature of cmdlets is their naming convention, Verb-Noun. The Verb part specifies the action the cmdlet performs, for example, Get, Set, Start, Stop, New, Remove, Out. The Noun part specifies the entity on which the action is performed, for example, Process, Service, Item, Content, EventLog.

Ein Schlüsselmerkmal von Cmdlets ist ihre Namenskonvention, Verb-Substantiv. Der Verb-Teil gibt die Aktion an, die das Cmdlet ausführt, zum Beispiel Get, Set, Start, Stop, New, Remove, Out. Der Substantiv-Teil gibt die Entität an, auf der die Aktion ausgeführt wird, zum Beispiel Process, Service, Item, Content, EventLog.

Examples. Get-Process retrieves a list of currently running processes. Set-Location changes the current working directory, like cd. Get-Help provides help about PowerShell cmdlets and concepts. Start-Service starts a specified service. Stop-Process stops a running process.

Beispiele. Get-Process ruft eine Liste der aktuell laufenden Prozesse ab. Set-Location ändert das aktuelle Arbeitsverzeichnis, wie cd. Get-Help bietet Hilfe zu PowerShell-Cmdlets und -Konzepten. Start-Service startet einen bestimmten Dienst. Stop-Process stoppt einen laufenden Prozess.

This consistent naming convention makes it easier to predict and discover commands. If you know you want to retrieve information, you'll likely use a Get cmdlet. If you want to change something, you'll look for a Set cmdlet.

Diese konsistente Namenskonvention macht es einfacher, Befehle vorherzusagen und zu entdecken. Wenn Sie wissen, dass Sie Informationen abrufen möchten, werden Sie wahrscheinlich ein Get-Cmdlet verwenden. Wenn Sie etwas ändern möchten, werden Sie nach einem Set-Cmdlet suchen.

Try it yourself. Once you have PowerShell open, see the Setup section below. Type Get-Date and press Enter. What does it show you? Type Get-Process and press Enter. Observe the list of running processes. Type Get-Service and press Enter. Notice the different types of information displayed compared to Get-Process.

Versuchen Sie es selbst. Sobald Sie PowerShell geöffnet haben, siehe den Setup-Abschnitt unten. Geben Sie Get-Date ein und drücken Sie Enter. Was zeigt es Ihnen? Geben Sie Get-Process ein und drücken Sie Enter. Beobachten Sie die Liste der laufenden Prozesse. Geben Sie Get-Service ein und drücken Sie Enter. Beachten Sie die verschiedenen Arten von Informationen, die im Vergleich zu Get-Process angezeigt werden.

Objects. As mentioned earlier, PowerShell cmdlets don't just return text, they return dot NET objects. Each object is a structured piece of data with properties, which are characteristics, and methods, which are actions it can perform.

Objekte. Wie bereits erwähnt, geben PowerShell-Cmdlets nicht nur Text zurück, sie geben dot NET-Objekte zurück. Jedes Objekt ist ein strukturiertes Datenstück mit Eigenschaften, das sind Merkmale, und Methoden, das sind Aktionen, die es ausführen kann.

When you run Get-Process, you're not just getting lines of text. You're getting a collection of process objects. Each of these objects has properties like ProcessName, Id, CPU, PM for Paged Memory, WS for Working Set memory, and many more.

Wenn Sie Get-Process ausführen, erhalten Sie nicht nur Textzeilen. Sie erhalten eine Sammlung von Prozessobjekten. Jedes dieser Objekte hat Eigenschaften wie ProcessName, Id, CPU, PM für Paged Memory, WS für Working Set Memory und viele mehr.

Because you're dealing with objects, you can access specific properties, like using the CPU usage of the explorer process. You can filter based on properties, show only processes using more than one hundred megabytes of memory. You can sort based on properties, list processes by their CPU usage. You can pass these rich objects to other cmdlets for further processing.

Da Sie mit Objekten arbeiten, können Sie auf bestimmte Eigenschaften zugreifen, wie die CPU-Nutzung des Explorer-Prozesses. Sie können basierend auf Eigenschaften filtern, nur Prozesse anzeigen, die mehr als einhundert Megabyte Speicher verwenden. Sie können basierend auf Eigenschaften sortieren, Prozesse nach ihrer CPU-Nutzung auflisten. Sie können diese reichhaltigen Objekte zur weiteren Verarbeitung an andere Cmdlets übergeben.

The pipeline. The pipeline is a powerful feature in PowerShell used to send the output, which are objects, of one cmdlet to be used as input for another cmdlet. The pipe symbol is used for this.

Die Pipeline. Die Pipeline ist eine mächtige Funktion in PowerShell, die verwendet wird, um die Ausgabe, das sind Objekte, eines Cmdlets als Eingabe für ein anderes Cmdlet zu senden. Das Pipe-Symbol wird dafür verwendet.

This allows you to chain cmdlets together to perform complex tasks in a concise way.

Dies ermöglicht es Ihnen, Cmdlets miteinander zu verketten, um komplexe Aufgaben auf prägnante Weise auszuführen.

Example. Get-Process pipe Sort-Object Property CPU Descending. First, Get-Process runs and outputs a collection of process objects. Second, the pipe symbol takes these process objects and pipes them as input to the Sort-Object cmdlet. Third, Sort-Object then sorts these process objects based on their CPU property in Descending order.

Beispiel. Get-Process Pipe Sort-Object Property CPU Descending. Erstens, Get-Process läuft und gibt eine Sammlung von Prozessobjekten aus. Zweitens, das Pipe-Symbol nimmt diese Prozessobjekte und leitet sie als Eingabe an das Sort-Object-Cmdlet weiter. Drittens, Sort-Object sortiert dann diese Prozessobjekte basierend auf ihrer CPU-Eigenschaft in absteigender Reihenfolge.

Another example. Get-Service pipe Where-Object, and then in curly braces, dollar sign underscore dot Status equals Running. First, Get-Service retrieves all service objects. Second, these objects are piped to Where-Object. Third, Where-Object filters these service objects, only keeping those where the Status property is equal to Running. Dollar sign underscore is a special variable that refers to the current object in the pipeline.

Ein weiteres Beispiel. Get-Service Pipe Where-Object und dann in geschweiften Klammern Dollar-Zeichen Unterstrich Punkt Status gleich Running. Erstens, Get-Service ruft alle Dienstobjekte ab. Zweitens, diese Objekte werden an Where-Object weitergeleitet. Drittens, Where-Object filtert diese Dienstobjekte und behält nur diejenigen, bei denen die Status-Eigenschaft gleich Running ist. Dollar-Zeichen Unterstrich ist eine spezielle Variable, die sich auf das aktuelle Objekt in der Pipeline bezieht.

Think about it. Consider the command Get-Process pipe Sort-Object Name. What do you think this command does? How is this different from how you might sort a list of processes in a traditional text-based shell? Why is the object-oriented nature of PowerShell particularly useful when combined with the pipeline?

Denken Sie darüber nach. Betrachten Sie den Befehl Get-Process Pipe Sort-Object Name. Was denken Sie, was dieser Befehl tut? Wie unterscheidet sich dies davon, wie Sie eine Liste von Prozessen in einer traditionellen textbasierten Shell sortieren würden? Warum ist die objektorientierte Natur von PowerShell besonders nützlich, wenn sie mit der Pipeline kombiniert wird?

Variables. Like any scripting language, PowerShell allows you to store data in variables. Variable names in PowerShell always start with a dollar sign.

Variablen. Wie jede Skriptsprache ermöglicht PowerShell Ihnen, Daten in Variablen zu speichern. Variablennamen in PowerShell beginnen immer mit einem Dollar-Zeichen.

Examples. Dollar sign myName equals in quotes CyberStudent stores a string. Dollar sign processCount equals in parentheses Get-Process dot Count stores the number of running processes. Dollar sign runningServices equals Get-Service pipe Where-Object with curly braces dollar sign underscore dot Status equals Running stores a collection of running service objects.

Beispiele. Dollar-Zeichen myName gleich in Anführungszeichen CyberStudent speichert eine Zeichenkette. Dollar-Zeichen processCount gleich in Klammern Get-Process Punkt Count speichert die Anzahl der laufenden Prozesse. Dollar-Zeichen runningServices gleich Get-Service Pipe Where-Object mit geschweiften Klammern Dollar-Zeichen Unterstrich Punkt Status gleich Running speichert eine Sammlung von laufenden Dienstobjekten.

You can then use these variables in other commands or scripts. To display the value of a variable, just type its name, like dollar sign myName or dollar sign processCount.

Sie können diese Variablen dann in anderen Befehlen oder Skripten verwenden. Um den Wert einer Variablen anzuzeigen, geben Sie einfach ihren Namen ein, wie Dollar-Zeichen myName oder Dollar-Zeichen processCount.

Basic syntax and parameters. Cmdlets can have parameters that modify their behavior. Parameters are typically prefixed with a hyphen.

Grundlegende Syntax und Parameter. Cmdlets können Parameter haben, die ihr Verhalten ändern. Parameter sind typischerweise mit einem Bindestrich versehen.

Example. Get-Help Get-Process Detailed. Get-Help is the cmdlet. Get-Process is an argument specifying what to get help for. Detailed is a parameter that tells Get-Help to show detailed information.

Beispiel. Get-Help Get-Process Detailed. Get-Help ist das Cmdlet. Get-Process ist ein Argument, das angibt, wofür Hilfe angezeigt werden soll. Detailed ist ein Parameter, der Get-Help anweist, detaillierte Informationen anzuzeigen.

Some parameters take values, like dash Name in quotes notepad in Get-Process dash Name in quotes notepad.

Einige Parameter nehmen Werte an, wie Bindestrich Name in Anführungszeichen notepad in Get-Process Bindestrich Name in Anführungszeichen notepad.

Aliases. PowerShell has aliases for common cmdlets to make typing faster, especially for users familiar with other shells.

Aliase. PowerShell hat Aliase für gängige Cmdlets, um das Tippen schneller zu machen, besonders für Benutzer, die mit anderen Shells vertraut sind.

dir or ls are aliases for Get-ChildItem, which lists files and directories. cd is an alias for Set-Location, which changes directory. cls is an alias for Clear-Host, which clears the screen. gps is an alias for Get-Process. select is an alias for Select-Object, used to pick specific properties of objects.

dir oder ls sind Aliase für Get-ChildItem, das Dateien und Verzeichnisse auflistet. cd ist ein Alias für Set-Location, das das Verzeichnis wechselt. cls ist ein Alias für Clear-Host, das den Bildschirm löscht. gps ist ein Alias für Get-Process. select ist ein Alias für Select-Object, das verwendet wird, um bestimmte Eigenschaften von Objekten auszuwählen.

While aliases are convenient for interactive use, it's generally recommended to use the full cmdlet names in scripts for clarity. You can find out what a command is an alias for using Get-Alias followed by the alias name, for example, Get-Alias dir.

Während Aliase für die interaktive Nutzung praktisch sind, wird im Allgemeinen empfohlen, die vollständigen Cmdlet-Namen in Skripten zu verwenden, um Klarheit zu schaffen. Sie können herausfinden, wofür ein Befehl ein Alias ist, indem Sie Get-Alias gefolgt vom Aliasnamen verwenden, zum Beispiel Get-Alias dir.

The help system. PowerShell has an excellent built-in help system. The Get-Help cmdlet is your best friend when learning PowerShell.

Das Hilfesystem. PowerShell hat ein ausgezeichnetes eingebautes Hilfesystem. Das Get-Help-Cmdlet ist Ihr bester Freund beim Erlernen von PowerShell.

To get help for a specific cmdlet, use Get-Help followed by the cmdlet name. Example, Get-Help Get-Process.

Um Hilfe für ein bestimmtes Cmdlet zu erhalten, verwenden Sie Get-Help gefolgt vom Cmdlet-Namen. Beispiel, Get-Help Get-Process.

Useful parameters for Get-Help include Detailed, which provides detailed information including parameter descriptions and examples. Examples shows only examples of how to use the cmdlet. Full shows all available help information. Online opens the online version of the help topic in your web browser, which is often the most up-to-date.

Nützliche Parameter für Get-Help umfassen Detailed, das detaillierte Informationen einschließlich Parameterbeschreibungen und Beispielen bietet. Examples zeigt nur Beispiele, wie das Cmdlet verwendet wird. Full zeigt alle verfügbaren Hilfeinformationen. Online öffnet die Online-Version des Hilfethemas in Ihrem Webbrowser, die oft am aktuellsten ist.

PowerShell also has conceptual help topics, often called about topics. These explain broader concepts, syntax, and features. To list all about topics, use Get-Help about underscore asterisk. To read a specific about topic, use Get-Help about underscore Objects or Get-Help about underscore Pipelines.

PowerShell hat auch konzeptionelle Hilfethemen, oft About-Themen genannt. Diese erklären umfassendere Konzepte, Syntax und Funktionen. Um alle About-Themen aufzulisten, verwenden Sie Get-Help about Unterstrich Stern. Um ein bestimmtes About-Thema zu lesen, verwenden Sie Get-Help about Unterstrich Objects oder Get-Help about Unterstrich Pipelines.

Updating help. The help files on your system can become outdated. You can update them by running Update-Help. You'll need to run this in a PowerShell session with Administrator privileges.

Hilfe aktualisieren. Die Hilfedateien auf Ihrem System können veraltet sein. Sie können sie aktualisieren, indem Sie Update-Help ausführen. Sie müssen dies in einer PowerShell-Sitzung mit Administratorrechten ausführen.

Try it yourself. Use Get-Help to find out what the Get-Command cmdlet does. Explore the parameters of Get-ChildItem using Get-Help Get-ChildItem Detailed. Try listing files in your current directory using Get-ChildItem. Then try Get-ChildItem dash Path C colon backslash Windows dash File. This will list only files in C colon backslash Windows.

Versuchen Sie es selbst. Verwenden Sie Get-Help, um herauszufinden, was das Get-Command-Cmdlet tut. Erkunden Sie die Parameter von Get-ChildItem mit Get-Help Get-ChildItem Detailed. Versuchen Sie, Dateien in Ihrem aktuellen Verzeichnis mit Get-ChildItem aufzulisten. Dann versuchen Sie Get-ChildItem Bindestrich Path C Doppelpunkt Backslash Windows Bindestrich File. Dies listet nur Dateien in C Doppelpunkt Backslash Windows auf.

Find an about topic that interests you, for example, Get-Help about underscore Variables, and read through it. If you can, try running Update-Help. You might need administrator rights.

Finden Sie ein About-Thema, das Sie interessiert, zum Beispiel Get-Help about Unterstrich Variables, und lesen Sie es durch. Wenn Sie können, versuchen Sie, Update-Help auszuführen. Sie benötigen möglicherweise Administratorrechte.

Getting started with the PowerShell console. PowerShell can be accessed through its console or through the PowerShell Integrated Scripting Environment, or ISE, on Windows, or other editors like Visual Studio Code which has excellent PowerShell support. For now, we'll focus on the console.

Erste Schritte mit der PowerShell-Konsole. PowerShell kann über seine Konsole oder über die PowerShell Integrated Scripting Environment, oder ISE, unter Windows oder andere Editoren wie Visual Studio Code, der ausgezeichnete PowerShell-Unterstützung hat, aufgerufen werden. Vorerst konzentrieren wir uns auf die Konsole.

On Windows, PowerShell is pre-installed on modern Windows versions, including Windows seven SP one and later, and Windows Server two thousand eight R two SP one and later.

Unter Windows ist PowerShell auf modernen Windows-Versionen vorinstalliert, einschließlich Windows sieben SP eins und später und Windows Server zweitausendacht R zwei SP eins und später.

Click the Start button or press the Windows key. Type powershell. You should see Windows PowerShell in the results. Click it to open the console. You might also see Windows PowerShell ISE, a graphical environment for writing and testing scripts, or just PowerShell, referring to the newer, cross-platform version if installed. For basic commands, Windows PowerShell is fine.

Klicken Sie auf die Start-Schaltfläche oder drücken Sie die Windows-Taste. Geben Sie powershell ein. Sie sollten Windows PowerShell in den Ergebnissen sehen. Klicken Sie darauf, um die Konsole zu öffnen. Sie könnten auch Windows PowerShell ISE sehen, eine grafische Umgebung zum Schreiben und Testen von Skripten, oder einfach PowerShell, was sich auf die neuere plattformübergreifende Version bezieht, falls installiert. Für grundlegende Befehle ist Windows PowerShell in Ordnung.

The console window will open, and you'll see a prompt, typically PS C colon backslash Users backslash YourUserName greater than sign. This indicates PowerShell is ready to accept commands. C colon backslash Users backslash YourUserName is your current directory.

Das Konsolenfenster wird sich öffnen und Sie werden eine Eingabeaufforderung sehen, typischerweise PS C Doppelpunkt Backslash Users Backslash IhrBenutzername Größer-als-Zeichen. Dies zeigt an, dass PowerShell bereit ist, Befehle anzunehmen. C Doppelpunkt Backslash Users Backslash IhrBenutzername ist Ihr aktuelles Verzeichnis.

Important. PowerShell execution policy. When you start running PowerShell scripts, files ending in dot ps one, you will likely encounter the execution policy. This is a safety feature in PowerShell that controls whether scripts can be run.

Wichtig. PowerShell-Ausführungsrichtlinie. Wenn Sie beginnen, PowerShell-Skripte auszuführen, Dateien die mit Punkt ps eins enden, werden Sie wahrscheinlich auf die Ausführungsrichtlinie stoßen. Dies ist eine Sicherheitsfunktion in PowerShell, die steuert, ob Skripte ausgeführt werden können.

By default, on Windows client computers, like your virtual machine, this policy is often set to Restricted, which prevents all scripts from running. You will need to change this to complete many of the exercises in this course.

Standardmäßig ist auf Windows-Client-Computern, wie Ihrer virtuellen Maschine, diese Richtlinie oft auf Restricted gesetzt, was verhindert, dass alle Skripte ausgeführt werden. Sie müssen dies ändern, um viele der Übungen in diesem Kurs abzuschließen.

Checking your current policy. Open PowerShell and type Get-ExecutionPolicy. If it says Restricted, you need to change it.

Überprüfen Ihrer aktuellen Richtlinie. Öffnen Sie PowerShell und geben Sie Get-ExecutionPolicy ein. Wenn es Restricted sagt, müssen Sie es ändern.

Changing the execution policy, recommended for this course. To allow locally created scripts to run, which is what you'll be doing, we recommend setting the execution policy to RemoteSigned for your user account. This is a good balance between security and usability for learning.

Ändern der Ausführungsrichtlinie, empfohlen für diesen Kurs. Um lokal erstellte Skripte ausführen zu lassen, was Sie tun werden, empfehlen wir, die Ausführungsrichtlinie für Ihr Benutzerkonto auf RemoteSigned zu setzen. Dies ist eine gute Balance zwischen Sicherheit und Benutzerfreundlichkeit zum Lernen.

Open PowerShell as Administrator. Click the Start Menu. Type powershell. Right-click on Windows PowerShell in the search results. Select Run as administrator. If a User Account Control, or UAC, prompt appears, click Yes.

Öffnen Sie PowerShell als Administrator. Klicken Sie auf das Startmenü. Geben Sie powershell ein. Klicken Sie mit der rechten Maustaste auf Windows PowerShell in den Suchergebnissen. Wählen Sie Als Administrator ausführen. Wenn eine Benutzerkontensteuerungsaufforderung erscheint, klicken Sie auf Ja.

Set the execution policy. In the Administrator PowerShell window, type the following command and press Enter. Set-ExecutionPolicy RemoteSigned dash Scope CurrentUser. You might be asked to confirm the change. Type Y and press Enter. Scope CurrentUser applies the policy only to your user account, not system-wide. This is generally safer and doesn't require administrator rights for every PowerShell session after this initial setup.

Legen Sie die Ausführungsrichtlinie fest. Geben Sie im Administrator-PowerShell-Fenster den folgenden Befehl ein und drücken Sie Enter. Set-ExecutionPolicy RemoteSigned Bindestrich Scope CurrentUser. Sie werden möglicherweise aufgefordert, die Änderung zu bestätigen. Geben Sie Y ein und drücken Sie Enter. Scope CurrentUser wendet die Richtlinie nur auf Ihr Benutzerkonto an, nicht systemweit. Dies ist im Allgemeinen sicherer und erfordert nach dieser anfänglichen Einrichtung keine Administratorrechte für jede PowerShell-Sitzung.

Verify the change. You can close the Administrator PowerShell window. Open a regular PowerShell window, not as administrator, and type Get-ExecutionPolicy. It should now show RemoteSigned. If it still shows Restricted, or if you see RemoteSigned for Process or MachinePolicy but Undefined or Restricted for CurrentUser, ensure you ran the Set-ExecutionPolicy command correctly in an Administrator PowerShell window with the Scope CurrentUser parameter.

Überprüfen Sie die Änderung. Sie können das Administrator-PowerShell-Fenster schließen. Öffnen Sie ein normales PowerShell-Fenster, nicht als Administrator, und geben Sie Get-ExecutionPolicy ein. Es sollte jetzt RemoteSigned anzeigen. Wenn es immer noch Restricted anzeigt, oder wenn Sie RemoteSigned für Process oder MachinePolicy sehen, aber Undefined oder Restricted für CurrentUser, stellen Sie sicher, dass Sie den Set-ExecutionPolicy-Befehl korrekt in einem Administrator-PowerShell-Fenster mit dem Parameter Scope CurrentUser ausgeführt haben.

What does RemoteSigned mean? Scripts you write yourself on your computer will run. Scripts downloaded from the internet, for example from websites, must be digitally signed by a trusted publisher to run. This provides a layer of protection against running potentially malicious scripts from untrusted sources.

Was bedeutet RemoteSigned? Skripte, die Sie selbst auf Ihrem Computer schreiben, werden ausgeführt. Skripte, die aus dem Internet heruntergeladen wurden, zum Beispiel von Websites, müssen digital von einem vertrauenswürdigen Herausgeber signiert sein, um ausgeführt zu werden. Dies bietet eine Schutzschicht gegen das Ausführen potenziell bösartiger Skripte aus nicht vertrauenswürdigen Quellen.

Other policy options, for your information. Restricted means no scripts can be run. Commands in the console work. This is the default on Windows clients. AllSigned means only scripts signed by a trusted publisher can be run. Unrestricted means all scripts can run. This is less secure and generally not recommended.

Andere Richtlinienoptionen, zu Ihrer Information. Restricted bedeutet, dass keine Skripte ausgeführt werden können. Befehle in der Konsole funktionieren. Dies ist die Standardeinstellung auf Windows-Clients. AllSigned bedeutet, dass nur Skripte, die von einem vertrauenswürdigen Herausgeber signiert sind, ausgeführt werden können. Unrestricted bedeutet, dass alle Skripte ausgeführt werden können. Dies ist weniger sicher und wird im Allgemeinen nicht empfohlen.

Bypass means nothing is blocked and there are no warnings or prompts. Useful for specific, temporary situations but should be used with caution. Undefined removes the assigned execution policy for a scope. If all scopes are Undefined, the effective policy is Restricted for Windows clients.

Bypass bedeutet, dass nichts blockiert wird und es keine Warnungen oder Aufforderungen gibt. Nützlich für spezifische, vorübergehende Situationen, sollte aber mit Vorsicht verwendet werden. Undefined entfernt die zugewiesene Ausführungsrichtlinie für einen Bereich. Wenn alle Bereiche Undefined sind, ist die effektive Richtlinie Restricted für Windows-Clients.

Security note. Changing the execution policy can have security implications. The RemoteSigned setting for CurrentUser is a reasonable balance for a learning environment. Avoid setting it to Unrestricted or Bypass globally unless you fully understand the risks. For our course, RemoteSigned for CurrentUser will be sufficient.

Sicherheitshinweis. Das Ändern der Ausführungsrichtlinie kann Sicherheitsauswirkungen haben. Die RemoteSigned-Einstellung für CurrentUser ist eine vernünftige Balance für eine Lernumgebung. Vermeiden Sie es, sie global auf Unrestricted oder Bypass zu setzen, es sei denn, Sie verstehen die Risiken vollständig. Für unseren Kurs wird RemoteSigned für CurrentUser ausreichend sein.

Basic navigation cmdlets. Get-Location, with alias pwd, shows your current directory path. Set-Location followed by a path, with alias cd, changes your current directory. For example, Set-Location C colon backslash Windows. Set-Location dot dot moves to the parent directory.

Grundlegende Navigations-Cmdlets. Get-Location, mit Alias pwd, zeigt Ihren aktuellen Verzeichnispfad. Set-Location gefolgt von einem Pfad, mit Alias cd, ändert Ihr aktuelles Verzeichnis. Zum Beispiel Set-Location C Doppelpunkt Backslash Windows. Set-Location Punkt Punkt wechselt zum übergeordneten Verzeichnis.

Get-ChildItem, with aliases dir and ls, lists the contents of the current directory or a specified path.

Get-ChildItem, mit Aliasen dir und ls, listet den Inhalt des aktuellen Verzeichnisses oder eines angegebenen Pfads auf.

Setup. For this course, you will primarily be using PowerShell within the Windows Virtual Machine that you should have set up in the Operating Systems two, Windows Intro lesson.

Einrichtung. Für diesen Kurs werden Sie hauptsächlich PowerShell innerhalb der virtuellen Windows-Maschine verwenden, die Sie in der Lektion Betriebssysteme zwei, Windows-Einführung, eingerichtet haben sollten.

Accessing PowerShell in your Windows virtual machine. Start your Windows virtual machine. Once logged into Windows, click the Start Menu. Type powershell. Select Windows PowerShell from the search results to open the console. This is the environment we will primarily use for PowerShell exercises related to Windows. Before running any scripts, ensure you have checked and, if necessary, updated your execution policy as described in the Important PowerShell Execution Policy section above.

Zugriff auf PowerShell in Ihrer virtuellen Windows-Maschine. Starten Sie Ihre virtuelle Windows-Maschine. Sobald Sie in Windows eingeloggt sind, klicken Sie auf das Startmenü. Geben Sie powershell ein. Wählen Sie Windows PowerShell aus den Suchergebnissen aus, um die Konsole zu öffnen. Dies ist die Umgebung, die wir hauptsächlich für PowerShell-Übungen im Zusammenhang mit Windows verwenden werden. Bevor Sie Skripte ausführen, stellen Sie sicher, dass Sie Ihre Ausführungsrichtlinie überprüft und gegebenenfalls aktualisiert haben, wie im Abschnitt Wichtige PowerShell-Ausführungsrichtlinie oben beschrieben.

Important note for the course. Unless specified otherwise, please assume all PowerShell activities and exercises are to be performed within your Windows virtual machine's PowerShell console. This ensures a consistent environment and focuses on PowerShell in its native Windows context, which is critical for many cybersecurity roles.

Wichtiger Hinweis für den Kurs. Sofern nicht anders angegeben, gehen Sie bitte davon aus, dass alle PowerShell-Aktivitäten und -Übungen in der PowerShell-Konsole Ihrer virtuellen Windows-Maschine durchgeführt werden sollen. Dies gewährleistet eine konsistente Umgebung und konzentriert sich auf PowerShell in seinem nativen Windows-Kontext, was für viele Cybersicherheitsrollen entscheidend ist.

Try it yourself. Open PowerShell in your Windows virtual machine. Use Get-Location to see your current directory. Use Set-Location to navigate to the C colon backslash directory. Use Get-ChildItem to list the contents of the C colon backslash directory.

Versuchen Sie es selbst. Öffnen Sie PowerShell in Ihrer virtuellen Windows-Maschine. Verwenden Sie Get-Location, um Ihr aktuelles Verzeichnis zu sehen. Verwenden Sie Set-Location, um zum C Doppelpunkt Backslash-Verzeichnis zu navigieren. Verwenden Sie Get-ChildItem, um den Inhalt des C Doppelpunkt Backslash-Verzeichnisses aufzulisten.

Try using an alias. Type dir and press Enter. Does it give the same result as Get-ChildItem? Clear your screen using Clear-Host or its alias cls. Check your current execution policy using Get-ExecutionPolicy. If it's Restricted, follow the steps in the Important PowerShell Execution Policy section to change it to RemoteSigned for CurrentUser.

Versuchen Sie, einen Alias zu verwenden. Geben Sie dir ein und drücken Sie Enter. Gibt es das gleiche Ergebnis wie Get-ChildItem? Löschen Sie Ihren Bildschirm mit Clear-Host oder seinem Alias cls. Überprüfen Sie Ihre aktuelle Ausführungsrichtlinie mit Get-ExecutionPolicy. Wenn es Restricted ist, folgen Sie den Schritten im Abschnitt Wichtige PowerShell-Ausführungsrichtlinie, um es für CurrentUser auf RemoteSigned zu ändern.

This pre-class material should give you a solid starting point. Experiment with the cmdlets mentioned, use Get-Help extensively, and get comfortable with the PowerShell console. The more you explore now, the more you'll get out of our live session!

Dieses Material vor dem Unterricht sollte Ihnen einen soliden Ausgangspunkt geben. Experimentieren Sie mit den erwähnten Cmdlets, verwenden Sie Get-Help ausgiebig und machen Sie sich mit der PowerShell-Konsole vertraut. Je mehr Sie jetzt erkunden, desto mehr werden Sie aus unserer Live-Sitzung herausholen!

The slides for the live session can be viewed here. Try not to peek before class. Spoilers inside!

Die Folien für die Live-Sitzung können hier angesehen werden. Versuchen Sie nicht zu spicken vor dem Unterricht. Spoiler enthalten!