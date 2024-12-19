import random


secret_number = random.randint(1, 100)

max_attempts = 10

print("Welcome to the Number Guessing Game!")
print(f"Guess the secret number between 1 and 100. You have {max_attempts} attempts.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the secret number ({secret_number}) correctly!")
        break
else:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}. Better luck next time!")
