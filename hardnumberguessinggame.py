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