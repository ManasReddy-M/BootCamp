import random

def guessing_game():
    """
    A simple number guessing game that prompts the user until the correct 
    random number is found, and tracks the number of attempts.
    """
    
    # 1. Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    
    # Initialize variables 
    attempts = 0
    guess = None  # Use None to ensure the while loop starts
    
    print("Welcome to the Number Guessing Game! 🎲")
    print("I have generated a secret number between 1 and 100.")
    
    # 2. Loop until the guess is correct
    while guess != secret_number:
        try:
            # Get user input
            guess_input = input("Enter your guess: ")
            
            # Convert input to an integer
            guess = int(guess_input)
            
            # Increment the attempt counter
            attempts += 1
            
            # 3. Give hints: "Too high" or "Too low"
            if guess < secret_number:
                print("Too low! Try a higher number. ⬆️")
            elif guess > secret_number:
                print("Too high! Try a lower number. ⬇️")
            
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a whole number.")
            # Do not increment attempts for invalid input
        
    # 4. Congratulate when correct
    print("-" * 30)
    print(f"🎉 Congratulations! You guessed the secret number ({secret_number}) correctly!")
    print(f"It took you {attempts} attempts.")
    print("-" * 30)

# Test the game
guessing_game()