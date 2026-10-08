#store a secret number between 1 and 50
#ask input for 7 attempts from user to guess the number
#if the number guessed is higher than the secret number then print "Too high"
#if the number guessed is lower than the secret number then print "Too low"
#if guessed right then print that it's the right guess and also
#print the number of attempts the user took to guess the secret number
#print the secret after 7 attempts

secret_number=31
attempts=0

while attempts < 7:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    if guess == secret_number:
        print("Correct!")
        print("It took", attempts, "attempts.")
        break
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")
else:
    print("Sorry, you've used all 7 attempts.")
    print("The secret number was", secret_number)

