def is_palindrome(string: str):
    if not(isinstance(string, str)):
        return False

    string = string.lower()
    new_string = ""
    for c in string:
        if 'a' <= c <= 'z':
            new_string += c
    x = 0
    while x < len(new_string):
        if new_string[x] != new_string[-1-x]:
            return False
        x += 1
    return True

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
        