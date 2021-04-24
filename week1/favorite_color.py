# greeting  and to ask the user to write your favorite color
print("Hello, you are welcome.")
color = input("Please type your favorite color: ")

# to verify if we have the same favorite color
my_color = "blue"
if (my_color == color):
    answer = " That is my favotite color too"
else:
    answer = "Your favorite color is cool"

# display and comment about the color that the user wrote.
print("Your favorite color is, " + color + "!")
print(answer)
