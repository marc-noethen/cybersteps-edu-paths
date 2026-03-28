Welcome to your preparation for our upcoming session on file systems and storage. Willkommen zu Ihrer Vorbereitung auf unsere kommende Sitzung über Dateisysteme und Speicherung.

Understanding how operating systems manage data is fundamental to many areas of cybersecurity, from digital forensics to system administration and security hardening. Zu verstehen, wie Betriebssysteme Daten verwalten, ist für viele Bereiche der Cybersicherheit von grundlegender Bedeutung, von der digitalen Forensik bis hin zur Systemverwaltung und Sicherheitshärtung.

This guide will introduce you to the key concepts. Dieser Leitfaden führt Sie in die wichtigsten Konzepte ein.

What is a file system? Was ist ein Dateisystem?

At its core, a file system is the method and data structure that an operating system uses to manage files on a hard drive or storage device. Im Kern ist ein Dateisystem die Methode und Datenstruktur, die ein Betriebssystem verwendet, um die Dateien auf einer Festplatte oder einem Datenträger zu verwalten.

Think of the system like a well-organized librarian for your computer's storage. Stellen Sie sich das System wie einen gut organisierten Bibliothekar für den Speicher Ihres Computers vor.

Without a file system, a hard drive would just be a huge, undifferentiated collection of bits, and finding specific information would be nearly impossible. Ohne ein Dateisystem wäre eine Festplatte nur eine riesige, undifferenzierte Sammlung von Bits, und das Auffinden bestimmter Informationen wäre nahezu unmöglich.

Key functions of a file system include organizing data, grouping data into files and folders, also called directories. Zu den wichtigsten Funktionen eines Dateisystems gehören das Organisieren von Daten, das Gruppieren von Daten in Dateien und Ordnern, auch als Verzeichnisse bezeichnet.

Naming conventions: allowing users and applications to give files and directories meaningful names. Benennungskonventionen: Ermöglicht es Benutzern und Anwendungen, Dateien und Verzeichnissen sinnvolle Namen zu geben.

Managing metadata: storing information about files, such as their size, creation or modification date, owner, and permissions. Verwaltung von Metadaten: Speicherung von Informationen über Dateien, wie z. B. ihre Größe, das Erstellungs- oder Änderungsdatum, Eigentümer und Berechtigungen.

Space management: tracking which parts of the storage medium are currently being used and which are free, and how files are allocated to specific blocks on the storage device. Platzverwaltung: Verfolgen, welche Teile des Speichermediums gerade benutzt werden und welche frei sind, und wie Dateien bestimmten Blöcken auf dem Speichergerät zugewiesen werden.

Data retrieval: providing a way to efficiently locate and access stored files. Datenabruf: Bereitstellung einer Möglichkeit, gespeicherte Dateien effizient zu lokalisieren und darauf zuzugreifen.

Data integrity and recovery: some file systems include mechanisms to prevent data corruption and recover data in the event of system crashes, for example journaling. Datenintegrität und Wiederherstellung: Einige Dateisysteme enthalten Mechanismen zur Verhinderung von Datenbeschädigung und zur Wiederherstellung von Daten im Falle von Systemabstürzen, z. B. Journaling.

Core concepts. Kernkonzepte.

Let's define some important terms you'll encounter. Definieren wir einige wichtige Begriffe, die Sie kennenlernen werden.

File: a named collection of related information recorded on secondary storage, such as a hard drive or SSD. Datei: Eine benannte Sammlung zusammengehöriger Informationen, die auf einem Sekundärspeicher, z. B. einer Festplatte oder SSD, aufgezeichnet wird.

It can be a document, an image, a program, or any other type of data. Dabei kann es sich um ein Dokument, ein Bild, ein Programm oder jede andere Art von Daten handeln.

Directory, or folder: a container that holds files and can also contain other directories. Verzeichnis oder Ordner: Ein Container, der Dateien enthält und auch andere Verzeichnisse enthalten kann.

This creates a hierarchical structure, similar to a physical filing cabinet with folders and subfolders, making it easier to organize and find files. Dadurch entsteht eine hierarchische Struktur, ähnlich wie bei einem physischen Aktenschrank mit Ordnern und Unterordnern, die das Organisieren und Auffinden von Dateien erleichtert.

Path: a string that specifies the unique location of a file or directory within the file system hierarchy. Pfad: Eine Zeichenkette, die den eindeutigen Ort einer Datei oder eines Verzeichnisses innerhalb der Hierarchie des Dateisystems angibt.

Absolute path: specifies the location from the root of the file system. Absoluter Pfad: Gibt den Speicherort ab dem Stamm des Dateisystems an.

For example, on Windows: C colon backslash Users backslash YourName backslash Documents backslash report dot docx, or on macOS slash Linux: slash home slash yourname slash documents slash report dot doc. Zum Beispiel unter Windows: C Doppelpunkt Backslash Users Backslash IhrName Backslash Dokumente Backslash report Punkt docx, oder unter macOS Schrägstrich Linux: Schrägstrich home Schrägstrich yourname Schrägstrich documents Schrägstrich report Punkt doc.

Relative path: specifies the location relative to the current working directory. Relativer Pfad: Gibt den Speicherort relativ zum aktuellen Arbeitsverzeichnis an.

For example, if you're currently in slash home slash yourname slash, a relative path to report dot doc could simply be documents slash report dot doc. Wenn Sie sich zum Beispiel gerade in Schrägstrich home Schrägstrich yourname Schrägstrich befinden, könnte ein relativer Pfad zu report Punkt doc einfach documents Schrägstrich report Punkt doc sein.

Metadata: this is data about data. Metadaten: Dies sind Daten über Daten.

For a file, metadata can include filename, file size, file type, for example dot txt, dot jpg, dot exe, timestamps, creation date, modification date, access date, permissions, who is allowed to read, write, or execute the file, owner and group information. Für eine Datei können die Metadaten Folgendes umfassen: Dateiname, Dateigröße, Dateityp, zum Beispiel Punkt txt, Punkt jpg, Punkt exe, Zeitstempel, Erstellungsdatum, Änderungsdatum, Zugriffsdatum, Berechtigungen, wer darf die Datei lesen, schreiben oder ausführen, Eigentümer und Gruppeninformationen.

Volume, or partition: a single accessible storage area with a single file system. Volume oder Partition: Ein einzelner zugänglicher Speicherbereich mit einem einzelnen Dateisystem.

Typically, a physical hard drive, like an HDD or SSD, can be divided into one or more partitions, and each partition can be formatted with a file system to become a volume. Normalerweise kann eine physische Festplatte, wie eine HDD oder SSD, in eine oder mehrere Partitionen unterteilt werden, und jede Partition kann mit einem Dateisystem formatiert werden, um ein Volume zu werden.

On Windows, these are often assigned drive letters, for example C colon, D colon. Unter Windows werden diesen oft Laufwerksbuchstaben zugewiesen, z. B. C Doppelpunkt, D Doppelpunkt.

Common file systems. Gemeinsame Dateisysteme.

Different operating systems and devices use different file systems. Verschiedene Betriebssysteme und Geräte verwenden unterschiedliche Dateisysteme.

While there are many, we'll focus on the ones most important for your work with Windows and common external media. Es gibt zwar viele, aber wir konzentrieren uns auf die Systeme, die für Ihre Arbeit mit Windows und den gängigen externen Medien am wichtigsten sind.

NTFS, New Technology File System: the primary file system for modern Windows operating systems. NTFS, New Technology File System: Das primäre Dateisystem für moderne Windows-Betriebssysteme.

Key features: robust security through access control lists, ACLs, journaling for crash recovery, support for large files slash volumes, built-in compression, and the Encrypting File System, EFS. Schlüsselmerkmale: Robuste Sicherheit durch Zugriffskontrolllisten, ACLs, Journaling für die Wiederherstellung bei Abstürzen, Unterstützung für große Dateien Schrägstrich Volumes, integrierte Komprimierung und das Encrypting File System, EFS.

Central to it is the Master File Table, MFT, which catalogs all files and directories. Kernstück ist die Master File Table, MFT, in der alle Dateien und Verzeichnisse katalogisiert sind.

FAT32, File Allocation Table 32: an older, simpler file system. FAT32, File Allocation Table 32: Ein älteres, einfacheres Dateisystem.

Current use: mainly for external storage like USB drives and SD cards due to its wide compatibility with various operating systems, Windows, macOS, Linux. Gegenwärtige Verwendung: Hauptsächlich für externe Speicher wie USB-Laufwerke und SD-Karten aufgrund seiner breiten Kompatibilität mit verschiedenen Betriebssystemen, Windows, macOS, Linux.

Limitations: maximum file size of 4 gigabytes and no advanced features like journaling and strong security permissions. Einschränkungen: Maximale Dateigröße von 4 Gigabyte und keine erweiterten Funktionen wie Journaling und starke Sicherheitsberechtigungen.

exFAT, Extended File Allocation Table: a modern replacement for FAT32, developed by Microsoft for flash media. exFAT, Extended File Allocation Table: Ein moderner Ersatz für FAT32, entwickelt von Microsoft für Flash-Medien.

Key features: overcomes the file and volume size limitations of FAT32 while maintaining good cross-platform compatibility. Schlüsselmerkmale: Überwindet die Beschränkungen der Datei- und Datenträgergröße von FAT32 und bietet gleichzeitig eine gute plattformübergreifende Kompatibilität.

Ideal for large USB drives and SD cards. Ideal für große USB-Laufwerke und SD-Karten.

Other notable systems: APFS, Apple File System, the modern standard for macOS, iOS, and other Apple devices, optimized for SSDs and encryption. Andere bemerkenswerte Systeme: APFS, Apple File System, der moderne Standard für macOS, iOS und andere Apple-Geräte, optimiert für SSDs und Verschlüsselung.

Ext4, Fourth Extended Filesystem, a common standard for Linux distributions, known for its stability and features. Ext4, Fourth Extended Filesystem, ein gängiger Standard für Linux-Distributionen, bekannt für seine Stabilität und Funktionen.

Storage concepts. Speicherkonzepte.

Understanding the underlying storage technology helps in understanding how file systems work. Das Verständnis der zugrunde liegenden Speichertechnologie hilft dabei, die Funktionsweise von Dateisystemen zu verstehen.

Hard Disk Drives, HDDs: traditional mechanical drives with spinning magnetic platters. Festplattenlaufwerke, HDDs: Traditionelle mechanische Laufwerke mit sich drehenden Magnetplatten.

Data is stored in sectors and tracks. Die Daten werden in Sektoren und Spuren gespeichert.

They offer high capacity at low cost but are slower and more vulnerable than SSDs. Sie bieten eine hohe Kapazität zu niedrigen Kosten, sind aber langsamer und anfälliger als SSDs.

Solid State Drives, SSDs: use flash memory chips, NAND flash, for storage and offer much faster performance, lower power consumption, and longer lifespan than HDDs, although often at higher cost per gigabyte. Solid State Drives, SSDs: Verwenden Flash-Speicherchips, NAND-Flash, für die Speicherung und bieten eine viel schnellere Leistung, einen geringeren Stromverbrauch und eine längere Lebensdauer als HDDs, allerdings oft zu höheren Kosten pro Gigabyte.

Formatting hard drives. Formatierung von Festplatten.

What is formatting? Was ist Formatieren?

Formatting a hard drive, partition, or storage device prepares it for data storage by, normally, erasing all existing data and setting up a selected file system, such as NTFS, FAT32, or exFAT. Beim Formatieren einer Festplatte, einer Partition oder eines Datenträgers wird diese oder dieser für die Datenspeicherung vorbereitet, indem normalerweise alle vorhandenen Daten gelöscht und ein ausgewähltes Dateisystem, wie NTFS, FAT32 oder exFAT, eingerichtet wird.

This process creates the necessary directory structures and control information that the operating system uses to read and write data to the device. Bei diesem Vorgang werden die erforderlichen Verzeichnisstrukturen und Steuerinformationen erstellt, die das Betriebssystem zum Lesen und Schreiben von Daten auf dem Gerät verwendet.

Why format? Warum formatieren?

First-time use: new drives or partitions must be formatted before they can be used to store files. Erstmalige Verwendung: Neue Laufwerke oder Partitionen müssen formatiert werden, bevor sie zum Speichern von Dateien verwendet werden können.

Changing file system: you can reformat a drive to change the file system, for example from FAT32 to NTFS to take advantage of larger file sizes or security features. Änderung des Dateisystems: Sie können ein Laufwerk neu formatieren, um das Dateisystem zu ändern, z. B. von FAT32 auf NTFS, um die Vorteile größerer Dateigrößen oder Sicherheitsfunktionen zu nutzen.

Erasing data: formatting is a common method to quickly erase all data from a drive, noting that a standard quick format may not securely erase the data so it could be recovered with special tools. Daten löschen: Das Formatieren ist eine gängige Methode, um schnell alle Daten von einem Laufwerk zu löschen, wobei zu beachten ist, dass ein standardmäßiges Schnellformat die Daten möglicherweise nicht sicher löscht, so dass sie mit speziellen Tools wiederhergestellt werden können.

Troubleshooting: sometimes reformatting can fix problems with a corrupted file system on a drive. Fehlerbehebung: Manchmal kann eine Neuformatierung Probleme mit einem beschädigten Dateisystem auf einem Laufwerk beheben.

The process: when you format a drive, you typically select the desired file system and assign a volume label, a name for the drive. Der Vorgang: Wenn Sie ein Laufwerk formatieren, wählen Sie in der Regel das gewünschte Dateisystem aus und vergeben eine Datenträgerbezeichnung, einen Namen für das Laufwerk.

The operating system then writes the file system data structures to the drive, making it ready for use. Das Betriebssystem schreibt dann die Datenstrukturen des Dateisystems auf das Laufwerk und macht es damit einsatzbereit.

Fragmentation. Fragmentierung.

Occurs when parts of a single file are stored in non-contiguous blocks on a storage device, primarily affecting performance on HDDs due to mechanical seek time. Tritt auf, wenn Teile einer einzelnen Datei in nicht zusammenhängenden Blöcken auf einem Speichergerät gespeichert werden, was sich in erster Linie aufgrund der mechanischen Suchzeit auf die Leistung von Festplatten auswirkt.

Defragmentation: a process that reorganizes files on an HDD so they are contiguous, improving access speed. Defragmentierung: Ein Prozess, bei dem Dateien auf einer Festplatte so reorganisiert werden, dass sie zusammenhängend sind, was die Zugriffsgeschwindigkeit verbessert.

SSDs and fragmentation: fragmentation is not a significant performance issue on SSDs due to near-instantaneous access to any storage location. SSDs und Fragmentierung: Fragmentierung ist bei SSDs aufgrund des nahezu sofortigen Zugriffs auf jeden Speicherplatz kein wesentliches Leistungsproblem.

Defragmenting SSDs is generally unnecessary and can contribute to wear. Die Defragmentierung von SSDs ist im Allgemeinen unnötig und kann zur Abnutzung beitragen.

Data protection on storage devices. Datenschutz auf Speichergeräten.

Protecting the data stored on these file systems is crucial. Der Schutz der auf diesen Dateisystemen gespeicherten Daten ist von entscheidender Bedeutung.

Two important strategies are backups and encryption. Zwei wichtige Strategien sind Backups und Verschlüsselung.

Backups. Backups.

A backup is a copy of data stored in a different location so it can be used to restore the original after a data loss. Ein Backup ist eine Kopie von Daten, die an einem anderen Ort gespeichert wird, damit sie nach einem Datenverlust zur Wiederherstellung des Originals verwendet werden kann.

Data loss can result from hardware slash software failures, data corruption, accidental deletion, or malicious attacks like ransomware. Datenverluste können durch Hardware-Schrägstrich-Softwarefehler, Datenbeschädigung, versehentliches Löschen oder bösartige Angriffe wie Ransomware entstehen.

Why backups are so important. Warum Backups so wichtig sind.

Disaster recovery: recovery from major hardware failures, for example hard drive crash. Wiederherstellung im Katastrophenfall: Wiederherstellung nach größeren Hardwarefehlern, z. B. Festplattenabsturz.

Accidental deletion slash modification: recovery of files that were accidentally removed or changed. Versehentliches Löschen Schrägstrich Ändern: Wiederherstellung von Dateien, die versehentlich entfernt oder geändert wurden.

Protection against malware: recovery of clean data after a ransomware attack or other malware incidents. Schutz vor Malware: Wiederherstellung sauberer Daten nach einem Ransomware-Angriff oder anderen Malware-Vorfällen.

Data integrity: ensuring that if data corruption occurs, a known good copy of the data is available. Datenintegrität: Sicherstellen, dass im Falle einer Datenbeschädigung eine bekannt gute Kopie der Daten verfügbar ist.

Common backup types, concept. Gängige Sicherungsarten, Konzept.

Full backup: copies all selected data. Vollständige Sicherung: Kopiert alle ausgewählten Daten.

It's the simplest to restore but consumes the most storage space and time. Sie ist am einfachsten wiederherzustellen, verbraucht aber den meisten Speicherplatz und die meiste Zeit.

Incremental backup: copies only the data that has changed since the last backup, full or incremental. Inkrementelle Sicherung: Kopiert nur die Daten, die sich seit der letzten Sicherung, vollständig oder inkrementell, geändert haben.

Faster backup, less storage needed, but recovery can be more complicated, requires the last full backup and all subsequent incremental backups. Schnellere Sicherung, weniger Speicherplatzbedarf, aber die Wiederherstellung kann komplizierter sein, erfordert die letzte vollständige Sicherung und alle nachfolgenden inkrementellen Sicherungen.

Differential backup: copies only the data that has changed since the last full backup. Differenzielle Sicherung: Kopiert nur die Daten, die sich seit der letzten vollständigen Sicherung geändert haben.

Faster to restore than incremental backups, requires only the last full backup and the last differential backup, but the backup size grows over time until the next full backup. Schneller wiederherstellbar als inkrementelle Sicherungen, erfordert nur die letzte Vollsicherung und die letzte differenzielle Sicherung, aber die Sicherungsgröße wächst mit der Zeit bis zur nächsten Vollsicherung.

Backup media and locations. Backup-Medien und Speicherorte.

External HDDs slash SSDs: common for personal backups. Externe Festplatten Schrägstrich SSDs: Üblich für persönliche Backups.

Network Attached Storage, NAS: centralized storage on a local network. Network Attached Storage, NAS: Zentraler Speicher in einem lokalen Netzwerk.

Cloud storage: services like OneDrive, Google Drive, iCloud, or dedicated backup services, for example Backblaze, Carbonite. Cloud-Speicher: Dienste wie OneDrive, Google Drive, iCloud oder spezielle Sicherungsdienste, z. B. Backblaze, Carbonite.

Provides offsite protection. Bietet Schutz außerhalb des Standorts.

Windows backup tools: Windows includes built-in utilities. Windows-Backup-Tools: Windows enthält integrierte Dienstprogramme.

File History: regularly backs up versions of files in Libraries, Desktop, Contacts, and Favorites folders to an external drive or network. Dateiverlauf: Sichert regelmäßig die Versionen der Dateien in den Ordnern Bibliotheken, Schreibtisch, Kontakte und Favoriten auf einem externen Laufwerk oder im Netzwerk.

Backup and Restore, Windows 7: a more traditional tool that allows system image backups and file slash folder backups. Sichern und Wiederherstellen, Windows 7: Ein eher traditionelles Tool, das Systemabbildsicherungen und Datei-Schrägstrich-Ordnersicherungen ermöglicht.

Also available in newer Windows versions. Auch in neueren Windows-Versionen verfügbar.

Storage encryption. Speicherverschlüsselung.

Encryption converts data into an unreadable format, ciphertext, that can only be decrypted with a specific key. Verschlüsselung wandelt Daten in ein unlesbares Format, Chiffretext, um, das nur mit einem bestimmten Schlüssel entschlüsselt werden kann.

Storage encryption protects data confidentiality, ensuring that even if unauthorized persons gain physical access to the storage device, they cannot read the data. Die Speicherverschlüsselung schützt die Vertraulichkeit der Daten und stellt sicher, dass selbst wenn Unbefugte physischen Zugang zum Speichergerät erhalten, sie die Daten nicht lesen können.

Full-Disk Encryption, FDE. Full-Disk Encryption, FDE.

Encrypts the entire storage volume, for example an entire HDD or SSD partition. Verschlüsselt das gesamte Speichervolumen, z. B. eine gesamte Festplatte oder SSD-Partition.

Data is automatically encrypted when written and decrypted when read, transparent to the user after initial authentication. Die Daten werden automatisch verschlüsselt, wenn sie geschrieben werden, und entschlüsselt, wenn sie gelesen werden, und zwar transparent für den Benutzer nach der ersten Authentifizierung.

BitLocker Drive Encryption: Microsoft's FDE solution integrated into the professional and enterprise editions of Windows. BitLocker Drive Encryption: Microsofts FDE-Lösung, die in die professionellen und Unternehmensversionen von Windows integriert ist.

It can encrypt the operating system volume and other data volumes. Sie kann das Betriebssystem-Volume und andere Datenvolumes verschlüsseln.

Often uses a Trusted Platform Module, TPM, chip for enhanced security. Verwendet häufig einen Trusted Platform Module-, TPM-, Chip für erhöhte Sicherheit.

Very effective against data theft from lost or stolen laptops or drives. Sehr effektiv gegen Datendiebstahl von verlorenen oder gestohlenen Laptops oder Laufwerken.

File slash folder encryption. Datei-Schrägstrich-Ordnerverschlüsselung.

Encrypts individual files or specific folders rather than the entire hard drive. Verschlüsselt einzelne Dateien oder bestimmte Ordner und nicht die gesamte Festplatte.

Encrypting File System, EFS: a feature of NTFS, Windows, that allows users to encrypt files and folders. Verschlüsselndes Dateisystem, EFS: Eine Funktion von NTFS, Windows, mit der Benutzer Dateien und Ordner verschlüsseln können.

Encryption is tied to the user's account. Die Verschlüsselung ist an das Konto des Benutzers gebunden.

If an unauthorized user accesses the system or copies the encrypted file to another location, they cannot open it without the original user's credentials or the recovery key. Wenn ein unbefugter Benutzer auf das System zugreift oder die verschlüsselte Datei an einen anderen Ort kopiert, kann er sie nicht ohne die Anmeldedaten des ursprünglichen Benutzers oder den Wiederherstellungsschlüssel öffnen.

Useful for protecting specific sensitive files on a shared system or for an additional layer of security. Nützlich für den Schutz bestimmter sensibler Dateien auf einem gemeinsam genutzten System oder für eine zusätzliche Sicherheitsebene.

Why encryption is important. Warum Verschlüsselung wichtig ist.

Confidentiality: protects sensitive data from unauthorized access, especially on portable devices, laptops, USB drives. Vertraulichkeit: Schützt sensible Daten vor unbefugtem Zugriff, insbesondere auf tragbaren Geräten, Laptops, USB-Laufwerken.

Compliance: many regulations, for example GDPR, HIPAA, require or recommend encryption to protect personal or sensitive data. Compliance: Viele Vorschriften, z. B. GDPR, HIPAA, verlangen oder empfehlen Verschlüsselung zum Schutz persönlicher oder sensibler Daten.

Protection against data breaches: if an encrypted device is stolen, the data remains protected, reducing the impact of the data breach. Schutz vor Datenschutzverletzungen: Wenn ein verschlüsseltes Gerät gestohlen wird, bleiben die Daten geschützt, was die Auswirkungen der Datenschutzverletzung verringert.

Windows specifics. Windows-Besonderheiten.

Since you'll be working extensively with Windows in this program, let's cover some specific aspects. Da Sie in diesem Programm viel mit Windows arbeiten werden, wollen wir auf einige spezielle Aspekte eingehen.

Drive letters: Windows uses drive letters, for example C colon, D colon, E colon, to represent volumes. Laufwerksbuchstaben: Windows verwendet Laufwerksbuchstaben, z. B. C Doppelpunkt, D Doppelpunkt, E Doppelpunkt, um Datenträger darzustellen.

Drive C colon is typically the primary system drive where Windows is installed. Das Laufwerk C Doppelpunkt ist normalerweise das primäre Systemlaufwerk, auf dem Windows installiert ist.

File Explorer: this is the primary graphical tool for navigating and managing files and folders in Windows. Datei-Explorer: Dies ist das wichtigste grafische Werkzeug zum Navigieren und Verwalten von Dateien und Ordnern in Windows.

You can view file properties, create folders, copy slash move slash delete files, etc. Sie können Dateieigenschaften anzeigen, Ordner erstellen, Dateien kopieren Schrägstrich verschieben Schrägstrich löschen, usw.

Disk Management: a built-in Windows utility, diskmgmt dot msc, that allows you to view and manage disks and volumes. Festplattenverwaltung: Ein integriertes Windows-Dienstprogramm, diskmgmt Punkt msc, mit dem Sie Festplatten und Datenträger anzeigen und verwalten können.

You can use it to view partitions and their file systems, create, delete, and format partitions, change drive letters, expand or shrink partitions, with limitations. Sie können es verwenden, um Partitionen und deren Dateisysteme anzuzeigen, Partitionen zu erstellen, zu löschen und zu formatieren, Laufwerksbuchstaben zu ändern, Partitionen zu erweitern oder zu verkleinern, mit Einschränkungen.

Windows C colon backslash drive directory structure. Windows C Doppelpunkt Backslash Laufwerk Verzeichnisstruktur.

This image is a hierarchical diagram illustrating the folder structure of the C colon backslash drive in a Windows operating system. Dieses Bild ist ein hierarchisches Diagramm, das die Ordnerstruktur des Laufwerks C Doppelpunkt Backslash in einem Windows-Betriebssystem veranschaulicht.

It shows important directories like Programs, Windows, and temp, with subfolders like Common Files, system32, and Microsoft Office. Es zeigt wichtige Verzeichnisse wie Programme, Windows und temp mit Unterordnern wie Common Files, system32 und Microsoft Office.

Try it yourself. Versuchen Sie es selbst.

Open File Explorer. Datei-Explorer öffnen.

Open File Explorer on your Windows VM. Öffnen Sie den Datei-Explorer auf Ihrer Windows-VM.

Identify the existing drive letters. Identifizieren Sie die vorhandenen Laufwerksbuchstaben.

Navigate to common system folders like C colon backslash Windows, C colon backslash Programs, and C colon backslash Users backslash YourUsername backslash Documents. Navigieren Sie zu gängigen Systemordnern wie C Doppelpunkt Backslash Windows, C Doppelpunkt Backslash Programme und C Doppelpunkt Backslash Benutzer Backslash IhrBenutzername Backslash Dokumente.

Check file properties. Dateieigenschaften prüfen.

Find any file, right-click and select Properties. Suchen Sie eine beliebige Datei, klicken Sie mit der rechten Maustaste und wählen Sie Eigenschaften.

Examine the General tab, type, location, size, attributes, and Details tab, metadata. Untersuchen Sie die Registerkarte Allgemein, Typ, Speicherort, Größe, Attribute, und die Registerkarte Details, Metadaten.

If you have an NTFS volume, look for the Security tab to see permissions. Wenn Sie ein NTFS-Volume haben, suchen Sie die Registerkarte Sicherheit, um die Berechtigungen zu sehen.

Search for backup and encryption options, exploration only. Sicherungs- und Verschlüsselungsoptionen suchen, nur Erkundung.

In the Windows search bar, type File History and open the utility to see the interface, you don't need to configure it now. Geben Sie in der Windows-Suchleiste Dateiverlauf ein und öffnen Sie das Programm, um die Schnittstelle zu sehen, Sie brauchen es jetzt nicht zu konfigurieren.

Search for BitLocker, Manage BitLocker. Suchen Sie nach BitLocker, Verwalten von BitLocker.

If your Windows version supports it, you'll see options to enable it for drives. Wenn Ihre Windows-Version dies unterstützt, sehen Sie Optionen, um es für Laufwerke zu aktivieren.

Only enable BitLocker if you're familiar with it and have recovery keys backed up. Aktivieren Sie BitLocker nur dann, wenn Sie damit vertraut sind und Wiederherstellungsschlüssel gesichert haben.

Explore Disk Management, exploration only. Erkunden Sie die Datenträgerverwaltung, nur Erkundung.

Press Windows key plus R, type diskmgmt dot msc, and press Enter. Drücken Sie Windows-Taste plus R, geben Sie diskmgmt Punkt msc ein, und drücken Sie die Eingabetaste.

Observe the layout. Beobachten Sie das Layout.

You'll see your physical disk or disks and the partitions slash volumes on them. Sie sehen Ihre physische oder physischen Festplatten und die Partitionen Schrägstrich Volumes darauf.

Note their file systems. Beachten Sie deren Dateisysteme.

Don't make any changes here unless you're sure what you're doing. Nehmen Sie hier keine Änderungen vor, wenn Sie sich nicht sicher sind, was Sie tun.

This tool is very powerful and incorrect use can lead to data loss. Dieses Tool ist sehr leistungsfähig und eine falsche Verwendung kann zu Datenverlust führen.

Just observe it for now. Beobachten Sie es vorerst einfach.

Think about it. Denken Sie darüber nach.

If you have a very important project file, would you rely solely on your computer's hard drive to store it? Wenn Sie eine sehr wichtige Projektdatei haben, würden Sie sich dann ausschließlich auf die Festplatte Ihres Computers verlassen, um sie zu speichern?

What backup strategy would you consider and why? Welche Sicherungsstrategie würden Sie in Betracht ziehen und warum?

When you delete a file, even if you empty the recycle bin, is the data immediately gone? Wenn Sie eine Datei löschen, auch wenn Sie den Papierkorb leeren, sind die Daten dann sofort weg?

How does this relate to file system operations and the possibility of data recovery? In welchem Zusammenhang steht dies mit Dateisystemoperationen und der Möglichkeit der Datenwiederherstellung?

How does formatting a drive typically affect existing data? Wie wirkt sich das Formatieren eines Laufwerks normalerweise auf die vorhandenen Daten aus?

What are the main benefits of using full-disk encryption like BitLocker on a corporate laptop? Was sind die Hauptvorteile der Verwendung einer Festplattenverschlüsselung wie BitLocker auf einem Firmenlaptop?

Are there any potential downsides or considerations? Gibt es irgendwelche potenziellen Nachteile oder Überlegungen?

This preparation will provide you with a solid foundation for our live session, where we'll deepen these concepts and experience them in practice. Diese Vorbereitung wird Ihnen eine solide Grundlage für unsere Live-Sitzung bieten, in der wir diese Konzepte vertiefen und in der Praxis erleben werden.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.

Try not to peek before class, spoilers inside. Versuche nicht vor dem Unterricht zu spicken, Spoiler drinnen.

