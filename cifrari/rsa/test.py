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

from rsa import keygen, encrypt_packed, decrypt_packed, encrypt_array, decrypt_array
from time import time
from sys import argv

target = 'big nose :==), unicode certified こんにちは'
btarget = bytearray(target.encode())

def test_array(priv, pub):
    start = time()
    print('\tEncryption...', end='')
    encrypted = encrypt_array(btarget, pub)
    print(f'\r\tEncrypted in {round(time() - start, 4)}')

    start = time()
    print('\tDecription...', end='')
    decrypted = decrypt_array(encrypted, priv)    
    print(f'\r\tDecripted in {round(time() - start, 4)}')

    print('\tOK' if bytearray(decrypted).decode() == target else 'FAILED')

def test_chunk(priv, pub):
    start = time()
    print('\tEncryption...', end='')
    encrypted = encrypt_packed(btarget, pub)
    print(f'\r\tEncrypted in {round(time() - start, 4)}')

    start = time()
    print('\tDecription...', end='')
    decrypted = decrypt_packed(encrypted, priv)    
    print(f'\r\tDecripted in {round(time() - start, 4)}')

    print('\tOK' if decrypted.decode() == target else 'FAILED')


def test_all():
    print('Generating keys')
    start = time()
    priv, pub = keygen(20089, 20101)
    print(f'\tin {round(time() - start, 3)}s')

    print('Testing array')
    test_array(priv, pub)

    print('Testing chunk')
    test_chunk(priv, pub)

if __name__ == "__main__":
    test_all()