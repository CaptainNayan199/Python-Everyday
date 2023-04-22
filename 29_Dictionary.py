# Dictionary in python are as similar as real world dictionary (oxford), it contains multiple keys with their respective values.
# They are ordered collection of data.
# It is the combination of key value pairs.
# It is enclosed inside a curly braces as like set
# We can create a mapped data/elements in the dictionary.
# they store multiple items in a single variable.
# previously dict was unordered, but now they made this ordered.

dic1 = {
    "Name": "Nayan",
    "Age" : 20,
    "College": "TU",
    "isMarried": False
}
# so this is my simple dictionary with some key and its respective values.
# now i can access those by referencing theirs keys

print(dic1) #this prints all the elements with keys as well as values.

# we can access individual or desired elements too

print(dic1["Name"])
print(dic1.get("Name"))
# we can use this two methods two get the values of the respected keys. Both are same method, but...

#PS: the first methods throws error if key is not found, but the second method does not throws error.

print(dic1["Nameee"]) # interpreter throws error saying key not found
print(dic1.get("Nameee")) # returns None if key is not found, does not throw the error

# they are like discard and remove method in sets, one throws error while other does not.

# Accessing multiple keys / values from a dict : 


dic1 = {"Name": "Nayan", "Age" : 20, "College": "TU", "isMarried": False
}

print(dict1.keys) # this returns all the keys present in the dictionary
print(dict1.values) #this returns all the values present in the dictionary





