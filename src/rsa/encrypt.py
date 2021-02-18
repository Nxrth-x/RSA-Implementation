import traceback

def encrypt(message: str, key: list) -> str:
    """Encrypts a message using the public keys

    Args:
        message (str): Message to be encrypted
        key (list): Public key to encrypt the message with

    Raises:
        Exception: Raises an exception if the encryption process fails

    Returns:
        str: Encrypted version of the original string
    """
    try:
        return "g".join([hex(pow(ord(letter), int(key[0]), int(key[1])))[2:] for letter in message])
    except Exception as e:
        raise Exception(f"Error whilst trying to encrypt the message, error: {e}")


def decrypt(message: str, key: list) -> str:
    """Decrypts a message using the private keys

    Args:
        message (str): Encrypted message to be decrypted
        key (list): Private key to decrypt the message

    Raises:
        Exception: Raises an excepton if the decryption process fails

    Returns:
        str: Decrypted version of the encrypted string
    """
    try:
        arr: list = message.split("g")
        message: str = "".join([chr(pow(int(element, 16), int(key[0]), int(key[1]))) for element in arr])
        return message    
    except Exception as e:
        traceback.print_exc()
        raise Exception(f"Error whilst trying to encrypt the message, error: {e}")
