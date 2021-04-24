
age = int(input("How old are you? "))
birthday = age+1
print(f"On your next birthday, you will be {birthday}")
print()

cartons = int(input("How many egg cartons do you have? "))
eggs = cartons*12
print(f"You have {eggs} eggs")
print()

cookies = int(input("How many cookies do you have? "))
if cookies == 0:
    portion = 0
    print(f"Each person may have {portion} cookies")
else:
    person = int(input("How many people are there? "))
    portion = cookies/person
    print(f"Each person may have {portion} cookies")
