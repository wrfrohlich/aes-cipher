import hashlib
import binascii
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher():
    def __init__(self):
        self.bs = 16

    def is_hex(self, value):
        """
        Retorna True se a string representa um valor hexadecimal válido.
        """
        try:
            int(value, 16)
            return True
        except ValueError:
            return False

    def encrypt(self, mode, key, text):
        plaintext = ' '.join(text)
        if self.is_hex(key):
            key = binascii.unhexlify(key)
        else:
            key = hashlib.sha256(key.encode()).digest()
        if mode.upper() == "CBC":
            pad = self.bs - len(plaintext) % self.bs
            plaintext += pad * chr(pad)
            iv = Random.new().read(self.bs)
            cipher = AES.new(key, AES.MODE_CBC, iv)
        elif mode.upper() == "CTR":
            cipher = AES.new(key, AES.MODE_CTR)
        ciphertext = cipher.encrypt(plaintext.encode())
        if mode.upper() == "CBC":
            data = {
                    'key': binascii.hexlify(key).decode(),
                    'iv': binascii.hexlify(iv).decode(),
                    'ciphertext': binascii.hexlify(ciphertext).decode()
            }
        elif mode.upper() == "CTR":
            data = {
                    'key': binascii.hexlify(key).decode(),
                    'ciphertext': binascii.hexlify(ciphertext).decode()
            }
        else:
            data = None
        return data

    def decrypt(self, mode, key, ciphertext):
        try:
            key = binascii.unhexlify(key)
            ciphertext = binascii.unhexlify(ciphertext)
            if mode.upper() == "CBC":
                iv = ciphertext[:self.bs]
                ciphertext = ciphertext[self.bs:]
                cipher = AES.new(key, AES.MODE_CBC, iv)
            elif mode.upper() == "CTR":
                cipher = AES.new(key, AES.MODE_CTR)
            return cipher.decrypt(ciphertext).decode('utf-8')
        except (ValueError, KeyError):
            return None
