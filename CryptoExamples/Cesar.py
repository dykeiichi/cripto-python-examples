from CryptoExamples import ROT

def encrypt(message: str) -> str:
    return ROT.encrypt(message, 3)

def decrypt(message: str) -> str:
    return ROT.decrypt(message, 3)

def encrypt(message: bytes) -> bytes:
    return ROT.encrypt(message, 3)

def decrypt(message: bytes) -> bytes:
    return ROT.decrypt(message, 3)