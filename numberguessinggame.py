import random

computer_no=random.randint(1,5)

def sameno(target,number):
    if target == number:
        result = "You Win"

    else:
        result="Take the L"

    return result

print("Let's guess a number")

guess=int(input("What is your guess?: "))

print(sameno(computer_no,guess))