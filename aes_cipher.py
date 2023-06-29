from sys import argv
from aes import AESCipher

if __name__ == '__main__':
    print()
    args = len(argv)
    if args <= 3:
        print("Please, insert the operation mode, key, and ciphertext")
    else:
        if argv[1].upper() != "CBC" and argv[1].upper() != "CTR":
            print("Please, insert the operation mode [ CBC | CTR ]")
            exit()
        aes = AESCipher()
        ciphertext = aes.encrypt(argv[1], argv[2], argv[3:args])
        if ciphertext is None:
            print("Incorrect encryption")
        else:
            print("Key: %s" % ciphertext.get("key", "-"))
            print("Ciphertext: %s" % ciphertext.get("ciphertext", "-"))
