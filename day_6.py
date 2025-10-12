#Exercise 1
# Create an empty tuple
# empty_tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# sisters = ('Ada', 'Gosia', 'Kasia')
# brothers = ('John', 'Adam')

# siblings = sisters + brothers
# print(len(siblings)) #5

# #add father and mother
# family_members = siblings + ('Zbychu', 'Ania')
# print(family_members)


#Exercise 2
# Unpack siblings and parents from family_members
# *siblings, father, mother = family_members


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely

# fruits = ('apple', 'orange')
# vegetables = ('tomato', 'potato', 'cucumber')
# animal = ('becon', 'meat')

# food_stuff_tp = fruits + vegetables + animal

# food_stuff_lt = list(food_stuff_tp)

# print(len(food_stuff_lt))
# middle = food_stuff_lt[3]
# print(middle)

# first3 = food_stuff_lt[:3]
# last3 = food_stuff_lt[-3:]
# print(first3)
# print(last3)

# del food_stuff_tp


# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

x = 'Estonia' in nordic_countries
print(x)

y = 'Iceland' in nordic_countries
print(y)