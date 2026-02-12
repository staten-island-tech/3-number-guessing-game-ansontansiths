def numberguesser():
    print("Welcome to the Number Guesser")
    print("I will think of a number between 1 and 10, and you have to guess.")
    
    import random
    number_to_guess = random.randint(1, 10)
    guessed_correctly = False
    
    while not guessed_correctly:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < number_to_guess:
                print("incorrect")
            elif user_guess > number_to_guess:
                print("over but still incorrect")
            else:
                guessed_correctly = True
                print(f"You've guessed the number {number_to_guess}")
                
numberguesser()