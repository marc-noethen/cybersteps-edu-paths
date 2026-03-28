def shift_char(char, shift):
    """Verschiebt einen einzelnen Buchstaben um shift Positionen."""
    if char.isupper():
        base = ord('A')
    elif char.islower():
        base = ord('a')
    else:
        return char
    
    shifted = (ord(char) - base + shift) % 26
    return chr(shifted + base)


def caesar_encrypt(text, shift):
    """Verschlüsselt text mit Caesar-Chiffre."""
    return "".join(shift_char(char, shift) for char in text)


def caesar_decrypt(text, shift):
    """Entschlüsselt text mit Caesar-Chiffre."""
    return caesar_encrypt(text, -shift)


# Brute-Force
cipher = "Wh wg pshhsf hc qfsohs hvob hc zsofb! Qfsohwbu wg hvs sggsbqs ct zwts."

for i in range(1, 26):
    print(f"Shift {i:2}: {caesar_decrypt(cipher, i)}")