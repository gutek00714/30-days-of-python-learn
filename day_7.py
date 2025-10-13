# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard

print(len(it_companies)) #7

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Ebay', 'Allegro', 'Samsung'])
print(it_companies)

it_companies.remove('Allegro')
print(it_companies)

#Remove metod will raise errors if selected item is not found. Discard doesn't raise any errors.

#Exercise 2
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely

joined = A.union(B)
print(joined)

print(A.intersection(B)) #{19, 20, 22, 24, 25, 26}

print(A.issubset(B)) #True

print(A.isdisjoint(B)) #False - they have common items

print(A.union(B)) 
print(B.union(A))

print(A.symmetric_difference(B)) #{27, 28} different items in both sets

del A
del B



#Exercise 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


age_set = set(age)
print(len(age)) #8
print(len(age_set)) #5

#string = text value, list = a list of things that can be edited, tuple = list of sorted things that can't be edited, set = a set of different and unsorted things (unique items)

sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_split = sentence.split()
sentence_set = set(sentence_split)
print(len(sentence_set))