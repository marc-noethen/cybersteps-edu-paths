# SAM-urai's Scroll

*Enthülle die Geheimnisse des lokalen Reiches.

**Ziel**

Extrahieren Sie Windows-Passwort-Hashes aus Registry-Hives und versuchen Sie, sie mit Kali zu knacken.

**Anweisungen**

1. Erstellen Sie einen schwachen lokalen Benutzer auf Ihrer Windows-VM (z.B. `testuser` `password123`)
2. Führen Sie in einer erweiterten Eingabeaufforderung aus:

```
reg save HKLM\SAM C:\Temp\sam.hiv
reg save HKLM\SYSTEM C:\Temp\system.hiv
```

1. Übertragen Sie die Hive-Dateien auf Ihren Kali-Rechner.
2. Extrahieren Sie die NTLM-Hashes mit [`secretsdump.py`] (http://secretsdump.py), das Teil der `impacket` Python-Bibliothek ist (installieren Sie es mit `pip3 install impacket` )

```
secretsdump.py -sam sam.hiv -system system.hiv LOCAL
```

1. Versuchen Sie, das Passwort des schwachen Benutzers mit Ihrem bevorzugten Tool zu knacken (John/Hashcat)

**Vorlage**

Screenshot des erfolgreichen Knackens des Passworts des schwachen Benutzers.