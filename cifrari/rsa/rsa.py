"""
TODO:
- generate primes (miller-rabin)
"""

from utils import lcm, cir, mpow
from sys import argv

def keygen(p, q):
    """
    Generate RSA keypairs
    """

    # Step 1
    n = p * q           

    # Step 2 
    m = lcm(p-1, q-1)
    m = int(m)

    # Step 3 -> 1 < c < m | gcd(c, m) = 1
    c = cir(2, m, m)

    # Step 4 -> 0 <= d < m | (cd) % m = 1
    d = [i for i in range(0, m) if (c * i) % m == 1][0]

    # private, public
    return (n, d), (n, c)

# TODO handle x >= n
def encrypt(x, key):
    """
    Encrypt a numeric sequence
    """
    n, c = key
    return mpow(x, c, n)

def decrypt(x, key):
    """
    Decrypt a numeric sequence
    """
    n, d = key
    return mpow(x, d, n)

# TODO split string in biggest chunks possible with the given n
def encrypt_str(msg, key):
    """
    Encrypt a string
    """
    return (encrypt(ord(c), key) for c in msg)

def decrypt_str(encrypted, key):
    """
    Decrypt an encrypted string
    """
    return ''.join(chr(decrypt(c, key)) for c in encrypted)

if __name__ == "__main__":
    msgd = 'big nose :==), unicode certified ©'
    msg = ' '.join(argv[1:]) if len(argv) > 1 else msgd

    print('Generating keys ...')
    priv, pub = keygen(577, 59)

    print(f'Encrypting `{msg}` ...')
    encrypted = encrypt_str(msg, pub)

    print('Decrypting ...')
    decrypted = decrypt_str(encrypted, priv)

    if decrypted == msg:
        print(f'OK')
    else:
        print('FAILED')
