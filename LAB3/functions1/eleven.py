def palindrome(str):
    newstr = str[::-1]
    if str == newstr:
        return print('{} - is palindrome'.format(str))
    return print('{} - is not palindrome'.format(str))

# str = input()
# palindrome(str)