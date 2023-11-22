def gronsfeld_encode(text, sequence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # алфавит
    encrypted_text = ""
    sequence_length = len(sequence)
    
    for i, char in enumerate(text):
        if char.isalpha():
            char_index = alphabet.index(char.lower())  # индекс текущей буквы в алфавите
            shift = int(sequence[i % sequence_length])  # получаем сдвиг по текущему индексу в последовательности
            encrypted_char_index = (char_index + shift) % len(alphabet)  # вычисляем индекс зашифрованной буквы
            encrypted_char = alphabet[encrypted_char_index]
            # print(f"{encrypted_char} = ({char_index} + {shift}) % 26")
            if char.isupper():
                encrypted_text += encrypted_char.upper()
            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def gronsfeld_decode(encrypted_text, sequence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # алфавит
    decrypted_text = ""
    sequence_length = len(sequence)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            char_index = alphabet.index(char.lower())  # индекс текущей буквы в алфавите
            shift = int(sequence[i % sequence_length])  # получаем сдвиг по текущему индексу в последовательности
            decrypted_char_index = (char_index - shift) % len(alphabet)  # вычисляем индекс расшифрованной буквы
            decrypted_char = alphabet[decrypted_char_index]
            # print(f"{decrypted_char} = ({char_index} - {shift}) % 26")
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def is_valid_gronsfeld_key(key):
    digits = "0123456789"
    
    if not key:
        return False
    
    for char in key:
        if char not in digits:
            return False
    
    return True
