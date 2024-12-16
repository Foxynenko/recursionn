def reverse_string_recursive(s):
    """
    Recursively prints a string in reverse order.

    :param s: The string to be reversed.
    """
    if len(s) == 0:
        return  # Base case: if string is empty, stop recursion
    else:
        # Print the last character
        print(s[-1], end='')
        # Recursively call with the rest of the string
        reverse_string_recursive(s[:-1])

# Example usage
reverse_string_recursive("tiger")