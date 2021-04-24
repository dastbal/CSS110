import random
play="yes"
while play == 'yes':
    guess=0
    times=0
    n= random.randint(1,100)
    while guess!=n:
        guess=int(input("What is your guess? "))
        print()

        if guess <n:
            times = times +1
            print(f"Your {guess} is lower ")
        elif guess>n:
            times = times +1
            print(f"Your {guess} is higher ")
        else:
            print(" You guessed it")
            times = times +1
    print(f" You have guessed {times} times")
    print()
    play= input("You wanna play again? YES or NO ")
    print()
    play= play.lower() 
    if play != 'yes':
        print("Thanks for playing with me")


