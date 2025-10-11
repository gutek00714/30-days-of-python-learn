# Exercise 1

name = 'kaziu'
last_name = 'nowak'
full_name = name + last_name
country = 'poland'
city = 'warszawa'
age = 100
year = 2025
is_married = False
is_true = True
is_light_on = True
a, b, c = 5, 10, 15

#Exercise 2

print(type(name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

print(len(name))

if len(name) > len(last_name):
    print("Name is longer than last name")
elif len(name) < len(last_name):
    print("Name is shorter than last name")
else:
    print("Name and last name are equal length.")

num_one = 5
num_two = 4

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = 30
pi = 3.14
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

radius2 = float(input("Enter radius: "))
area = pi * radius2 ** 2

first_name = input("Enter first name: ")
last_name1 = input("Enter last name: ")
country1 = input("Enter country: ")
age1 = input("Enter age: ")