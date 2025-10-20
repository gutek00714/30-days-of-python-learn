# Exercise 1
import re
# # What is the most frequent word in the following paragraph?
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# words = re.findall(r'\b\w+\b', paragraph, re.I)

# unique_words = set(words) #set has no duplicates

# paragraph_list = []
# for word in unique_words:
#     count = len(re.findall(fr'\b{word}\b', paragraph, re.I))
#     paragraph_list.append((count, word))

# paragraph_list.sort(reverse=True)
# # print(paragraph_list)



# # The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# # Extract these numbers from this whole text and find the distance between the two furthest particles.
# txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
# points = re.findall(r'-?\d+', txt, re.I)
# # print(points)
# points = list(map(int, points))
# sorted_points = sorted(points)  #better to sort them even though the numbers are already in order in the sentence
# # print(sorted_points)
# distance = sorted_points[-1] - sorted_points[0]
# print(distance)


#Exercise 2
# # Write a pattern which identifies if a string is a valid python variable
# # ^[A-Za-z_]\w*$     #^ - start of the string, [] - can contain all letters and underscore, \w* - zero or more word characters (letters, digits, underscores), $ - end of string
# def is_valid_variable(txt):
#     check = r'^[A-Za-z_]\w*$'
#     return bool(re.match(check, txt))

# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True



#Exercise 3
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

txt = re.sub(r'[%@&$#;]', '', sentence)
print(txt)

words = re.findall(r'\b\w+\b', txt, re.I)  #w without + will find only 1 letter words (I and a)
sorted_words = set(words)
txt_list = []

for word in sorted_words:
    count = len(re.findall(fr'\b{word}\b', txt, re.I))
    txt_list.append((count, word))

txt_list.sort(reverse=True)
print(txt_list[:3])