def prepare_key(key):
    key = key.replace(" ", "").upper()
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    key = key.replace("J", "I")  # Replace J with I
    return key

def generate_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [[""] * 5 for _ in range(5)]  # Initialize with empty strings
    key_index = 0

    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                while alphabet:
                    char = alphabet[0]
                    alphabet = alphabet[1:]
                    if char not in "".join(matrix[i] + matrix[j]):
                        matrix[i][j] = char
                        break

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    key = prepare_key(key)
    matrix = generate_matrix(key)
    ciphertext = ""
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = plaintext.replace("J", "I")

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = ""
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]

        if char1 == char2:
            char2 = "X"
            i += 1

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ciphertext += matrix[row1][col1] + matrix[row2][col2]
        i += 2

    return ciphertext

# Example usage for encryption:
key = "KEYWORD"
plaintext = "HELLO WORLD"
encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
