import secrets
import string

def secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

print("Secure Password:", secure_password(16))
