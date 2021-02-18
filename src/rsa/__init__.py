import random
from rsa.keys import define_e, define_d
from rsa.encrypt import encrypt, decrypt
from rsa.utils import PRIMES as primes

def generate_keys() -> tuple:
    """Generates a pair of keys to encrypt messages

    Returns:
        tuple: Tuple containing both the public and private key
    """
    p = int(primes[random.randint(1, len(primes) - 1)])
    q = int(primes[random.randint(1, len(primes) - 1)])

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = define_e(phi_n)
    public = (e, n)

    d = define_d(e, phi_n)
    private = (d, n)

    return public, private
