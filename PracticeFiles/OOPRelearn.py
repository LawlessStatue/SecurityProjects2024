"""class Pet: # super = class we inherit from
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #try to remember
        self.color = color
    
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

class Dog(Pet): 
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

f= Fish("Bubbles", 10)
f.speak()
p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Black")
c.show()
d= Dog("Jill", 25)
d.speak()

class Person:
    numberPeople = 0
    gravity = -9.8
  
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_People(cls): # no object, actiong on class
        return cls.numberPeople
    
    @classmethod
    def add_person(cls):
        cls.numberPeople += 1
    

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_People())
"""

class Math:

    @staticmethod #stays the same
    def add5(x):
        return x + 5
    
    @staticmethod #stays the same
    def pr():
        print("run")

Math.pr()