import random
def game():
    a=[2,3,5,4]
    b=int(input("ENTER THE VALUE"))
    c=random.choice([2,3,5,4])
    if(b!=c):
        print("you lose the game")
        game()
    else:
        print("you win the game")
game()
