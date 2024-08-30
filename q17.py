# 17	Write a menu driven program to handle a linear stack called Books contains (book number, book name and cost).
# Write the user defined functions:
# •	PUSH (N) to add N book details each containing the above-mentioned information.
#          N to be accepted by user. Display the stack after adding all records.
# •	POP() to delete the book details of last item added. Display the updated stack.
# •	DISPLAY() to display all books details having price more than 500.

stack = []


def get():
    z = [[print(y, end=" ") for y in x] + [print()] for x in stack]


def push(n):
    print("Enter data for each book")
    data = [
        [int(input("Book no. =>")), input("Book Name =>"), int(input("Cost =>"))]
        for i in range(n)
    ]
    stack.extend(data)
    get()


def pop():
    stack.pop()
    get()


def displays():
    print("Books over cost 500")
    [[print(y, end=" ") for y in x] + [print()] for x in stack if x[2] >= 500]


print("Book stack")


while True:
    print("Select operation", "1> Display", "2> Pop", "3> Push", "4> end", sep="\n")
    ch = int(input())

    if ch == 1:
        displays()
    elif ch == 2:
        pop()
    elif ch == 3:
        push(int(input("no. of books=>")))

    elif ch == 4:
        print("ending")
        break

    else:
        continue
