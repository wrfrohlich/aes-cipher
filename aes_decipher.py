
from sys import argv
from aes import AESCipher

if __name__ == '__main__':
    print()
    if len(argv) <= 3:
        print("Please, insert the operation mode, key, and plaintext")
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