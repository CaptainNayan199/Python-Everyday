# So lets talk about **kwargs in today session.

# **kwargs - same as *args, but will pack all the arguments into a dictionary, and is basically for keyword arguments, very useful when we need to accept multiple and different dta types key word arguments


# kwargs - keyword arguments

# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.


# Eg 1 : 

def price(**kwargs):
    for key, value in kwargs.items():
        print("Price of %s is %s" % (key, value))

price(Apple=200, Mango=400, Grapes=500, Kiwi=1000)