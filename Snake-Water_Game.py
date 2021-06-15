print("Designed By : Ankush")

import  random

if __name__== "__main__":
    print("\nWelcome To Snake Water Gun Game!\n\n")

    attempt = 1
    my_point = 0
    c_point = 0

    while (attempt<=10):
        lst=["s","w","g"]
        a=random.choice(lst)

        b = input("Enter Your Choice(Snake(s),Water(w),Gun(g)): ")
        b = b.lower()

        if b=='s' and a=='s':
            print("Tie")
            print(f"You Choose Snake and Computer Also Choose Snake\n")
            print("Nobody get point")

        elif b=='w' and a=='w':
            print("Tie")
            print(f"You Choose Water and Computer Also Choose Water\n")
            print("Nobody get point")

        elif b=='g' and a=='g':
            print("Tie")
            print(f"You Choose Gun and Computer Also Choose Gun\n")
            print("Nobody get point")
                
        elif b=='s' and a=='w':
            my_point=my_point + 1
            print(f"You Choose Snake and Computer Choose Water\n")
            print("Snake Drunk Water\n")
            print("you won this round")
            print("You have 1 point\n")

        elif b=='w' and a=='s':
            c_point=c_point + 1        
            print(f"You choose Water and computer choose Snake\n")
            print("Snake Drunk Water\n")
            print("You loss this round")
            print("Computer have 1 point\n")

        elif b=='w' and a=='g':
            my_point=my_point + 1
            print(f"You Choose Water and Computer Choose Gun\n")
            print("The Gun Sank in Water\n")
            print("you won this round")
            print("You have 1 point\n")

        elif b=='g' and a=='w':
            c_point=c_point + 1        
            print(f"You Choose Gun and Computer Choose Water\n")
            print("The Gun Sank in Water\n")
            print("You loss this round")
            print("Computer have 1 point\n")

        elif b=='g' and a=='s':
            my_point=my_point + 1
            print(f"You Choose Gun and Computer Choose Snake\n")
            print("The Gun shoot the snake\n")
            print("you won this round")
            print("You have 1 point\n")

        elif b=='s' and a=='g':
            c_point=c_point + 1        
            print(f"You Choose Snake and Computer Choose Gun\n")
            print("The Gun shoot the snake\n")
            print("You loss this round")
            print("Computer have 1 point\n")

        else:
            print("Invalid Input\n")    
            continue

        print("\nNumber of guess left: {}".format(10 - attempt))
        attempt = attempt+1


        if attempt>10:
            print("\nGame Over")

        print(f"Your score:{my_point}\n\nComputer score:{c_point}")    

        if c_point<my_point:
            print("You Won this game and Computer Lost")
        elif c_point>my_point:
            print("you lost the game and Computer Won")    
        else:
            print("Tie")    
            print("Both have equal points")

        print("number of gusses left",11-attempt,)    
        attempt = attempt+1

        if attempt>10:
            print("\nGame over! ")

        if c_point > my_point:
            print("\nComputer wins and you lose!")

        if c_point < my_point:
            print("\nYou win and the computer loses!")

        print(f"\nYour points are {my_point} and Computer's points are {c_point}!\n")
