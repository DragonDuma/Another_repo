#  Class: A user-defined prototype for an object that defines a set of attributes that
# characterize any object of the class. The attributes are data members (class
# variables and instance variables) and methods, accessed via dotted notation.
#  Class variable: A variable that is shared by all instances of a class. Class variables
# are defined within a class but outside any of the class's methods. Class variables
# are not used as frequently as instance variables are.
#  Data member: A class variable or instance variable that holds data associated with
# a class and its objects.
#  Function overloading: The assignment of more than one behavior to a particular
# function. The operation performed varies by the types of objects or arguments
# involved.
#  Instance variable: A variable that is defined inside a method and belongs only to
# the current instance of a class.
#  Inheritance: The transfer of the characteristics of a class to other classes that are
# derived from it.
#  Instance: An individual object of a certain class. An object obj that belongs to a
# class Circle, for example, is an instance of the class Circle.
# Instantiation: The creation of an instance of a class.
# Method : A special kind of function that is defined in a class definition.
# Object: A unique instance of a data structure that is defined by its class. An object
# comprises both data members (class variables and instance variables) and
# methods.
#  Operator overloading: The assignment of more than one function to a particular
# operator.

# You're saying, Fido is a brown dog with 4 legs while Spot is a bit of a cripple and is mostly yellow. The __init__
# function is called a constructor, or initializer, and is automatically called when you create a new instance of a
# class. Within that function, the newly created object is assigned to the parameter self. The notation self.legs is an
# attribute called legs of the object in the variable self. Attributes are kind of like variables, but they describe
# the state of an object, or particular actions (functions) available to the object.
#
# However, notice that you don't set color for the doghood itself - it's an abstract concept. There are attributes
# that make sense on classes. For instance, population_size is one such - it doesn't make sense to count the Fido
# because Fido is always one. It does make sense to count dogs. Let us say there are 200 million dogs in the world.
# It's the property of the Dog class. Fido has nothing to do with the number 200 million, nor does Spot. It's called a
# "class attribute", as opposed to "instance attributes" that are colour or legs above.
# python OOP basically allows you to make your own data types
# The rest of My comments are useless, having an __init__ simply requires a class to have required values when the class
# is called and then the other called methods are acted upon that class.
# The method or otherwise must explicitly call it to ensure proper initialization of the base class part of the instance


class Person:
    pass  # An empty block


p = Person()
print(p)


class WellSaySomething:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("Hi Grandma!!", age, name)  # so I need to pass the function to a variable then print from that variable
# instead of directly from a classes object

    def bark(self, volume):  # the self here must use an instance of the class
        print('woof woof!', volume)


barky = WellSaySomething(16, "Woof")
print(WellSaySomething.bark(barky, "loud"))
print(WellSaySomething.bark(barky, "no"))  # so you can assign the very same variable and print with another value

# the reason you would need __init__, you will need to make a new instance of that object because one object of that
# class already exists
greeting = WellSaySomething(17, "lol")  # need to make the class function a variable or an 'object' to
# access it via dotted notation

one_instance = WellSaySomething(18, "Daniel")
another_instance = WellSaySomething(17, "Granny")


class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name  # no longer need self.name = self.name can simply write the parameter as its name
        self.major = major  # self.major is an attribute of the student class, so the name of the student major is going
        self.gpa = gpa      # to be equal to the value passed in
        self.is_on_probation = is_on_probation  # these are instance variables they are variables of the instance of
# this object

    def on_honor_role(self):  # this is a class function, giving or modifying information about the class
        if self.gpa >= 3.5:
            return True
        else:
            return False

# The rest of My comments are useless, having an __init__ simply requires a class to have required values when the class
# is called and then the other called methods are acted upon that class.
# The method or otherwise must explicitly call it to ensure proper initialization of the base class part of the instance

# The __init__() function is called automatically every time the class is being used to create a new object; it
# 'initializes' a new object of that class. 


student1 = Student("Daniel", "Electrical Engineering", 4.0, False)
student2 = Student("Ronald", "Econ", 3.2, True)
print(student1.gpa)
print(student2.is_on_probation)
print(student2.on_honor_role())
print(student1.on_honor_role())


class Chef:
    def make_chicken(self):  # these are asking to be changed to static because there is no self because of no __init__
        print("The Chef makes chicken.")

    def make_salad(self):
        print("He also makes salad")

    def make_spaghetti(self):
        print("and spaghetti")


my_Chef = Chef()  # test inheritance out here today
my_Chef.make_chicken()


class Special_Chef(Chef):
    def makeRamen(self):
        print("This guy makes ramen as well.")

    def make_salad(self):  # you can override a certain inheritance by making an identically named function and giving
        print("But this dudes salad is different.")   # it new instructions


myasianchef = Special_Chef()
myasianchef.make_salad()

# By what you wrote, you are missing a critical piece of understanding: the difference between a class and an object.
# __init__ doesn't initialize a class, it initializes an instance of a class or an object. Each dog has colour,
# but dogs as a class don't. Each dog has four or fewer feet, but the class of dogs doesn't.
# The class is a concept of an object. When you see Fido and Spot, you recognise their similarity, their doghood.
# That's the class.

# Instantiated definition: In a computer system, any time a new context is created based on some model, it is said that
# the model has been instantiated. In practice, this instance usually has a data structure in common with other
# instances, but the values stored in the instances are separate.
