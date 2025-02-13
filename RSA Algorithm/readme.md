# RSA Algorithm Implementation

This project implements the RSA (Rivest–Shamir–Adleman) algorithm, a widely used public-key cryptosystem for secure data transmission. It provides functionality for key generation, encryption, and decryption using the RSA algorithm.

## Features

- Generation of RSA key pairs (public and private keys)
- Message encryption using the public key
- Message decryption using the private key
- Parallelized encryption and decryption for improved performance
- Support for 2048-bit security level (customizable)

## Requirements

- Python 3.x
- gmpy2
- sympy
- multiprocessing (built-in)

To install the required packages, run:
pip install -r requirements.txt

## Usage

1. Run the `main.py` script:
python main.py

2. Choose whether you want to encrypt (E) or decrypt (D) a message.

3. For encryption:
   - Enter the message you want to encrypt.
   - The program will display the original message and the encrypted message.

4. For decryption:
   - Enter the encrypted message (each chunk separated by a space).
   - The program will display the decrypted message.

## How it works

1. **Key Generation**: The program generates two large prime numbers and computes the public and private keys.

2. **Encryption**: The message is converted to ASCII values and then encrypted using the public key.

3. **Decryption**: The encrypted message is decrypted using the private key and converted back to text.

4. **Parallelization**: The encryption and decryption processes use multiprocessing to utilize all available CPU cores, improving performance for large messages.

## Security Note

This implementation uses a 2048-bit key length, which is considered secure for general use. However, for critical applications, please consult current cryptographic standards and best practices.
