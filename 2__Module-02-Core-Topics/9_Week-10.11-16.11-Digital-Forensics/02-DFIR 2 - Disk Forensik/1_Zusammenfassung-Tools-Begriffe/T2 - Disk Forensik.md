The File System: The Librarian of Your Disk. Das Dateisystem: Der Bibliothekar Ihrer Festplatte.

If a partition is a library, the file system is the librarian. Wenn eine Partition eine Bibliothek ist, ist das Dateisystem der Bibliothekar.

It knows where every book, every file, is, how much space it takes up, and when it was created, modified, or even just read. Es weiß, wo jedes Buch, jede Datei ist, wie viel Platz sie einnimmt und wann sie erstellt, geändert oder sogar nur gelesen wurde.

Different operating systems use different file systems, and as an investigator, you must learn their languages. Verschiedene Betriebssysteme verwenden unterschiedliche Dateisysteme, und als Ermittler müssen Sie deren Sprachen lernen.

NTFS, New Technology File System: The standard for modern Windows. NTFS, New Technology File System: Der Standard für modernes Windows.

It's forensically rich, tracking vast amounts of metadata. Es ist forensisch reichhaltig und verfolgt große Mengen an Metadaten.

This will be our primary focus. Dies wird unser Hauptfokus sein.

ext4, Fourth Extended Filesystem: The default for most Linux distributions, including your Kali VM. ext4, Fourth Extended Filesystem: Der Standard für die meisten Linux Distributionen, einschließlich Ihrer Kali VM.

FAT, File Allocation Table: Older and simpler. FAT, File Allocation Table: Älter und einfacher.

You'll find it on USB drives and SD cards for its wide compatibility. Sie finden es auf USB Laufwerken und SD Karten wegen seiner breiten Kompatibilität.

APFS, Apple File System: The modern standard for macOS. APFS, Apple File System: Der moderne Standard für macOS.

A Deeper Look at NTFS. Ein tieferer Blick auf NTFS.

The heart of an NTFS volume is the Master File Table. Das Herz eines NTFS Volumes ist die Master File Table.

This isn't just a table; it's a database of every file and directory on the volume. Dies ist nicht nur eine Tabelle, es ist eine Datenbank jeder Datei und jedes Verzeichnisses auf dem Volume.

For a forensic investigator, the MFT is a treasure trove. Für einen forensischen Ermittler ist die MFT eine Schatzkammer.

Each file is represented by an MFT record containing its metadata. Jede Datei wird durch einen MFT Eintrag dargestellt, der ihre Metadaten enthält.

This includes: Standard Information: Contains key timestamps, Created, Modified, Accessed. Dies umfasst: Standardinformationen: Enthält wichtige Zeitstempel, Erstellt, Geändert, Zugegriffen.

File Name: Contains the file's name and another set of the same timestamps. Dateiname: Enthält den Namen der Datei und einen weiteren Satz derselben Zeitstempel.

Why two sets? Warum zwei Sätze?

Sometimes they don't match! Manchmal stimmen sie nicht überein!

A discrepancy between the timestamps can be a critical indicator of suspicious activity, such as an attacker using tools to alter file modification times, a technique known as timestomping. Eine Diskrepanz zwischen den Zeitstempeln kann ein kritischer Indikator für verdächtige Aktivitäten sein, wie ein Angreifer, der Werkzeuge verwendet, um Dateiänderungszeiten zu verändern, eine Technik, die als Timestomping bekannt ist.

The File Name timestamps are harder to change, often leaving behind a vital clue. Die Dateiname Zeitstempel sind schwieriger zu ändern und hinterlassen oft einen wichtigen Hinweis.

Beyond the MFT, NTFS maintains other crucial metadata files. Über die MFT hinaus pflegt NTFS andere wichtige Metadatendateien.

LogFile: A journal of changes to the file system. LogFile: Ein Journal der Änderungen am Dateisystem.

It can be used to see recent file system activity, even potentially reconstructing actions that occurred between full system snapshots. Es kann verwendet werden, um aktuelle Dateisystemaktivitäten zu sehen und potenziell sogar Aktionen zu rekonstruieren, die zwischen vollständigen System Snapshots aufgetreten sind.

UsnJrnl, Update Sequence Number Journal: Records all changes made to files on the volume, providing a high level log of what was added, deleted, or modified. UsnJrnl, Update Sequence Number Journal: Zeichnet alle Änderungen an Dateien auf dem Volume auf und liefert ein hochrangiges Protokoll dessen, was hinzugefügt, gelöscht oder geändert wurde.

The Truth About Deleted Files. Die Wahrheit über gelöschte Dateien.

Here is one of the most important concepts in forensics: when a user deletes a file, the data is not immediately erased. Hier ist eines der wichtigsten Konzepte in der Forensik: Wenn ein Benutzer eine Datei löscht, werden die Daten nicht sofort gelöscht.

Instead, the file system simply marks the file's MFT entry as inactive and the clusters it occupied as unallocated space. Stattdessen markiert das Dateisystem einfach den MFT Eintrag der Datei als inaktiv und die von ihr belegten Cluster als nicht zugewiesenen Speicherplatz.

The actual ones and zeros of the file remain on the disk, waiting to be overwritten by new data. Die tatsächlichen Einsen und Nullen der Datei verbleiben auf der Festplatte und warten darauf, von neuen Daten überschrieben zu werden.

This unallocated space is a primary hunting ground for investigators. Dieser nicht zugewiesene Speicherplatz ist ein primäres Jagdgebiet für Ermittler.

This is where data carving comes in. Hier kommt das Data Carving ins Spiel.

Data carving is a technique where forensic tools scan the raw data in the unallocated space, looking for known file headers and footers. Data Carving ist eine Technik, bei der forensische Werkzeuge die Rohdaten im nicht zugewiesenen Speicherplatz scannen und nach bekannten Dateiköpfen und Fußzeilen suchen.

For example, a JPEG file always starts with the bytes FF D8 FF. Zum Beispiel beginnt eine JPEG Datei immer mit den Bytes FF D8 FF.

When it finds a known header, it carves out the data that follows until it hits the file's footer or a specified size, allowing it to reconstruct the file even without any file system metadata. Wenn es einen bekannten Kopf findet, schnitzt es die folgenden Daten heraus, bis es auf die Fußzeile der Datei oder eine bestimmte Größe trifft, wodurch es die Datei rekonstruieren kann, selbst ohne jegliche Dateisystem Metadaten.

Think about it. Denken Sie darüber nach.

An attacker gains access to a Windows server, downloads a sensitive file, and then deletes it to cover their tracks. Ein Angreifer erhält Zugriff auf einen Windows Server, lädt eine sensible Datei herunter und löscht sie dann, um seine Spuren zu verwischen.

What specific artifacts within the NTFS file system, like the MFT, LogFile, slack space, or unallocated space, might allow you to prove not only that the file existed, but also when it was created and accessed, even after it was deleted? Welche spezifischen Artefakte innerhalb des NTFS Dateisystems, wie die MFT, LogFile, Slack Space oder nicht zugewiesener Speicherplatz, könnten es Ihnen ermöglichen zu beweisen, dass die Datei nicht nur existierte, sondern auch wann sie erstellt und aufgerufen wurde, selbst nachdem sie gelöscht wurde?

Setup. Einrichtung.

Autopsy is a powerful open source digital forensics platform. Autopsy ist eine leistungsstarke Open Source Plattform für digitale Forensik.

Please install it on your Windows VM before the session. Bitte installieren Sie es auf Ihrer Windows VM vor der Sitzung.

The slides for the live session can be viewed here. Die Folien für die Live Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside! Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!