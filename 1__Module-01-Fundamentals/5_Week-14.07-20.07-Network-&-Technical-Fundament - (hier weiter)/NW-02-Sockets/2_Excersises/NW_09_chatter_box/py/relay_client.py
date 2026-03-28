import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 12345

# Socket erstellen und verbinden
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Verbunden mit Server {HOST}:{PORT}")
print("Tippe '/quit' zum Beenden")

def receive_messages():
    """Läuft in eigenem Thread - empfängt Nachrichten vom Server"""
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                message = data.decode('utf-8')
                print(f"\n[Empfangen]: {message}")
            else:
                # Server hat Verbindung geschlossen
                print("\nVerbindung zum Server verloren")
                break
        except:
            break

# Thread starten
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()
"""

**🎓 Warum Threading?
┌─────────────────────────────────────────┐
│           OHNE THREADING                │
│                                          │
│  input() ──► blockiert ──► recv() wartet│
│  PROBLEM: Kann nicht gleichzeitig!      │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│           MIT THREADING                  │
│                                          │
│  Thread 1: input() ──► Senden           │
│  Thread 2: recv()  ──► Empfangen        │
│  LÖSUNG: Beide laufen parallel!         │
└─────────────────────────────────────────┘

"""
# Haupt-Thread: Benutzereingabe und Senden
while True:
    try:
        message = input("")
        
        if message.strip().lower() == '/quit':
            client_socket.send(message.encode('utf-8'))
            print("Chat beendet")
            break
            
        if message:
            client_socket.send(message.encode('utf-8'))
            
    except KeyboardInterrupt:
        print("\nVerbindung wird getrennt...")
        break

client_socket.close()

"""
## 🧪 Phase 4: Testen

### Testanleitung:
Terminal 1 (Server):
    > python relay_server.py
    Server läuft auf 127.0.0.1:12345
    Warte auf Client 1...

Terminal 2 (Client 1):
    > python relay_client.py
    Verbunden mit Server...

Terminal 3 (Client 2):
    > python relay_client.py
    Verbunden mit Server...

Jetzt können Client 1 und 2 chatten!

"""