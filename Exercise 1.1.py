# EXERCISE 1.1.: Write a program that asks the user to give a string as input and:
# Case 1) if the string contains more than 3 characters, prints the number 1
# Case 2) otherwise, prints the number 0

print()
print(('-' * 13) + ' Exercise 1.1 ' + ('-' * 13))
print()

# Ask the user to input a string
user_input = input("Please enter a string: ")

# Check the length of the string using a single if statement
if len(user_input) > 3:
    print(1)

else:
    print(0)

print()
print('-' * 40)
print()
