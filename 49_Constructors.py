# A constructor is a special type of member function that is called automatically when an object is created
# They help in creating an object, helps in initialization
# There are in general two types of constructor; default and parameterized 


class Cons:
    name= "Nayan"
    age = 20

    def Data(self):
        print(f"Name is {self.name} and age is {self.age}")

obj = Cons()
obj.Data()