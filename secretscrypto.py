import hashlib
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def hash_secret(password, algorithm='sha512'):

    # Convert password string to bytes
    password_bytes = password.encode('utf-8')

    # Create SHA-256 hash object
    if algorithm == 'sha256' :

        sha256_hash = hashlib.sha256()

        # Update the hash object with the password bytes
        sha256_hash.update(password_bytes)

        # Get the hexadecimal representation of the hash
        hashed_password = sha256_hash.hexdigest()

    elif algorithm == 'sha512' :

        sha512_hash = hashlib.sha512()

        sha512_hash.update(password_bytes)

        hashed_password = sha512_hash.hexdigest()

    return hashed_password


def secret_crypto_action(origin_key, password, action):

    # Convert the provided SHA-256 key to bytes
    key_bytes = bytes.fromhex(origin_key)

    # Derive a 32-byte key using PBKDF2 with 100,000 iterations
    kdf = PBKDF2HMAC(
        backend=default_backend() ,
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'',
        iterations=100000
        )

    derived_key = base64.urlsafe_b64encode(kdf.derive(key_bytes))

    # Create Fernet cipher instance using the derived key
    cipher = Fernet(derived_key)

    # Encrypt/Decrypt the password using the cipher

    if action == 'encrypt' :

        return cipher.encrypt(str(password).encode())

    elif action == 'decrypt' :

        return cipher.decrypt(str(password).encode('utf-8'))

    return '(Error) Invalid Argument: Action'
