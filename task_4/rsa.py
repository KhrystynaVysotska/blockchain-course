from math import gcd


def get_e(n, phi):
    for potential_e in reversed(range(3, n)):
        if gcd(potential_e, phi) == 1:
            return potential_e


def get_d(e, n, phi):
    for potential_d in reversed((range(3, n))):
        if (potential_d * e) % phi == 1:
            return potential_d


def key_gen():
    p = 7237
    q = 6823

    n = p * q
    phi = (p - 1) * (q - 1)

    print("Started public key generation...")
    e = get_e(n, phi)

    print("Started private key generation...")
    d = get_d(e, n, phi)

    return n, e, d


def encrypt(number, e, n):
    return pow(number, e, n)


def decrypt(cipher, d, n):
    return pow(cipher, d, n)


if __name__ == "__main__":
    while True:
        option = input("Type e for encrypting, d for decrypting, g for keygen: ")

        if option == 'd':
            message = int(input("message = "))
            public_key_n = int(input("n = "))
            public_key_d = int(input("d = "))

            decrypted = decrypt(message, public_key_d, public_key_n)
            print(f"Encrypted: {decrypted}")
        elif option == 'e':
            message = int(input("message = "))
            private_key_n = int(input("n = "))
            private_key_e = int(input("e = "))

            encrypted = encrypt(message, private_key_e, private_key_n)
            print(f"Encrypted: {encrypted}")
        elif option == 'g':
            n, e, d = key_gen()

            print(f"n={n}")
            print(f"e={e}")
            print(f"d={d}")
