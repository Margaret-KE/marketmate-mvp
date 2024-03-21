# secret_key.py

from django.core.management.utils import get_random_secret_key

def generate_secret_key():
    secret_key = get_random_secret_key()
    with open('.env', 'a') as f:
        f.write(f'SECRET_KEY={secret_key}\n')

if __name__ == '__main__':
    generate_secret_key()

