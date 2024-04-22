class Dog:
    def __init__(self, name, age, breed, birthday):
        self.name = name
        self.age = age
        self.breed = breed
        #1 Improve by addining birthday attribute
        self.birthday = birthday
        self.is_hungry = True

    def bark(self):
            return "Woof! Woof!"
        
    def eat(self):
            self.is_hungry = False
            return f"{self.name} is eating"
        
        #3 Improve by making the dog hungry after playing
    def play(self):
            #4 Improve by ensuring the dog does not play if hungry
            if not self.is_hungry:
                self.is_hungry = True
                return f"{self.name} done playing"
            else:
                return f"{self.name} won't play"