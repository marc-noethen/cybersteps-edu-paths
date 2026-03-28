## 📊 Zusammenfassung nach dem 80/20-Prinzip

**1. Was ist ein Socket?**

- Ein Socket = **IP-Adresse + Portnummer**
- Wie eine vollständige Postadresse: IP = Straße/Hausnummer, Port = Wohnungsnummer
- Ermöglicht gezielten Datenaustausch zwischen spezifischen Programmen

**2. Client-Server-Grundprinzip:**

- **Server**: Wartet passiv `bind()` → `listen()` → `accept()`)
- **Client**: Initiiert aktiv die Verbindung `connect()`)
- Wie Restaurant (Server) und Gast (Client)

**3. Die 4 wichtigsten Socket-Funktionen:**

```python
# SERVER:
server_socket.bind(("0.0.0.0", 9999))  # Port reservieren
server_socket.listen(1)                 # Auf Verbindungen warten
connection, addr = server_socket.accept()  # Client akzeptieren

# CLIENT:
client_socket.connect(("127.0.0.1", 9999))  # Zum Server verbinden
```

**4. Daten senden/empfangen:**

- Alles wird als **Bytes** übertragen
- String → Bytes: `.encode('utf-8')`
- Bytes → String: `.decode('utf-8')`

```python
socket.sendall("Hallo".encode('utf-8'))  # Senden
data = socket.recv(1024).decode('utf-8') # Empfangen
```

**5. Praktisches Beispiel:**

- Server startet auf Port 9999 und wartet
- Client verbindet sich zu `localhost:9999`
- Client sendet "Hi server!"
- Server empfängt die Nachricht
- Beide schließen die Verbindung

**Windows 11 Besonderheit:**

- Terminal öffnen: `Windows-Taste + R` → `cmd` oder `powershell`
- Zwei Terminals parallel öffnen für Server und Client
- Python ausführen: `python server.py` bzw. `python client.py`

**Merksatz:** Ein Socket ist die Kombination aus IP-Adresse (welcher Computer) und Port (welches Programm). Server warten, Clients verbinden sich.

---

## Verwendete Tools

|Verwendete Tools|Bedeutung|
|---|---|
|Python `socket` Bibliothek|Eingebautes Python-Modul zum Erstellen von Netzwerkverbindungen|
|VS Code|Code-Editor zum Schreiben und Ausführen der Python-Skripte|
|Terminal / PowerShell (Windows 11)|Kommandozeile zum Ausführen von Python-Skripten `python server.py`)|
|`127.0.0.1` / `localhost`|Loopback-Adresse - verweist auf den eigenen Computer|

---

## Technische Fachbegriffe

|Technische Fachbegriffe|Bedeutung|
|---|---|
|**Socket**|Kommunikationsendpunkt einer Anwendung im Netzwerk (IP + Port)|
|**Port**|Nummer (0-65535) zur Identifikation einer spezifischen Anwendung auf einem Computer|
|**IP-Adresse**|Eindeutige Adresse eines Computers im Netzwerk (z.B. `192.168.1.10`)|
|**Client-Server-Modell**|Kommunikationsmuster: Server wartet, Client initiiert die Verbindung|
|**bind()**|Funktion zum "Beanspruchen" einer IP-Adresse und eines Ports durch den Server|
|**listen()**|Server wartet auf eingehende Verbindungen|
|**accept()**|Server akzeptiert eine Client-Verbindung und erstellt einen neuen Socket dafür|
|**connect()**|Client stellt Verbindung zum Server her|
|**sendall()**|Sendet Daten über den Socket (als Bytes)|
|**recv()**|Empfängt Daten über den Socket (als Bytes)|
|**encode() / decode()**|Umwandlung zwischen String und Bytes (UTF-8)|
|**Well-Known Ports**|Standardports 0-1023 für bekannte Dienste (z.B. Port 80 für HTTP, 443 für HTTPS)|
|**Wichtige Vokabeln**||
|**Endpoint**|Endpunkt einer Netzwerkverbindung|
|**Listening**|Zustand des Servers beim Warten auf Verbindungen|
|**Binding**|Verknüpfen eines Sockets mit einer IP-Adresse und einem Port|
|**Connection**|Aktive Verbindung zwischen Client und Server|
|**localhost**|Der eigene Computer (127.0.0.1)|
|**Interface**|Netzwerkschnittstelle (z.B. WLAN, LAN)|
|**0.0.0.0**|Bedeutet "alle verfügbaren Netzwerkschnittstellen" beim Server|