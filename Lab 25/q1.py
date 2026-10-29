"""Define a class called ’Car’. The class intance should take required arguments as make,
model, year and color. Define default values of ’False’ for the attributes called ’started’,
0 for the attribute ’speed’, and ’200’ as the maximum speed. There should be a total of
7 attributes in the __init__ function."""

class Car:
    showroom = "NewAge"

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name

    @staticmethod
    def show_intro_message():
        print("This class represents cars and their attributes.")


# (a) Create an instance of the above class called toyota_camry with arguments of car
# make as ’Toyota’, model as ’Camry’, year as ’2022’ and color ’Red’. Print the values of
# these attributes using the instance you just created.

toyota_camry = Car("Toyota", "Camry", 2022, "Red")

print("Toyota Camry attributes:")
print("Make:", toyota_camry.make)
print("Model:", toyota_camry.model)
print("Year:", toyota_camry.year)
print("Color:", toyota_camry.color)
print("Started:", toyota_camry.started)
print("Speed:", toyota_camry.speed)
print("Maximum speed:", toyota_camry.max_speed)


# (b) Create another instance of this class called ’ford mustang’ with make as ”Ford”,
# model as ”Mustang”, year 2022 and color ’Black’.Print all the 7 attributes for this instance.

ford_mustang = Car("Ford", "Mustang", 2022, "Black")

print("\nFord Mustang attributes:")
print("Make:", ford_mustang.make)
print("Model:", ford_mustang.model)
print("Year:", ford_mustang.year)
print("Color:", ford_mustang.color)
print("Started:", ford_mustang.started)
print("Speed:", ford_mustang.speed)
print("Maximum speed:", ford_mustang.max_speed)


# (c) How can you be sure that the above attributes belong to the instance and not the
# class? Try typing print(Car.make). Do you get an error, and if so what error do you
# get? How will you fix this error in your main program?

try:
    print(Car.make)
except AttributeError as e:
    print(type(e).__name__ + ":", e)

print("Toyota make:", toyota_camry.make) # Correct way to access an instance attribute


# (d) Execute the command print(Car.__dict__). Describe the output. The __dict__
# attribute holds a dictionary containing the writable members of the underlying class or
# instance. Each key value represents an attribute or method name. When you access a
# class member through the class object, Python automatically searches for the member’s
# name in the __dict. If the name isn’t there, you get an AttributeError.

print("\nCar class dictionary:")
print(Car.__dict__)


# (e) Now define a class attribute called showroom with value NewAge. Also define a function
#  with decorator @classmethod that changes this value upon user request.
#  Again print the value of __dict__ attribute, what is the output? Describe the output.

print("\nOriginal showroom:", Car.showroom)

Car.change_showroom("AutoWorld")

print("Updated showroom:", Car.showroom)
print("\nUpdated Car class dictionary:")
print(Car.__dict__)


# (f) Print the value of toyota_camry.__dict__. How is this output different from
# Car.__dict__? Explain.

print("\nToyota Camry instance dictionary:")
print(toyota_camry.__dict__)


# (g) Python also supports what are called magic methods or dunder (double underscore)
# methods that are called automatically in response to specific operations. For example, de-
# fine a function as below. and execute the statement print(str(<name-of_class)).
# Test this with the above two class instances you created. For example str(toyota_camry).
# What is the output? There are other magic methods such as ___iter__, __repr__ etc.

print("\nString representation:")
print(str(toyota_camry))
print(str(ford_mustang))


# (h) Define a static method called show_intro_message that prints the purpose of this class.

print("\nIntroduction:")
Car.show_intro_message()
