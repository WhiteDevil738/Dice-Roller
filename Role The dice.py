import random
while True:#Repeate The code
    #Function To Roll The dice
    def rool_the_dice(roll):
        roll = roll
        a = random.randrange(1,7)
        if roll =="":
            return a
    roll = input("To Roll The Dice Press Enter")#input for Starting The game
    Roll = rool_the_dice(roll)#Roll Is Equal To roll_the_code function
    print("The Dice Stoped At:",Roll)#To get where the dice is stoped
    #exit Game 
    print("Exit press 1 else 2:")
    Exit = int(input())
    if Exit == 2:
        pass
    else:
        print("Hope You Enjoyed The Game")
        break
