For this course, we will not be performing acquisition ourselves; we will work with pre captured memory dumps. Für diesen Kurs werden wir die Erfassung nicht selbst durchführen, wir werden mit bereits erfassten Speicherabbildern arbeiten.

In the real world, tools like FTK Imager, Redline, or specialized hardware are used for this critical task. In der realen Welt werden Werkzeuge wie FTK Imager, Redline oder spezialisierte Hardware für diese kritische Aufgabe verwendet.

Number two, Analysis: Making Sense of the Chaos. Nummer zwei, Analyse: Dem Chaos einen Sinn geben.

A raw memory dump is a massive, unstructured binary file, potentially gigabytes in size. Ein rohes Speicherabbild ist eine massive, unstrukturierte Binärdatei, potenziell Gigabytes groß.

It's impossible to interpret manually. Es ist unmöglich, sie manuell zu interpretieren.

We need a specialized tool to parse this data and reconstruct the underlying operating system structures. Wir brauchen ein spezialisiertes Werkzeug, um diese Daten zu analysieren und die zugrunde liegenden Betriebssystemstrukturen zu rekonstruieren.

This is where Volatility comes in. Hier kommt Volatility ins Spiel.

Volatility is a powerful, open source memory forensics framework. Volatility ist ein leistungsstarkes Open-Source-Framework für Speicherforensik.

It contains a collection of plugins, each designed to find and present a specific type of artifact. Es enthält eine Sammlung von Plugins, die jeweils darauf ausgelegt sind, eine bestimmte Art von Artefakt zu finden und darzustellen.

For example, the windows dot pslist dot PsList plugin knows how to walk through the raw data of a Windows memory dump and identify the data structures that represent running processes, presenting them in a readable list. Zum Beispiel weiß das windows punkt pslist punkt PsList Plugin, wie es durch die Rohdaten eines Windows-Speicherabbilds geht und die Datenstrukturen identifiziert, die laufende Prozesse darstellen, und präsentiert sie in einer lesbaren Liste.

To do this, Volatility needs to know the exact map of the operating system that was running. Um dies zu tun, muss Volatility die genaue Karte des Betriebssystems kennen, das lief.

The data structures for a process in Windows 10 are different from those in Windows 7. Die Datenstrukturen für einen Prozess in Windows 10 unterscheiden sich von denen in Windows 7.

In the older Volatility 2, investigators had to manually find and provide a profile that matched the OS version. Im älteren Volatility 2 mussten Ermittler manuell ein Profil finden und bereitstellen, das mit der Betriebssystemversion übereinstimmte.

The modern Volatility 3 is much more intelligent; it uses symbol tables and can often automatically identify the OS and version, making the analysis process much faster and more reliable. Das moderne Volatility 3 ist viel intelligenter, es verwendet Symboltabellen und kann oft automatisch das Betriebssystem und die Version identifizieren, was den Analyseprozess viel schneller und zuverlässiger macht.

Try it yourself. Probieren Sie es selbst aus.

Now that you have Volatility 3 on your machine, let's explore its capabilities. Jetzt, da Sie Volatility 3 auf Ihrer Maschine haben, lassen Sie uns seine Fähigkeiten erkunden.

Open a terminal, navigate to your Volatility 3 directory, for example, cd tilde slash Desktop slash forensics slash volatility3 dash 2.5.0, and run the following command: python3 vol dot py dash dash help. Öffnen Sie ein Terminal, navigieren Sie zu Ihrem Volatility 3 Verzeichnis, zum Beispiel cd Tilde Schrägstrich Desktop Schrägstrich forensics Schrägstrich volatility3 Bindestrich 2.5.0, und führen Sie den folgenden Befehl aus: python3 vol punkt py Bindestrich Bindestrich help.

This command lists all the available plugins, which are the core tools we use for analysis. Dieser Befehl listet alle verfügbaren Plugins auf, die die Kernwerkzeuge sind, die wir für die Analyse verwenden.

Look through the list of Windows plugins. Schauen Sie sich die Liste der Windows-Plugins an.

Can you identify the full name of a plugin that seems designed to list running processes? Können Sie den vollständigen Namen eines Plugins identifizieren, das dafür konzipiert zu sein scheint, laufende Prozesse aufzulisten?

What about one that might show active network connections? Was ist mit einem, das aktive Netzwerkverbindungen zeigen könnte?

We will use these plugins and more in our class. Wir werden diese Plugins und mehr in unserem Unterricht verwenden.

Setup. Einrichtung.

Before our live session, you need to set up your analysis environment. Vor unserer Live-Sitzung müssen Sie Ihre Analyseumgebung einrichten.

We will be using Volatility 3. Wir werden Volatility 3 verwenden.

Number one, Install Volatility 3. Nummer eins, Installieren Sie Volatility 3.

Volatility 3 is a Python based tool, so it doesn't have a traditional installer. Volatility 3 ist ein Python-basiertes Werkzeug, daher hat es kein traditionelles Installationsprogramm.

You simply download its source code. Sie laden einfach seinen Quellcode herunter.

Navigate to the official Volatility 3 releases page on GitHub. Navigieren Sie zur offiziellen Volatility 3 Veröffentlichungsseite auf GitHub.

Find the latest release, it will be at the top of the page. Finden Sie die neueste Version, sie wird oben auf der Seite sein.

Under the Assets section for the latest release, download the source code ZIP file, for example, volatility3 dash 2 dot X dot X dot zip. Unter dem Abschnitt Assets für die neueste Version laden Sie die Quellcode-ZIP-Datei herunter, zum Beispiel volatility3 Bindestrich 2 Punkt X Punkt X Punkt zip.

Create a dedicated folder for our forensics work. Erstellen Sie einen dedizierten Ordner für unsere Forensikarbeit.

A good place is on your Desktop, for example, tilde slash Desktop slash forensics. Ein guter Ort ist auf Ihrem Desktop, zum Beispiel Tilde Schrägstrich Desktop Schrägstrich forensics.

Unzip the downloaded file into your forensics folder. Entpacken Sie die heruntergeladene Datei in Ihren Forensik-Ordner.

This will create a new folder containing the framework, for example, tilde slash Desktop slash forensics slash volatility3 dash 2.5.0. Dies erstellt einen neuen Ordner, der das Framework enthält, zum Beispiel Tilde Schrägstrich Desktop Schrägstrich forensics Schrägstrich volatility3 Bindestrich 2.5.0.

Inside this new folder, you will find a file named vol dot py. In diesem neuen Ordner finden Sie eine Datei mit dem Namen vol Punkt py.

This is the executable script we will use to run Volatility. Dies ist das ausführbare Skript, das wir verwenden werden, um Volatility auszuführen.

Number two, Download a Sample Memory Image. Nummer zwei, Laden Sie ein Beispiel-Speicher-Image herunter.

To practice, we need a memory dump to analyze. Zum Üben brauchen wir ein Speicherabbild zum Analysieren.

The Volatility Foundation provides several sample images. Die Volatility Foundation stellt mehrere Beispiel-Images bereit.

Visit the Volatility Sample Memory Images page. Besuchen Sie die Volatility Sample Memory Images Seite.

Download the win7 underscore x64 underscore memdump dot zip file. Laden Sie die win7 Unterstrich x64 Unterstrich memdump Punkt zip Datei herunter.

This is a memory dump from a 64 bit Windows 7 machine that contains traces of a staged attack. Dies ist ein Speicherabbild von einer 64-Bit-Windows-7-Maschine, die Spuren eines inszenierten Angriffs enthält.

Unzip the file. Entpacken Sie die Datei.

This will give you win7 underscore x64 underscore memdump dot vmem. Dies gibt Ihnen win7 Unterstrich x64 Unterstrich memdump Punkt vmem.

Place the win7 underscore x64 underscore memdump dot vmem file directly inside your main forensics folder, that is, at the same level as your volatility3 dash 2.5.0 folder. Platzieren Sie die win7 Unterstrich x64 Unterstrich memdump Punkt vmem Datei direkt in Ihrem Haupt-Forensik-Ordner, das heißt auf derselben Ebene wie Ihr volatility3 Bindestrich 2.5.0 Ordner.

Number three, Verify Your Setup. Nummer drei, Überprüfen Sie Ihre Einrichtung.

Let's run a simple command to ensure everything is working correctly. Lassen Sie uns einen einfachen Befehl ausführen, um sicherzustellen, dass alles korrekt funktioniert.

Open your terminal, Terminal on macOS. Öffnen Sie Ihr Terminal, Terminal auf macOS.

Navigate into the Volatility 3 directory you created. Navigieren Sie in das Volatility 3 Verzeichnis, das Sie erstellt haben.

The command will be similar to this, adjust the version number if needed: cd tilde slash Desktop slash forensics slash volatility3 dash 2.5.0. Der Befehl wird ähnlich sein, passen Sie die Versionsnummer bei Bedarf an: cd Tilde Schrägstrich Desktop Schrägstrich forensics Schrägstrich volatility3 Bindestrich 2.5.0.

Now, run the windows dot info dot Info plugin. Führen Sie nun das windows Punkt info Punkt Info Plugin aus.

This plugin performs a basic check of the memory dump and provides summary information about the operating system. Dieses Plugin führt eine grundlegende Überprüfung des Speicherabbilds durch und liefert zusammenfassende Informationen über das Betriebssystem.

python3 vol dot py: This executes the Volatility script using your system's Python 3 interpreter. python3 vol Punkt py: Dies führt das Volatility-Skript mit dem Python 3 Interpreter Ihres Systems aus.

f dot dot slash win7 underscore x64 underscore memdump dot vmem: The f flag specifies the file path to the memory dump. f Punkt Punkt Schrägstrich win7 Unterstrich x64 Unterstrich memdump Punkt vmem: Das f Flag gibt den Dateipfad zum Speicherabbild an.

The dot dot slash part is a shortcut that means go up one directory level, which is where we placed the dot vmem file. Der Punkt Punkt Schrägstrich Teil ist eine Abkürzung, die bedeutet, gehe eine Verzeichnisebene nach oben, wo wir die Punkt vmem Datei platziert haben.

windows dot info dot Info: This is the name of the plugin we want to run. windows Punkt info Punkt Info: Dies ist der Name des Plugins, das wir ausführen möchten.

Your full command will look exactly like this: python3 vol dot py dash f dot dot slash win7 underscore x64 underscore memdump dot vmem windows dot info dot Info. Ihr vollständiger Befehl wird genau so aussehen: python3 vol Punkt py Bindestrich f Punkt Punkt Schrägstrich win7 Unterstrich x64 Unterstrich memdump Punkt vmem windows Punkt info Punkt Info.

The command will take a moment to initialize and run. Der Befehl wird einen Moment brauchen, um zu initialisieren und auszuführen.

If successful, you will see a table of information about the memory dump, including its Kernel Base, DTB, System Time, and OS version. Bei Erfolg sehen Sie eine Tabelle mit Informationen über das Speicherabbild, einschließlich seiner Kernel Base, DTB, Systemzeit und Betriebssystemversion.

If you see this output, your setup is correct! Wenn Sie diese Ausgabe sehen, ist Ihre Einrichtung korrekt!

Troubleshooting Tip: If you get an error like command not found: python3, it means Python 3 is not correctly installed or not in your system's PATH. Fehlerbehebungstipp: Wenn Sie einen Fehler wie Befehl nicht gefunden: python3 erhalten, bedeutet dies, dass Python 3 nicht korrekt installiert ist oder nicht im PATH Ihres Systems liegt.

You may need to install or reinstall it from the official Python website. Möglicherweise müssen Sie es von der offiziellen Python-Website installieren oder neu installieren.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside! Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!