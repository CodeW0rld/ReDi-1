# Work on this exercise alone or in a group.
# 1. Create a shopping list with 5 elements.
# 2. Define and print the shopping_list
# 3. Add three more elements to the shopping list, by using input() and shopping_list.append()
# 4. Sort the shopping list alphabetically.
# 5. Remove the second element from your list (find the right command in the Python Documentation: https://docs.python.org/3/tutorial/datastructures.html)

"""
shopping_list = ['orange', 'banana', 'strawberry', 'melon', 'pear']

print("Original Shopping List:")
print(shopping_list)

item1 = input("Enter item 1 to add to the shopping list: ")
item2 = input("Enter item 2 to add to the shopping list: ")
item3 = input("Enter item 3 to add to the shopping list: ")


shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)

shopping_list.sort()

del shopping_list[1]

print("Modified Shopping List:")
print(shopping_list)
"""
# ask user for input of lastname, firstname and store data (at least twice)
# put the data into a list
# print list of firstnames     

name_list = []

count = 0
while count < 2:
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    name_tuple = (last_name, first_name)
    name_list.append(name_tuple)
    count += 1
    
print("List of First Names:")

for last_name, first_name in name_list:
    print(first_name)