#Exercise 1
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

dog = {}
dog['name'] = 'Azor'
dog['color'] = 'brown'
dog['breed'] = 'German Shepard'
dog['legs'] = '4'
dog['age'] = '2'
print(dog)

student = {'first_name' : 'Aga',
           'last_name' : 'Kowalska',
           'gender' : 'femanle',
           'age' : '20',
           'martial status' : 'single',
           'skills' : ['drawing', 'dancing'],
           'country' : 'poland',
           'city' : 'poznan',
           'address' : 'poznanska 25'
}

print(len(student)) #9

skills = student['skills']
print(skills)
print(type(skills)) #list

student['skills'].append('singing') #add singing

keys = student.keys() #get keys as a list
print(keys)

values = student.values() #get values as a list
print(values)

print(student.items()) #change dictionary to a list of tuples

student.pop('first_name') #delete first_name
print(student)

del student