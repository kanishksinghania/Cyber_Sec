def s_box_substitution(input_val):
    s_box = [
        [9, 4, 10, 11],
        [13, 1, 8, 5],
        [6, 2, 0, 3],
        [12, 14, 15, 7]
    ]
    row = int(input_val[0], 2)
    col = int(input_val[1:], 2)
    return format(s_box[row][col], '04b')

def round_key_generation(key, round_num):
    round_keys = []
    key_parts = [key[:8], key[8:]]
    for i in range(round_num):
        key_parts[1] = key_parts[1][1:] + key_parts[1][0]
        round_key = key_parts[0] + key_parts[1]
        round_keys.append(round_key)
    return round_keys

def add_round_key(state, round_key):
    return format(int(state, 2) ^ int(round_key, 2), '08b')

def substitution_bytes(state):
    return ''.join(s_box_substitution(state[i:i + 4]) for i in range(0, 8, 4))

def permutation_nibble(state):
    return state[2:] + state[:2]

def s_aes_encrypt(plaintext, key):
    round_keys = round_key_generation(key, 2)
    state = plaintext
    for round_key in round_keys:
        state = add_round_key(state, round_key)
        state = substitution_bytes(state)
        state = permutation_nibble(state)
    state = add_round_key(state, round_keys[-1])
    return state

if __name__ == "__main__":
    plaintext = "11010001"
    key = "1010000010011010"
    
    ciphertext = s_aes_encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
