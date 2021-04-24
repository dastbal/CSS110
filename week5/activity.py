x= int(input("What is the first number? "))
y= int(input("What is the second number? "))
first= "The first number is not greater"
equal= "The numbers are not equal"
second=" The second number is not greater"
if  x > y:
    first="The first number is greater"
    second="The second number is not greater"
elif x < y:
    first= "The first number is not greater"
    second="The second number is  greater"
else:
    equal ="The numbers are equal"

print(first)
print(equal)
print(second)

animal = input("What is your favorite animal? ")
favorite_animal = "That one is not my favorite."
animal = animal.lower()
if animal== "lion" :
    favorite_animal= "That one is my favorite."
print(favorite_animal)