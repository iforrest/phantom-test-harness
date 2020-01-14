from cryptography.fernet import Fernet

cipher_suite = Fernet(Fernet.generate_key())

def encrypt(stuff):
    return cipher_suite.encrypt(stuff)

def decrypt(stuff):
    return cipher_suite.decrypt(stuff)