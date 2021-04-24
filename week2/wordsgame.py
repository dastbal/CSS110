print("Please enter the following: ")
# ask the user for the answer
adjective = input("adjective: ")
animal = input("animal: ")
v1 = input("verb: ")
exclamation = input("exclamation: ")
v2 = input("verb: ")
v3 = input("verb: ")
food = input("food: ")
vowels = "aeiou"

# validate if we nned to display a or an
first_letter = food[0]
an_a = "a"
if first_letter in vowels:
    an_a = "an"
# to print the result
print()
print("Your story is: ")
print()
print(
    f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {v1} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {v2} over and over. Miraculously, that caused it to stop, but not before it tried to {v3} right in front of my family. Finally, to feel better I ate {an_a} {food}. ")
