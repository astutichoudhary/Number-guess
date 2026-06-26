import random

def game():
    print("----Welcome to The Ultimate Number Guesser Game----")

    low = int(input("Enter lower limit of your range: "))
    high = int(input("Enter upper limit of your range: "))

    print("You now have 7 chances to guess your number.")

    num = random.randint(low,high)
    i = 1
    for i in range(1,8):
        guess_num = int(input(f"{i}. Enter your guess number: "))
        if guess_num==num:
            print(f"You got it.{num} is the correct number. Congratulations!\n")
            end()
            # break
        elif guess_num>num:
            print("Too high.")
        elif guess_num<num:
            print("Too low.")
        else:
            print(f"Enter a valid integer between {low} and {high}")

    for i in range(7,8):
        print(f"Sorry! You failed at guessing the number. The number was {num}")
        end()


def end():
    end = input("Press Enter for replay.\n")
    while True:
        if end=="":
            game()
        else:
            break

game()
end()