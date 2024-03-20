"""
Exercises related to sets


python_hybrid_class = ['foo', 'bar']
ui_ux_class = ['bar', 'baz']

#Given a list of students in 2 classes, print overall unique students

overall_students = set(python_hybrid_class).union(ui_ux_class)
print(overall_students)

#UseCase: Given a list of students in 2 classes, find students attending both classes
students_attending_all_classes = set(python_hybrid_class).intersection(
    ui_ux_class)
print(students_attending_all_classes)

#Ex1 

set_1 = {"A", "B", "E", "J", "L", "O", "K", "Y", "N"}
set_2 = {"c", "B", "D", "N", "P", "Y", "A", "J", "M"}

#print common elements in both sets
common_elements = set_1.intersection(set_2)
print(common_elements)

#print total number of number unique alphabets from both set
unique_alphabets = set_1.union(set_2)
print(len(unique_alphabets))

#print alphabets that are in set2 but not in set1
set_2_alphabets = set_1.symmetric_difference(set_2)
print(set_2_alphabets)
"""
#List Comprehension 

python_hybrid_class = [
    {"name":"foo","country":"vietnam"},
    {"name":"bar","country":"mongolia"}
]

student_names_list = [student["name"] for student in python_hybrid_class]

print(student_names_list)