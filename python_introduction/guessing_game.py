import random

while True:
    secret_number = random.randint(1, 10)
    guess_count = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        guess_count += 1

        match guess:
            case n if n == secret_number:
                print("Congratulations, you guessed it!")
                print(f"It took you {guess_count} guess(es) to win the game.")
                break
            case n if n > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case n if n < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break