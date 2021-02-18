import random, math

def define_d(e: int, phi_n: int) -> int:
    """Generates D, which is a number that satisfies the condition "(d * e) % n == 1"

    Args:
        e (int): A value generated using the define_e function that satisfies the condition "1 < e < phi_n"
        phi_n (int): A value generated using the original prime numbers that is "(p - 1) * (q - 1)"

    Returns:
        int: A value that satisfies the condition "(d * e) % n == 1"
    """
    phi_aux = phi_n

    x, old_x = 0, 1
    y, old_y = 1, 0

    while(phi_n != 0):
        quotient = e // phi_n
        e, phi_n = phi_n, e - quotient * phi_n
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return old_x if old_x >= 0 else old_x + phi_aux


def define_e(phi_n: int) -> int:
    """Generates a number that is between 1 < e < phi_n and checks if it is coprime with phi_n

    Args:
        phi_n (int): A value generated using the original prime numbers that is "(p - 1) * (q - 1)"

    Returns:
        int: A value that satisfies the condition "1 < e < phi_n"
    """
    while(True):
        e = random.randint(2, phi_n - 1)
        if(math.gcd(e, phi_n) == 1):
            return e
