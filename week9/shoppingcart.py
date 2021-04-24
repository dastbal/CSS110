print('Welcome to the Shopping Cart Program!')

print()
items = []
precios = []

choose = ' '

while choose != 5:
    choose = int(input('Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit  \n Please enter an action: \n'))
    if choose < 6:
        if choose == 1:
            print()
            item = input('What item would you like to add? \n')
            print(f'What is the price of the {item}? ')
            precio = input()
            precio = int(precio)
            items.append(item)
            precios.append(precio)
            print(f' {item} has been added to the cart.')
        elif choose == 2:
            print()
            x = 'Items'
            print(f' {x:16}', end=" ")
            print("Prices")

            size_of_list = len(items)
            for i in range(size_of_list):
                print(f' {i+1} {items[i]:15}', f'{precios[i]}')

        elif choose == 3:
            remove = int(input(' Which item would you like to remove? \n'))
            remove = remove - 1

            items.pop(remove)
            precios.pop(remove)
            print('Item removed.')

        elif choose == 4:
            sum = 0
            print(" The prices of the items is")
            for i in precios:
                sum = (sum+i)
            print(f"${sum}")

    else:
        print('Please select again because this number not exist \n')
print('Thanks, goodbye.')
