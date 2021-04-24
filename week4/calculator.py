child_meal = float(input("What is the price of a child's meal? ")) #4.50
adult_meal = float(input("What is the price of an adult's meal? ")) # 9.00
price_drink = float(input("What is the price of a drink ")) # 9.00
drinks = float(input("How many drinks ")) # 9.00
children = int(input("How many children are there? ")) #4
adults = int(input("How many adults are there? ")) #2
tax_rate = float(input("What is the sales tax rate? ")) #6

subtotal = (child_meal * children) + (adult_meal * adults) + (price_drink * drinks)
sale_tax = subtotal *(tax_rate/100)
total = subtotal + sale_tax


print()
print(f"Subtotal: $ {subtotal} ")
print(f"Sales Tax: $ {sale_tax:.2f}")
print(f"Total: $ {total} ")
print()
payment = float(input("What is the payment amount? ")) # 40
print()
change = payment - total
if  change < 0 :
    need = -1 * change
    
    change = f"you need {need:.2f} for paying the bill"
    print(change)
else:
    print(f"Change: $ { change:.2f}")