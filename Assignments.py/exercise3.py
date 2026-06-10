#Secret number game 
secret_number = int(input("Pick a secret number between 1 and 100: "))
attempts = 3
attempt = 1

while attempt <= attempts:
    raw_guess = input(f"Attempt {attempt}/{attempts} - Enter your guess: ")
    try:
        guess = int(raw_guess)
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if guess == secret_number:
        print(f"Congratulations! {guess} is the correct number.")
        break

    if guess > secret_number:
        print("Too high. Try a lower number.")
    else:
        print("Too low. Try a higher number.")

    if attempt < attempts:
        print("Keep going, you still have more attempts.")
    else:
        print("That was your last attempt.")

    attempt += 1
else:
    print(f"Correct number: {secret_number}")


