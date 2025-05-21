guess= int(input('Enter an Integer number: '))
secret_num = 4

while guess != secret_num:
            

            if guess < 1 or guess > 10:
                print("Your guess is out of range. Please guess a number between 1 and 10.")
            elif guess < secret_num:
                print("Too low! Try again.")
            elif guess > secret_num:
                print("Too high! Try again.")

print("Congratulations") 
