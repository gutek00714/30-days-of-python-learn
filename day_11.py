#Exercise 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# def add_two_numbers(a, b):
#     return a + b

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

# def area_of_circle(r):
#     pi = 3.14
#     return pi * r * r

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

# def add_all_nums(*nums):
#     total = 0
#     for num in nums:
#         if not isinstance(num, int):    #isinstance(5, int) - check if the number 5 is an intiger
#             print("Item not a number")
#         total += num
#     return total

# # Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def convert_celsius_to_fahrenheit(celsius):
#     f = (celsius * 9/5) + 32
#     return f

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

# def check_season(month):
#     month = month.capitalize()
#     if month in {'December', 'January', 'February'}:
#         return 'Winter'
#     elif month in {'March', 'April', 'May'}:
#         return 'Spring'
#     elif month in {'June', 'July', 'August'}:
#         return 'Summer'
#     elif month in {'September', 'October', 'November'}:
#         return 'Autumn'
#     else:
#         return 'Invalid month'

#Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1, x2, y1, y2):
#     return (y2 - y1) / (x2 - x1)

# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(lst):
#     for i in lst:
#         print(i)

# #Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# lst = [1, 2, 3, 4, 5]
# def reverse_list(lst):
#     reversed_list = []
#     for i in lst:
#         reversed_list.insert(0, i)
#     return reversed_list

# print(reverse_list(lst))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# lst = ['apple', 'banana', 'kiwi']
# def capitalize_list_items(lst):
#     new_list = [word.capitalize() for word in lst]
#     return new_list
# print(capitalize_list_items(lst))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# lst = ['apple', 'banana', 'kiwi']
# item = 'pear'
# def add_item(lst, item):
#     lst.append(item)
#     return lst
# print(add_item(lst, item))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# item = 'Mango'
# def remove_item(food_staff, item):
#     food_staff.remove(item)
#     return food_staff
# print(remove_item(food_staff, item))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# x = 5
# def sum_of_numbers(x):
#     total = 0
#     for i in range(x + 1):
#         total += i
#     return total
# print(sum_of_numbers(x))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# x = 5
# def sum_of_odds(x):
#     total = 0
#     for i in range(x + 1):
#         if i % 2 != 0:
#             total += i
#         else:
#             continue
#     return total
# print(sum_of_odds(x))


#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# x = 5
# def sum_of_even(x):
#     total = 0
#     for i in range(x + 1):
#         if i % 2 == 0:
#             total += i
#         else:
#             continue
#     return total
# print(sum_of_even(x))



#Exercise 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# x = 100
# def evens_and_odds(x):
#     if x < 1:
#         print('This is not a positive integer')
#     total_even = 0
#     total_odd = 0
#     for i in range(x + 1):
#         if i % 2 == 0:
#             total_even += 1
#         else:
#             total_odd += 1
#     return total_even, total_odd 
# print(f'Total number of even: {evens_and_odds(x)}, total number of odds: {evens_and_odds(x)}')

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# x = 5
# def factorial(x):
#     total = 1
#     for i in range(1, x + 1): #it has to start from 1, because x0 always gives 0
#         total = total * i
#     return total
# print(factorial(x))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
# lst = []
# def is_empty(lst):
#     if len(lst) == 0:
#         return True
#     else:
#         return False

# print(is_empty(lst))


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range.
# lst = [5, 1, 2, 4, 3, 5, 1]
# def calculate_mean(lst):
#     mean = 0
#     for i in lst:
#         mean += i
#     mean = mean / len(lst)
#     return mean
# print(calculate_mean(lst))

# def calculate_median(lst):
#     lst.sort()
#     x = len(lst)
#     if x % 2 != 0:
#         median = lst[x // 2]
#     else:
#         median = (lst[x // 2 - 1] + lst[x // 2]) / 2
#     return median
# print(calculate_median(lst))

# def calculate_mode(lst):
#     max_number = 0
#     count = 0 
#     for i in lst:
#         count_current = 0
#         for j in lst:
#             if j == i:
#                 count_current += 1
#         if count_current > count:
#             count = count_current
#             max_number = i
#     return max_number
# print(calculate_mode(lst))

# def calculate_mode(lst):
#     dict_numbers_count = {}
#     for i in lst:
#         if i in dict_numbers_count:
#             dict_numbers_count[i] = dict_numbers_count[i] + 1
#         else:
#             dict_numbers_count[i] = 1
#     max_value = max(dict_numbers_count.values())
#     lst_max_number = []
#     for i in dict_numbers_count:
#         if max_value == dict_numbers_count[i]:
#             lst_max_number.append(i)
#     return lst_max_number
# print(calculate_mode(lst))
    
# def calculate_range(lst):
#     highest_number = max(lst)
#     lowest_number = min(lst)
#     range = highest_number - lowest_number
#     return range
# print(calculate_range(lst))


#Exercise 3
# Write a function called is_prime, which checks if a number is prime.
# number = int(input('Type a number: '))
# def is_prime(number):
#     if number <= 1:
#         print('Not a prime number')
#         return
#     for i in range(2, number):
#         if number % i == 0:
#             print('Not a prime number')
#             return
#     print('Prime number')
# is_prime(number)


# Write a functions which checks if all items are unique in the list.
# lst = [5, 1, 2, 4, 3]
# def all_unique(lst):
#     lst_numbers = []
#     for i in (lst):
#         if i in lst_numbers:
#             return False
#         lst_numbers.append(i)
#     return True
# print(all_unique(lst))                         #my first thought by list comparison

# lst = [5, 1, 2, 4, 3]
# def all_unique(lst):
#     if len(lst) != len(set(lst)):
#         return False
#     return True
# print(all_unique(lst))                           #second option by changing list into a set which removes duplicates


#Write a function which checks if all the items of the list are of the same data type.
# lst = [5, 1, 'banana']
# def same__data_type(lst):
#     first = type(lst[0])
#     for i in lst:
#         if type(i) != first:
#             return False
#     return True
# print(same__data_type(lst))


#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from countries_data import countries
# def most_spoken_languages(countries):
#     all_languages = []

#     for i in countries:
#         all_languages.extend(i['languages'])

#     language_count = {}
#     for language in all_languages:
#         if language in language_count:
#             language_count[language] += 1
#         else:
#             language_count[language] = 1

#     sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)  #x represents each element being sorted. x[1] is the second item in the touple. 

#     sorted_languages = sorted_languages[:10]  #get 10 most spoken languages

#     result = []

#     for language in sorted_languages:
#         result.append(language[0])

#     return result
# print(most_spoken_languages(countries))


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries):
    population = []

    for i in countries:
        population.append((i['name'], i['population'])) #double bracket because this is a tuple - which is in brackets. And the outer brackets are from the population.append()

    sorted_population = sorted(population, key=lambda item: item[1], reverse=True)

    sorted_population = sorted_population[:10]

    result = []

    for i in sorted_population:
        result.append(i[0])
    
    return result
print(most_populated_countries(countries))