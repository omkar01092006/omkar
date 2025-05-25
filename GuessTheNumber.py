 GuessTheNumber.py
import random
print("Name:Omkar")
print("USN:1AY24AI079")
print("Section:O")

def guess_the_number():
  
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    attempts = 0
    guessed_number = None

    
    while guessed_number != number_to_guess:
        
        try:
            guessed_number = int(input("Enter your guess: "))
            attempts += 1

            
            if guessed_number < number_to_guess:
                print("Too low! Try again.")
            elif guessed_number > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


guess_the_number()
