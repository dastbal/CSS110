loan = int(input("How large is the loan? "))

history = int(input("How good is your credit history? "))

income = int(input("How high is your income? "))

payment = int(input("How large is your down payment? "))

decicion = True

if  loan >= 5:
    if history >= 7 and income>=7 :
        decicion = True
    elif history >= 7 or income>=7 :
        if  payment >= 5:
            decicion = True
        else:
            decicion = False
    elif history < 7 and income < 7:
        decicion = False
else: 
    if history <4:
        decicion = False
    else:
        if  payment >= 7 or income>=7 :
            decicion = True
        elif  payment >= 4 and  income>= 4 :
            decicion = True
        else:
            decicion = False

if decicion:
    print(" decision : yes")
else:
    print(" decision : No")
