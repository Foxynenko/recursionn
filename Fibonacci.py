def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Приклади використання
print(fibonacci_recursive(2))  # Output: 1
print(fibonacci_recursive(3))  # Output: 2
print(fibonacci_recursive(4))  # Output: 3
