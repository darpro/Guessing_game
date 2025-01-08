import random
print("In this game you will have to guess a number randomly picked by the computer in the lest amount of times")
low = int(input("Enter the minimum of the range: "))
high = int(input("Enter the maximum o the range: "))
num = random.randint(low,high)
print(num)
choice = int(input("Make a guess!: "))
while choice > high or choice < low :
    choice = int(input("Please enter a number between the chosen range: "))
while choice != num :
    choice = int(input("Try again: "))
if choice == num :
    print("You have won!!! ")