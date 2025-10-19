# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #Exercise 1
# #Explain the difference between map, filter, and reduce.
# #map - iterates over the list (modify the data); filter - filters the list to meet the criteria - takes only True or False (narrow down the data); reduce - reduces the list to just 1 value by iterating over it (combine the data)

# #Explain the difference between higher order function, closure and decorator
# #higher order function - a function that takes another function as an argument or returns a function as a result; closure - function inside a function; decorator - we use it if we want to modify the existing function but without actualy editing it's code

# # Use for loop to print each country in the countries list.
# # for i in countries:
# #     print(i)


# # # Use for to print each name in the names list.
# # for i in names:
# #     print(i)

# # # Use for to print each number in the numbers list.
# # for i in numbers:
# #     print(i)



# #Exercise 2
# # Use map to create a new list by changing each country to uppercase in the countries list
# countries_upper = map(lambda x: x.upper(), countries)
# # print(list(countries_upper))

# # Use map to create a new list by changing each number to its square in the numbers list
# numbers_square = map(lambda x: x ** 2, numbers)
# # print(list(numbers_square))

# #Use map to change each name to uppercase in the names list
# # def upper_case(name):
# #     return name.upper()

# # names_upper_case = map(upper_case, names)
# # print(list(names_upper_case))                                   #wanted to try it without lambda

# names_upper_case = map(lambda x: x.upper(), names)
# # print(list(names_upper_case))                                     #lambda version


# #Use filter to filter out countries containing 'land'.
# def contains_land(x):
#     if 'land' in x:
#         return True
#     else:
#         return False
    
# land = filter(contains_land, countries)
# # print(list(land))

# # Use filter to filter out countries having exactly six characters.
# def is_six_characters(x):
#     if len(x) == 6:
#         return True
#     else:
#         return False

# countries_six = filter(is_six_characters, countries)
# # print(list(countries_six))

# #Use filter to filter out countries containing six letters and more in the country list.
# def six_more_characters(x):
#     if len(x) >= 6:
#         return True
#     else:
#         return False
    
# six_more = filter(six_more_characters, countries)
# # print(list(six_more))

# #Use filter to filter out countries starting with an 'E'
# def contain_e(x):
#     if x[0] == 'E':
#         return True
#     else:
#         return False

# e_contain = filter(contain_e, countries)
# # print(list(e_contain))

# # Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# lst = names + numbers
# def get_string_lists(item):
#     if isinstance(item, str):
#         return True
#     else:
#         return False

# string_list = filter(get_string_lists, lst)
# # print(list(string_list))

# # Use reduce to sum all the numbers in the numbers list.
# from functools import reduce   #IMPORTANT!!!
# def add_two_numbers(x, y):
#     return int(x) + int(y)

# sum_of_list = reduce(add_two_numbers, numbers)
# # print(sum_of_list)

# #Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# concatenate = reduce(lambda x, y: x + ", " + y, countries[:-1])
# sentence = f"{concatenate}, and {countries[-1]} are north European countries"
# # print(sentence)

# # Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# from countries import countries
# def categorize_countries(countries):
#     countries_list = []
#     for i in countries:
#         if 'land' in i:
#             countries_list.append(i)
#     return countries_list

# # print(categorize_countries(countries))          #works only with 'land'

# def categorize_countries(word):
#     countries_list = []
#     for i in countries:
#         if word in i:
#             countries_list.append(i)
#     return countries_list

# # print(categorize_countries('land'))
# # print(categorize_countries('ia'))
# # print(categorize_countries('island'))
# # print(categorize_countries('stan'))


# #Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# def countries_dict(countries):
#     dictionary = {}
#     for i in countries:
#         if i[0] not in dictionary.keys():
#             dictionary[i[0]] = 1
#         else:
#             dictionary[i[0]] += 1
#     return dictionary

# # print(countries_dict(countries))


# #Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# def get_first_ten_countries(countries):
#     return countries[:10]

# # print(get_first_ten_countries(countries))

# # Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# def get_last_ten_countries(countries):
#     return countries[-10:]

# # print(get_last_ten_countries(countries))


#Exercise 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.

from countries_data import countries
sorted_names = sorted(countries, key=lambda country: country['name'])
sorted_capital = sorted(countries, key=lambda country: country['capital'])
sorted_population = sorted(countries, key=lambda country: country['population'])

from collections import Counter

def most_spoken_languages(countries):
    all_languages = []
    for country in countries:
        all_languages.extend(country['languages']) #flatten all languages
    count = Counter(all_languages) #count each language
    top_10 = count.most_common(10) #get top 10 languages
    return top_10

# print(most_spoken_languages(countries))    

sorted_population_top_10 = sorted(countries, key=lambda country: country['population'], reverse=True)[:10] # can add [:10] at the end to get only top 10 countries

print(sorted_population_top_10)