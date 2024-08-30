# 13  Write a program using python to get 10 players name and their score. Write the input in a csv file.
#  Accept a player name using python.Read the csv file to display the name and the score.
#  If the player’s name is not found give an appropriate message.
import csv

file = open("players.csv", "w", newline="")

data = ["Player Name", "Score"]
data += [[input("Player Name=>"), int(input("Score=>"))] for x in range(10)]
writer = csv.writer(file)
writer.writerows(data)
file.close()

file = open("players.csv", "r")
play_nam = input("Enter Player Name =>").strip()
reader = csv.reader(file)
w = [[x, y] for x, y in reader]
if not play_nam in dict(w).keys():
    print("No such player in record")
else:
    m = [print(f"Player Name =>{i[0]}\tScore=>{i[1]}") for i in w if i[0] == play_nam]

file.close()
