def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Shift the character by the key value (Caesar cipher)
            shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Reverse the shift to decrypt the character
            original_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            decrypted_text += original_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
key = 3
message = "hello world 123"
encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
