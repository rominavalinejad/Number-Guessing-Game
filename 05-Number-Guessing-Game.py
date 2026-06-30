# Number Guessing Game

# Level 1
# Step 1: Generate a random The secret number
import random
secret_number = random.randint(1, 20)

print("-" *45)
print("💠Welcome to the Guessing Game!💠")
print("Hum... I'm thinking of a number between 1 and 20!")
print("-" *45)

# Step 2: Loop until the user guesses corectly
while True:
    
    try:
        guess = int(input("Enter your guess:"))
    
# Step 4: Check the valid range
        if guess < 1 or guess > 20:
            print("Invalid number!⚠️\nPlease enter a number strictly between 1 and 20")
            continue
    
# Step 3: Conditional logic to evaluate the guess
        elif guess == secret_number:
            print("Congratulations! You guessed it right!🏆")
            break
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
             print("Too low! Try a larger number.")

    except ValueError:
            print("Please enter a number!❌")
        
print("-" *45)
