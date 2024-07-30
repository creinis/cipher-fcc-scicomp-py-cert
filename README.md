## Caesar and Vigenere Ciphers

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Caesar and Vigenere Ciphers applications, follow the instructions in the Setup section below.

## Project Structure

- `caesar_cipher.py`: Contains the implementation of the Caesar cipher.
- `vigenere_cipher.py`: Contains the implementation of the Vigenere cipher.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/cipher-fcc-scicomp-py-cert.git
   cd cipher

2. Run the Caesar cipher script:
   ```bash
   python3 caesar_cipher.py
   ```

3. Run the Vigenere cipher script:
   ```bash
   python3 vigenere_cipher.py
   ```

## Caesar Cipher

### Functionality

The Caesar cipher shifts each letter in the message by a specified offset. This simple substitution cipher is one of the oldest and most well-known encryption techniques.

### Practical Use Case

The Caesar cipher can be used for basic encryption tasks where security is not a primary concern, such as encoding messages for children or simple puzzles. It demonstrates the fundamental concept of shifting letters in the alphabet, making it an excellent educational tool for learning about cryptography.

### Benefits

- **Simplicity:** Easy to understand and implement.
- **Educational Value:** Provides a basic introduction to encryption and decryption techniques.

## Vigenere Cipher

### Functionality

The Vigenere cipher uses a keyword to encrypt and decrypt the message. Each letter in the plaintext is shifted by an amount determined by the corresponding letter in the keyword, creating a more secure encryption method compared to the Caesar cipher.

### Practical Use Case

The Vigenere cipher is suitable for more complex encryption needs where increased security is desired. It is often used in educational settings to teach about polyalphabetic substitution ciphers and their advantages over simpler techniques like the Caesar cipher.

### Benefits

- **Increased Security:** Provides better protection against frequency analysis compared to the Caesar cipher.
- **Educational Value:** Demonstrates more advanced concepts in cryptography, such as the use of a keyword and varying shift amounts.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
