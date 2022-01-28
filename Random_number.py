import random
a1 = input(" Hey Buddy ! Enter Your Name :: \n  ")
print(a1, ": Welcome To number Guesses Game !!  :) ")
a = input("Do you want to play ? Yes /NO  ")
if a == "yes":
    print(" !!  Okay Let's Play :)")
    top_of_range = input(": type a Number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print(" Please type a larger number  Next time : ")
            quit()
    else:
        print("Please type a number :: Next Time , ")
        quit()
    random_number = random.randint(0, top_of_range)
    guess = 0
    while True:
        guess += 1
        use_guess = input("Make a Guess :\n ")
        if use_guess.isdigit():
            use_guess = int(use_guess)
        else:
            print("Please type  a Number Nex time : ")
            continue
        if use_guess == random_number:
            print('!! Congratulation  🎉 !!  Your Answer is Correct !!  ')
            break
        elif use_guess >= random_number:
            print("Please Accesses a small number !! \n")
        else:
            print("please Accesses a Greater Number !! \n")
    print("You Got it is ", guess, "guesses")
else:
    print(" Okay Quit the game ! ")
    quit()

print(a1, " = > !! Thanks To Play this game !!   <= ")
