def vigenere_encode(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    key_index = 0
    for letter in plaintext:
        if letter.isalpha():
            offset = ord('A')
            keyword_letter = keyword[key_index]
            key_letter_index = ord(keyword_letter) - offset
            letter_index = ord(letter) - offset
            ciphertext += chr(((letter_index + key_letter_index) % 26) + offset)
            # print(f"{chr(((letter_index + key_letter_index) % 26) + offset)} = ({letter_index} + {key_letter_index}) + {offset}")
            key_index = (key_index + 1) % len(keyword)
        else:
            ciphertext += letter
    return ciphertext

def vigenere_decode(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    key_index = 0
    for letter in ciphertext:
        if letter.isalpha():
            offset = ord('A')
            keyword_letter = keyword[key_index]
            key_letter_index = ord(keyword_letter) - offset
            letter_index = ord(letter) - offset
            plaintext += chr(((letter_index - key_letter_index) % 26) + offset)
            # print(f"{chr(((letter_index - key_letter_index) % 26) + offset)} = ({letter_index} - {key_letter_index}) % 26 + {offset}")
            key_index = (key_index + 1) % len(keyword)
        else:
            plaintext += letter
    return plaintext

def is_valid_vigenere_key(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    
    if not key:
        return False
    
    for char in key:
        if char not in alphabet:
            return False
    
    return True