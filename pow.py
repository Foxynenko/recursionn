def my_pow(x, n):
    # Базовий випадок: будь-яке число в ступені 0 дорівнює 1
    if n == 0:
        return 1
    # Якщо n від'ємне, обчислюємо 1 / x^|n|
    if n < 0:
        return 1 / my_pow(x, -n)
    # Якщо n парне, використовуємо правило: x^n = (x^(n/2))^2
    if n % 2 == 0:
        half = my_pow(x, n // 2)
        return half * half
    # Якщо n непарне, використовуємо правило: x^n = x * x^(n-1)
    else:
        return x * my_pow(x, n - 1)

# Приклади використання
print(my_pow(2.00000, 10))  # Output: 1024.00000
print(my_pow(2.10000, 3))   # Output: 9.26100
print(my_pow(2.00000, -2))  # Output: 0.25000
