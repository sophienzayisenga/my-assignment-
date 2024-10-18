def is_palindrome(n):
    n_strings = ''.join( n.split()).lower()
    return n_strings == n_strings[::-1]
s_string = input("enter string:")
if is_palindrome(s_string):
    print(f"the name:{s_string} is palindrome")
else:
    print(f"the name:{s_string} is not palindrome")

    