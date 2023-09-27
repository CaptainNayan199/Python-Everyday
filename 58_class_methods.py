# class methods are special kinds of methods that belongs to class itself, rather than to any instances of that class. It is a special kind of class function that is only work the class, not for the objects created from the class.
# They are defined inside a class, just like regular methods.
# The can be called inside a class, without need to define or create an object

# Why to create class methods ? 
# To modify class level variables

# How to create a class methods? - to create a class method in python we should use @classmethod as a decorator, and it should have the  class itself (usually named cls, or you can give any name) as its first argument. Here's a simple example:

class Myclass:
    class_variable = 10 # a class level variable with its value 10

    def __init__(self, a):
        self.instance_variable = a
    

    @classmethod
    def class_method(cl, x):
        cl.class_variable += x