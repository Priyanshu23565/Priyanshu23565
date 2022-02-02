import random
import turtle

a = input(": Enter Your Name : \n \t ")
print(a, " Welcome to Project number 5 / This is a Combine Project ")
a1 = int(input(" : ==> [1] Number Quiz Game! [2] Number Guesses Game ! [3] Star Programme [4] Snake Water Gun  <==:\n"))
if a1 == 1:
                #  First Game is Quiz Game 

    print(": => : Welcome to Quiz game !! <=: ")
    a = input(" Do you want to play YES(Y)/NO(N) ")
    if a == 'Y' or a == "y":
        print("Let's play !! :) ")
        score = 0
        print("1).  X=10 \n     Y=5 \n for i in range(X-Y*2) \n print( \'%\' i )  \n[1]. 0 \n[2]. 2 \n[3]. 5 \n[4]. 8")
        a = 1
        answer = int(input("Enter Your answer ! \n"))
        if a == answer:
            print("Your Answer is correct !! ")
            score = score + 1
        else:
            print("invalid answer !🤔😑 !")

        print("2).  Where is the memory type .?  \n[1]. 7 \n[2] 2 \n[3] 8 \n[4] 5")
        answer2 = 2
        answer = int(input("Enter Your Answer !  \n"))
        if answer == answer2:
            print("Your answer is correct !  ")
            score = score + 1
        else:
            print("Invalid answer ! ")

        print("3. Where is the taj mahal is located .? \n(1).Aligarh  \n(2).Delhi \n(3).Goa \n(4). Agra ")
        answer_2 = 4
        answer = int(input("Enter Your Answer ! \n "))
        if answer == answer_2:
            print(" Congratulation 🎉🎉 good  Your answer is correct !! ")
            score = score + 1
        else:
            print("Invalid answer ")

        print(
            "4. Full Form of CPU .? \n(1).Central Processing unit  \n(2).Central Proesing unit \n(3).Cntral Processing unit \n(4). cntral Processing unit a ")
        answer_2 = 1
        answer = int(input("Enter Your Answer ! \n "))
        if answer == answer_2:
            print(" Congratulation  good  Your answer is correct !! ")
            score = score + 1
        else:
            print("Invalid answer ")

        while score == 4:
            print(a1, ":  Congratulation 🎉🎉 Good Bro \n \t Total Score is : ", score)
            break
        while score <= 3:
            print(a1, ": So! Sorry Bro  please Try Again ! \n \t Total Score is : ", score)
            break

        print(a1, "\t \n  : Thank You Bro ! Enjoy The Game !! 😃😃! ")
    else:
        print("Okay Bro ")
        quit()

        #                  Second Game is Number Guesses Game 

elif a1 == 2:
    print(a, ": Welcome To Number Guesses Game !!  :) ")
    b = input("Do you want to play ? Yes[Y]/NO[N]  ")
    if b == 'y' or b == 'Y':
        print(" !!  Okay Let's Play :)")
        top_of_range = input(": Type a Number : \n ")
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


                            #    Thered Game is Star Programme . 
elif a1 == 3:
    print(a1, ": Welcome to Star Programme ::  ")
    b1 = input(": Do you  want  play  Yes/No Than Click [Y] & [N] : \n \t ")
    if b1 == "y" or b1 == "Y":
        def star(color):
            b.begin_fill()
            b.getscreen().bgcolor('red')
            b.fillcolor(color)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.end_fill()

            b.backward(200)
            b.begin_fill()
            b.fillcolor(color)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.forward(200)
            b.left(216)
            b.end_fill()
            #
            # b.right(200)

            # b.left(150)
            # b.begin_fill()
            # b.fillcolor(color)
            # b.forward(200)
            # b.left(216)
            # b.forward(200)
            # b.left(216)
            # b.forward(200)
            # b.left(216)
            # b.forward(200)
            # b.left(216)
            # b.forward(200)
            # b.left(216)
            # b.end_fill()


        b = turtle.Turtle()
        star('yellow')
        turtle.done()
        print(a1, "\n \t  : Thank you for Enjoy This Game ! :: ")
    else:
        print("Okay  bye bye !! ")
        quit()
                    #  Snake Water Gun Game     
                    
elif a1 == 4:

    def gameWin(co, you):
        if co == you:
            return None
        elif co == 'snake':
            if you == 'water':
                return False
            elif you == 'gun':
                return True
        elif co == 'water':
            if you == 'snake':
                return True
            elif you == 'gun':
                return False
        elif co == 'gun':
            if you == 'water':
                return True
        elif you == 'snake':
            return False


    print(a1, ": Welcome To Snake Water Game  GAME ! :) !  :) ")
    s1 = int(input(": Click 1 in Run the code ! ! \n "))
    if s1 == 1:
        bb = input("Do you want to play ? Yes/NO  :")
        if bb == "yes":
            print(" !!  Okay Let's Play :) ")
            print("Computer Turn :: Snake[s]  water[w]  gun[g] !!  ? \n")
            r = random.randint(1, 3)
            if r == 1:
                computer = 'snake'
            elif r == 2:
                computer = 'water'
            elif r == 3:
                computer = 'gun'
            y = input("Your Turn :: Snake[s]  water[w]  gun[g] ...?")
            a = gameWin(computer, y)
            print(f" Computer Choose is : {computer}")
            print(f" Your Choose is :  {y}")
            if a is None:
                print(" The Game is Tie !So 🤥🤥🤕 So!  please Try again !  ")
            elif a:
                print(" Congratulation ! 🎇 ✨ 🎉!   You Win ")
            else:
                print('you Lose !😥 😕! Please try Again  !! ')
        else:
            print(a1, " Okay Quit the Game bye bye !!! ")
            quit()
    else:
        print("Okay bye bye !! ")

else:
    print("Bye bye !! ")
