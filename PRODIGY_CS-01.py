# Define the character set
CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext, shift):
    """
    Encrypts the given plaintext using the Caesar cipher with the specified shift value.

    Args:
        plaintext (str): The plaintext message to be encrypted.
        shift (int): The number of positions to shift each character in the alphabet.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ''
    for char in plaintext.upper():
        if char in CHARS:
            # Shift the character by the specified amount
            new_index = (CHARS.index(char) + shift) % len(CHARS)
            ciphertext += CHARS[new_index]
        else:
            # Leave non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using the Caesar cipher with the specified shift value.

    Args:
        ciphertext (str): The ciphertext to be decrypted.
        shift (int): The number of positions to shift each character in the alphabet.

    Returns:
        str: The decrypted plaintext.
    """
    plaintext = ''
    for char in ciphertext.upper():
        if char in CHARS:
            # Shift the character back by the specified amount
            new_index = (CHARS.index(char) - shift) % len(CHARS)
            plaintext += CHARS[new_index]
        else:
            # Leave non-alphabetic characters unchanged
            plaintext += char
    return plaintext


def main():
    """
    Main function to handle user input and encryption/decryption.
    """
    while True:
        print("Welcome to the Caesar Cipher Encryption/Decryption Tool!")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Encrypt a message
            plaintext = input("Enter the plaintext message: ")
            shift = int(input("Enter the shift value: "))
            ciphertext = encrypt(plaintext, shift)
            print(f"Ciphertext: {ciphertext}")

        elif choice == '2':
            # Decrypt a message
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value: "))
            plaintext = decrypt(ciphertext, shift)
            print(f"Plaintext: {plaintext}")

        elif choice == '3':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
