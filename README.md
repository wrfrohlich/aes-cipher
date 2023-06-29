# aes-cipher
AES - Advanced Encryption Standard

Algorithm encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR).
In all cases the 16-byte encryption IV is chosen at random and is prepended to the ciphertext.
For CBC encryption PKCS5 padding scheme was used. Implement both encryption and decryption.
In the following questions were given an AES key and a ciphertext/plaintext (all are hex encoded) and the goal is to recover the plaintext and enter it in the input boxes provided below.

## Tasks:

### Task 1:
* CBC key:
```
140b41b22a29beb4061bda66b6747e14
```

* CBC Ciphertext:
```
4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81
```

### Task 2:
* CBC key:
```
140b41b22a29beb4061bda66b6747e14
```

* CBC Ciphertext:
```
5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253
```

### Task 3:
* CTR key:
```
36f18357be4dbd77f050515c73fcf9f2
```

* CTR Ciphertext:
```
69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329
```

### Task 4:
* CTR key:
```
36f18357be4dbd77f050515c73fcf9f2
```

* CTR Ciphertext:
```
770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451
```

### Task 5:
* CTR key:
```
36f18357be4dbd77f050515c73fcf9f2
```

* CTR Plaintext:
```
5468697320697320612073656e74656e636520746f20626520656e63727970746564207573696e672041455320616e6420435452206d6f64652e
```

### Task 6:
* CBC key:
```
140b41b22a29beb4061bda66b6747e14
```

* CBC Plaintext:
```
4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e
```

## Commands:
### Encryption:
Encrypt AES CBC:
```
python3 aes_cipher.py CBC 140b41b22a29beb4061bda66b6747e14 4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e
```

Encrypt AES CBC:
```
python3 aes_cipher.py CBC MyKey Hello World it is a crypto test
```

Encrypt AES CTR:
```
python3 aes_cipher.py CTR 36f18357be4dbd77f050515c73fcf9f2 5468697320697320612073656e74656e636520746f20626520656e63727970746564207573696e672041455320616e6420435452206d6f64652e
```

Encrypt AES CTR:
```
python3 aes_cipher.py CTR MyKey Hello World it is a crypto test
```

### Decryption:
Decrypt AES CBC:
```
python3 aes_decipher.py CBC 140b41b22a29beb4061bda66b6747e14 4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81
```

Decrypt AES CBC:
```
python3 aes_decipher.py CBC 347b261d0165818507e780223d9fcbd6b8036544b3373ba419b092132c9d09db 75fd27bad9e9f118ac7a138ed04615e966bd09192410c5aed330e01ed8d60aa78487785478c0f63e7272e9e094dd26ac
```

Decrypt AES CTR:
```
python3 aes_decipher.py CTR 36f18357be4dbd77f050515c73fcf9f2 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329
```

Decrypt AES CTR:
```
python3 aes_decipher.py CTR 347b261d0165818507e780223d9fcbd6b8036544b3373ba419b092132c9d09db 4c0673306ca4c48785381726e95d7061a9af357c5b7e4a893df6d110e8645eb05f67fcd006bce408fe422fcf61f25f
```