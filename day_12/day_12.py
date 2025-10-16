# from mymodule import generate_full_name
# print(generate_full_name('Asabeneh', 'Yetayeh'))

#Exercise 1
# Write a function which generates a six digit/character random_user_id. 

# import random
# import string
# def random_user_id():
#     characters = string.ascii_letters + string.digits
#     user_id = ''
#     for i in range(6):
#         user_id += random.choice(characters)
#     return user_id
# print(random_user_id())



# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# import random
# import string
# def user_id_gen_by_user():
#     try:
#         number_of_characters = int(input('Enter the number of characters: '))
#         number_of_id = int(input('Enter the number of id: '))
#         characters = string.ascii_letters + string.digits
#         user_id = ''
#         lst_user_id = []
#         for j in range(number_of_id):
#             for i in range(number_of_characters):
#                 user_id += random.choice(characters)
#             lst_user_id.append(user_id)
#             user_id = ''
#         return lst_user_id
#     except:
#         print('Not an int')
    
# print(user_id_gen_by_user())


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

# import random
# def rgb_color_gen():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return f'rgb({r}, {g}, {b})'
# print(rgb_color_gen())


#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #.
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

# import random
# import string
# def list_of_hexa_colors():
#     try:
#         number_of_hexa = int(input('Enter the number of hexa: '))
#         lst_hexa_colors = []
#         hexa_color = '#'
#         characters = string.ascii_lowercase[:6] + string.digits
#         for j in range(number_of_hexa):
#             for i in range(6):
#                 hexa_color += random.choice(characters)
#             lst_hexa_colors.append(hexa_color)
#             hexa_color = '#'
#         return lst_hexa_colors
#     except:
#         print('Not an int')
# # print(list_of_hexa_colors())


# # Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# # import random
# def list_of_rgb_colors():
#     try:
#         number_of_colors = int(input('Enter the number of colors: '))
#         lst_rgb_colors = []
#         rgb_color = 'rgb('
#         for i in range(number_of_colors):
#             r = random.randint(0, 255)
#             g = random.randint(0, 255)
#             b = random.randint(0, 255)
#             rgb_color = f'rgb({r}, {g}, {b})'
#             lst_rgb_colors.append(rgb_color)
#         return lst_rgb_colors
#     except:
#         print('Not an int')
# # print(list_of_rgb_colors())


# # Write a function generate_colors which can generate any number of hexa or rgb colors.
# def generate_colors():
#     hexa_or_rgb = input('Do you want hexa or rgb? ')
#     if hexa_or_rgb == 'hexa':
#         return list_of_hexa_colors()
#     elif hexa_or_rgb == 'rgb':
#         return list_of_rgb_colors()
#     else:
#         return 'Wrong input'
# print(generate_colors())



#Exercise 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# import random

# lst = [1, 2, 3, 4, 5]
# def shuffle_list(lst):
#     lst_shuffle = lst
#     random.shuffle(lst_shuffle)
#     return lst_shuffle
# print(shuffle_list(lst))


#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def random_numbers_array():
    lst_random = []
    while len(lst_random) < 7:
        x = random.randint(0, 9)
        if x not in lst_random:
            lst_random.append(x)
    return lst_random
print(random_numbers_array())