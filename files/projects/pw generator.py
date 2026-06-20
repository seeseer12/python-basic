import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

print("Strong Password:", generate_password(16))
