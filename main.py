import random

MAX_DIGITS = 3
MAX_GUESSES = 10

def generate_random_number():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(digits)

    random_number: list[int] = []
    for i in range(0, MAX_DIGITS):
        random_number.append(digits[i])

    return random_number


def generate_clues(secret_number: list[int], user_guess: list[int]):
    clues: list[str] = []

    for i in range(0, len(secret_number)):
        if user_guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif user_guess[i] in secret_number:
            clues.append("Pico")

    if len(clues) == 0:
        clues.append("Bagles")

    return clues


def main():
    print(f'''
I am thinking of a {MAX_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:  That means:
    Pico     One digit is correct but in the wrong position.
    Fermi    One digit is correct in the right position.
    Bagles   No digit is correct.
'''.strip())
    while True:
        secret_number = generate_random_number()
        print(f'DEBUG: The secret_number is -> {secret_number}')
        
        current_guess = 0
        while current_guess < MAX_GUESSES:
            print(f"Guesses remaining: {MAX_GUESSES - current_guess}")
            user_input = input("Guess: ")

            if len(user_input) != 3:
                print("Invalid input provided")
                continue
            
            try:
                user_guess = [ int(x) for x in user_input ]
            except ValueError:
                print("Invalid input provided")
                continue
            
            if user_guess == secret_number:
                print("You got it!")
                break

            clues = sorted(generate_clues(secret_number, user_guess))
            print(", ".join(clues))
            current_guess += 1

        if current_guess == MAX_GUESSES:
            print(f'''
You ran out of guesses.
The answer was {"".join([str(x) for x in secret_number])}
'''.strip())
        
        awaiting_input = True
        while awaiting_input:
            user_input = input("Do you want to play again? (y/n): ")
            if user_input.lower() in ['y', 'n']:
                if user_input.lower() == 'n':
                    return
                awaiting_input = False


if __name__ == '__main__':
    main()
