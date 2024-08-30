# 16 stack of student’s information contains Roll_no, Name and Grade.
# Write a python program to create a stack containing students' information for the number of students entered by the user.
# Now create the following methods with created stack as an argument to display and update the stack.
# display(stack) – To display the information of all the students saved in stack.
# Push(stack) – To display previously saved information, accept new information for a student and update the stack.


stack = []


def create() -> None:
    n = int(input("Enter no. of students =>"))
    print("Enter data for each students ")
    data = [
        [int(input("Roll no. =>")), input("Name =>"), input("Grade =>")]
        for i in range(n)
    ]
    stack.extend(data)


def display(stac: list) -> None:
    if not len(stac) == 0:
        print("Data in stack is =>")
        z = [[print(y, end=" ") for y in x] + [print()] for x in stac]
    else:
        print("No Data")


def push(stac: list) -> None:
    display(stac)
    data = [int(input("Roll no. =>")), input("Name =>"), input("Grade =>")]
    stac.append(data)


create()
push(stack)
display(stack)
