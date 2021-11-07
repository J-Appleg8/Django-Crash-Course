# ##############################################################################################
# Object Oriented Programming (OOP) - Part 1 ###################################################

# Lets start the lesson by remembering about the Basic Python Objects.
# For example:
l = [1, 2, 3]

# Remember how we could call methods on a list?
l.count(2)


# What we want to do is create an object that has methods or attributes inside of it
# That can be used to affect the object itself

# In Python, everything is an object
# using print(type([1,2,3])) would return back that it is a class: 'list' type object
# print(type(20.0)) --> <class 'float'>

# First step is learning how to create our own classes so that we can create our own objects

# ####################################################################
# Class

# Note how x is now the reference to our new instance of a Sample class.
# In other words, we **instantiate** the Sample class.
print("----------- Creating Instance Of Class -----------------------")
print("")


class Sample:
    pass


x = Sample()
print(type(x))


# ###################################################################################################
# 1.) Object Oriented Programming (OOP) - Part 2 ########################################################

# Inside of the class we currently just have pass.
#  But we can define class attributes and methods.
#
# An **attribute** is a characteristic of an object.
# A **method** is an operation we can perform with the object.

# For example we can create a class called Dog
# An attribute of a dog may be its breed or its name
# While a method of a dog may be defined by a .bark() method which returns a sound.


####################################################################
# 2.) Attributes

# The syntax for creating an attribute is:
# ---self.attribute = something

# Whenever you have a class, you will be defining methods inside of the class
# --The __init__() special method is used to initialize the attributes of an object
# ---Add attributes to the method by entering parameters inside of the __init__() paren

# If attributes other than just 'self' are added to a method:
# ---Then you must provide that as an argument when creating an instance of that class

# Example: attribute 'breed' was added
# ---__init__(self, breed)

# So it will error out if you tried to say:
# ---mydog = Dog()

# The special method __init__() is called automatically right after the object has been created:
# ---def __init__(self, breed):

# Once we initialize the object, we call the __init__() method automatically

# Then each attribute in a class definition begins with a reference to the instance object
# ---Which is basically saying "refer to this particular instance of this object"
# ---It is by convention named 'self'

# The breed is the argument
# ---The value is passed during the instantiation, or initialization, of the class self
# ---Where we say self.breed = breed
# And now we have created an instance of the Dog class

# self.breed = breed
# ---breed on the right hand of the = is the input name
# ---self.name is assigning the .name to the initialization of that dog

print("")
print("----------- Creating init Method -----------------------")
print("")


class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed="Lab", name="Sammy")
print(type(mydog))
print(mydog.breed)
print(mydog.name)


####################################################################
# 3.) Class Object Attributes

# In Python there are also *class object attributes*. These Class Object
# Attributes are the same for any instance of the class. For example, we could
# create the attribute *species* for the Dog class. Dogs regardless of their
# breed,name, or other attributes will always be mammals.
# We apply this logic in the following manner:

# Note that the Class Object Attribute is defined outside of any methods in the
# class. Also by convention, we place them first before the init.


class Cat:

    # Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


####################################################################
# 4.) Methods

# Methods are functions defined inside of the body of a class
# ---Are used to perform operations with the attributes of our objects

# You can basically think of methods as functions acting on an Object that take
# ---the Object itself into account through its *self* argument.

# Passing the keyword self tells the method area that its not a free-floating function but that
# Its a method of that class
print("")
print("----------- Creating Method Inside Class -----------------------")
print("")


class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(100)
print(myc.radius)
print(myc.area())


####################################################################
# 5.) Inheritance

# Inheritance is a way to form new classes using classes that have already been defined
# ---The newly formed classes are called derived classes
# ---The classes that we derive from are called base classes

# Important benefits of inheritance are code reuse and reduction of complexity of a program
# ---The derived classes (descendants) override or extend the functionality of base classes (ancestors)

# In this example, we have two classes: Animal and Dog
# ---The Animal is the base class
# ---The Dog is the derived class.

# The derived class inherits the functionality of the base class.
# ---* It is shown by the eat() method.

# The derived class modifies existing behavior of the base class.
# ---* shown by the whoAmI() method.

# Finally, the derived class extends the functionality of the base class, by defining a new bark() method.
print("")
print("----------- Class Inheritance -----------------------")
print("")


class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("Dog eating")


mya = Animal()
mya.who_am_i()
mya.eat()

print("----------- descendant class ---------------")

mydogg = Dog()
mydogg.who_am_i()
mydogg.eat()
mydogg.bark()


####################################################################
# 6.) Special Methods

# Classes in Python can implement certain operations with special method names
# These methods are not actually called directly but by Python specific language syntax.


print("")
print("----------- Special Methods -----------------------")
print("")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author {}, Pages {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


b = Book("Python", "James", 200)

print(b)
print(len(b))
del b

# For more great resources on this topic, check out:
#
# [Jeff Knupp's Post](https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
#
# [Mozilla's Post](https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming)
#
# [Tutorial's Point](http://www.tutorialspoint.com/python/python_classes_objects.htm)
#
# [Official Documentation](https://docs.python.org/2/tutorial/classes.html)
