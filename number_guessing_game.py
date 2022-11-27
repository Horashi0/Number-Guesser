import time
import random
import sys

record = []

print("Welcome to my number guesser game. The number is between 1-100 and you have 5 lives. Good luck ")
time.sleep(1.5)
number = random.randint(1, 100)
loopkiller = False


def main():
    lives = [5]
    for i in range(5):
        time.sleep(1)
        number_guesser = int(input("Please guess a number between 1-100: "))
        if number_guesser > 100 or number_guesser < 0:
            time.sleep(1)
            print("Invalid input, restarting game")
            main()
        if number_guesser > number:
            time.sleep(1)
            print("The number is less than", number_guesser)
            lives.append(-1)

        if number_guesser < number:
            time.sleep(1)
            print("The number is greater than", number_guesser)
            lives.append(-1)

        lives_calculated = sum(lives)
        time.sleep(1)
        print("Lives left:", lives_calculated)

        if number_guesser == number:
            time.sleep(1)
            print("Well done! You guessed the correct number")
            time.sleep(1)
            print("You used", lives_calculated, "/5")
            sys.exit()

        if lives_calculated == 0:
            time.sleep(1)
            print(
                "Bad luck! You did not guess the correct answer better luck next time! The number was: ", number)

        number_guesser_string = str(number_guesser)
        record.append(number_guesser_string)


main()
