# 9	Write a Python program to find tuples with positive elements in list of tuples.

test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]
print([x for x in test_list if sorted(x)[0] >= 0])
