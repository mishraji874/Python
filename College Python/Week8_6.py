def caesar_cipher_encrypt(message, shift):
    message = message.upper()

    def shift_char(char):
        if char.isalpha():
            code = ord(char) - ord('A')

            shifted_code = (code + shift) % 26

            return chr(shifted_code + ord('A'))
        else:
            return char

    encrypted_message = ''.join(map(shift_char, message))

    return encrypted_message

message = "SECRET MESSAGE"
shift = 3
encrypted_message = caesar_cipher_encrypt(message, shift)
print(encrypted_message)