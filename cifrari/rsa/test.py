"""
p = 20089, q = 20101
-> max chunks size 3
   more than that is technically incorrect
   and i'm not sure their bench can be considered 
   correct as well

| ch | dect |
| -- | ---- |
|  1 | 48.9 |
|  2 | 24.3 |
|  3 | 16.8 |
|  4 | 12.8 |
|  5 | 10.6 |
|  6 |  8.1 |

not very deterministic, i guess
python's chaching is helping as well,
it definitely do with key generation,
but it's good to see that chunking somehow helps
"""

from rsa import keygen, encrypt_packed, decrypt_packed
from time import time
from sys import argv

if __name__ == "__main__":
    msgd = 'big nose :==), unicode certified こんにちは'
    msg = ' '.join(argv[1:]) if len(argv) > 1 else msgd
    msg = bytearray(msg.encode())
    size = None

    print('Generating keys... ')
    strt = time()
    priv, pub = keygen(20089, 20101)
    # priv, pub = keygen(15226050279225333605356183781326374297180681149613, 80688657908494580122963258952897654000350692006139)
    print(f'\tin {round(time() - strt, 3)}s')

    print('Encrypting... ')
    strt = time()
    encrypted = encrypt_packed(msg, pub, size)
    print(f'\tin {round(time() - strt, 3)}s')

    print('Decrypting... ')
    strt = time()
    decrypted = decrypt_packed(encrypted, priv, size)
    print(f'\tin {round(time() - strt, 3)}s')

    print(decrypted.decode())
