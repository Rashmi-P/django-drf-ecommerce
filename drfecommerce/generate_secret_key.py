from django.utils.crypto import get_random_string

def get_secret_key():
    chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*(-_+=)"
    return get_random_string(50, chars)

secret_key = get_secret_key()
print(secret_key)
