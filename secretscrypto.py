from cryptography.fernet import Fernet
import hashlib

def hash_secret(password):

    # Convert password string to bytes
    password_bytes = password.encode('utf-8')

    # Create SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password


def encrypt_secret(master_password_from_db, secret) :
    return  secret

