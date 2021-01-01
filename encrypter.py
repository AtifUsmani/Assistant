from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
def encrypt(message):
    # token = f.encrypt(b"A really secret message. Not for prying eyes.")
    token = f.encrypt(message)
    print(token)

def decrypt(token):
    decrypted = f.decrypt(token)
    print(decrypted)