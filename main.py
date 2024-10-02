from cryptography.fernet import Fernet
from sys import exit as endProgram

def genKey():
    """This generates a random usable key for the cryptography library and returns it"""
    key = Fernet.generate_key()
    return key.decode('utf-8')

def encryptWithKey(key: str, msg: str):
    """Encrypt a message with a given key."""
    fernet = Fernet(key.encode('utf-8'))
    encMsg = fernet.encrypt(msg.encode())
    return encMsg.decode('utf-8')

def decryptWithKey(key: str, encMsg: str):
    """Decrypt a message with a given key."""
    fernet = Fernet(key.encode())
    decMsg = fernet.decrypt(encMsg.encode('utf-8'))
    return decMsg.decode('utf-8')

if __name__ == "__main__":
    userKey = input("--Provide the key for decryption. Leave empty if you'd like a new key--\n")

    if userKey == "":
        # Return a key for future usage if none is provided
        newKey = genKey()
        print("--You didn't input any key--\n--Here's a new key for decryption--\n", newKey)
    operation = ""
    validOp = False
    while (validOp == False):
        operation = input("--Would you like encrypt or decrypt a message? (encrypt/decrypt/generate/quit)--\n").lower()
        match operation:
            case "encrypt":
                validOp = True
                userInput = input("--Type in the message you'd like to encrypt--\n")
                print("--Here's the encrypted message--")
                print(encryptWithKey(userKey, userInput))
            case "decrypt":
                validOp = True
                userInput = input("--Type in the message you'd like to decrypt--\n")
                print("--Here's the decrypted message--")
                print(decryptWithKey(userKey, userInput))
            case "generate":
                validOp = True
                print("--Here's the generated key--")
                print(genKey())
            case "quit":
                validOp = True
                print("--Ending the program--")
                endProgram()
            case _:
                print("--That's not an option, try again--")