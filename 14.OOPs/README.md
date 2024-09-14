# OOP IN PYTHON

#### To map with real world scenarios, we started using objects in code

#### This is called OBJECT ORIENTED PROGRAMMING

## Class And Object in Python

#### Class is a blueprint for creating objects.

    # Creating class
    class Student:
        name = "Alicent"

    # Creating object(instance)
    s1 = Student()
    print(s1.name)

## \_\_init\_\_ Function

### Constructor

#### All classes have a function called \_\_init\_\_(), which is always executed when the object is being initiated.

    # Creating class
    class Student:

        #Default Constructor
        def __init__(self):
            pass

        # Parameterized constructor
        def __init__(self,fullname):
            self.name = fullname

#### The self parameter is a reference to the current instance of the class, and is used to access varaiables that belongs to the class.

## Class And Instance Attributes

**Class Attribute** => _Defined for class and they are common for every objects of the class_ <br>
**Object Attribute** => _Defined for objects and they differ from each obj._

### Priority of obj_attr > Priority of class_attr

## Methods

**Methods are functions that belongs to objects.**<br>
Example :

    # Creating class
    class Student:
        def __init__(self,fullname):
            self.name = fullname
        def hello(self):
            print("hello",self.name)

    # Creating Object
    S1 = Student()
    S1.hello()

## Static Method

**Methods that dont use self parameter and works at class level**

    class Student:
        @staticmethod
        def college():
            print("Model Engineering College")

_Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it._

## ABSTRACTION

#### Hiding the implementation details of a class and only showing the essential features to the user.

## ENCAPSULATION

#### Wrapping data and functions into a single unit(object).
