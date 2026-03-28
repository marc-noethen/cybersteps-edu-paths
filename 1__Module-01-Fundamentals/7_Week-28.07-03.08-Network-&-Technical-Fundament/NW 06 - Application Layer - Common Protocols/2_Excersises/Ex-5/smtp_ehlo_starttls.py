import smtplib

def main():
    try:
        # Mit Googles SMTP-Server auf Port 587 verbinden
        server = smtplib.SMTP('smtp.googlemail.com', 587, timeout=10)
        print("Verbindung hergestellt.")

        # Debug-Level auf 1 setzen, um den Austausch zu sehen (optional)
        server.set_debuglevel(1)

        # EHLO senden
        code, msg = server.ehlo()
        print(f"EHLO Antwortcode: {code}")
        print("Server-Fähigkeiten:")
        print(msg.decode())

        # In Zeilen aufteilen und nach STARTTLS suchen
        capabilities = msg.decode().split('\n')
        starttls_supported = any('STARTTLS' in line for line in capabilities)

        if starttls_supported:
            print("✅ STARTTLS wird vom Server unterstützt.")
        else:
            print("❌ STARTTLS wird NICHT unterstützt.")

        # Verbindung ordentlich beenden
        server.quit()
        print("Verbindung geschlossen.")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
