numbers = []
number = -1

while number != 0:
    number = int(input('Please enter a number: '))
    if number != 0:
        numbers.append(number)

print(numbers)

sum = 0

for number in numbers:
    sum = sum + number

print(f'The sum is: {sum}')

count = 0

count = sum / len(numbers)

print(f'The average is: {count}')

max = 0
numbers.sort()
print(numbers)
max_number = len(numbers) - 1
max = numbers[max_number]

print(f' The max number is {max}')
