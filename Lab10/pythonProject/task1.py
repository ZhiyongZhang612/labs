def shift_char(char, shift):
    """
    Shift a single character by the given shift amount.
    :param char: The character to shift.
    :param shift: The shift amount.
    :return: Shifted character or the original if non-alphabetic.
    """
    if char.isupper():
        return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    elif char.islower():
        return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    return char


def caesar_encrypt(text, shift):
    """
    Encrypt the text using Caesar Cipher with functional style.
    """
    return ''.join(map(lambda char: shift_char(char, shift), text))


def caesar_decrypt(text, shift):
    """
    Decrypt the text using Caesar Cipher with functional style.
    """
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    # Example usage
    original_text = "Functional Programming!"
    shift_value = 5

    # Encrypt
    encrypted_text = caesar_encrypt(original_text, shift_value)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}")

    # Decrypt
    decrypted_text = caesar_decrypt(encrypted_text, shift_value)
    print(f"Decrypted: {decrypted_text}")
