def atbash_encode(text):
    ciphertext = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                ciphertext += chr(ord('z') - (ord(char) - ord('a')))
                # print(f"{chr(ord('z') - (ord(char) - ord('a')))} = {ord('z')} - ({ord(char)} - {ord('a')})")
            else:
                ciphertext += chr(ord('Z') - (ord(char) - ord('A')))
                # print(f"{chr(ord('Z') - (ord(char) - ord('A')))} = {ord('Z')} - ({ord(char)} - {ord('A')})")
        else:
            ciphertext += char
    return ciphertext

def atbash_decode(ciphertext):
    plaintext = atbash_encode(ciphertext)  
    return plaintext
