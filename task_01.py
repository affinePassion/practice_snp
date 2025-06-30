def is_palindrome(string):
    if not isinstance(string, (str, int)):
        return False

    if isinstance(string, int):
        string = str(string)
    
    string = string.lower()
    new_string = ""
    for c in string:
        if 'a' <= c <= 'z' or '0' <= c <= '9':
            new_string += c
    x = 0
    while x < len(new_string):
        if new_string[x] != new_string[-1-x]:
            return False
        x += 1
    return True

print(is_palindrome("A man, a plan, a canal -- Panama"))  # => True
print(is_palindrome("Madam, I'm Adam!"))                 # => True
print(is_palindrome(333))                                # => True
print(is_palindrome(None))                               # => False
print(is_palindrome("Abracadabra"))                      # => False
        