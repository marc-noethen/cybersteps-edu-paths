Welcome to the world of digital forensics, where every byte tells a story. Willkommen in der Welt der digitalen Forensik, wo jedes Byte eine Geschichte erzählt.

Last session, we introduced the field of Digital Forensics and Incident Response. In der letzten Sitzung haben wir das Gebiet der digitalen Forensik und Incident Response vorgestellt.

Now, we move from the conceptual to the concrete. Jetzt bewegen wir uns vom Konzeptionellen zum Konkreten.

We're going to zoom in on the most fundamental source of digital evidence: the storage disk. Wir werden uns auf die grundlegendste Quelle digitaler Beweise konzentrieren: die Speicherplatte.

To a forensic investigator, a disk isn't just a place to store files; it's a crime scene where every action leaves a trace. Für einen forensischen Ermittler ist eine Festplatte nicht nur ein Ort, um Dateien zu speichern, sondern ein Tatort, an dem jede Handlung eine Spur hinterlässt.

Understanding how data is stored, managed, and deleted is the bedrock of uncovering that evidence. Das Verständnis, wie Daten gespeichert, verwaltet und gelöscht werden, ist die Grundlage für die Aufdeckung dieser Beweise.

The First Rule: Preserve the Evidence. Die erste Regel: Bewahre die Beweise.

Before we touch a single byte, we must internalize the cardinal rule of digital forensics: do no harm. Bevor wir ein einziges Byte berühren, müssen wir die wichtigste Regel der digitalen Forensik verinnerlichen: richte keinen Schaden an.

The original evidence is sacrosanct. Die ursprünglichen Beweise sind unantastbar.

Any action we take, even just booting up a computer, can alter hundreds or thousands of files, overwriting critical data and potentially rendering the evidence inadmissible. Jede Handlung, die wir vornehmen, selbst das bloße Hochfahren eines Computers, kann Hunderte oder Tausende von Dateien verändern, kritische Daten überschreiben und möglicherweise die Beweise unzulässig machen.

To prevent this, investigators use write blockers. Um dies zu verhindern, verwenden Ermittler Schreibblocker.

These are devices, either hardware or software, that sit between the investigator's machine and the evidence disk, allowing data to be read but physically preventing any data from being written back. Dies sind Geräte, entweder Hardware oder Software, die zwischen dem Computer des Ermittlers und der Beweisfestplatte sitzen und das Lesen von Daten erlauben, aber physisch verhindern, dass Daten zurückgeschrieben werden.

Once the evidence is protected, the first step is always to create a forensic image, a bit for bit, identical copy of the entire disk, including all the empty spaces and deleted files. Sobald die Beweise geschützt sind, besteht der erste Schritt immer darin, ein forensisches Abbild zu erstellen, eine bit für bit identische Kopie der gesamten Festplatte, einschließlich aller leeren Bereiche und gelöschten Dateien.

We work on this image, never on the original. Wir arbeiten an diesem Abbild, niemals am Original.

This preserves the original evidence in its pristine, unaltered state. Dies bewahrt die ursprünglichen Beweise in ihrem makellosen, unveränderten Zustand.

Common forensic image formats include the raw dd format and the more advanced EnCase format, which includes metadata and compression. Gängige forensische Abbildformate umfassen das rohe dd Format und das fortschrittlichere EnCase Format, das Metadaten und Komprimierung beinhaltet.

From Physical Disk to Logical File. Von der physischen Festplatte zur logischen Datei.

When you save a file, you see a simple icon in a folder. Wenn Sie eine Datei speichern, sehen Sie ein einfaches Symbol in einem Ordner.

But the journey from your command to that stored file involves multiple layers of abstraction. Aber der Weg von Ihrem Befehl zu dieser gespeicherten Datei umfasst mehrere Abstraktionsebenen.

As an investigator, you must peel back these layers to find the truth. Als Ermittler müssen Sie diese Ebenen zurückschälen, um die Wahrheit zu finden.

A physical disk, like an SSD or HDD, is just a raw block of storage. Eine physische Festplatte, wie eine SSD oder HDD, ist nur ein roher Speicherblock.

To make it usable, an operating system divides it into one or more partitions. Um sie nutzbar zu machen, teilt ein Betriebssystem sie in eine oder mehrere Partitionen auf.

Think of this like dividing a large, empty warehouse into smaller, designated sections. Stellen Sie sich das vor wie die Aufteilung eines großen, leeren Lagerhauses in kleinere, zugewiesene Bereiche.

Each partition can then be formatted with a file system, which acts as the warehouse's inventory management system. Jede Partition kann dann mit einem Dateisystem formatiert werden, das als Bestandsverwaltungssystem des Lagerhauses fungiert.

The file system creates a structured space, often called a volume, like the C drive, where it can keep track of every single file. Das Dateisystem erstellt einen strukturierten Bereich, oft als Volume bezeichnet, wie das C Laufwerk, wo es jede einzelne Datei verfolgen kann.

Disk: The physical storage hardware. Festplatte: Die physische Speicherhardware.

Partition: A logical section of a disk. Partition: Ein logischer Abschnitt einer Festplatte.

File System: A set of rules and data structures for storing and organizing files on a volume. Dateisystem: Eine Reihe von Regeln und Datenstrukturen zum Speichern und Organisieren von Dateien auf einem Volume.

Volume: A single, accessible storage area with a single file system, for example, C drive. Volume: Ein einzelner, zugänglicher Speicherbereich mit einem einzigen Dateisystem, zum Beispiel C Laufwerk.

Try it yourself. Probieren Sie es selbst aus.

Let's make this tangible. Lassen Sie uns dies greifbar machen.

Open a terminal on your Kali Linux VM and run the lsblk command, List Block Devices. Öffnen Sie ein Terminal auf Ihrer Kali Linux VM und führen Sie den lsblk Befehl aus, Liste der Blockgeräte.

This tool shows you the block devices, your disks, and how they are partitioned and mounted. Dieses Werkzeug zeigt Ihnen die Blockgeräte, Ihre Festplatten, und wie sie partitioniert und eingebunden sind.

You'll see an output showing your main disk, for example, sda or vda, its partitions, for example, sda1, sda2, and where they are mounted in the file system, for example, root, boot efi. Sie sehen eine Ausgabe, die Ihre Hauptfestplatte zeigt, zum Beispiel sda oder vda, ihre Partitionen, zum Beispiel sda1, sda2, und wo sie im Dateisystem eingebunden sind, zum Beispiel root, boot efi.

You are looking at the logical structure of your own virtual hard disk. Sie betrachten die logische Struktur Ihrer eigenen virtuellen Festplatte.

Partitioning Schemes: MBR versus GPT. Partitionierungsschemata: MBR gegen GPT.

Before a disk can be partitioned, it needs a master plan. Bevor eine Festplatte partitioniert werden kann, braucht sie einen Masterplan.

This is the partitioning scheme, and it defines how the partitions are structured. Dies ist das Partitionierungsschema, und es definiert, wie die Partitionen strukturiert sind.

For decades, the standard was the Master Boot Record. Jahrzehntelang war der Standard der Master Boot Record.

The MBR is a tiny section at the very beginning of the disk that holds the partition table, the map of the disk's layout. Der MBR ist ein winziger Abschnitt am Anfang der Festplatte, der die Partitionstabelle enthält, die Karte des Festplattenlayouts.

However, MBR is old technology and has limitations, for example, only supports disks up to 2 terabytes. Allerdings ist MBR eine alte Technologie und hat Einschränkungen, zum Beispiel unterstützt es nur Festplatten bis zu 2 Terabyte.

Modern systems use the GUID Partition Table. Moderne Systeme verwenden die GUID Partitionstabelle.

It's more robust, supports much larger disks, and crucially for forensics, it keeps a backup of the partition table at the end of the disk. Sie ist robuster, unterstützt viel größere Festplatten und, entscheidend für die Forensik, bewahrt eine Sicherungskopie der Partitionstabelle am Ende der Festplatte auf.

If an attacker tries to corrupt the primary partition table to hide a partition, a savvy investigator knows to check for the backup. Wenn ein Angreifer versucht, die primäre Partitionstabelle zu beschädigen, um eine Partition zu verstecken, weiß ein versierter Ermittler, dass er nach der Sicherung suchen muss.

