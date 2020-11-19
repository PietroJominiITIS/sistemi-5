"""
When encrypting with rsa I can have values ranging up to n,
often n being a rather large integer. By converting each character 
of a string I convert a set of relatively small integers.
I then pack them into blocks of k bytes, dynamically calculating k
based on n, to always convert the largest possible numbers and reduce
computation time.

Knowing that the python's chars range from 1 to 4 bytes I can safely
convert a string into a set of 4-byte integers. I can then pack the
resulting byte array using bitwise shifts.

The unpacking procedure is similar.
"""

from functools import reduce

def pack(l, size):
    """Pack a bytearray in chunks of s bytes"""
    for i in range(0, len(l), size):
        c = l[i:i+size]
        if len(c) < size:
            k = [0]*size
            k[-len(c):] = c
            c = k
        yield reduce(lambda a, b: a << 8 | b, c)

def unpack(chunks, size):
    """Unpack a bytearray from chunks of n bytes"""
    bts = bytearray()
    for c in chunks:
        b = []
        for _ in range(size):
            b.append(c & 0xff)
            c = c >> 8
        # bts.extend(filter(lambda a: a != 0, reversed(b)))
        bts.extend(reversed(b))
    return bts

def computed_size(n):
    """Compute optimal chunks size"""
    i = 0
    while 2**(8*i) - 1 < n:
        i += 1
    return i - 1
