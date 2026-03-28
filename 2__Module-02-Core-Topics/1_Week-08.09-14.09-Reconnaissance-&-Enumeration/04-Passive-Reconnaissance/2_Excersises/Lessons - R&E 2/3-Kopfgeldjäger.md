- Einige Regeln sind in Stein gemeißelt, andere auf einer Webseite.

**Ziel**

Die Bedeutung von Nutzungsbedingungen, Richtlinien zur verantwortungsvollen Offenlegung von Informationen und Bug Bounty-Programmen bei der Interaktion mit Websites und Online-Diensten aus der Sicherheitsperspektive zu verstehen.

**Anweisungen**

1. Wählen Sie **eine** der folgenden bekannten Technologieunternehmen/Plattformen:
    - Google
    - Microsoft
    - Facebook (Meta)
    - Apfel
    - GitHub
2. Suchen Sie mit einer Suchmaschine die offizielle Seite "Bug Bounty Program" oder "Responsible Disclosure Policy" des von Ihnen gewählten Unternehmens.
3. Lesen Sie sich die wichtigsten Punkte der Richtlinie durch. Suchen Sie insbesondere nach:
    - Welche Arten von Systemen oder Produkten fallen in den Geltungsbereich (was dürfen Sie testen, wenn überhaupt)?
        - `Google-eigene Browser-Erweiterungen, mobile & Web-Apps; neue Firmen 6-Monate ausgeschlossen`
    - Welche Arten von Schwachstellen oder Aktivitäten sind ausdrücklich vom Geltungsbereich ausgeschlossen (was dürfen Sie _nicht_ tun)?
        - `Drittanbieter-Apps, Sandbox-XSS ohne Datenimpact, Blogspot JavaScript, legitime Weiterleitungen, wenig realistische Interaktionen, veraltete Browser, Bannerinfos allein, Spoofing bei Gmail, DOS/Spam/Phishing etc.`
    - Wie möchte das Unternehmen, dass Forscher Schwachstellen melden?
        - `Über bughunters.google.com/report (PGP optional, Tracking-ID, evtl. CVE-Vergabe)`
    - Bietet das Unternehmen Belohnungen (Bounties) für gültige Meldungen von Sicherheitslücken an? Wenn ja, was könnte die Höhe der Belohnung beeinflussen (z. B. Schweregrad)?
        - `Ja; Höhe richtet sich nach Schweregrad & Kontext, z. B. bei AI nach Angriffsszenarien bzw. betroffenen Komponenten`
4. Fassen Sie in Ihren eigenen Worten die wichtigsten Aspekte zusammen, die Sie zu den Punkten 3a, 3b, 3c und 3d gefunden haben.
5. Warum ist es für jeden, der sich für Sicherheitstests interessiert, wichtig, solche Richtlinien sorgfältig zu lesen und zu befolgen, bevor er versucht, Schwachstellen in den Anlagen eines Unternehmens zu finden?
    1. `Weil man sich sonst Strafbar macht und zur Dunklen Seite der Macht gewechselt ist :D`

**Einreichung**

Reichen Sie ein Dokument ein, das Folgendes enthält:

- Den Namen des von Ihnen gewählten Unternehmens.
- Die URL der Seite des Bug Bounty Programms oder der Responsible Disclosure Policy.
- Ihre zusammengefassten Antworten zu den Punkten 3a, 3b, 3c und 3d.
- Ihre Antwort auf Punkt 5.