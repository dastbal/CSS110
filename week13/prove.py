def wind_chill(T, V):
    x = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    return x


def convert(c):
    return c*(9/5) + 32


def print_loop_of_windchill(T, choose):
    if (choose == 'F'):
        T = T
    elif (choose == 'C'):
        T = convert(T)
    else:
        print('Please select (F/C)')
    for i in range(5, 61, 5):
        print(
            f'At temperature {T}F, and Wind speed {i} mph, the windchill is: {wind_chill(T,i):.2f}')


T = float(input('What is the value temperature? '))
choose = input('Fahrenheit or Celsius (F/C)? ').upper()

while(choose != 'F' and choose != 'C'):
    choose = input('Fahrenheit or Celsius (F/C)? ').upper()


print_loop_of_windchill(T, choose)
