#Exercise 1
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero_numbers = [i for i in numbers if i < 0 or i == 0]
# print(negative_and_zero_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row in list_of_lists for sub_row in row for number in sub_row]   #yellow [] = list, pink [] = row, blue [] = sub_row
#print(flattened_list)

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuple = [(number, 1, number**1, number**2, number**3, number**4, number**5) for number in range(11)]
# print(list_of_tuple)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [[country.upper(), country[:3].upper(), capital.upper()] for row in countries for (country, capital) in row]
# print(flatten_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country, 'city': city} for row in countries for (country, city) in row]
# print(dict_countries)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_names = [(name + ' ' + last_name) for row in names for (name, last_name) in row]
# print(lst_names)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2 : (y2 - y1) / (x2 - x1)
print(slope(-3, 2, 8, -11))