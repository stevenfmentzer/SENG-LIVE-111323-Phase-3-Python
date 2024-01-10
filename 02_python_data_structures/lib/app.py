# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
more_pet_names = ['Barbie']
# Reading Information From Lists
#2. ✅ Return the first pet name 
pet_names[0]

#3. ✅ Return all pet names beginning from the 3rd index
pet_names[3:]

#4. ✅ Return all pet names before the 3rd index
pet_names[0:2]

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
pet_names[3:7]

#6. ✅ Find the index of a given element
pet_names.index('Luke')

#7. ✅ Reverse the original list
pet_names[::-1]
pet_names.reverse()

#8. ✅ Return the frequency of a given element 
pet_names.count('Luke')

# Updating Lists
#9. ✅ Change the first element to all uppercase 
pet_names[0].upper()

#10. ✅ Append a new name to the list
pet_names.append("Ben")

#11. ✅ Add a new name at a specific index
pet_names.insert(3, "Ken")

#12. ✅ Add two lists together 
pet_names.extend(more_pet_names)

#13. ✅ Remove the final element from the list
pet_names.pop()

#14. ✅ Remove element by specific index
pet_names.pop(3)
pet_names.remove(pet_names[3])

#15. ✅ Remove a specific element 
pet_names.remove("Rose")

#16. ✅ Remove all pet names from the list
pet_names.clear()

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable
    # List : Mutable
    # Tuple : Immutable

# Tuple is an immutable data type that can also store many types of data.

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = ( 1, 2, 3, 4, 5, 6, 7, 7, 7, 7 )

#18. ✅ Print the first pet age
pet_ages[0]

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
pet_ages.pop()

#20. ✅ Attempt to change the first element (should error)
pet_ages[0] = 13

# Tuple Methods
#21. ✅ Return the frequency of a given element
pet_ages.count(12)

#22. ✅ Return the index of a given element 
pet_ages.index(12)

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
number_range = range(10)

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}
pet_info_rose = dict(name='rose', age=11, breed='domestic long')

#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_2 = dict(name="Hazel", age=2, breed="labdoodle")


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
print(pet_info_rose['name'])

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
print(pet_info_rose.get('age'))

# Updating 
#29. ✅ Update the pets age to 12
pet_info_rose['age'] = 12

#30. ✅ Update the other pets age to 26
pet_info_spot['age'] = 26
pet_info_spot.update({'age' : 26})

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
del pet_info_rose['age']

#31. ✅ Delete the other pets age using ".pop"
pet_info_spot.pop('age')

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_rose.popitem()

# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
for num in range(10):
    print (num)

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
for num in range(50,60,2):
    print (num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info: 
    print (pet)

#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
def function_1(input_list):
    for item in input_list: 
        print (item)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
#[{}, {}, {}] #2 
def count_increment(lst):
    counter = 0
    while(counter < len(lst)):
            counter += 1
    return counter
# count_increment(pet_info)

def count_list_items(input_list):
    counter = 0 
    while counter < len(input_list):
        counter += 1
    return counter

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

def update_pet_age(pet_list, name, new_age):
    index = 0
    while index < len(pet_list) and pet_list[index]['name'] != name: 
        index += 1
        if index < len(pet_list):
            pet_list[index]['age'] = new_age
        else: return 'pet not found'

# update_age(pet_info, 'rose', 120)


# def update_age(lst, name, age):
#     idx = 0
#     print(len(lst), idx)
#     while idx < len(lst) and lst[idx].get('name') != name:
#         print("every item----", lst[idx])
#         idx += 1
#     if idx < len(lst) and lst[idx].get('name') == name:
#         print(lst[idx])
#         lst[idx]['age'] = age
#         return lst[idx]
#     else:
#         return 'pet not found'


# pet_info = [{'name': 'rose', 'age': 100}, {'name': 'lily', 'age': 80}]
# result = update_age(pet_info, 'rose', 120)
# print(result)

                 
# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
uppercase_names = [pet['name'].upper() for pet in pet_info]

print(uppercase_names)

# find like
#40. ✅ Use list comprehension to find a pet named spot
spot_pet = [pet for pet in pet_info if pet['name'].lower() == 'spot']

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
pet_under_3 = [ each_pet for each_pet in pet_info 
    if each_pet.get('age') < 3]

pet_3 = [pet for pet in pet_info if pet['age'] < 3]

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

pet_3_generator = (pet for pet in pet_info if pet['age'] < 3)