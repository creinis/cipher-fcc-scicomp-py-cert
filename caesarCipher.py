text = ''
shift = 0

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            
    
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    
caesar(text, shift)