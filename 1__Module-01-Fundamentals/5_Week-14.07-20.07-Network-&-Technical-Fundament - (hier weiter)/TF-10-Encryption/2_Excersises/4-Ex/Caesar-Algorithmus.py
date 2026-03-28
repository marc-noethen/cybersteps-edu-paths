

def caesar_encrypt(text, shift):
    result = "" 

    for char in text:
        if char.isupper():
            char = ord(char) - ord('A')
            char += shift
            char = char % 26                # Erst Modulo (Wraparound)
            char = chr(char + ord("A"))  
            result += char

        elif char.islower():
            char = ord(char) - ord('a')
            char += shift
            char = char % 26                # Erst Modulo (Wraparound)
            char = chr(char + ord("a"))  
            result += char

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    result = "" 

    for char in text:
        if char.isupper():
            char = ord(char) - ord('A')
            char -= shift
            char = char % 26                # Erst Modulo (Wraparound)
            char = chr(char + ord("A"))  
            result += char

        elif char.islower():
            char = ord(char) - ord('a')
            char -= shift
            char = char % 26                # Erst Modulo (Wraparound)
            char = chr(char + ord("a"))  
            result += char

        else:
            result += char

    return result


# test = caesar_decrypt("Wh wg pshhsf hc qfsohs hvob hc zsofb! Qfsohwbu wg hvs sggsbqs ct zwts.", 6)
# print(test)


for i in range(1,26):
    test = caesar_decrypt("Wh wg pshhsf hc qfsohs hvob hc zsofb! Qfsohwbu wg hvs sggsbqs ct zwts.", i)
    print(test)

# Answer 
# Shift-Key 14
# It is better to create than to learn! Creating is the essence of life.