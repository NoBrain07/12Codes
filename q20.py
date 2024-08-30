# 20	Create an employee table in SQL with attributes - empno, ename and salary.
#     Integrate SQL with Python by importing the MySQL module.
# •	Display all the employee details.
# •	Insert a new record in the table by accepting the details from the user.
# •	Delete an employee record based on the employee number entered by the user.
#     Display the contents of the employee table after deletion using a Python script.


import mysql.connector as conn

dbs = conn.connect(host="localhost", user="root", password="admin", database="School")

myc = dbs.cursor()
sequel = "INSERT INTO employee VALUES (%s,%s,%s)"

"""
data = [
    (1, "Jereme Plewman", 57111),
    (2, "Fitzgerald Moine", 41775),
    (3, "Caryl Dinsell", 10003),
    (4, "Raddie Johnston", 61888),
    (5, "Aimil Midlar", 55176),
    (6, "Timoteo Badam", 69049),
    (7, "Helene Artingstall", 77545),
    (8, "Giovanna Enrdigo", 46236),
    (9, "Victor Ruffli", 68686),
    (10, "Jasmin MacGuffog", 77522),
]
myc.executemany(sequel, data)
dbs.commit()
"""
# see all data


def show_data():
    myc.execute("select * from employee;")
    data1 = myc.fetchall()
    for i in data1:
        print(i)


# new record
def new_record():
    new_rec = int(input("empno")), input("Ename"), int(input("Salary"))
    myc.execute(sequel, new_rec)
    dbs.commit()


def delete_rec():
    enum = int(input("Employee Id =>"))
    myc.execute(f"Delete from students where empno = {enum}")
    dbs.commit()
    show_data()


delete_rec()
