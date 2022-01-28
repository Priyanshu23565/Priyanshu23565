'''

a1 = input("Hey Bro ! Please Enter Your Name ! \n ")

print("Good AfterNoon : ", a1)
print(a1, " : Welcome To Quiz Game !! :) ")
a = input("Do you want to play ? Yes /NO  ")
if a == "yes":
    print(" !!  Okay Let's Play :)")
    answer = input("Which City Capital of India  ..?🤔 ")
    if answer == "Delhi":
        print(": Congratulation 🎉 Your Answer is correct :) \n \t : ", answer, ": Is The Capital of INDIA ")
    else:
        print("Sorry Your Answer Is Incorrect because Name is First Character is Greater 😕  !! please try Again !!  ")

    answer = input("Where is the Tajmahal Located .?🤔 ")
    if answer == "Agra":
        print(":: Congratulation 🎉 Your Answer is correct :) ")
    else:
        print("Your Answer is Incorrect !! ")


else:
    print("Incorrect Please Try Again !!")


'''

'''
    print(" Do You want to use Calculator  yes/No ")
    b = " Do You want to use Calculator  yes/No "
    if b == "yes":
        print("[1] Addition [2] Subtraction [3] Multiplication [4] Division ")
        c = int(input("Enter the Choose value :  \n  "))
        if c == 1:
            f1 = int(input("Enter The first Value :: \n"))
            f2 = int(input("Enter The Second Value :: \n"))
            Sum = f1 + f2
            print("Addition is : ", Sum)
        elif c == 2:
            f1 = int(input("Enter The first Value :: \n"))
            f2 = int(input("Enter The Second Value :: \n"))
            Sub = f1 - f2
            print("Subtraction is : ", Sub)
        elif c == 3:
            f1 = int(input("Enter The first Value :: \n"))
            f2 = int(input("Enter The Second Value :: \n"))
            Mul = f1 * f2
            print("Multiplication is : ", Mul)
        elif c == 4:
            f1 = int(input("Enter The first Value :: \n"))
            f2 = int(input("Enter The Second Value :: \n"))
            Div = f1 / f2
            print("Subtraction is : ", Div)
        else:
            print("The Value is Incorrect")
    else:
        print(b, ": Okay !! Let's Continue the next question !!  ")
'''



a1 = input("Hey Bro ! Please Enter Your Name ! \n ")

print("Good AfterNoon : ", a1)
print(a1, " : Welcome To Quiz Game !! :) ")
a = input("Do you want to play ? Yes /NO  ")
if a == "yes":
    print(" !!  Okay Let's Play :)")
    chance = 1
    score = 0
    print("1)  Where is the the type of Memory .?   \n[a].  2 \n[b].  3 \n[c].  4 \n[d].  5  ")
    answer_1 = "a"
    for i in range(chance):
        answer = input("Enter The Answer  \n ")
        if answer.lower() == answer_1:
            print("!: Congratulation 🎉 Your Answer is correct :) ! ")
            score = score + 1

        else:
            print("Incorrect Answer !!! ")

    print("2)  Where is the Tajmahal in located  .?   \n[a].  Mumbai \n[b].  Agra \n[c].  Goa \n[d].  Delhi  ")
    answer_2 = "b"
    for i in range(chance):
        answer = input("Enter The Answer  \n ")
        if answer.lower() == answer_2:
            print(":: Congratulation 🎉 Your Answer is correct :) ")
            score = score + 1

        else:
            print("Incorrect Answer !!! ")

    print("3).  Which is the capital of India . ?    \n[a].  Agra \n[b].  Goa \n[c].  Delhi \n[d].  Mumbai  ")
    answer_2 = "c"
    for i in range(chance):
        answer = input("Enter The Answer  \n ")
        if answer.lower() == answer_2:
            print(":: Congratulation 🎉 Your Answer is correct :) ")
            score = score + 1

        else:
            print("Incorrect Answer !!! ")
    print("4).  Who Python Created  .? : \n[a]. Guido Van Rossum \n[b]. Elon Musk \n[c]. Bill Gates \n[d]. MarkZuckerberg ")
    answer_2 = "a"
    for i in range(chance):
        answer = input("Enter The Answer  \n ")
        if answer.lower() == answer_2:
            print("::: Congratulation 🎉 Your Answer is correct :) (●'◡'●)")
            score = score + 1

        else:
            print("Incorrect Answer !!! ")

    while score > 3:
        print("Will Done ! Yor Score was : 😎 ! (❁´◡`❁) Total Score : ", score)
        break
    while score == 3:
        print("Better luck next time 🤔🤨 ", score)
        break
    while score <= 2:
        print("Fail 😫( ´･･)ﾉ(._.`)  !! 🤔🤨  \n \t  Total Score :", score)
        break

    print(" !!=>  ", a1, "  \n \t  === >>  ! Thank You The Simple Quiz Game !!! < ==")
else:
    quit()
