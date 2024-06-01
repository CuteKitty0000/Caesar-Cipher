import string

print('''  _  _______ _______ _________     ___  _________     _______ _______ 
 | |/ / _   _|__   __|__   __\ \   / / |/ /  __ \ \   / /  __ \__   __|
 | ' /  | |    | |     | |   \ \_/ /| ' /| |__) \ \_/ /| |__) | | |   
 |  <   | |    | |     | |    \   / |  < |  _  / \   / |  ___/  | |   
 | . \ _| |_   | |     | |     | |  | . \| | \ \  | |  | |      | |   
 |_|\_\_____|  |_|     |_|     |_|  |_|\_\_|  \_\ |_|  |_|      |_|   
      
by https://github.com/CuteKitty0000
                                                                      
                                                                      ''')

class CaesarCipher:
    def __init__(self):
        self.shift = None

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + self.shift) % 26 + base)
            else:
                result += char
        return result

    def decrypt(self, text):
        return self.encrypt(text)

def main():
    cipher = CaesarCipher()

    choice = input("What you want to do encrypt or decrypt (e / d): ").lower()

    if choice not in ['e', 'd']:
        print("meow! Please type 'e' for 'encrypt' or 'd' for 'decrypt'.")
        return

    message = input("message to hide: ")

    shift_str = input("Enter the shift value (an integer): ")
    if not shift_str.isdigit():
        print("Invalid shift value! Please enter an integer.")
        return
    shift = int(shift_str) % 26

    cipher.shift = shift

    if choice == 'e':
        print("Encrypted message:", cipher.encrypt(message))
    else:
        print("Decrypted message:", cipher.decrypt(message))

if __name__ == "__main__":
    main()
