Willkommen zu Ihrer Einführung in die Windows-Registrierung! Sie ist eine wichtige Komponente des Windows-Betriebssystems, und das Verständnis ihrer Struktur und ihres Zwecks ist für viele Aufgaben im Bereich der Cybersicherheit von entscheidender Bedeutung, von der digitalen Forensik bis zur Systemhärtung.

## Was ist die Windows-Registrierung?

Stellen Sie sich die Windows-Registrierung als das zentrale Nervensystem oder als eine riesige, hierarchische Datenbank für Ihr Windows-Betriebssystem vor. Sie speichert eine große Menge an Konfigurationseinstellungen und Optionen für das Betriebssystem selbst, für Hardwaregeräte, Softwareanwendungen, Benutzereinstellungen und Systemrichtlinien. Jedes Mal, wenn Sie ein neues Programm installieren, den Desktophintergrund ändern oder ein neues USB-Laufwerk anschließen, wird die Registrierung wahrscheinlich mit neuen Informationen aktualisiert.

Die Registrierung wurde erstmals mit Windows 3.1 eingeführt und ist seither ein zentraler Bestandteil jeder Windows-Version. Sie ersetzte das ältere, weniger zentralisierte System, bei dem zahlreiche INI-Dateien (Initialisierungsdateien) zum Speichern von Einstellungen verwendet wurden.

**Zu den wichtigsten Funktionen der Registry gehören:**

- Speichern der Hardwarekonfiguration (z. B. welche Treiber für welche Geräte geladen werden sollen).
- Verwaltung von Softwareeinstellungen (z. B. Installationspfade, Benutzereinstellungen für Anwendungen).
- Steuerung von Benutzerprofilen und -einstellungen (z. B. Aussehen des Desktops, Spracheinstellungen).
- Pflege von Einstellungen auf Systemebene (z. B. Boot-Parameter, Sicherheitsrichtlinien).

Da sie so wichtige Informationen enthält, ist die Registrierung ein häufiges Ziel für Malware und eine Fundgrube für forensische Ermittler.

![[Pasted image 20251002113452.png]]

## Struktur der Registrierung

Die Registry ist nicht nur eine riesige Datei, sondern eine komplexe Struktur aus mehreren Dateien, die "Hives" genannt werden und in den Speicher geladen werden, wenn das System hochfährt oder sich ein Benutzer anmeldet. Die Struktur, mit der Sie interagieren (z. B. über den Registrierungseditor), ist eine logische, hierarchische Ansicht dieser Hives.

Diese Hierarchie besteht aus:

1. **Root Keys (oder vordefinierte Schlüssel/Handles):** Dies sind die obersten Container in der Registrierung. Es gibt fünf Haupt-Root Keys, die oft mit "HK" abgekürzt werden:
    - **`HKEY_CLASSES_ROOT` (HKCR):** Enthält Informationen über Dateiverknüpfungen (z. B. welches Programm eine "txt"-Datei öffnet), OLE-Daten (Object Linking and Embedding) und COM-Objektregistrierungen. Dieser Schlüssel ist eigentlich eine kombinierte Ansicht von `HKEY_LOCAL_MACHINE\\Software\\Classes` und `HKEY_CURRENT_USER\\Software\Classes`.
    - **`HKEY_CURRENT_USER` (HKCU):** Speichert Einstellungen, die für den aktuell angemeldeten Benutzer spezifisch sind. Dazu gehören Dinge wie der Desktophintergrund, der Bildschirmschoner, die Anwendungseinstellungen und die Einstellungen für die Ordneransicht. Dies ist ein Zeiger auf einen Unterschlüssel innerhalb von `HKEY_USERS`, der der Sicherheitskennung (SID) des aktuellen Benutzers entspricht.
    - **`HKEY_LOCAL_MACHINE` (HKLM):** Enthält Konfigurationsinformationen für den lokalen Computer, unabhängig davon, wer angemeldet ist. Dazu gehören Hardwareeinstellungen (Treiber, Geräte), systemweite Softwareeinstellungen und Betriebssystemkonfigurationen. Dies ist eine der kritischsten Hives.
    - **`HKEY_USERS` (HKU):** Enthält Benutzerprofile für alle Benutzer, die sich auf dem Computer angemeldet haben, sowie ein Standardprofil. Das Profil eines jeden Benutzers wird unter seiner SID gespeichert. HKEY_CURRENT_USER" ist hier ein Link zum spezifischen SID-Unterschlüssel des aktuellen Benutzers.
    - **`HKEY_CURRENT_CONFIG` (HKCC):** Hier werden Informationen über das Hardwareprofil gespeichert, das der lokale Computer beim Start verwendet. Dies ist im Allgemeinen ein Zeiger auf einen Unterschlüssel innerhalb von `HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Hardware Profiles\\Current`.
2. **Schlüssel und Unterschlüssel:** Innerhalb jedes Stammschlüssels gibt es "Schlüssel", die mit Ordnern in einem Dateisystem vergleichbar sind. Schlüssel können andere Schlüssel (sogenannte "Unterschlüssel") enthalten, wodurch eine baumartige Struktur entsteht. Diese Organisation hilft dabei, zusammengehörige Einstellungen logisch zu gruppieren. Sie können zum Beispiel einen Schlüssel für eine bestimmte Softwareanwendung finden und innerhalb dieses Schlüssels Unterschlüssel für die verschiedenen Komponenten oder Einstellungen.
3. **Werte:** In den Schlüsseln und Unterschlüsseln werden die eigentlichen Konfigurationsdaten in "Werten" gespeichert. Jeder Wert besteht aus drei Teilen:
    - **Name:** Ein beschreibender Name für den Wert (z. B. "ScreenSaveTimeOut"). Ein Schlüssel kann einen "Standard"-Wert haben, der oft keinen expliziten Namen hat.
    - **Typ:** Der Datentyp der gespeicherten Information. Übliche Typen sind:
        - `REG_SZ`: Eine Textzeichenkette mit fester Länge.
        - `REG_EXPAND_SZ`: Ein erweiterbarer String, der Umgebungsvariablen enthalten kann (z.B. `%SystemRoot%`).
        - `REG_BINARY`: Rohe Binärdaten.
        - REG_DWORD`: Eine 32-Bit-Zahl.
        - REG_QWORD`: Eine 64-Bit-Zahl.
        - `REG_MULTI_SZ`: Ein Multi-String-Wert, mit dem mehrere Texteinträge in einem einzigen Wert gespeichert werden können.
    - **Data:** Der tatsächliche Inhalt der Einstellung (z. B. "600" für ein 10-minütiges Bildschirmschoner-Timeout oder "C:\Program Files\MyApp\app.exe" für einen Anwendungspfad).

![[Pasted image 20251002113605.png]]

## Register in der Cybersicherheit

Das Verständnis des Registers ist für die Cybersicherheit aus mehreren Gründen entscheidend:

- **Digitale Forensik:** Die Registry ist eine Fundgrube für Beweise. Ermittler können finden:
    - Zeitstempel für Schlüsseländerungen.
    - Listen kürzlich ausgeführter Programme (`RunMRU`).
    - Angeschlossene USB-Geräte.
    - Verlauf der Netzwerkverbindungen.
    - Benutzeraktivitäten und Kontoinformationen.
- **Malware-Analyse & Persistenz:** Malware nutzt die Registry häufig, um:
    - Persistenz zu erreichen: Durch Hinzufügen von Einträgen zu "Ausführen"-Schlüsseln (z. B. `HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run` oder `HKCU\\Software\\Microsoft\Windows\\CurrentVersion\\Run`) kann Malware sicherstellen, dass sie bei jedem Systemstart oder bei der Anmeldung eines Benutzers automatisch gestartet wird.
    - Eigene Konfigurationsdaten speichern.
    - Sicherheitssoftware deaktivieren oder das Systemverhalten ändern.
    - Seine Anwesenheit verbergen.
- **Systemhärtung und Konfigurationsmanagement:** Sicherheitsexperten ändern die Einstellungen der Registrierung, um:
    - Verbesserung der Sicherheit durch Deaktivierung unnötiger Dienste oder Funktionen.
    - Sicherheitsrichtlinien durchzusetzen.
    - Protokollierung und Prüfung zu konfigurieren.
- **Reaktion auf einen Vorfall:** Während eines Vorfalls untersuchen die Mitarbeiter die Registrierung, um das Ausmaß einer Kompromittierung zu verstehen, die TTPs (Taktiken, Techniken und Verfahren) der Angreifer zu identifizieren und Indikatoren für eine Kompromittierung (IOCs) zu finden.
- **Schwachstellenbewertung:** Einige Schwachstellen können mit unzulässigen Registrierungsberechtigungen oder Konfigurationen zusammenhängen.

![[Pasted image 20251002113613.png]]

## Zugriff auf die Registry: Der Registrierungseditor (Regedit)

Windows bietet ein eingebautes Werkzeug, den Registrierungseditor (`regedit.exe`), um die Registrierung anzuzeigen und zu ändern.

**Wichtige Vorsicht:** Die Registry enthält wichtige Systemeinstellungen. **Eine falsche Änderung der Registrierung kann zu einer schweren Instabilität des Systems führen oder sogar verhindern, dass Ihr System hochfährt.** Bei dieser Vorbereitung werden Sie nur die Registrierung einsehen, aber nichts ändern. Seien Sie immer äußerst vorsichtig, wenn Sie Änderungen vornehmen müssen, und stellen Sie sicher, dass Sie ein Backup haben oder wissen, wie Sie die Einstellungen wiederherstellen können, falls etwas schief geht.

![[Pasted image 20251002113620.png]]

### Versuchen Sie es selbst: Erkundung mit Regedit

1. Drücken Sie auf Ihrer virtuellen Windows-Maschine die Tastenkombination "Windows-Taste + R", um das Dialogfeld Ausführen zu öffnen.
2. Geben Sie `regedit` ein und drücken Sie Enter oder klicken Sie auf OK.
3. Wenn eine Aufforderung zur Benutzerkontensteuerung (UAC) erscheint, klicken Sie auf "Ja".
4. Das Fenster des Registrierungseditors wird geöffnet. Im linken Bereich werden die Stammschlüssel aufgelistet, wie die Ordner im Datei-Explorer.
5. Versuchen Sie, zum folgenden Schlüssel zu navigieren: "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths".
    - Klicken Sie auf den Pfeil neben "HKEY_CURRENT_USER", um ihn zu erweitern.
    - Erweitern Sie dann `Software`, dann `Microsoft`, dann `Windows`, dann `CurrentVersion`, dann `Explorer`.
    - Klicken Sie schließlich auf den Schlüssel `TypedPaths`.
6. Beobachten Sie die Werte im rechten Fenster. Was sehen Sie? Dies sind Pfade, die Sie kürzlich in die Adressleiste des Datei-Explorers oder in das Dialogfeld Ausführen eingegeben haben.

Ändern Sie **keine** Werte. Beobachten Sie einfach. Schließen Sie den Registrierungseditor, wenn Sie fertig sind.

### Denken Sie darüber nach

Betrachten Sie die bereits erwähnten "Ausführen"-Schlüssel (z. B. "HKEY_LOCAL_MACHINE", "Software", "Microsoft", "Windows", "Aktuelle Version", "Ausführen"). Wenn Sie ein Malware-Autor wären, der möchte, dass sein Programm jedes Mal automatisch gestartet wird, wenn sich ein Benutzer am Computer anmeldet, welchen "Ausführen"-Schlüssel würden Sie anvisieren und warum? Was wäre, wenn Sie es nur für den aktuell infizierten Benutzer starten wollten?

Diese Vorbereitung wird Ihnen eine solide Grundlage für unsere Live-Sitzung bieten, in der wir uns eingehender mit der Funktionsweise der Registrierung, ihrer Verwendung (und ihrem Missbrauch) sowie ihrer Analyse aus der Perspektive der Cybersicherheit befassen werden.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-10-Registry-tb6lzgwcd0b2j8g?mode=doc](https://gamma.app/docs/Operating-Systems-10-Registry-tb6lzgwcd0b2j8g?mode=doc)

Try not to peek before class - spoilers inside!

</aside>