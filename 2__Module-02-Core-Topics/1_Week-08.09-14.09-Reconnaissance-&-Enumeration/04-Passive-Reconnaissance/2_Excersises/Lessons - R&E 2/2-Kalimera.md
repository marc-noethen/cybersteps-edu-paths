_Guten Morgen, hackers_

**Ziel**

Um sicherzustellen, dass Ihre lokale virtuelle Kali-Linux-Maschine betriebsbereit ist, üben Sie die grundlegende Navigation und das Auffinden wichtiger Tools. (Es wird davon ausgegangen, dass Sie für diese Übung eine lokale Kali Linux VM installiert haben und diese gemäß den Einrichtungsanweisungen Ihres Programms läuft).

**Anweisungen**

1. Starten Sie Ihre lokale virtuelle Kali Linux-Maschine und melden Sie sich an.
2. Öffnen Sie ein Terminal-Fenster.
3. Führen Sie den Befehl `hostname` aus. Was ist die Ausgabe?
    1. `kali`
4. Führen Sie den Befehl `ip addr show eth0` aus (oder `ip addr show ens33` oder einen ähnlichen Schnittstellennamen, wenn `eth0` nicht Ihre Haupt-IP anzeigt). Ermitteln und notieren Sie die primäre IPv4-Adresse Ihrer Kali-VM.
    1. 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 00:0c:29:34:f5:87 brd ff:ff:ff:ff:ff:ff inet `192.168.80.128/24` brd 192.168.80.255 scope global dynamic noprefixroute eth0 valid_lft 1742sec preferred_lft 1742sec inet6 fe80::5c13:4ea3:1278:7642/64 scope link noprefixroute valid_lft forever preferred_lft forever
5. Benutze das Kali Linux Anwendungsmenü (normalerweise am oberen oder seitlichen Bildschirmrand):
    - Suchen Sie die Stelle, an der sich typischerweise "Metasploit Framework" befindet (beachten Sie die Kategorie, z. B. "04 - Execution" - die Kategorien können je nach Kali-Version leicht variieren).
        - `03, 04, 06, 12`
    - Suchen Sie den Ort, an dem "Nmap" (ein Netzwerk-Scanner) normalerweise zu finden ist.
        - `01, - Network Information`
    - Suchen Sie den Ort, an dem sich typischerweise "Wireshark" (ein Netzwerkprotokoll-Analysator) befindet.
        - `09 Discovery`
6. Wie lautet der vollständige Pfad zur ausführbaren Datei "nmap" auf deinem Kali-System? (Tipp: Benutze den Befehl `which nmap` im Terminal).
    1. `/usr/bin/nmap`

**Einreichung**

Reichen Sie ein Dokument ein, das Folgendes enthält:

- Ihre Antwort auf Anweisung 3 (Ausgabe von `hostname`).
- Ihre Antwort auf Anweisung 4 (IPv4-Adresse Ihrer Kali VM).
- Die Kategorien im Anwendungsmenü, in denen Sie Metasploit, Nmap und Wireshark gefunden haben (Anweisung 5).
- Ihre Antwort auf Anweisung 6 (vollständiger Pfad zu `nmap`).
- Ein Screenshot Ihres Kali-Linux-Desktops, der ein geöffnetes Terminal-Fenster mit einem der ausgeführten Befehle zeigt.