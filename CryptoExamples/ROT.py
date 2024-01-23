from typing import List


ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
    '^', '_', '`', '{', '|', '}', '~', 'ñ', 'Ñ',
]


def encrypt(message: str, password: int) -> str:
    encrypted_chars = []
    for char in message:
        if char in ALPHABET:
            encrypted_chars.append(ALPHABET[(ALPHABET.index(char) + password) % len(ALPHABET)])
        else:
            encrypted_chars.append(char)
    return "".join(encrypted_chars)


# equivalent to encrypt() with password = -password
def decrypt(message: str, password: int) -> str:
    encrypted_chars = []
    for char in message:
        if char in ALPHABET:
            encrypted_chars.append(ALPHABET[(ALPHABET.index(char) - password) % len(ALPHABET)])
        else:
            encrypted_chars.append(char)
    return "".join(encrypted_chars)


def encrypt(message: bytes, password: int) -> bytes:
    encryped_bytes = []
    for byte in message:
        encryped_bytes.append((byte + password) % 256)
    return encryped_bytes


# equivalent to encrypt() with password = -password
def decrypt(message: bytes, password: int) -> bytes:
    encryped_bytes = []
    for byte in message:
        encryped_bytes.append((byte - password) % 256)
    return encryped_bytes
