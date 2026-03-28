*Warum kannst du Mimi nicht rauslassen?*

**Ziel** 

Beobachten Sie, wie Endpunkt-Sicherheitslösungen (wie Windows Defender oder andere Sicherheitseinstellungen) auf Versuche reagieren, bekannte Angriffstools herunterzuladen, und untersuchen Sie gängige Umgehungstechniken.

**Anweisungen**

1. Öffnen Sie auf Ihrer **lokalen Windows-VM** (nicht der TryHackMe-VM) einen Webbrowser. Stellen Sie sicher, dass Ihr Defender aktiviert ist!
2. Versuchen Sie, die neueste stabile Version von Mimikatz aus dem offiziellen GitHub-Repository herunterzuladen: `https://github.com/gentilkiwi/mimikatz/releases`.
3. Beachten Sie alle Warnungen, Blockierungen oder Quarantänen von Windows Defender oder anderer Sicherheitssoftware.
4. Überprüfen Sie den "Schutzverlauf" oder "In Quarantäne gestellte Bedrohungen" von Windows Defender, um zu sehen, ob das Tool erkannt wurde (dies kann davon abhängen, welche anderen Sicherheitseinstellungen ein- oder ausgeschaltet sind - recherchieren Sie dazu).
5. Versuchen Sie, andere Windows-Sicherheitsmaßnahmen zu deaktivieren (finden Sie heraus, wie sie funktionieren) **außer Defender** und sehen Sie sich den Unterschied im "Schutzverlauf" an. Es ist wichtig, die Schutzschichten zu verstehen.
6. Nennen Sie auf der Grundlage Ihrer Beobachtungen und Online-Recherchen drei gängige Techniken, die Angreifer verwenden, um Endpunkt-Sicherheitslösungen (wie Antivirus/EDR) zu umgehen oder zu umgehen, wenn sie versuchen, Tools wie Mimikatz auszuführen.

**Einreichung**

1. Screenshot, der das Ergebnis Ihres Download-Versuchs zeigt (z. B. Download-Leiste des Browsers, Benachrichtigung von Windows Defender).
2. Screenshot des "Schutzverlaufs" von Windows Defender oder eines vergleichbaren Programms, der die Erkennung zeigt (falls vorhanden).
3. Eine kurze Textantwort, in der Sie erklären, was bei Ihrem Downloadversuch passiert ist, und die drei von Ihnen untersuchten Umgehungstechniken auflisten.