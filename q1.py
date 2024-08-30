# 1.	Write a Python Program Enter ‘*’ Between two identical characters in a string.

strg, new_str = input("Enter String =>"), " "

for i in strg:
    if i != new_str[-1]:
        new_str += i
    else:
        new_str += "*" + i
print(f"The new string is =>{new_str.lstrip()}")
