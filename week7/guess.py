import random




times= 0
magic = random.randint(1,100)
guess = int(input(' guess the number: '))
while guess!=magic:
    while guess < magic:
        print('higher')
        times = times+1
        guess = int(input(' guess the number: '))
    while guess > magic:
        print('lower')
        times = times+1
        guess = int(input(' guess the number: '))


    print('You guessed it')
    times= times+1
    print(f" you guessed {times} times")
