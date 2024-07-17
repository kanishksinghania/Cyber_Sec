from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_key_pair():
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message, hashes.SHA256())
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message, hashes.SHA256())
        print("Signature is valid.")
    except Exception as e:
        print(f"Signature is invalid: {e}")

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    message = b"Hello, this is a message to be signed."
    
    signature = sign_message(private_key, message)
    print("Message signed.")
    
    verify_signature(public_key, message, signature)
