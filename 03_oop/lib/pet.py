#!/usr/bin/env python3
import ipdb
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 


class Pet:
    pass
# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 


# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg


# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

class Flower:
    def __init__(self, name, color, region):
        self.name = name
        self.color = color
        self.region = region

# Creating instances of the Flower class
flower1 = Flower(name="Poppy", color="Red", region="Mediterranean")
flower2 = Flower(name="Tiger Lily", color="Orange", region="Asia")
flower3 = Flower(name="Sunflower", color="Yellow", region="North America")

# Accessing attributes of each flower instance
print("Flower 1: Name - {}, Color - {}, Region - {}".format(flower1.name, flower1.color, flower1.region))
print("Flower 2: Name - {}, Color - {}, Region - {}".format(flower2.name, flower2.color, flower2.region))
print("Flower 3: Name - {}, Color - {}, Region - {}".format(flower3.name, flower3.color, flower3.region))

class Owner: 
    def __init__(self, age):
        self.age = age

    def get_name(self):
        print("retrieveing owner's name")
    
    def set_name(self, name):
        print("setting up owner's name")
        if(isinstance(name, str)): # isinstance returns True/False
            self._name = name
        else: 
            print("name must be a string")

katie = Owner(18)
katie.set_name("KATIE")
print(katie.get_name())

katie.get_name()
ipdb.set_trace()
