import random

print("Let's guess a number")

computer_no = random.randint(1,20)

guessestaken = 0
score = 5

while guessestaken < 5:
    guess = int(input("What is your guess?: "))

    guessestaken = guessestaken + 1

    if guess == computer_no:
        score = 6 - guessestaken
        s = str(score)

        print('You win with a score of ' + s)
        
        break

    elif guess > computer_no:
        print('Your guess is too high')

    else:
        print('Your guess is too low')

if guess == computer_no:
    
    print("Done")

else:
    print("Take the L. The computer guessed number is " + str(computer_no))