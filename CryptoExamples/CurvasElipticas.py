import base64
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey

def encrypt(data: bytes, password: bytes):
    encrypted_array: list = []
    i=0
    for d in data:
        encrypted_array.append(((d + password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(encrypted_array)

def decrypt(data: bytes, password: bytes):
    decrypted_array: list = []
    i=0
    for d in data:
        decrypted_array.append(((d - password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(decrypted_array)

def write(data: bytes, path: str):
    with open(path, "wb") as file:
        file.write(data)

def read(path: bytes):
    with open(path, "rb") as file:
        return file.read()

def genKeyPair():
    kp = SigningKey.generate()
    return kp._seed

def bytesToString(data: bytes):
    return base64.encodebytes(data).decode("utf-8")

def stringToBytes(data: str):
    return base64.decodebytes(data.encode("utf-8"))

def sign(msg: str, seed: bytes):
    sign_key = SigningKey(seed)
    signed_raw = sign_key.sign(msg.encode("utf-8"))
    return signed_raw

def register(username: str, password: str):
    seed: bytes = genKeyPair()
    signed: dict = sign(username, seed)
    write(encrypt(seed, password.encode("utf-8")), f"{username}.key")
    print(signed)
    write(signed, f"{username}.cer")

def login(user: str, password: str):
    seed: bytes = decrypt(read(f"{user}.key"), password.encode("utf-8"))
    signed_raw: bytes = read(f"{user}.cer")
    print(signed_raw)
    verify_key = SigningKey(seed).verify_key
    print(verify_key._key)
    try:        
        verify_key.verify(signed_raw)
        return True
    except BadSignatureError:
        return False