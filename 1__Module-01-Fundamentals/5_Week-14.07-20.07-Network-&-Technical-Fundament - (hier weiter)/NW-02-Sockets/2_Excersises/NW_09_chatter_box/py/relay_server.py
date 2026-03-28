import socket
import select

# Konfiguration
HOST = '127.0.0.1'  # localhost - nur lokale Verbindungen
PORT = 12345        # Beliebiger Port über 1024

# Server-Socket erstellen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Option: Adresse wiederverwenden (verhindert "Address already in use" Fehler)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# An Adresse und Port binden
server_socket.bind((HOST, PORT))

# Auf Verbindungen lauschen (maximal 2 in der Warteschlange)
server_socket.listen(2)

print(f"Server läuft auf {HOST}:{PORT}")

clients = []

print("Warte auf Client 1...")
client1, addr1 = server_socket.accept()
print(f"Client 1 verbunden: {addr1}")
clients.append(client1)

print("Warte auf Client 2...")
client2, addr2 = server_socket.accept()
print(f"Client 2 verbunden: {addr2}")
clients.append(client2)

print("Beide Clients verbunden! Chat startet...")

# Sockets auf non-blocking setzen
for client in clients:
    client.setblocking(False)

running = True

while running:
    try:
        # select überwacht beide Sockets auf eingehende Daten
        readable, _, _ = select.select(clients, [], [], 0.1)
        
        for sock in readable:
            try:
                data = sock.recv(1024)
                
                if data:
                    message = data.decode('utf-8')
                    
                    # Prüfen auf Quit-Nachricht
                    if message.strip().lower() == '/quit':
                        print(f"Ein Client hat sich verabschiedet")
                        running = False
                        break
                    
                    # Nachricht an den ANDEREN Client weiterleiten
                    for other_client in clients:
                        if other_client != sock:
                            other_client.send(data)
                            
                else:
                    # Leere Daten = Client hat Verbindung getrennt
                    print("Ein Client hat die Verbindung getrennt")
                    running = False
                    break
                    
            except socket.error:
                pass
                
    except KeyboardInterrupt:
        print("\nServer wird beendet...")
        running = False

"""
**🎓 Erklärung des `select`:**

select.select(read_list, write_list, error_list, timeout)
       │          │           │          │
       │          │           │          └─► Timeout in Sekunden (0.1 = 100ms)
       │          │           └─► Sockets auf Fehler prüfen
       │          └─► Sockets die bereit zum Schreiben sind
       └─► Sockets die Daten zum Lesen haben

"""

# Alle Verbindungen schließen
for client in clients:
    client.close()
server_socket.close()
print("Server beendet")

