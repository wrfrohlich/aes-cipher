
import binascii
from sys import argv
from Crypto.Cipher import AES

class AESCipher():
    def __init__(self):
        self.bs = 16

    def decrypt(self, mode, key, ciphertext):
        try:
            key = binascii.unhexlify(key)
            ciphertext = binascii.unhexlify(ciphertext)
            if mode.upper() == "CBC":
                iv = ciphertext[:self.bs]
                ciphertext = ciphertext[self.bs:]
                cipher = AES.new(key, mode, iv)
            elif mode.upper() == "CTR":
                cipher = AES.new(key, mode)
            return cipher.decrypt(ciphertext).decode('utf-8')
        except (ValueError, KeyError):
            return None

if __name__ == '__main__':
    print()
    if len(argv) <= 3:
        print("Please, insert the operation mode, key, and ciphertext")
    else:
        if argv[1].upper() != "CBC" and argv[1].upper() != "CTR":
            print("Please, insert the operation mode [ CBC | CTR ]")
            exit()
        aes = AESCipher()
        plaintext = aes.decrypt(argv[1], argv[2], argv[3])
        if plaintext is None:
            print("Incorrect decryption")
        else:
            print(plaintext)
