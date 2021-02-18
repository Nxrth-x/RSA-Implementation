import time
import random
import rsa

def generate_random_word():
    return "".join([chr(random.randint(16, 512)) for i in range(random.randint(16, 255))])

def test_encrypt_and_decrypt_function():
    for _ in range(1, 512):
        public, private = rsa.generate_keys()
        original = generate_random_word()
        encrypted = rsa.encrypt(original, public)
        decrypted = rsa.decrypt(encrypted, private)

        assert original == decrypted
