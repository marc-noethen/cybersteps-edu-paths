_Dissecting history's hacks: from headlines to Metasploit modules._

**Ziel**

Analyse eines offiziellen Berichts über einen bekannten Cyberangriff, Identifizierung der verwendeten Angriffsvektoren und Zuordnung zu potenziellen Testtools oder Modulen innerhalb des Metasploit Frameworks.

**Anleitungen**

1. **Lesen Sie den Target Data Breach Report:**
    - Lesen Sie den Bericht der Mitarbeiter des U.S.-Senatsausschusses: "[A 'Kill Chain' Analysis of the 2013 Target Data Breach.](https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883)"
    - Konzentrieren Sie sich darauf, die Abfolge der Ereignisse zu verstehen, wie sich die Angreifer zunächst Zugang verschafft haben, dann weiter vorgedrungen sind und schließlich die Daten exfiltriert haben. Achten Sie genau auf die erwähnten spezifischen Schwachstellen oder Techniken.
2. **Analysieren Sie den Bericht:**
    - Identifizieren Sie anhand des Berichts möglichst viele verschiedene primäre Angriffsvektoren oder Schlüsselmechanismen, die bei dem Datenmissbrauch durch Target eine zentrale Rolle gespielt haben.
    - Erläutern Sie für jeden identifizierten Vektor/Mechanismus, wie er auf der Grundlage der Informationen im Bericht zum Erfolg der Angreifer beigetragen hat.
3. **Verbindung zu Metasploit:**
    - Starten Sie `msfconsole` in Ihrer Kali VM.
    - Für jeden der beiden Vektoren/Mechanismen, die Sie im Target-Bericht identifiziert haben:
        - Überlegen Sie, um welche Art von Schwachstelle oder Technik es sich handelt.
        - Benutzen Sie den "search"-Befehl in "msfconsole", um ein Metasploit-Modul zu finden (es könnte ein "Exploit"-, "Auxiliary"- oder "Post"-Modul sein), das ein ethischer Hacker benutzen könnte, um eine ähnliche Art von Schwachstelle oder Angriffsphase zu _testen_, _zu simulieren_ oder _mit ihr zu interagieren_.
        - Notieren Sie den vollständigen Pfad des Metasploit-Moduls, das Sie gefunden haben, und erläutern Sie kurz, warum Sie glauben, dass dieses Modul konzeptionell für den im Zielbericht beschriebenen Vektor relevant ist. Sie brauchen keine Module auszuführen.

**Einreichung**

Reichen Sie ein Dokument ein, das Folgendes enthält:

1. Für jeden der von Ihnen identifizierten Angriffsvektoren/-mechanismen:
    - Eine klare Beschreibung des Vektors/Mechanismus, wie er bei dem Angriff auf das Ziel verwendet wurde.
    - Eine Erklärung, wie dieser Vektor/Mechanismus zu dem Vorfall beigetragen hat.
2. Für jeden identifizierten Vektor/Mechanismus:
    - Der vollständige Pfad des konzeptionell verwandten Metasploit-Moduls, das Sie gefunden haben.
    - Eine kurze Erklärung, warum Sie dieses Modul in Bezug auf den Vektor ausgewählt haben.
3. Ein Screenshot Ihrer `msfconsole`, der einen Ihrer `Suchbefehle` und dessen Ergebnisse zeigt.