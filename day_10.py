#Exercise 1
# Iterate 0 to 10 using for loop, do the same using while loop.
# for i in range(11):
#     print(i)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1



# Iterate 10 to 0 using for loop, do the same using while loop.
# for i in range(10, -1, -1):  #10 - starting number; -1 - loop ends before -1 so on 0; -1 - counting backwards
#     print(i)

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1



#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# x = ['#']
# for i in x:
#     print(x)
#     x.append('#')
#     if len(x) > 7:
#         break                                                          #first try

# for i in range(1, 8): #run 1 to 7 times                                #second try
#     print('#' * i) #repeat the hashtag symbol i times in the line



#Use nested loops to create the following:
# i = 0
# while i <= 7:
#     print('# ' * 8)                                                    #not nested
#     i += 1

# for i in range(8):
#     for x in range(8):
#         print('#', end=' ')
#     print()



# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# for i in range(11):
#     x = i * i
#     print(f'{i} x {i} = {x}')



# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# items = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for i in items:
#     print(i)



# Use for loop to iterate from 0 to 100 and print only even numbers
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue 



# Use for loop to iterate from 0 to 100 and print only odd numbers
# for i in range(101):
#     if i % 2 != 0:
#         print(i)
#     else:
#         continue



#Exercise 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# suma = 0
# for i in range(101):
#     suma += i
# print('The sum of all numbers is', suma)



#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# odd_sum = 0
# even_sum = 0
# for i in range(101):
#     if i % 2 == 0:
#         even_sum += i
#     if i % 2 != 0:
#         odd_sum += i
# print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')



#Exercise 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# from countries import countries

# for i in countries:
#     if 'land' in i:
#         print(i)



#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# a = ['banana', 'orange', 'mango', 'lemon']
# for i in a[::-1]:
#     print(i)



# Go to the data folder and use the countries_data.py file.
#     What are the total number of languages in the data
#     Find the ten most spoken languages from the data
#     Find the 10 most populated countries in the world

from countries_data import countries

# all_languages = []

# for i in countries:
#     all_languages.extend(i['languages'])

# all_languages = set(all_languages)
# print(len(all_languages))             #convert to set because it doent't allow duplicates   # len 112


# Find the ten most spoken languages from the data
all_languages = []

for i in countries:
    all_languages.extend(i['languages'])

language_count = {}
for language in all_languages:
    if language in language_count:
        language_count[language] += 1
    else:
        language_count[language] = 1

sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)  #x represents each element being sorted. x[1] is the second item in the touple. 

sorted_languages = sorted_languages[:10]  #get 10 most spoken languages

for language in sorted_languages:
    print(language[0])



#Find the 10 most populated countries in the world
population = []

for i in countries:
    population.append((i['name'], i['population'])) #double bracket because this is a tuple - which is in brackets. And the outer brackets are from the population.append()

sorted_population = sorted(population, key=lambda item: item[1], reverse=True)

sorted_population = sorted_population[:10]

for i in sorted_population:
    print(i[0])