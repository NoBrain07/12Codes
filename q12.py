# 12	Write a python program to create a binary file with name and roll number.
# Search for a given roll number and display name, if not found display appropriate message.
import pickle

inp, n = ["Roll no.", "Name"], int(input("no.of students=>"))
inp += [[input("Roll no.=>"), input("Name=>")] for i in range(n)]
file = open("students.dat", "wb")
temp = [pickle.dump(x, file) for x in inp]
file.close()

file = open("students.dat", "rb")
search_roll = input("roll no. of record required =>")

while True:
    try:
        x = pickle.load(file)
        if x[0] == search_roll:
            print(f"the student is =>{x[1]}")
            break
        else:
            continue
    except:
        print(f"No student with roll no {search_roll}")
        break

file.close()
