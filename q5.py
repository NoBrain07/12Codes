# 5	Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward


def is_palindrome(strg):
    if strg == strg[::-1]:
        print(f"'{x}' is a Palindrome")
    else:
        print(f"'{x}' is not a Palindrome")


x = input("Enter String =>")
is_palindrome(x)
