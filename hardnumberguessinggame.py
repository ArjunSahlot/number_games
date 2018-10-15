import random

computer_no=random.randint(1,20)

def sameno(target,number):
    if target == number:
        result = "You Win"

    elif target>number:
        result = "Low"

    else:
        result="High"

    return result

print("Let's guess a number")

guess=int(input("What is your guess?: "))

high_or_low = sameno(computer_no,guess)

while high_or_low != "You Won, BOOOOOO!!!!!":
    if high_or_low == "Low":
        guess=int(input("Too Low. Try again: "))
    else:
        guess=int(input("Too High. Try again: "))   

    high_or_low = sameno(computer_no,guess)

input("Exit")