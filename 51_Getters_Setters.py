# A function that are used to set any values (return) for any function can be referred to as getters and setters

# Getters in python - It is used to access the value of an object properties. They are used to return the value of a specific property. They are defined using the @property decorator.

# In Python property()is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(), and delete()

# Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code. 


class Myclass:
    def __init__(self, value):
        self._value = value
        
    def shoe(self):
        print("Value is ", self._value)
        
        
    @property
    def val(self):
        return self._value * 100
    
    



obj = Myclass(10)
obj.shoe()
print(obj.val)