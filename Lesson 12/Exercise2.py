from Exercise1 import Dog

# Creating a Dog object
my_dog = Dog(name="Puppy", age=2, breed="Shiba", birthday="2020-01-01")

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")
print(f"My dog's breed is {my_dog.breed}.")
print(f"My dog's birthday is {my_dog.birthday}.")

print(my_dog.bark())
print(my_dog.eat())
print(my_dog.play())

my_dog.is_hungry = True


#1 Improve by printing birthday attribute
#2 Improve by calling play method
#3 Improve by making the dog hungry after playing