import random


class StreamCipher:
    def __init__(self):
        self.a = 55
        self.b = 24
        self.n = 32
        self.key = ""

    def generate_key(self, text_key):
        self.key = text_key

    def encrypt(self, plaintext):
        encrypted_text = ''
        key_length = len(self.key)
        for i in range(len(plaintext)):
            encrypted_text += chr(ord(plaintext[i]) ^ ord(self.key[i % key_length]))
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ''
        key_length = len(self.key)
        for i in range(len(ciphertext)):
            decrypted_text += chr(ord(ciphertext[i]) ^ ord(self.key[i % key_length]))
        return decrypted_text


# Пример использования:

# Создаем объект потокового шифра
stream_cipher = StreamCipher()

# Задаем текстовый ключ
text_key = "Se"

# Генерируем ключевую последовательность
stream_cipher.generate_key(text_key)

# Ваш текст для шифрования
plaintext = "000"

# Шифруем текст
encrypted_text = stream_cipher.encrypt(plaintext)

# Выводим зашифрованный текст
print("Encrypted Text:", encrypted_text)

# Дешифруем текст
decrypted_text = stream_cipher.decrypt(encrypted_text)

# Выводим дешифрованный текст
print("Decrypted Text:", decrypted_text)

# encrypted_text = input()
# decrypted_text = stream_cipher.decrypt(encrypted_text)
# print("Decrypted Text:", decrypted_text)