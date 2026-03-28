# Test modul and logic
import hashlib 

passwort = "Test"
hash_objekt = hashlib.sha256(passwort.encode())
hash_hex = hash_objekt.hexdigest()

print(f"Passwort: {passwort}")
print(f"SHA-256:  {hash_hex}")

# Target Hash
# d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1

"""
 For every possible password (a, b, c, ... aa, ab, ac...)│
│     1. Calculate hash                                    │
│     2. Compare with target hash                         │
│     3. Match? → FOUND! 
"""

#%% Separate execution
import hashlib 
target_hash = "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1"
test = hashlib.sha256("a".encode()).hexdigest()

print(f"Hash von 'a': {test}")
print(f"Match mit Ziel? {test == target_hash}")

# %%
