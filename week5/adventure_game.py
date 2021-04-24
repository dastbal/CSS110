print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. ")

i = 0
while ( i==0 ):
    mf= input(" Which one do you want to pick up?  MATCH and a FLASHLIGHT.  ")
    mf = mf.lower()
    if mf =="match" or mf== "flashlight":
        i = 1

if mf== "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 
    i = 0
    while ( i==0 ):
        rh =input(" Do you want to RUN, or HIDE behind a tree? ") 
        rh = rh.lower()
        if rh =="run" or rh == "hide":
            i = 1
    if rh =="run" :
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 

    else:
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 

else:
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. ") 
    i = 0
    while ( i==0 ):
        fl = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ") 
        fl = fl.lower()
        if fl == "follow" or fl == "look":
            i = 1
    if fl == "follow":
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 


    else:
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.") 






