 Explanation of the Caesar Cipher Script

1. Character Set Definition (`CHARS`):
   - The `CHARS` variable defines the character set used for encryption and decryption, which includes the uppercase English alphabet (`'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`).

2. Encrypt and Decrypt Functions:
   - The `encrypt` function encrypts the given plaintext by shifting each character forward by a specified number of positions in the `CHARS` list.
   - The `decrypt` function decrypts the given ciphertext by shifting each character backward by the specified number of positions in the `CHARS` list.

3. Main Function (`main`):
   - The `main` function serves as the entry point of the program. It provides a user interface to interact with the Caesar cipher tool.
   - It displays a menu with options to:
     1. Encrypt a message.
     2. Decrypt a message.
     3. Exit the program.
   - Based on the user's choice, the program prompts for the necessary input (plaintext/ciphertext and shift value) and processes the input using the appropriate function.

4. Handling User Choices:
   - Encrypting a Message: If the user chooses to encrypt a message, the `encrypt` function is called with the user's input, and the resulting ciphertext is displayed.
   - Decrypting a Message: If the user chooses to decrypt a message, the `decrypt` function is called with the user's input, and the resulting plaintext is displayed.
   - Exiting the Program: If the user chooses to exit, the program breaks out of the loop and terminates.
   - Invalid Choice Handling: If the user enters an invalid choice, the program displays an error message and prompts the user again.

5. Script Execution (`if __name__ == "__main__":`):
   - The block `if __name__ == "__main__":` ensures that the `main` function is executed only when the script is run directly, not when it is imported as a module in another script.

Usage Instructions:

1. Run the script.
2. Follow the menu prompts to either encrypt or decrypt a message.
3. Enter the plaintext or ciphertext and the desired shift value when prompted.
4. The program will display the encrypted or decrypted message accordingly.
5. To exit the program, choose the "Exit" option from the menu.

 Notes:

- This implementation assumes that the input text contains only uppercase alphabetic characters and possibly non-alphabetic characters (e.g., spaces, punctuation). Non-alphabetic characters are not altered by the encryption or decryption process.
- If you need to handle lowercase characters or other character sets, you will need to modify the `CHARS` variable and adjust the logic in the `encrypt` and `decrypt` functions accordingly.
