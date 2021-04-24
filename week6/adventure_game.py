print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. ")

i = 0
while ( i==0 ):
    mf= input(" Which one do you want to pick up?  MATCH and a FLASHLIGHT.  ")
    mf = mf.lower()
    if mf =="match" or mf== "flashlight":
        i = 1
    else:
            print(" choose again")

# first level option 1

if mf== "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 
    i = 0
    while ( i==0 ):
        rh =input(" Do you want to RUN, or HIDE behind a tree? ") 
        rh = rh.lower()
        if rh =="run" or rh == "hide":
            i = 1
        else:
            print(" choose again")

# second level option 1

    if rh =="run" :
        print("You run so quickly to away of the bear, but the noise made that the grizzly bear follows you.") 
        i = 0
        while ( i==0 ):
            rh =input(" You want to FIGHT , or SING  agisnt the bear. ") 
            rh = rh.lower()
            if rh =="fight" or rh == "sing":
                i = 1
            else: 
                print("choose again")

# Third leve option 1
        if rh=="fight":
            print( "You are Dead.")

# Third level option 2
        else:
            print("you scared the grizzly bear with your voice")
            print("Now, you can continue walking through a dark forest")

# second level option 2 
    else:
        print(" you are safe, the grizzly bear did not see you")



#  first level option 2

else:
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. ") 
    i = 0
    while ( i==0 ):
        fl = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ") 
        fl = fl.lower()
        if fl == "follow" or fl == "look":
            i = 1
        else:
            print(" choose again")
#  second level option 1
    if fl == "follow":
        print("You follow the Path,so you find a house tree in front of you") 
        i = 0
        while ( i==0 ):
            rh =input(" You want to CONTINUE walking, or GO to the house tree ") 
            rh = rh.lower()
            if rh =="continue" or rh == "go":
                i = 1
            else:
                print(" choose again")
#  third level option 1

        if rh=="continue":
            print( "You lost in the dark forest.")

#  third level option 2
        else:
            print("You found a good plae to staring the starts")
            print("You found the exit to the dark forest")
#  second level option 
    else:
        print("You look a tiny rabbit eating leaves ") 
        i = 0
        while ( i==0 ):
            rh =input(" You want to CAUGHT it, or TAKE it a picture ") 
            rh = rh.lower()
            if rh =="caught" or rh == "take":
                i = 1
            else:
                print(" choose again")

#  third level option 1
        if rh=="caught":
            print( "You cooked the rabbit you loved it, it was delicious")
#  third level option 2
        else:
            print("it was so dark that the picture was bad")
            print("The rabbit ran away into the dark")






