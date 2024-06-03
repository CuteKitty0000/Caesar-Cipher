import string

print('''  _  _______ _______ _________     ___  _________     _______ _______ 
 | |/ / _   _|__   __|__   __\ \   / / |/ /  __ \ \   / /  __ \__   __|
 | ' /  | |    | |     | |   \ \_/ /| ' /| |__) \ \_/ /| |__) | | |   
 |  <   | |    | |     | |    \   / |  < |  _  / \   / |  ___/  | |   
 | . \ _| |_   | |     | |     | |  | . \| | \ \  | |  | |      | |   
 |_|\_\_____|  |_|     |_|     |_|  |_|\_\_|  \_\ |_|  |_|      |_|   
      
by https://github.com/CuteKitty0000
                                                                      
                                                                      ''')

class CC:
    def __init__(self, s=0):
        self.s = s

    def e(self, t):
        r = ""
        for c in t:
            if c.isalpha():
                b = ord('A') if c.isupper() else ord('a')
                r += chr((ord(c) - b + self.s) % 26 + b)
            else:
                r += c
        return r

    def d(self, t):
        r = ""
        for c in t:
            if c.isalpha():
                b = ord('A') if c.isupper() else ord('a')
                r += chr((ord(c) - b - self.s) % 26 + b)
            else:
                r += c
        return r

def main():
    c = CC()
    ch = input("e for encrypt, d for decrypt ( e / d ) : ").lower()
    if ch not in ['e', 'd']:
        print("Meow!, pls enter 'e' for encrypt, 'd' for decrypt")
        return

    m = input("msg to encrypt : ")
    ss = input("shift: ")
    if not ss.isdigit():
        print("Meow!, shift must be an integer")
        return
    s = int(ss) % 26
    c.s = s

    if ch == 'e':
        print("encrypted msg : ", c.e(m))
    else:
        print("decrypted msg : ", c.d(m))

if __name__ == "__main__":
    main()
