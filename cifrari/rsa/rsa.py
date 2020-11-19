"""
TODO:
- generate primes (miller-rabin)
"""

from utils import lcm, cir, mpow
from packed import pack, unpack, computed_size
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

def encrypt_packed(l, key):
    n, _ = key
    size = computed_size(n)
    data = pack(l, size)
    return (encrypt(c, key) for c in data)

def decrypt_packed(l, key):
    n, _ = key
    size = computed_size(n)
    data = (decrypt(c, key) for c in l)
    return unpack(data, size)

if __name__ == "__main__":
    msgd = 'big nose :==), unicode certified こんにちは'
    msg = ' '.join(argv[1:]) if len(argv) > 1 else msgd

    print('Generating keys ...')
    priv, pub = keygen(20089, 20101)

    print('Encrypting...')
    encrypted = encrypt_packed(bytearray(msg.encode()), pub)

    print('Decrypting...')
    decrypted = decrypt_packed(encrypted, priv).decode()

    print(decrypted)