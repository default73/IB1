def least_significant_bit(number):
    # Используем побитовую операцию "И" с 1, чтобы получить младший бит
    lsb = number & 1
    return lsb

# Пример использования
number = 41  # Например, число 42
lsb = least_significant_bit(number)
print("Самый младший бит числа", number, ":", lsb)