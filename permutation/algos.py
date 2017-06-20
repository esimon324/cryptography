import random

alphabet = []
for i in range(256):
    alphabet.append(chr(i))
    
def encrypt(plaintext,password):
    alpha = list(alphabet)
    cypher = list(alphabet)
    
    random.seed(password)
    random.shuffle(cypher)
    
    map = {}
    for i in range(len(cypher)):
        map[alphabet[i]] = cypher[i]
            
    cyphertext = ''
    for char in plaintext:
        cyphertext = cyphertext + map[char]
        
    return cyphertext
    
def decrypt(cyphertext,password):
    alpha = list(alphabet)
    cypher = list(alphabet)
    
    random.seed(password)
    random.shuffle(cypher)
    
    map = {}
    for i in range(len(cypher)):
        map[cypher[i]] = alphabet[i]
            
    plaintext = ''
    for char in cyphertext:
        plaintext = plaintext + map[char]
        
    return plaintext
