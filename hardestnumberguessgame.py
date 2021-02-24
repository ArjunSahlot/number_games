#
#  Number games
#  A small number guessing game in Python
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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