# 8	Write a python program to search an element in a list and display the frequency of element
# present in list and their location by using user defined function.
# [List and search element should be entered by user]


def freq_loc(lst, elem):
    req1 = [x for x in range(len(lst)) if lst[x] == elem]
    print(f"frequency of element is {lst.count(elem)}")
    print(f"locations(index) =>{req1}")


list_i = [
    "1",
    "2",
    "3",
    "3",
    "4",
    "5",
    "5",
    "5",
    "5",
    "5",
    "6",
]  # eval(input("Enter list=>").strip())
ele = input("Search element=>")

freq_loc(list_i, ele)
