# 3.Write a Python function to find whether the number entered by the user is automorphic or not.


def is_automorphic(num):
    if str(int(num) ** 2)[-1] == str(num)[-1]:
        print(f"The number {num} is automorphic")
    else:
        print(f"The number {num} is not automorphic")


n = input("Number=>")
is_automorphic(n)
