ROUNDS_NUMBER = 80

H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0


def f(t: int, x: int, y: int, z: int) -> int:
    if 0 <= t <= 19:
        return (x & y) | ((~x) & z)
    if 20 <= t <= 39:
        return x ^ y ^ z
    if 40 <= t <= 59:
        return (x & y) | (x & z) | (y & z)
    if 60 <= t <= 79:
        return x ^ y ^ z


def k(t: int) -> int:
    if 0 <= t <= 19:
        return 0x5a827999
    if 20 <= t <= 39:
        return 0x6ed9eba1
    if 40 <= t <= 59:
        return 0x8f1bbcdc
    if 60 <= t <= 79:
        return 0xca62c1d6
