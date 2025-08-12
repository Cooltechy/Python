#Program to encrypts a message by adding a key value to each character
def encrypt_message(message, key):
    encrypted_message = ''.join(chr(ord(char) + key) for char in message)
    return encrypted_message    

if __name__ == "__main__":
    message = input("Enter a message to encrypt: ")
    key = int(input("Enter a key value (integer): "))
    encrypted_message = encrypt_message(message, key)
    print("Encrypted message:", encrypted_message)

    