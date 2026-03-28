_Ich muss sie alle finden! (Das heißt, die richtigen Exploit-Module)._

**Ziel**

Üben der Verwendung von `msfconsole`, um detaillierte Informationen über Metasploit-Module im Zusammenhang mit bestimmten Schwachstellen oder Aufgaben zu finden und zu erhalten.

**Anweisungen**

1. Starten Sie Ihre lokale Kali Linux VM, öffnen Sie ein Terminal und starten Sie `msfconsole`.
2. **Szenario 1:** Sie haben von einer kritischen Sicherheitslücke in Apache Struts gehört, die mit der CVE-ID "CVE-2017-5638" gekennzeichnet ist.
    - Verwenden Sie den Befehl "search", um Exploit-Module im Zusammenhang mit dieser CVE zu finden.
        - `search CVE-2017-5638`
    - Identifizieren Sie ein relevantes Exploit-Modul aus den Suchergebnissen. Notieren Sie seinen vollständigen Pfad.
        - `exploit/multi/http/struts2_content_type_ognl`
    - Verwenden Sie den Befehl "info <full_module_path>" für dieses Modul. Wie lautet der "Rang" dieses Exploits und was sagt dieser Rang im Allgemeinen über seine Zuverlässigkeit oder Auswirkungen aus?
        - `info exploit/multi/http/struts2_content_type_ognl`
            
        - `Rank = Excellent, Sehr zuverlässig; funktioniert in den meisten Fällen stabil und reproduzierbar.`
            
            |Rang|Bedeutung|
            |---|---|
            |**Excellent**|Sehr zuverlässig; funktioniert in den meisten Fällen stabil und reproduzierbar.|
            |Great|Funktioniert zuverlässig, aber erfordert evtl. bestimmte Bedingungen.|
            |Good|Funktioniert oft, aber kann fehlschlagen oder unvollständig sein.|
            |Normal|Durchschnittlich zuverlässig.|
            |Average|Weniger zuverlässig, kann leicht fehlschlagen.|
            |Low|Selten erfolgreich, oft nur Proof-of-Concept.|
            |Manual|Muss manuell angepasst oder vorbereitet werden.|
            
3. **Szenario 2:** Sie müssen einen Hilfsscan durchführen, um nach offenen TCP-Ports auf einem Zielcomputer zu suchen.
    - Verwenden Sie den Befehl `search`, um Hilfsmodule zu finden, die für TCP-Port-Scans entwickelt wurden.
        - `search portscan`
    - Identifizieren Sie ein relevantes Hilfsscanner-Modul. Notieren Sie seinen vollständigen Pfad.
        - `auxiliary/scanner/portscan/tcp`
    - Verwenden Sie den Befehl `info <full_module_path>` für dieses Modul. Was sind mindestens zwei "Erforderliche" Optionen für dieses Modul (außer `RHOSTS`, wenn es aufgelistet ist, konzentrieren Sie sich auf andere wie `PORTS` oder `THREADS`)?
        - `PORTS 1-10000 yes Ports to scan (e.g. 22-25,80,110-900)'`
        - `THREADS 1 yes The number of concurrent threads (max one per host)`
4. Wie lautet der Befehl in `msfconsole`, um alle verfügbaren Optionen für ein aktuell ausgewähltes Modul zu sehen?
    1. `show options`

**Vorlage**

Reichen Sie ein Dokument ein, das Folgendes enthält:

- Für Szenario 1: Den vollständigen Modulpfad, seinen Rang und was der Rang bedeutet.
- Für Szenario 2: Den vollständigen Modulpfad und mindestens zwei seiner "erforderlichen" Optionen (außer `RHOSTS`).
- Ihre Antwort auf Anweisung 4 (der Befehl zum Anzeigen der Optionen).
- Ein Bildschirmfoto Ihrer `msfconsole`, das die Ausgabe eines der von Ihnen ausgeführten `info`Befehle zeigt.