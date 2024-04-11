import random

DIGITS = ["1", "2", "3", "4", "5", "6"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        digit = random.choice(DIGITS)
        code.append(digit)

    return code    


def guess_code():
    
    while True:

        guess = input("Guess: ").split(" ")

        if len(guess) != CODE_LENGTH:
          print(f"You must guess {CODE_LENGTH} digits.")
          continue

        for digit in guess:
            if digit not in DIGITS:  
                print(f"Invalid digit {digit}, Try again.")
                break
        else:
            break
    return guess        


def check_code(guess, real_code):
    digit_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for digit in real_code:
        if digit not in digit_counts:
            digit_counts[digit] = 0
        digit_counts[digit] += 1

    for guess_digit, real_digit in zip(guess, real_code):
        if guess_digit == real_digit:
            correct_pos += 1
            digit_counts[guess_digit] -= 1

    for guess_digit, real_digit in zip(guess, real_code):
        if guess_digit in digit_counts and digit_counts[guess_digit] > 0:
            incorrect_pos += 1
            digit_counts[guess_digit] -= 1

    return correct_pos, incorrect_pos        


def game():

    print(f"Welcome to master mind, you have {TRIES} tries to guess the code")
    print("The valid digits are", *DIGITS)
    code = generate_code()
    for attemps in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attemps} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")



        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries! the code was: ", *code)

if __name__ == "__main__":
    game()
        