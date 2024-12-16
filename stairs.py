def climb_stairs_recursive(n):
    if n == 1:  # Якщо тільки одна сходинка
        return 1
    elif n == 2:  # Якщо дві сходинки
        return 2
    else:
        return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

# Приклади використання
print(climb_stairs_recursive(2))  # Output: 2
print(climb_stairs_recursive(3))  # Output: 3
print(climb_stairs_recursive(4))  # Output: 5
