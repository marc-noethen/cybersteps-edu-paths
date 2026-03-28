Willkommen zu Ihrer Vorbereitung auf unsere kommende Sitzung über Dateisysteme und Speicherung. Zu verstehen, wie Betriebssysteme Daten verwalten, ist für viele Bereiche der Cybersicherheit von grundlegender Bedeutung, von der digitalen Forensik bis hin zur Systemverwaltung und Sicherheitshärtung. Dieser Leitfaden führt Sie in die wichtigsten Konzepte ein.

## Was ist ein Dateisystem?

Im Kern ist ein **Dateisystem** die Methode und Datenstruktur, die ein Betriebssystem verwendet, um die Dateien auf einer Festplatte oder einem Datenträger zu verwalten. Stellen Sie sich das System wie einen gut organisierten Bibliothekar für den Speicher Ihres Computers vor. Ohne ein Dateisystem wäre eine Festplatte nur eine riesige, undifferenzierte Sammlung von Bits, und das Auffinden bestimmter Informationen wäre nahezu unmöglich.

Zu den wichtigsten Funktionen eines Dateisystems gehören:

- **Organisieren von Daten:** Gruppieren von Daten in Dateien und Ordnern (auch als Verzeichnisse bezeichnet).
- **Benennungskonventionen:** Ermöglicht es Benutzern und Anwendungen, Dateien und Verzeichnissen sinnvolle Namen zu geben.
- **Verwaltung von Metadaten:** Speicherung von Informationen _über_ Dateien, wie z. B. ihre Größe, das Erstellungs- oder Änderungsdatum, Eigentümer und Berechtigungen.
- **Space Management:** Verfolgen, welche Teile des Speichermediums gerade benutzt werden und welche frei sind, und wie Dateien bestimmten Blöcken auf dem Speichergerät zugewiesen werden.
- **Datenabruf:** Bereitstellung einer Möglichkeit, gespeicherte Dateien effizient zu lokalisieren und darauf zuzugreifen.
- **Datenintegrität und -wiederherstellung:** Einige Dateisysteme enthalten Mechanismen zur Verhinderung von Datenbeschädigung und zur Wiederherstellung von Daten im Falle von Systemabstürzen (z. B. Journaling).

![[Pasted image 20250929201921.png]]

Die Daten werden in Sektoren und Spuren gespeichert. Sie bieten eine hohe Kapazität zu niedrigen Kosten, sind aber langsamer und anfälliger als SSDs.
    
- **Solid State Drives (SSDs):** Verwenden Flash-Speicherchips (NAND-Flash) für die Speicherung und bieten eine viel schnellere Leistung, einen geringeren Stromverbrauch und eine längere Lebensdauer als HDDs, allerdings oft zu höheren Kosten pro Gigabyte.
    
- **Formatierung von Festplatten:**
    
    - **Was ist Formatieren?** Beim Formatieren einer Festplatte, einer Partition oder eines Datenträgers wird diese/r für die Datenspeicherung vorbereitet, indem (normalerweise) alle vorhandenen Daten gelöscht und ein ausgewähltes Dateisystem (wie NTFS, FAT32 oder exFAT) eingerichtet wird. Bei diesem Vorgang werden die erforderlichen Verzeichnisstrukturen und Steuerinformationen erstellt, die das Betriebssystem zum Lesen und Schreiben von Daten auf dem Gerät verwendet.## Kernkonzepte

Definieren wir einige wichtige Begriffe, die Sie kennenlernen werden:

- **Datei:** Eine benannte Sammlung zusammengehöriger Informationen, die auf einem Sekundärspeicher (z. B. einer Festplatte oder SSD) aufgezeichnet wird. Dabei kann es sich um ein Dokument, ein Bild, ein Programm oder jede andere Art von Daten handeln.
- **Verzeichnis (oder Ordner):** Ein Container, der Dateien enthält und auch andere Verzeichnisse enthalten kann. Dadurch entsteht eine hierarchische Struktur, ähnlich wie bei einem physischen Aktenschrank mit Ordnern und Unterordnern, die das Organisieren und Auffinden von Dateien erleichtert.
- **Pfad:** Eine Zeichenkette, die den eindeutigen Ort einer Datei oder eines Verzeichnisses innerhalb der Hierarchie des Dateisystems angibt.
    - **Absoluter Pfad:** Gibt den Speicherort ab dem Stamm des Dateisystems an. Zum Beispiel unter Windows: "C:\Users\\IhrName\\Dokumente\\report.docx" oder unter macOS/Linux: "/home/yourname/documents/report.doc".
    - **Relativer Pfad:** Gibt den Speicherort relativ zum aktuellen Arbeitsverzeichnis an. Wenn Sie sich zum Beispiel gerade in `/home/yourname/` befinden, könnte ein relativer Pfad zu `report.doc` einfach `documents/report.doc` sein.
- **Metadaten:** Dies sind "Daten über Daten". Für eine Datei können die Metadaten Folgendes umfassen:
    - Dateiname
    - Dateigröße
    - Dateityp (z. B. .txt, .jpg, .exe)
    - Zeitstempel (Erstellungsdatum, Änderungsdatum, Zugriffsdatum)
    - Berechtigungen (wer darf die Datei lesen, schreiben oder ausführen)
    - Eigentümer und Gruppeninformationen
- **Volume (oder Partition):** Ein einzelner zugänglicher Speicherbereich mit einem einzelnen Dateisystem. Normalerweise kann eine physische Festplatte (wie eine HDD oder SSD) in eine oder mehrere Partitionen unterteilt werden, und jede Partition kann mit einem Dateisystem formatiert werden, um ein Volume zu werden. Unter Windows werden diesen oft Laufwerksbuchstaben zugewiesen (z. B. C:, D:).

## Gemeinsame Dateisysteme

Verschiedene Betriebssysteme und Geräte verwenden unterschiedliche Dateisysteme. Es gibt zwar viele, aber wir konzentrieren uns auf die Systeme, die für Ihre Arbeit mit Windows und den gängigen externen Medien am wichtigsten sind:

- **NTFS (New Technology File System):**
    - Das primäre Dateisystem für moderne Windows-Betriebssysteme.
    - **Schlüsselmerkmale:** Robuste Sicherheit durch Zugriffskontrolllisten (ACLs), Journaling für die Wiederherstellung bei Abstürzen, Unterstützung für große Dateien/Volumes, integrierte Komprimierung und das Encrypting File System (EFS). Kernstück ist die Master File Table (MFT), in der alle Dateien und Verzeichnisse katalogisiert sind.
- **FAT32 (File Allocation Table 32):**
    - Ein älteres, einfacheres Dateisystem.
    - **Gegenwärtige Verwendung:** Hauptsächlich für externe Speicher wie USB-Laufwerke und SD-Karten aufgrund seiner breiten Kompatibilität mit verschiedenen Betriebssystemen (Windows, macOS, Linux).
    - **Einschränkungen:** Maximale Dateigröße von 4 GB und keine erweiterten Funktionen wie Journaling und starke Sicherheitsberechtigungen.
- **exFAT (Extended File Allocation Table):**
    - Ein moderner Ersatz für FAT32, entwickelt von Microsoft für Flash-Medien.
    - **Schlüsselmerkmale:** Überwindet die Beschränkungen der Datei- und Datenträgergröße von FAT32 und bietet gleichzeitig eine gute plattformübergreifende Kompatibilität. Ideal für große USB-Laufwerke und SD-Karten.
- **Andere bemerkenswerte Systeme:**
    - **APFS (Apple File System):** Der moderne Standard für macOS, iOS und andere Apple-Geräte, optimiert für SSDs und Verschlüsselung.
    - **Ext4 (Fourth Extended Filesystem):** Ein gängiger Standard für Linux-Distributionen, bekannt für seine Stabilität und Funktionen.

## Speicherkonzepte

Das Verständnis der zugrunde liegenden Speichertechnologie hilft dabei, die Funktionsweise von Dateisystemen zu verstehen.

- **Festplattenlaufwerke (HDDs):** Traditionelle mechanische Laufwerke mit sich drehenden Magnetplatten. 

    
    ![[Pasted image 20250929201948.png]]
    
    - **Warum formatieren?**
        - **Erstmalige Verwendung:** Neue Laufwerke oder Partitionen müssen formatiert werden, bevor sie zum Speichern von Dateien verwendet werden können.
        - **Änderung des Dateisystems:** Sie können ein Laufwerk neu formatieren, um das Dateisystem zu ändern (z. B. von FAT32 auf NTFS, um die Vorteile größerer Dateigrößen oder Sicherheitsfunktionen zu nutzen).
        - **Daten löschen:** Das Formatieren ist eine gängige Methode, um schnell alle Daten von einem Laufwerk zu löschen (wobei zu beachten ist, dass ein standardmäßiges "Schnellformat" die Daten möglicherweise nicht sicher löscht, so dass sie mit speziellen Tools wiederhergestellt werden können).
        - **Fehlerbehebung:** Manchmal kann eine Neuformatierung Probleme mit einem beschädigten Dateisystem auf einem Laufwerk beheben.
    - **Der Vorgang:** Wenn Sie ein Laufwerk formatieren, wählen Sie in der Regel das gewünschte Dateisystem aus und vergeben eine Datenträgerbezeichnung (einen Namen für das Laufwerk). Das Betriebssystem schreibt dann die Datenstrukturen des Dateisystems auf das Laufwerk und macht es damit einsatzbereit.
- **Fragmentierung:**
    
    - Tritt auf, wenn Teile einer einzelnen Datei in nicht zusammenhängenden Blöcken auf einem Speichergerät gespeichert werden, was sich in erster Linie aufgrund der mechanischen Suchzeit auf die Leistung von Festplatten auswirkt.
    - **Defragmentierung:** Ein Prozess, bei dem Dateien auf einer Festplatte so reorganisiert werden, dass sie zusammenhängend sind, was die Zugriffsgeschwindigkeit verbessert.
    
    ![[Pasted image 20250929201959.png]]
    
    - **SSDs und Fragmentierung:** Fragmentierung ist bei SSDs aufgrund des nahezu sofortigen Zugriffs auf jeden Speicherplatz kein wesentliches Leistungsproblem. Die Defragmentierung von SSDs ist im Allgemeinen unnötig und kann zur Abnutzung beitragen.

## Datenschutz auf Speichergeräten

Der Schutz der auf diesen Dateisystemen gespeicherten Daten ist von entscheidender Bedeutung. Zwei wichtige Strategien sind Backups und Verschlüsselung.

### Backups

Ein **Backup** ist eine Kopie von Daten, die an einem anderen Ort gespeichert wird, damit sie nach einem Datenverlust zur Wiederherstellung des Originals verwendet werden kann. Datenverluste können durch Hardware-/Softwarefehler, Datenbeschädigung, versehentliches Löschen oder bösartige Angriffe wie Ransomware entstehen.

![[Pasted image 20250929202008.png]]

- **Warum Backups so wichtig sind:**
    
    - **Wiederherstellung im Katastrophenfall:** Wiederherstellung nach größeren Hardwarefehlern (z. B. Festplattenabsturz).
    - **Versehentliches Löschen/Ändern:** Wiederherstellung von Dateien, die versehentlich entfernt oder geändert wurden.
    - **Schutz vor Malware:** Wiederherstellung sauberer Daten nach einem Ransomware-Angriff oder anderen Malware-Vorfällen.
    - **Datenintegrität:** Sicherstellen, dass im Falle einer Datenbeschädigung eine bekannt gute Kopie der Daten verfügbar ist.
- **Gängige Sicherungsarten (Konzept):**
    
    - **Vollständige Sicherung:** Kopiert alle ausgewählten Daten. Sie ist am einfachsten wiederherzustellen, verbraucht aber den meisten Speicherplatz und die meiste Zeit.
    - **Inkrementelle Sicherung:** Kopiert nur die Daten, die sich seit der _letzten Sicherung_ (vollständig oder inkrementell) geändert haben. Schnellere Sicherung, weniger Speicherplatzbedarf, aber die Wiederherstellung kann komplizierter sein (erfordert die letzte vollständige Sicherung und alle nachfolgenden inkrementellen Sicherungen).
    - **Differenzielle Sicherung:** Kopiert nur die Daten, die sich seit der _letzten vollständigen Sicherung_ geändert haben. Schneller wiederherstellbar als inkrementelle Sicherungen (erfordert nur die letzte Vollsicherung und die letzte differenzielle Sicherung), aber die Sicherungsgröße wächst mit der Zeit bis zur nächsten Vollsicherung.
    

    ![[Pasted image 20250929202018.png]]
    
- - Erweitern oder Verkleinern von Partitionen (mit Einschränkungen).
**Backup-Medien und Speicherorte:**
    
    - **Externe Festplatten/SSDs:** Üblich für persönliche Backups.
    - **Network Attached Storage (NAS):** Zentraler Speicher in einem lokalen Netzwerk.
    - **Cloud-Speicher:** Dienste wie OneDrive, Google Drive, iCloud oder spezielle Sicherungsdienste (z. B. Backblaze, Carbonite). Bietet Schutz außerhalb des Standorts.
- **Windows-Backup-Tools:** Windows enthält integrierte Dienstprogramme:
    
    - **Dateiverlauf:** Sichert regelmäßig die Versionen der Dateien in den Ordnern "Bibliotheken", "Schreibtisch", "Kontakte" und "Favoriten" auf einem externen Laufwerk oder im Netzwerk.
    - **Sichern und Wiederherstellen (Windows 7):** Ein eher traditionelles Tool, das Systemabbildsicherungen und Datei-/Ordnersicherungen ermöglicht. Auch in neueren Windows-Versionen verfügbar.

### Speicherverschlüsselung

**Verschlüsselung** wandelt Daten in ein unlesbares Format (Chiffretext) um, das nur mit einem bestimmten Schlüssel entschlüsselt werden kann. Die Speicherverschlüsselung schützt die Vertraulichkeit der Daten und stellt sicher, dass selbst wenn Unbefugte physischen Zugang zum Speichergerät erhalten, sie die Daten nicht lesen können.

- **Full-Disk Encryption (FDE):**
    - Verschlüsselt das gesamte Speichervolumen (z. B. eine gesamte Festplatte oder SSD-Partition).
    - Die Daten werden automatisch verschlüsselt, wenn sie geschrieben werden, und entschlüsselt, wenn sie gelesen werden, und zwar transparent für den Benutzer (nach der ersten Authentifizierung).
    - **BitLocker Drive Encryption:** Microsofts FDE-Lösung, die in die professionellen und Unternehmensversionen von Windows integriert ist. Sie kann das Betriebssystem-Volume und andere Datenvolumes verschlüsseln. Verwendet häufig einen Trusted Platform Module (TPM)-Chip für erhöhte Sicherheit.
    - Sehr effektiv gegen Datendiebstahl von verlorenen oder gestohlenen Laptops oder Laufwerken.
- **Datei-/Ordnerverschlüsselung:**
    - Verschlüsselt einzelne Dateien oder bestimmte Ordner und nicht die gesamte Festplatte.
    - Verschlüsselndes Dateisystem (EFS):** Eine Funktion von NTFS (Windows), mit der Benutzer Dateien und Ordner verschlüsseln können. Die Verschlüsselung ist an das Konto des Benutzers gebunden. Wenn ein unbefugter Benutzer auf das System zugreift oder die verschlüsselte Datei an einen anderen Ort kopiert, kann er sie nicht ohne die Anmeldedaten des ursprünglichen Benutzers oder den Wiederherstellungsschlüssel öffnen.
    - Nützlich für den Schutz bestimmter sensibler Dateien auf einem gemeinsam genutzten System oder für eine zusätzliche Sicherheitsebene.
- **Warum Verschlüsselung wichtig ist:**
    - **Vertraulichkeit:** Schützt sensible Daten vor unbefugtem Zugriff, insbesondere auf tragbaren Geräten (Laptops, USB-Laufwerke).
    - **Compliance:** Viele Vorschriften (z. B. GDPR, HIPAA) verlangen oder empfehlen Verschlüsselung zum Schutz persönlicher oder sensibler Daten.
    - **Schutz vor Datenschutzverletzungen:** Wenn ein verschlüsseltes Gerät gestohlen wird, bleiben die Daten geschützt, was die Auswirkungen der Datenschutzverletzung verringert.

## Windows-Besonderheiten

Da Sie in diesem Programm viel mit Windows arbeiten werden, wollen wir auf einige spezielle Aspekte eingehen:

- **Laufwerksbuchstaben:** Windows verwendet Laufwerksbuchstaben (z. B. `C:`, `D:`, `E:`), um Datenträger darzustellen. Das Laufwerk `C:` ist normalerweise das primäre Systemlaufwerk, auf dem Windows installiert ist.
- **Datei-Explorer:** Dies ist das wichtigste grafische Werkzeug zum Navigieren und Verwalten von Dateien und Ordnern in Windows. Sie können Dateieigenschaften anzeigen, Ordner erstellen, Dateien kopieren/verschieben/löschen, usw.
- **Festplattenverwaltung:** Ein integriertes Windows-Dienstprogramm ("diskmgmt.msc"), mit dem Sie Festplatten und Datenträger anzeigen und verwalten können. Sie können es verwenden, um:
    - Partitionen und deren Dateisysteme anzeigen.
    - Partitionen erstellen, löschen und **formatieren**.
    - Laufwerksbuchstaben ändern.
    
![[Pasted image 20250929202029.png]]

### Windows C:\ Laufwerk Verzeichnisstruktur

Dieses Bild ist ein hierarchisches Diagramm, das die Ordnerstruktur des Laufwerks C:\ in einem Windows-Betriebssystem veranschaulicht. Es zeigt wichtige Verzeichnisse wie Programme, Windows und temp mit Unterordnern wie Common Files, system32 und Microsoft Office.

![[Pasted image 20250929202046.png]]

### Versuchen Sie es selbst

1. **Datei-Explorer öffnen:**
    - Öffnen Sie den Datei-Explorer auf Ihrer Windows-VM.
    - Identifizieren Sie die vorhandenen Laufwerksbuchstaben.
    - Navigieren Sie zu gängigen Systemordnern wie "C:\\Windows", "C:\\Programme" und "C:\\Benutzer"[IhrBenutzername]\\Dokumente".
2. **Dateieigenschaften prüfen:**
    - Suchen Sie eine beliebige Datei. Klicken Sie mit der rechten Maustaste und wählen Sie "Eigenschaften".
    - Untersuchen Sie die Registerkarten **Allgemein** (Typ, Speicherort, Größe, Attribute) und **Details** (Metadaten).
    - Wenn Sie ein NTFS-Volume haben, suchen Sie die Registerkarte **Sicherheit**, um die Berechtigungen zu sehen.
3. **Sicherungs- und Verschlüsselungsoptionen suchen (nur Erkundung):**
    - Geben Sie in der Windows-Suchleiste "Dateiverlauf" ein und öffnen Sie das Programm, um die Schnittstelle zu sehen (Sie brauchen es jetzt nicht zu konfigurieren).
    - Suchen Sie nach "BitLocker" (Verwalten von BitLocker). Wenn Ihre Windows-Version dies unterstützt, sehen Sie Optionen, um es für Laufwerke zu aktivieren. Aktivieren Sie BitLocker nur dann, wenn Sie damit vertraut sind und Wiederherstellungsschlüssel gesichert haben.
4. **Erkunden Sie die Datenträgerverwaltung (nur Erkundung):**
    - Drücken Sie "Windows-Taste + R", geben Sie "diskmgmt.msc" ein, und drücken Sie die Eingabetaste.
    - Beobachten Sie das Layout. Sie sehen Ihre physische(n) Festplatte(n) und die darauf befindlichen Partitionen/Volumes. Beachten Sie deren Dateisysteme.
    - Nehmen Sie hier keine Änderungen vor, wenn Sie sich nicht sicher sind, was Sie tun. Dieses Tool ist sehr leistungsfähig und eine falsche Verwendung kann zu Datenverlust führen. Beobachten Sie es vorerst einfach.

### Denken Sie darüber nach

- Wenn Sie eine sehr wichtige Projektdatei haben, würden Sie sich dann ausschließlich auf die Festplatte Ihres Computers verlassen, um sie zu speichern? Welche Sicherungsstrategie würden Sie in Betracht ziehen und warum?
- Wenn Sie eine Datei "löschen" (auch wenn Sie den Papierkorb leeren), sind die Daten dann sofort weg? In welchem Zusammenhang steht dies mit Dateisystemoperationen und der Möglichkeit der Datenwiederherstellung? Wie wirkt sich das "Formatieren" eines Laufwerks normalerweise auf die vorhandenen Daten aus?
- Was sind die Hauptvorteile der Verwendung einer Festplattenverschlüsselung wie BitLocker auf einem Firmenlaptop? Gibt es irgendwelche potenziellen Nachteile oder Überlegungen?

Diese Vorbereitung wird Ihnen eine solide Grundlage für unsere Live-Sitzung bieten, in der wir diese Konzepte vertiefen und in der Praxis erleben werden.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-9-File-Systems-Storage-6xaft3qrxy5p20f?mode=doc](https://gamma.app/docs/Operating-Systems-9-File-Systems-Storage-6xaft3qrxy5p20f?mode=doc)

Try not to peek before class - spoilers inside!

</aside>