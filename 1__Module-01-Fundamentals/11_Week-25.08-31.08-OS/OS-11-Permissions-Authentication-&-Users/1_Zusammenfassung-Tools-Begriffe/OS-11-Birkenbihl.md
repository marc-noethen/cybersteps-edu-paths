Welcome to the pre-class preparation for our lesson on Permissions, Authentication, and Users in Windows! Willkommen zur Vorbereitung vor dem Unterricht für unsere Lektion über Berechtigungen, Authentifizierung und Benutzer in Windows!

Understanding these concepts is fundamental to cybersecurity, as they control who can access what and what they can do with it. Das Verständnis dieser Konzepte ist grundlegend für die Cybersicherheit, da sie kontrollieren, wer auf was zugreifen kann und was damit getan werden kann.

This preparation will lay the groundwork for our live session. Diese Vorbereitung wird die Grundlage für unsere Live-Sitzung legen.

Users and Accounts Benutzer und Konten

In an operating system, a user represents an individual who can interact with the system. In einem Betriebssystem repräsentiert ein Benutzer eine Person, die mit dem System interagieren kann.

To manage this interaction, each user is typically assigned a user account. Um diese Interaktion zu verwalten, wird jedem Benutzer typischerweise ein Benutzerkonto zugewiesen.

This account is a collection of information that tells Windows who you are, what you can do, and what your preferences are. Dieses Konto ist eine Sammlung von Informationen, die Windows mitteilt, wer Sie sind, was Sie tun können und was Ihre Einstellungen sind.

There are primarily two types of user accounts you'll encounter on a standalone Windows machine. Es gibt hauptsächlich zwei Arten von Benutzerkonten, auf die Sie auf einem eigenständigen Windows-Computer stoßen werden.

Administrator Accounts: These accounts have full control over the computer. Administrator-Konten: Diese Konten haben die volle Kontrolle über den Computer.

They can install software and hardware, access all files on the system, change system settings, and manage other user accounts. Sie können Software und Hardware installieren, auf alle Dateien im System zugreifen, Systemeinstellungen ändern und andere Benutzerkonten verwalten.

It's powerful, and with great power comes great responsibility! Es ist mächtig, und mit großer Macht kommt große Verantwortung!

Running as an administrator all the time can be risky, as any malicious software that runs under an administrator account will also have full control. Die ganze Zeit als Administrator zu arbeiten kann riskant sein, da jede bösartige Software, die unter einem Administrator-Konto läuft, ebenfalls volle Kontrolle haben wird.

Standard User Accounts: These accounts have limited privileges. Standard-Benutzerkonten: Diese Konten haben eingeschränkte Privilegien.

They can run applications and change settings that affect only their own account, but they cannot perform system-wide changes like installing most software, modifying critical system files, or changing settings for other users without providing credentials for an administrator account. Sie können Anwendungen ausführen und Einstellungen ändern, die nur ihr eigenes Konto betreffen, aber sie können keine systemweiten Änderungen vornehmen, wie die Installation der meisten Software, das Ändern kritischer Systemdateien oder das Ändern von Einstellungen für andere Benutzer, ohne Anmeldeinformationen für ein Administrator-Konto bereitzustellen.

This is the recommended account type for daily use. Dies ist der empfohlene Kontotyp für die tägliche Nutzung.

Windows also has built-in accounts like SYSTEM, Local Service, and Network Service which are used by the operating system and services, but you typically don't log in with these directly. Windows hat auch integrierte Konten wie SYSTEM, Local Service und Network Service, die vom Betriebssystem und Diensten verwendet werden, aber Sie melden sich normalerweise nicht direkt mit diesen an.

These accounts have specific, often highly privileged, purposes for running background tasks and services. Diese Konten haben spezifische, oft hochprivilegierte Zwecke für die Ausführung von Hintergrundaufgaben und Diensten.

User Groups Benutzergruppen

To simplify the management of permissions, Windows uses user groups. Um die Verwaltung von Berechtigungen zu vereinfachen, verwendet Windows Benutzergruppen.

Instead of assigning permissions to each user individually, you can assign permissions to a group, and then add users to that group. Anstatt jedem Benutzer einzeln Berechtigungen zuzuweisen, können Sie Berechtigungen einer Gruppe zuweisen und dann Benutzer zu dieser Gruppe hinzufügen.

All users in the group inherit the permissions assigned to the group. Alle Benutzer in der Gruppe erben die der Gruppe zugewiesenen Berechtigungen.

This makes managing access much more efficient, especially when dealing with many users. Dies macht die Verwaltung des Zugriffs viel effizienter, besonders wenn man mit vielen Benutzern zu tun hat.

Common default groups in Windows include: Administrators. Members have full, unrestricted control of the computer. Häufige Standardgruppen in Windows sind: Administratoren. Mitglieder haben volle, uneingeschränkte Kontrolle über den Computer.

Users. Members can perform common tasks like running applications and managing their own files, but are prevented from making system-wide changes or modifying files belonging to other users unless explicitly permitted. Benutzer. Mitglieder können alltägliche Aufgaben wie das Ausführen von Anwendungen und das Verwalten ihrer eigenen Dateien durchführen, werden aber daran gehindert, systemweite Änderungen vorzunehmen oder Dateien anderer Benutzer zu ändern, es sei denn, dies wird ausdrücklich erlaubt.

Guests. Members have temporary access with very limited rights. This group is often disabled by default for security reasons. Gäste. Mitglieder haben temporären Zugriff mit sehr eingeschränkten Rechten. Diese Gruppe ist aus Sicherheitsgründen oft standardmäßig deaktiviert.

Backup Operators. Members can back up and restore files on the computer, regardless of their individual file permissions. Sicherungsoperatoren. Mitglieder können Dateien auf dem Computer sichern und wiederherstellen, unabhängig von ihren individuellen Dateiberechtigungen.

This is necessary for backup software to function correctly. Dies ist notwendig, damit Sicherungssoftware korrekt funktioniert.

Remote Desktop Users. Members are permitted to log in to the computer remotely using Remote Desktop. Remotedesktop-Benutzer. Mitglieder dürfen sich aus der Ferne über Remotedesktop am Computer anmelden.

Try it yourself Versuchen Sie es selbst

On your Windows virtual machine, press Windows key plus R to open the Run dialog. Drücken Sie auf Ihrer virtuellen Windows-Maschine die Windows-Taste plus R, um das Dialogfeld Ausführen zu öffnen.

Type compmgmt dot msc and press Enter. This opens Computer Management. Geben Sie compmgmt Punkt msc ein und drücken Sie Enter. Dies öffnet die Computerverwaltung.

In the left pane, navigate to System Tools, Local Users and Groups, Groups. Im linken Bereich navigieren Sie zu Systemtools, Lokale Benutzer und Gruppen, Gruppen.

Observe the list of built-in groups. You can double-click a group to see its members, though some system groups might not show members easily here or might be managed differently. Beobachten Sie die Liste der integrierten Gruppen. Sie können auf eine Gruppe doppelklicken, um ihre Mitglieder zu sehen, obwohl einige Systemgruppen ihre Mitglieder hier möglicherweise nicht einfach anzeigen oder anders verwaltet werden.

Don't make any changes. Nehmen Sie keine Änderungen vor.

Think about it Denken Sie darüber nach

Why is it generally a bad idea to use an Administrator account for everyday tasks like browsing the internet or checking emails? Warum ist es im Allgemeinen eine schlechte Idee, ein Administrator-Konto für alltägliche Aufgaben wie das Surfen im Internet oder das Überprüfen von E-Mails zu verwenden?

If you needed to install a new trusted application, what would you expect to happen if you were logged in as a Standard User? Wenn Sie eine neue vertrauenswürdige Anwendung installieren müssten, was würden Sie erwarten, wenn Sie als Standard-Benutzer angemeldet wären?

Authentication: Who Are You? Authentifizierung: Wer sind Sie?

Authentication is the process of verifying the identity of a user, process, or device. Authentifizierung ist der Prozess der Überprüfung der Identität eines Benutzers, Prozesses oder Geräts.

It's like showing your ID to prove you are who you say you are before you're allowed into a restricted area. Es ist wie das Vorzeigen Ihres Ausweises, um zu beweisen, dass Sie sind, wer Sie sagen, dass Sie sind, bevor Sie in einen eingeschränkten Bereich gelassen werden.

Common authentication methods include: Passwords. The most common form of authentication. Häufige Authentifizierungsmethoden sind: Passwörter. Die häufigste Form der Authentifizierung.

A secret string of characters that only the user should know. Strong passwords are long, complex, and unique. Eine geheime Zeichenfolge, die nur der Benutzer kennen sollte. Starke Passwörter sind lang, komplex und einzigartig.

PINs, or Personal Identification Numbers. Often used for quick access, especially with Windows Hello. PINs, oder persönliche Identifikationsnummern. Oft verwendet für schnellen Zugriff, besonders mit Windows Hello.

Shorter than passwords but usually tied to a specific device, offering a balance of convenience and security for device login. Kürzer als Passwörter, aber normalerweise an ein bestimmtes Gerät gebunden, was eine Balance zwischen Komfort und Sicherheit für die Geräteanmeldung bietet.

Biometrics. Uses unique physical characteristics. Examples include fingerprint scanners, facial recognition like Windows Hello, and iris scanners. Biometrie. Verwendet einzigartige physische Merkmale. Beispiele sind Fingerabdruckscanner, Gesichtserkennung wie Windows Hello und Iris-Scanner.

Smart Cards or Security Keys. Physical devices that must be present to authenticate, often used in corporate environments for stronger security. Smart Cards oder Sicherheitsschlüssel. Physische Geräte, die zur Authentifizierung vorhanden sein müssen, oft in Unternehmensumgebungen für stärkere Sicherheit verwendet.

Multi-Factor Authentication, or MFA. Enhances security by requiring two or more different authentication factors. Multi-Faktor-Authentifizierung, oder MFA. Erhöht die Sicherheit, indem zwei oder mehr verschiedene Authentifizierungsfaktoren erforderlich sind.

For example, something you know, like a password, AND something you have, like a code from an authenticator app on your phone or a security key, AND or OR something you are, like biometric. Zum Beispiel etwas, das Sie wissen, wie ein Passwort, UND etwas, das Sie haben, wie einen Code aus einer Authentifizierungs-App auf Ihrem Telefon oder einen Sicherheitsschlüssel, UND oder ODER etwas, das Sie sind, wie Biometrie.

When you log into Windows, you're undergoing an authentication process. Wenn Sie sich bei Windows anmelden, durchlaufen Sie einen Authentifizierungsprozess.

The system compares the credentials you provide, for example username and password, against its local security database, the Security Account Manager or SAM file, or in a domain environment against a central directory like Active Directory. Das System vergleicht die von Ihnen bereitgestellten Anmeldeinformationen, zum Beispiel Benutzername und Passwort, mit seiner lokalen Sicherheitsdatenbank, dem Security Account Manager oder der SAM-Datei, oder in einer Domänenumgebung mit einem zentralen Verzeichnis wie Active Directory.

Try it yourself Versuchen Sie es selbst

Review your current Windows login method on your virtual machine. Are you using a password, PIN, or is Windows Hello configured, if your virtual machine environment supports it? Überprüfen Sie Ihre aktuelle Windows-Anmeldemethode auf Ihrer virtuellen Maschine. Verwenden Sie ein Passwort, eine PIN, oder ist Windows Hello konfiguriert, falls Ihre Umgebung der virtuellen Maschine dies unterstützt?

No need to change anything, just observe. Sie müssen nichts ändern, beobachten Sie einfach.

Think about the websites or apps you use that offer MFA. Why do they offer it, especially for sensitive accounts like banking or email? Denken Sie über die Websites oder Apps nach, die Sie verwenden und die MFA anbieten. Warum bieten sie es an, besonders für sensible Konten wie Banking oder E-Mail?

Permissions: What Can You Do? Berechtigungen: Was können Sie tun?

Once a user is authenticated, permissions, also known as authorizations, determine what resources the user can access and what actions they can perform on those resources. Sobald ein Benutzer authentifiziert ist, bestimmen Berechtigungen, auch bekannt als Autorisierungen, auf welche Ressourcen der Benutzer zugreifen kann und welche Aktionen er mit diesen Ressourcen durchführen kann.

Resources can include files, folders, printers, registry keys, and other system objects. Ressourcen können Dateien, Ordner, Drucker, Registrierungsschlüssel und andere Systemobjekte umfassen.

Permissions are crucial for protecting data and maintaining system stability. Berechtigungen sind entscheidend für den Schutz von Daten und die Aufrechterhaltung der Systemstabilität.

They ensure that users can only access the information they need and cannot accidentally or intentionally damage the system or compromise sensitive data. Sie stellen sicher, dass Benutzer nur auf die Informationen zugreifen können, die sie benötigen, und nicht versehentlich oder absichtlich das System beschädigen oder sensible Daten gefährden können.

The Principle of Least Privilege Das Prinzip der geringsten Privilegien

This is a core security concept. It states that a user or process should only be granted the minimum level of access, or permissions, necessary to perform its legitimate functions. Dies ist ein grundlegendes Sicherheitskonzept. Es besagt, dass einem Benutzer oder Prozess nur das Mindestmaß an Zugriff oder Berechtigungen gewährt werden sollte, das zur Ausführung seiner legitimen Funktionen erforderlich ist.

For example, if a user only needs to read documents in a specific folder, they should not be given write or delete permissions for that folder. Wenn ein Benutzer beispielsweise nur Dokumente in einem bestimmten Ordner lesen muss, sollten ihm keine Schreib- oder Löschberechtigungen für diesen Ordner gegeben werden.

Adhering to this principle significantly reduces the potential damage from errors, malware, or compromised accounts. Die Einhaltung dieses Prinzips reduziert erheblich den potenziellen Schaden durch Fehler, Malware oder kompromittierte Konten.

File and Folder Permissions, or NTFS Permissions Datei- und Ordnerberechtigungen, oder NTFS-Berechtigungen

Windows uses the NT File System, or NTFS, which supports a rich set of permissions for files and folders. Windows verwendet das NT-Dateisystem, oder NTFS, das eine umfangreiche Reihe von Berechtigungen für Dateien und Ordner unterstützt.

These permissions can be very granular, allowing for precise control over access. Diese Berechtigungen können sehr detailliert sein und eine präzise Kontrolle über den Zugriff ermöglichen.

Common NTFS permissions include: Full Control. Allows users to read, write, modify, execute, change attributes, delete files and subfolders, and take ownership. Häufige NTFS-Berechtigungen umfassen: Vollzugriff. Ermöglicht Benutzern zu lesen, zu schreiben, zu ändern, auszuführen, Attribute zu ändern, Dateien und Unterordner zu löschen und den Besitz zu übernehmen.

Modify. Allows users to read, write, modify, execute, and delete. Ändern. Ermöglicht Benutzern zu lesen, zu schreiben, zu ändern, auszuführen und zu löschen.

Read and Execute. Allows users to display folder contents, read files, and run executable files or applications. Lesen und Ausführen. Ermöglicht Benutzern, Ordnerinhalte anzuzeigen, Dateien zu lesen und ausführbare Dateien oder Anwendungen auszuführen.

List Folder Contents. For folders, allows users to see the names of files and subfolders within a folder. Does not grant access to the files themselves. Ordnerinhalt auflisten. Für Ordner ermöglicht es Benutzern, die Namen von Dateien und Unterordnern innerhalb eines Ordners zu sehen. Gewährt keinen Zugriff auf die Dateien selbst.

Read. Allows users to open and view files and their attributes, like creation date and size. Lesen. Ermöglicht Benutzern, Dateien und ihre Attribute zu öffnen und anzuzeigen, wie Erstellungsdatum und Größe.

Write. Allows users to create new files and subfolders within a folder, write data to files, and append to files. Schreiben. Ermöglicht Benutzern, neue Dateien und Unterordner innerhalb eines Ordners zu erstellen, Daten in Dateien zu schreiben und an Dateien anzuhängen.

These permissions can be set to Allow or Deny. Importantly, Deny permissions usually override Allow permissions. Diese Berechtigungen können auf Zulassen oder Verweigern gesetzt werden. Wichtig ist, dass Verweigern-Berechtigungen normalerweise Zulassen-Berechtigungen überschreiben.

This means if a user is a member of two groups, one that is allowed access and another that is denied access to the same resource, the user will typically be denied. Das bedeutet, wenn ein Benutzer Mitglied von zwei Gruppen ist, eine, der Zugriff gewährt wird, und eine andere, der der Zugriff auf dieselbe Ressource verweigert wird, wird dem Benutzer normalerweise der Zugriff verweigert.

This is a key concept in troubleshooting access issues. Dies ist ein Schlüsselkonzept bei der Fehlersuche bei Zugriffsproblemen.

Try it yourself Versuchen Sie es selbst

On your Windows virtual machine, open File Explorer and navigate to your Desktop. Öffnen Sie auf Ihrer virtuellen Windows-Maschine den Datei-Explorer und navigieren Sie zu Ihrem Desktop.

Right-click in an empty space and select New, Text Document. Name it MyTestFile dot txt. Klicken Sie mit der rechten Maustaste in einen leeren Bereich und wählen Sie Neu, Textdokument. Benennen Sie es MyTestFile Punkt txt.

Right-click on MyTestFile dot txt and select Properties. Klicken Sie mit der rechten Maustaste auf MyTestFile Punkt txt und wählen Sie Eigenschaften.

Go to the Security tab. Gehen Sie zum Sicherheits-Tab.

Observe the list under Group or user names. Select different users or groups, for example your current user account, the Administrators group, the SYSTEM account, and see how the permissions listed below, like Full control, Read, Write, change. Beobachten Sie die Liste unter Gruppe oder Benutzernamen. Wählen Sie verschiedene Benutzer oder Gruppen aus, zum Beispiel Ihr aktuelles Benutzerkonto, die Administratoren-Gruppe, das SYSTEM-Konto, und sehen Sie, wie sich die unten aufgeführten Berechtigungen, wie Vollzugriff, Lesen, Schreiben, ändern.

Notice the checkmarks in the Allow or Deny columns. Beachten Sie die Häkchen in den Spalten Zulassen oder Verweigern.

Optional: Click the Advanced button for a more detailed view. Here you can see permissions entries, inheritance, and the owner of the file. Optional: Klicken Sie auf die Schaltfläche Erweitert für eine detailliertere Ansicht. Hier können Sie Berechtigungseinträge, Vererbung und den Besitzer der Datei sehen.

Do not make any changes, just explore the interface. Nehmen Sie keine Änderungen vor, erkunden Sie einfach die Benutzeroberfläche.

Ownership Besitz

In Windows, every file and folder, and other system objects, has an owner. In Windows hat jede Datei und jeder Ordner und andere Systemobjekte einen Besitzer.

The owner is typically the user account that created the object. Der Besitzer ist normalerweise das Benutzerkonto, das das Objekt erstellt hat.

The owner of an object has a special status. They can always change the permissions for that object, even if they have been denied all other access through permission settings. Der Besitzer eines Objekts hat einen besonderen Status. Er kann immer die Berechtigungen für dieses Objekt ändern, selbst wenn ihm aller anderer Zugriff durch Berechtigungseinstellungen verweigert wurde.

This ensures that someone always has control over an object to fix permission misconfigurations. Dies stellt sicher, dass immer jemand die Kontrolle über ein Objekt hat, um Fehlkonfigurationen von Berechtigungen zu beheben.

Taking ownership is an administrative privilege that allows an administrator to seize ownership of a file or folder, often necessary for accessing objects created by other users or by the system. Besitz übernehmen ist ein administratives Privileg, das es einem Administrator ermöglicht, den Besitz einer Datei oder eines Ordners zu übernehmen, oft notwendig für den Zugriff auf Objekte, die von anderen Benutzern oder vom System erstellt wurden.

User Account Control, or UAC Benutzerkontensteuerung, oder UAC

You've likely encountered User Account Control, or UAC, in Windows. Sie sind wahrscheinlich auf die Benutzerkontensteuerung, oder UAC, in Windows gestoßen.

It's the feature that dims your screen and asks for confirmation, or administrator credentials, before allowing an application to make changes that could affect your computer's settings or files, for example installing software or changing system-wide settings. Es ist die Funktion, die Ihren Bildschirm abdunkelt und um Bestätigung oder Administrator-Anmeldeinformationen bittet, bevor sie einer Anwendung erlaubt, Änderungen vorzunehmen, die die Einstellungen oder Dateien Ihres Computers beeinflussen könnten, zum Beispiel Software zu installieren oder systemweite Einstellungen zu ändern.

UAC helps enforce the principle of least privilege, even for administrator accounts. UAC hilft, das Prinzip der geringsten Privilegien durchzusetzen, selbst für Administrator-Konten.

When an administrator logs in, most of their applications run with standard user privileges by default, using a filtered token. Wenn sich ein Administrator anmeldet, laufen die meisten seiner Anwendungen standardmäßig mit Standard-Benutzer-Privilegien, unter Verwendung eines gefilterten Tokens.

Only when an action requires administrative privileges does UAC prompt for elevation. Nur wenn eine Aktion administrative Privilegien erfordert, fordert UAC zur Erhöhung auf.

This elevation process grants the application the full administrator privileges for that specific task. Dieser Erhöhungsprozess gewährt der Anwendung die vollen Administrator-Privilegien für diese spezifische Aufgabe.

This helps prevent malicious software from silently gaining administrative control. Dies hilft zu verhindern, dass bösartige Software stillschweigend administrative Kontrolle erlangt.

Think about it Denken Sie darüber nach

Consider a shared folder in a company. Why would it be important to set different permissions for different groups of users, for example Accountants versus Interns? Betrachten Sie einen gemeinsamen Ordner in einem Unternehmen. Warum wäre es wichtig, verschiedene Berechtigungen für verschiedene Benutzergruppen festzulegen, zum Beispiel Buchhalter versus Praktikanten?

How does UAC contribute to the security of a Windows system even when you are logged in as an administrator? Wie trägt UAC zur Sicherheit eines Windows-Systems bei, selbst wenn Sie als Administrator angemeldet sind?

That's it for your pre-class preparation! Das war's für Ihre Vorbereitung vor dem Unterricht!

By understanding these core concepts of users, authentication, and permissions, and by familiarizing yourself with where to find these settings in Windows, you'll be well-prepared for our interactive session. Indem Sie diese Kernkonzepte von Benutzern, Authentifizierung und Berechtigungen verstehen und sich damit vertraut machen, wo Sie diese Einstellungen in Windows finden, werden Sie gut vorbereitet für unsere interaktive Sitzung sein.

We'll explore these topics in more detail and see them in action. Wir werden diese Themen ausführlicher untersuchen und sie in Aktion sehen.

The slides for the live session can be viewed here at this link. Try not to peek before class, spoilers inside! Die Folien für die Live-Sitzung können hier unter diesem Link angesehen werden. Versuchen Sie nicht vor dem Unterricht zu spicken, Spoiler enthalten!