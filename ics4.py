import random

def generate_key_pair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = choose_coprime(phi_n)
    d = modinv(e, phi_n)
    public_key = (n, e)
    private_key = (n, d)
    return private_key, public_key

def generate_prime_number():
    while True:
        num = random.getrandbits(10) + 1024
        if is_prime(num):
            return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def choose_coprime(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            return e

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt_message(public_key, message):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt_message(private_key, ciphertext):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    message = "My name is Kanishk Singhania."
    ciphertext = encrypt_message(public_key, message)
    print(f"Ciphertext: {ciphertext}")
    decrypted_message = decrypt_message(private_key, ciphertext)
    print(f"Decrypted Message: {decrypted_message}")
