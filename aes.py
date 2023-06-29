from hashlib import sha256
from binascii import hexlify, unhexlify
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Counter import new
from Crypto.Util.Padding import pad, unpad

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

    def conv_text(self, plaintext):
        if self.is_hex(plaintext):
            byte_string = unhexlify(plaintext)
            plaintext = byte_string.decode('utf-8')
        print("Plaintext: %s" % plaintext)
        plaintext = plaintext.encode('utf-8')
        return plaintext

    def conv_key(self, key):
        if self.is_hex(key):
            key = unhexlify(key)
        else:
            key = sha256(key.encode()).digest()
        return key

    def unpadding(self, mode, plaintext):
        if mode.upper() == "CBC":
            plaintext = unpad(plaintext, self.bs)
        return plaintext

    def get_cbc_cipher(self, key, iv):
        return AES.new(key, AES.MODE_CBC, iv)

    def get_ctr_cipher(self, key, iv):
        counter = new(128, initial_value=int.from_bytes(iv, byteorder='big'))
        return AES.new(key, AES.MODE_CTR, counter=counter)

    def encrypt(self, mode, key, text):
        plaintext = ' '.join(text)
        plaintext = self.conv_text(plaintext)
        key = self.conv_key(key)
        iv = Random.new().read(self.bs)
        if mode.upper() == "CBC":
            plaintext = pad(plaintext, self.bs)
            cipher = self.get_cbc_cipher(key, iv)
        elif mode.upper() == "CTR":
            cipher = self.get_ctr_cipher(key, iv)
        else:
            exit("Operation Mode not supported")
        ciphertext = cipher.encrypt(plaintext)
        data = {
            'key': hexlify(key).decode(),
            'ciphertext': hexlify(iv + ciphertext).decode()
        }
        return data

    def decrypt(self, mode, key, ciphertext):
        key = unhexlify(key)
        ciphertext = unhexlify(ciphertext)
        iv = ciphertext[:self.bs]
        ciphertext = ciphertext[self.bs:]
        if mode.upper() == "CBC":
            cipher = self.get_cbc_cipher(key, iv)
        elif mode.upper() == "CTR":
            cipher = self.get_ctr_cipher(key, iv)
        else:
            exit("Operation Mode not supported")
        plaintext = cipher.decrypt(ciphertext)

        plaintext = self.unpadding(mode, plaintext)
        return plaintext.decode('utf-8')
