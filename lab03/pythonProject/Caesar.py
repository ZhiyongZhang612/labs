class Caesar:
    def __init__(self,shift):
        self.shift=shift
    def encrypt(self,plain_text):
            encrypted_text =""
            for char in plain_text:
                if char.isalpha():
                    ascii_set = 65 if char.isupper() else 97
                    encrypted_char = chr((ord(char) - ascii_set + self.shift) % 26 + ascii_set)
                    encrypted_text+=encrypted_char
                else: encrypted_text += char
            return encrypted_text
    def decrypt(self,cipher_text):
        decrypted_text=""
        for char in decrypted_text:
            if char.isalpha():
                ascii_set = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_set - self.shift) % 26 + ascii_set)
                decrypted_text += decrypted_char
            else: decrypted_text += char
        return decrypted_text

cipher=Caesar(3)
print(cipher.encrypt("Hello, World!"))
print(cipher.decrypt("KHOOR zruog$"))

cipher=Caesar(6)
print(cipher.encrypt("zzz")) #prints “fff”
print(cipher.decrypt("FFF")) #prints “zzz”

cipher=Caesar(-6) # Negative keys should be supported!
print(cipher.encrypt("FFF")) #prints “zzz





