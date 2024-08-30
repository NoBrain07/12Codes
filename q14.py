# 14	Write a Python program to get item details (code, description and price) for multiple items from
#   the user and create a csv file by writing all the item details in one go.

import csv

file = open("items.csv", "w+", newline="")
data = [
    (input("Code->"), input("Description->"), input("Price->"))
    for x in range(int(input("no. of items =>")))
]
writer = csv.writer(file)
writer.writerows(data)
