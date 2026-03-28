import hashlib
import itertools

# === KONFIGURATION ===
alphabet = "abcdefghijklmnopqrstuvwxyz"
ziel_hash = "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1"
# max_laenge = 3  # Längen testen 1, 2, 3
max_laenge = 10  # Längen testen 1, 2, 3, 4
# max_laenge = 5  # Längen testen 1, 2, 3, 4, 5

for laenge in range(1, max_laenge + 1):
    print(f"Teste Länge {laenge}...")
    
    for kombination in itertools.product(alphabet, repeat=laenge):       
        passwort = "".join(kombination)
    
        passwort_hash = hashlib.sha256(passwort.encode()).hexdigest()
        
        if passwort_hash == ziel_hash:
            print(f"✅ GEFUNDEN: {passwort}")
            exit()  

print("❌ Nicht gefunden im getesteten Bereich")