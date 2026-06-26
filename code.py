import random


def game():
    print("----Welcome to The Ultimate Number Guesser Game----")

    low = int(input("Enter lower limit of your range: "))
    high = int(input("Enter upper limit of your range: "))

    print("You now have 7 chances to guess your number.")

    num = random.randint(low,high+1)
    
    size = high - low +1
    print(f"Your range of numbers is {size}\nLet the guessing begin!")

    for i in range(1,8):

        guess_num = int(input(f"{i}. Enter your guess number: "))
        
        diff = abs(guess_num-num)

        if guess_num==num:
            print(f"You got it.{num} is the correct number. Congratulations!\n")
            end()

        elif (guess_num in range(low,high+1)):
            if guess_num>num:
                if diff >= size/5: # for 100 range, 20%
                    print("Too high.")
                elif diff >= size/10:# for 100 range, 10%
                    print("High.")
                elif diff >= size/20: # for 100 range,10%
                    print("Close. Still high.")
                elif diff < size/20: # for 100 range, error less than 5%
                    print("Right there. Still low.")
            
            elif guess_num<num:
                if diff >= size/5: # for 100 range, 20%
                    print("Too low.")
                elif diff >= size/10:# for 100 range, 10%
                    print("Low.")
                elif diff >= size/20: # for 100 range,10%
                    print("Close. Still low.")
                elif diff <= size/20: # for 100 range, error less than 5%
                    print("Right there. Still low.")

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