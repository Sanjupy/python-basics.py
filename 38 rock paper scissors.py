import random
while True:

    choices=["rock","paper","scissors"]

    computer=random.choice(choices)
    player=None
    while player not in choices:

        player=input("rock ,paper or scissors?:")
    if player==computer:
        print("computer:",computer)
        print("player",player)
        print("tie")

    elif player=="rock":
        if computer=="paper":
            print("computer:",computer)
            print("player",player)
            print("lose")
    
        if computer=="scissors":
            print("computer:",computer)
            print("player",player)
            print("lose")

    elif player=="paper":
        if computer=="rock":
            print("computer:",computer)
            print("player",player)
            print("win")
    
        if computer=="scissors":
            print("computer:",computer)
            print("player",player)
            print("lose")


    elif player=="scissors":
        if computer=="rock":
            print("computer:",computer)
            print("player",player)
            print("lose")
    
        if computer=="paper":
            print("computer:",computer)
            print("player",player)
            print("win")
    play_again=input("wanna play again? yes/no:").lower()

    if play_again!="yes":
        break

print("bye")
