import gmpy2
from sympy import randprime
from multiprocessing import Pool
import os

# Function to generate large prime numbers
def generate_large_prime(bits=2048):
    return randprime(2**(bits-1), 2**bits)

# Function to compute modular inverse using gmpy2
def mod_inv(e, phi):
    return gmpy2.invert(e, phi)

# RSA Key Generation
def generate_rsa_keys(bits=2048):
    print("Generating large primes...")
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Standard public exponent
    e = 65537

    # Compute modular inverse (private key d)
    d = mod_inv(e, phi)

    print("Keys generated successfully!")
    return (n, e, d)

# Encryption function using modular exponentiation
def encrypt_chunk(chunk, e, n):
    return gmpy2.powmod(chunk, e, n)  # c = m^e % n

# Parallelized Encryption
def encrypt_message(message, e, n):
    message_chunks = [ord(char) for char in message]  # Convert to ASCII values
    
    with Pool(os.cpu_count()) as pool:  # Use all available CPU cores
        encrypted_chunks = pool.starmap(encrypt_chunk, [(chunk, e, n) for chunk in message_chunks])
    
    return encrypted_chunks

# Decryption function
def decrypt_chunk(chunk, d, n):
    return chr(int(gmpy2.powmod(chunk, d, n)))  # Convert back to character

# Parallelized Decryption
def decrypt_message(encrypted_chunks, d, n):
    with Pool(os.cpu_count()) as pool:
        decrypted_chars = pool.starmap(decrypt_chunk, [(chunk, d, n) for chunk in encrypted_chunks])

    return "".join(decrypted_chars)

# Main RSA Execution
if __name__ == "__main__":
    bits = 2048  # 2048-bit security level
    n, e, d = generate_rsa_keys(bits)
    print("\nKeys generated successfully!\nLet's start!")
    choice = input("Press 'E' if you want to encrypt a message and 'D' if you want to decrypt a message.")
    
    if choice.upper() == 'E':
        message = input("Enter the message: ")
        print("\nOriginal Message:", message)

        # Encrypt message
        encrypted_message = encrypt_message(message, e, n)
        print("\nEncrypted Message:", encrypted_message)
    elif choice.upper() == 'D':
        encrypted_message = input("Enter the encrypted message (each chunk separated by a space): ").split()
        decrypted_message = decrypt_message(encrypted_message, d, n)
        print("\nDecrypted Message:", decrypted_message)
        
    else:
        print("Invalid choice!")
    
    print("\n RSA Encryption & Decryption Successful!")
