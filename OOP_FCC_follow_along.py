
# The method or otherwise must explicitly call it to ensure proper initialization of the base class part of the instance
# the object is the calling and assigning of a class to a variable if you want to make a new variable or object with
# that class you will need __init__ to initialize a new instance of that class to a new object.
# The second purpose is it allows you to pass arguments to a class when calling the class. Without this function inside
# the class when you call the class no arguments would be able to go inside thereby getting nothing in return.

# Instance variables are declared inside a class method using the self keyword. We use a constructor to
# define and initialize the instance variables.


class Item:
    def __init__(self, name: str, price: float, quantity):  # you can add data types to these
        self.name = name  # so basically instead of assigning these variables outside of the class you can use __init__
        self.price = price  # to allow it to initialize a new instance everytime called with these instance variables
        self.quantity = quantity  # ready to have something assigned

        assert price >= 0  # assert need no colon you can add a string with assert to give an error message
        assert quantity >= 0, f'quantity cannot be zero or less, your\'s was {self.quantity}.'

    def calc_total_price(self):  # it is invisible but __new__ is called before __init__, so a __new__ class object is
        # __init__ialized To create instances of a class, you call the class using class name and pass in whatever
        # arguments its __init__ method accepts.
        return self.price * self.quantity

# The rest of My comments are useless, having an __init__ simply requires a class to have required values when the class
# is called and then the other called methods are acted upon that class.
# The method or otherwise must explicitly call it to ensure proper initialization of the base class part of the instance


item1 = Item("phone", 100, 5)  # this is the class itself not the functions therein
item2 = Item("laptop", 1000, 3)
print(Item.calc_total_price(item1))
item3 = 5

print(item1.name)
print(item2.price)
print(type(item1))
print(type(item2))
print(type(Item))  # Built-in types are now also labelled classes, and you can extend them at will.

# More Magic Methods:


# Classic vs Static Methods: Until you create an instance with __init__ there is no self. Need to learn about static MDs

# The getattr(obj, name[, default]): to access the attribute of object.
# The hasattr(obj,name): to check if an attribute exists or not.
# The setattr(obj,name,value): to set an attribute. If attribute does not exist, then it would be created.
# The delattr(obj, name): to delete an attribute.


# The rest of My comments are useless, having an __init__ simply requires a class to have required values when the class
# is called and then the other called methods are acted upon that class.
# The method or otherwise must explicitly call it to ensure proper initialization of the "base class" of the instance.
# Making a class is making your own data type, when you check it's item type it will be set to the class.

# it is invisible but __new__ is called before __init__, so a __new__ class object is
# __init__ialized To create instances of a class, you call the class using class name and pass in whatever
# arguments its __init__ method accepts.

