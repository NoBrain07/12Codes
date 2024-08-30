# 2.	Write a Program to enter the number and print the Floyd’s Triangle in decreasing order.

n = int(input("Enter Number =>"))

y = [[print(n - j, end=" ") for j in range(x)] + [print()] for x in range(1, n + 1)]

# for i in range(1, num + 1):
#    for j in range(i):
#        print(num - j, end=" ")
#    print()
#
