#Exercise 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# age = int(input('Enter your age: '))
# if age > 18:
#     print('You are old enough to learn to drive.')
# else:
#     gap = 18 - age
#     print(f'You need {gap} more years to learn to drive.')



#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# my_age = 20
# your_age = int(input('Enter your age: '))
# if my_age > your_age:
#     diff = my_age - your_age
#     if diff == 1:
#         print(f'I am {diff} year older than you')
#     else:
#         print(f'I am {diff} years older than you')
# elif my_age < your_age:
#     diff = your_age - my_age
#     if diff == 1:
#         print(f'You are {diff} year older than me')
#     else:
#         print(f'You are {diff} years older than me')
# else:
#     print('We are the same age')



# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# a = int(input('Enter number one: '))
# b = int(input('Enter number two: '))

# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print('a is smaller than b')
# else:
#     print('a is equal to b')


#Exercise 2
# Write a code which gives grade to students according to theirs scores:

# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# score = int(input('Enter your score: '))
# if 90 <= score <= 100:
#     print('Grade: A')
# elif 70 <= score <= 89:
#     print('Grade: B')
# elif 60 <= score <= 69:
#     print('Grade: C')
# elif 50 <= score <= 59:
#     print('Grade: D')
# else:
#     print('Grade: F')




# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer.

# month = input('Ener month: ').capitalize()     #capitalize makes it case-insensitive - every combination of the word will work - october, OCTOBER, October
# if month == 'September' or month == "October" or month == "November":  #done with or
#     print('It is Autumn')
# elif month in ['December', 'January', 'February']:  # done with list
#     print('Winter')
# elif month in ["March", "April", "May"]:
#     print("The season is Spring.")
# elif month in ["June", "July", "August"]:
#     print("The season is Summer.")
# else:
#     print('Invalid month.')





# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# a = input('Type a fruit: ')
# if a in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(a)
#     print(fruits)




#Exercise 3
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:     Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person['skills']
    mid_skill = len(skills) // 2
    print(skills[mid_skill])

    if 'Python' in skills:
        print('True')
    else:
        print('False')
    
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print('He is backend developer')
    elif set(skills) == {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person['first_name']} {person["last_name"]} lives in {person["country"]}. He is married')
