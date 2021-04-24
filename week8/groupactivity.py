n = int(input('columns: '))
n = n+1

space = 2

if n*n > 100:
    space = 3
elif n*n > 1000:
    space = 4


for x in range(1, n):

    for y in range(1, n):

        print(f'{x*y:{space}}', end=" ")
    print()
