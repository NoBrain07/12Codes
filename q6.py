# 6	Write a Python Program to count number of pairs in a list whose product is
# divisible by a value K entered by the user.

# [int(input("->")) for x in range(int(input("How Many Numbers =>")))]

lst, k = [x for x in range(1, 6)], int(input("Value of k =>"))
a = []
req1 = [
    a.extend([tuple(sorted([y, x])) for y in lst if (y * x) % k == 0 if x != y])
    for x in lst
]
req = list(set(a))
print(f"pairs divisible by {k} =>{len(req)}")
