# Antwort von 104.18.27.120: Bytes=32 Zeit=249ms TTL=58
import socket
# Socket erstellen
# AF_INET = IPv4 Adressfamilie
# SOCK_STREAM = TCP Protokoll (zuverlässig, verbindungsorientiert)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ziel definieren
server_ip = "208.91.197.27"  # Die IP die du mit nslookup gefunden hast
server_port = 80              # HTTP Standard-Port

# Verbindung aufbauen
client_socket.connect((server_ip, server_port))

# HTTP-Request als String
hostname = "example.com"
request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"

# String zu Bytes konvertieren und senden
client_socket.sendall(request.encode())

# Bis zu 4096 Bytes empfangen
response = client_socket.recv(4096)

# Bytes zu String dekodieren
# errors='ignore' ignoriert ungültige Zeichen
decoded_response = response.decode(errors='ignore')
print(decoded_response)

# Verbindung beenden
client_socket.close()