import random


def game():
    low = int(input("Enter lower limit of your range: "))
    high = int(input("Enter upper limit of your range: "))

    print("You now have 7 chances to guess your number.")
    num = random.randint(low,high)
    i = 1
    for i in range(1,8):
        guess_num = int(input("Enter your guess number: "))
        if guess_num==num:
            print(f"You got it.{num} is the correct number. Congratulations!\n")
            break
        elif guess_num>num:
            print("Too high.")
        elif guess_num<num:
            print("Too low.")
        else:
            print(f"Enter a valid integer between {low} and {high}")
        i += 1
    if i==7 and guess_num!=num:
        print(f"Sorry! You failed at guessing the number. The number was {num}")

print("----Welcome to The Ultimate Number Guesser Game----")

game()

# def end():
#     end = input("Press Enter for replay and q for exiting the game.")
# while True:
#     if end=="":
#         game()
#     elif end=="q":
#         break
#     else:
#         print("Invalid.")
#         end()
     
     






