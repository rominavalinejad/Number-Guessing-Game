# Number Guessing Game

# Level 1
# Step 1: The secret number
secret_number = 12
print("-" *45)
print("💠Welcome to the Guessing Game!💠")
print("Hum... I'm thinking of a number between 1 and 20!")
print("-" *45)

# Step 2: Get user input
try:
    guess = int(input("Enter your guess:"))
    
# Step 4: Check the valid range
    if guess < 1 or guess > 20:
        print("Invalid number!⚠️\nPlease enter a number strictly between 1 and 20")
    
# Step 3: Conditional logic to evaluate the guess
    elif guess == secret_number:
        print("Congratulations! You guessed it right!🏆")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print("Too low! Try a larger number.")

except ValueError:
        print("Please enter a number!❌")
        
print("-" *45)
