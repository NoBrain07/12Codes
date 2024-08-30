# 10	Write a program to copy all the lines that contain the character `a' in a file and write it to another file.

file1 = open(input("Filename=>") + ".txt", "r")
file2 = open("out.txt", "w")
file2.writelines([x for x in file1.readlines() if " a " in x.lower()])

file1.close(), file2.close()
