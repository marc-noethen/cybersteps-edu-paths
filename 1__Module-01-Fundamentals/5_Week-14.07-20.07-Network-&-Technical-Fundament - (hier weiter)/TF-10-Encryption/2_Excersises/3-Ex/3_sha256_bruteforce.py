"""
SHA-256 Brute-Force Passwort-Cracker
====================================
Autor: [DEIN NAME]
Datum: [DATUM]
Aufgabe: Passwort-Rätsel - Hash-Cracking mit Python

Beschreibung:
    Dieses Skript findet ein unbekanntes Passwort, indem es systematisch
    alle möglichen Kombinationen aus Kleinbuchstaben durchprobiert und
    deren SHA-256 Hash mit einem Ziel-Hash vergleicht.

Ziel-Hash: d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1
Ergebnis:  pass (4 Zeichen)
"""

import hashlib      # Für SHA-256 Hash-Berechnung
import itertools    # Für Kombinationsgenerierung (product)
import time         # Für Zeitmessung

# ============================================================================
# KONFIGURATION
# ============================================================================

# Der zu knackende SHA-256 Hash
ZIEL_HASH = "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1"

# Erlaubte Zeichen: nur englische Kleinbuchstaben (a-z)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Maximale Passwortlänge die getestet wird
MAX_LAENGE = 5

# ============================================================================
# HAUPTFUNKTION: BRUTE-FORCE ANGRIFF
# ============================================================================

def brute_force_sha256(ziel_hash, alphabet, max_laenge):
    """
    Führt einen Brute-Force Angriff auf einen SHA-256 Hash durch.
    
    Parameter:
        ziel_hash (str):  Der zu knackende SHA-256 Hash (64 Hex-Zeichen)
        alphabet (str):   Erlaubte Zeichen für das Passwort
        max_laenge (int): Maximale Passwortlänge zum Testen
    
    Rückgabe:
        str: Das gefundene Passwort oder None wenn nicht gefunden
    """
    
    versuche = 0  # Zähler für Anzahl der getesteten Kombinationen
    
    # Teste alle Längen von 1 bis max_laenge
    for laenge in range(1, max_laenge + 1):
        
        # Berechne Anzahl möglicher Kombinationen für diese Länge
        kombinationen_gesamt = len(alphabet) ** laenge
        print(f"\n[*] Teste Länge {laenge} ({kombinationen_gesamt:,} Kombinationen)...")
        
        # Generiere alle Kombinationen dieser Länge
        for kombination in itertools.product(alphabet, repeat=laenge):
            
            # Tuple zu String konvertieren: ('p','a','s','s') -> "pass"
            passwort_versuch = "".join(kombination)
            
            # SHA-256 Hash des Versuchs berechnen
            hash_versuch = hashlib.sha256(passwort_versuch.encode()).hexdigest()
            
            versuche += 1
            
            # Vergleich: Stimmt der Hash überein?
            if hash_versuch == ziel_hash:
                return passwort_versuch, versuche  # GEFUNDEN!
    
    # Nicht gefunden im getesteten Bereich
    return None, versuche

# ============================================================================
# PROGRAMMSTART
# ============================================================================

if __name__ == "__main__":
    
    print("=" * 60)
    print("   SHA-256 BRUTE-FORCE PASSWORT-CRACKER")
    print("=" * 60)
    print(f"\n[i] Ziel-Hash:    {ZIEL_HASH}")
    print(f"[i] Alphabet:     {ALPHABET} ({len(ALPHABET)} Zeichen)")
    print(f"[i] Max. Länge:   {MAX_LAENGE}")
    print(f"\n[*] Starte Brute-Force Angriff...")
    
    # Zeitmessung starten
    start_zeit = time.time()
    
    # Brute-Force ausführen
    ergebnis, versuche = brute_force_sha256(ZIEL_HASH, ALPHABET, MAX_LAENGE)
    
    # Zeitmessung beenden
    end_zeit = time.time()
    dauer = end_zeit - start_zeit
    
    # Ergebnis ausgeben
    print("\n" + "=" * 60)
    
    if ergebnis:
        print(f"   ✅ PASSWORT GEFUNDEN: {ergebnis}")
        print("=" * 60)
        print(f"\n[+] Passwort:     {ergebnis}")
        print(f"[+] Länge:        {len(ergebnis)} Zeichen")
        print(f"[+] Versuche:     {versuche:,}")
        print(f"[+] Dauer:        {dauer:.2f} Sekunden")
        print(f"[+] Geschw.:      {versuche/dauer:,.0f} Hashes/Sekunde")
        
        # Verifikation: Hash des gefundenen Passworts berechnen
        verifizierung = hashlib.sha256(ergebnis.encode()).hexdigest()
        print(f"\n[*] Verifizierung:")
        print(f"    Ziel-Hash:    {ZIEL_HASH}")
        print(f"    Berechnet:    {verifizierung}")
        print(f"    Match:        {'✅ JA' if verifizierung == ZIEL_HASH else '❌ NEIN'}")
    else:
        print(f"   ❌ NICHT GEFUNDEN")
        print("=" * 60)
        print(f"\n[-] Versuche:     {versuche:,}")
        print(f"[-] Dauer:        {dauer:.2f} Sekunden")
        print(f"[-] Hinweis:      Erhöhe MAX_LAENGE und versuche erneut")

    print("\n" + "=" * 60)
    print("   PROGRAMMENDE")
    print("=" * 60)
