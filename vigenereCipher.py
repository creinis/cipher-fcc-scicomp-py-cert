text = ''
custom_key = ''

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    
    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            
            # Define the offset and the encrypted/decrypted letter
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


