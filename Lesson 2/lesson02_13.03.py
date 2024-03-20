"""
name = input("Enter your name: ")
nickname = input("Enter your nickname: ")
color = input("Enter your favorite color: ")
print(name, "--", nickname, "--", color)
"""

"""
user_num1 =input("Enter a number: ")
num1 = float(user_num1)
user_num2 = input("Enter another number: ")
num2 = float(user_num2)
print(type(user_num1))
print(type(user_num2))

print(user_num1 + user_num2)
print(num1 + num2)
"""

"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print (num1 + num2)
"""

#Devision for if, elif, else

"""
answer = input("Do you like ice cream (Y/N): ")

#if answer == "Y" or answer == "y":
if answer.lower() == "y" or answer.lower() == "yes":
    print("Great! Let's go get some!")
else:
    print("Ooh too bad, I'm really craving ice cream.")

print("Thanks for chatting")
"""

"""
number = int(input("Enter a number: "))
if number < 0:
    print("You entered a negative number.")
elif number == 0:
    print("You entered 0.")
else:
    print("You entered a positive number.")
    
print("Thanks for playing!")
"""

'''
current_number = 1
max_printed_number = 10

while current_number <= max_printed_number:
    print("Printing number:", current_number)
    # current_number = current_number + 1
    current_number += 1
print("Thanks!")
'''

'''
for counter in range(0, 30, -3):
    print(counter)
'''

'''
user_input =int(input("Enter any whole number: "))

if user_input < 0:
    print("Negative numbers aren't permitter.")
elif user_input == 0:
    print(0)
else:
    result = 0

    for x in range(0, user_input+1):
        result += x
    
    print(result)
'''

#Divison Loops

while True:
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter another number: "))

    print(num_one, "/", num_two, "=", num_one / num_two)

    response = input("Try again? (Y/N) :")
    if response.lower() == "n":
        break