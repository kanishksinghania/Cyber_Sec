import hashlib

def calculate_hash(message):
    hash_object = hashlib.sha256()
    hash_object.update(message)
    return hash_object.hexdigest()

if __name__ == "__main__":
    message = b"Hello, this is a message for integrity checking."
    
    hash_value = calculate_hash(message)
    print(f"Hash Value: {hash_value}")
