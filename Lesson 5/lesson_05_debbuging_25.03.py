my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_element(element):
    print(element)

total_sum = 0
for element in my_list:
    total_sum += element
    print_element(element)
    if element > 5:
        print(element)

print("finished")