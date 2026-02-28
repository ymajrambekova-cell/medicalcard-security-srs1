class CaesarCipher:
    def __init__(self, shift: int = 4):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        result = ""
        for char in text:
            result += chr((ord(char) + self.shift) % 65535)
        return result

    def decrypt(self, text: str) -> str:
        result = ""
        for char in text:
            result += chr((ord(char) - self.shift) % 65535)
        return result


def main():
    cipher = CaesarCipher()

    password = input("Введите пароль: ")

    encrypted = cipher.encrypt(password)
    print("Зашифрованный пароль:", encrypted)

    decrypted = cipher.decrypt(encrypted)
    print("Расшифрованный пароль:", decrypted)


if __name__ == "__main__":
    main()