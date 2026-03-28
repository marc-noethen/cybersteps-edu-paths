[Gobuster Directory Bruteforce - Arbeitsvorlage](Gobuster%20Directory%20Bruteforce%20-%20Arbeitsvorlage%20272588ff46e680d78a47c1c708cdc6b2.md)

*Found you!*

**Ziel**

Verwenden Sie das Tool `gobuster`, um einen Brute-Force-Angriff auf Verzeichnisse durchzuführen und eine versteckte administrative Schnittstelle zu entdecken.

**Anleitung**

1. Verwenden Sie das Kommandozeilen-Tool `gobuster`, um nach Verzeichnissen auf der [Gin & Juice Shop](https://ginandjuice.shop/) Website (verwundbare Webanwendung von PortSwigger) zu suchen.
2. Sie brauchen eine gute Wortliste. Eine Standard-Wortliste ist `directory-list-2.3-small.txt` aus der SecLists-Sammlung. Wenn Sie SecLists nicht haben, enthalten viele Linux-Distributionen für Sicherheitstests ähnliche Listen in `/usr/share/wordlists/`.
3. Konstruieren Sie den `gobuster`Befehl. Er wird in etwa so aussehen: `go [Pfad_zu_Ihrer_Wortliste.txt]`.
4. Führen Sie den Befehl aus und analysieren Sie die Ausgabe. Suchen Sie nach allen Pfaden, die einen `200` oder `302` Statuscode zurückgeben, da diese auf vorhandene Ressourcen hinweisen. Sie suchen speziell nach einem Pfad, der sich auf die Verwaltung bezieht.

**Einreichung**

Reichen Sie einen Screenshot Ihres Terminals ein, der den von Ihnen ausgeführten Befehl "gobuster" und die Ausgabe zeigt, in der das versteckte Verwaltungsverzeichnis angezeigt wird.