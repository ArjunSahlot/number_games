import random
computer_no=random.randint(0,10)
print("Do you ready for the challenge " )
user = str(input("[ Y/n ] " ))
user2 = user.lower()
if user2 == "y" :
    def sameno(target,number):
        if target == number:
            result = "You Win"
           
        else:
            result="Wrong !! Try again : "
        return result
    print("You have to guess numbers between 0 and 10 ")
    print("Let's guess a number")
    guess=int(input("What is your guess?: "))
    print(sameno(computer_no,guess))
   



if user2 == "n" :
    print("AS your choice : Thanks for playing : ")
                                    
