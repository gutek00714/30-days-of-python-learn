# #Exercise 1
# # Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
# # with open('./data/obama_speech.txt', 'r') as f:
# #     txt = f.read()
# #     lines = txt.splitlines()
# #     print(len(lines)) #66

# #     words = txt.split()
# #     print(len(words)) #2400                                   #works only with 1 txt file

# def count_lines_and_words(file_uri):
#     with open(file_uri, 'r') as f:
#         txt = f.read()
#         lines = txt.splitlines()
#         print(len(lines)) 

#         words = txt.split()
#         print(len(words)) 

# # count_lines_and_words('./data/obama_speech.txt') #a 66 2400
# # count_lines_and_words('./data/michelle_obama_speech.txt') #b 83 2204
# # count_lines_and_words('./data/donald_speech.txt') #c 48 1259
# # count_lines_and_words('./data/melina_trump_speech.txt') #d 33 1375

# #Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# import json
# from collections import Counter

# def most_spoken_languages(filename, n):
#     with open(filename, 'r', encoding='utf-8') as f:
#         countries_dct = json.load(f)
#     languages_list = []
#     for i in countries_dct:
#         languages_list.extend(i['languages'])
    
#     count = Counter(languages_list)

#     most_common = sorted([(count, language) for language, count in count.items()], key=lambda x:x[0], reverse=True)
#     return most_common[:n]

# # print(most_spoken_languages('./data/countries_data.json', 10))

# # Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# def most_populated_countries(filename, n):
#     with open(filename, 'r', encoding='utf-8') as f:
#         countries_dct = json.load(f)
#     countries_list = []

#     for i in countries_dct:
#         countries_list.append({'country': i['name'], 'population': i['population']})

#     sorted_countries_list = sorted(countries_list, key=lambda x: x['population'], reverse=True)
#     return sorted_countries_list[:10]

# # print(most_populated_countries('./data/countries_data.json', 10))


#Exercise 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
email_list = []
with open('./data/email_exchanges_big.txt', 'r', encoding='utf-8') as f:
    for i in f:
        if i.startswith('From:'):
            email = re.findall(r'[\w.+-]+@[\w-]+\.+[\w.-]+', i)
            if email:
                email_list.extend(email)

# print(email_list[:10])

#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
from collections import Counter

def find_most_common_words(file_uri, n):
    with open(file_uri, 'r', encoding='utf-8') as f:
        all_words = []
        txt = f.read()
        words = txt.split()

        count = Counter(words)

        most_common = sorted([(count, words) for words, count in count.items()], key=lambda x : x[0], reverse=True)
        return most_common[:n]

# print(find_most_common_words('./data/donald_speech.txt', 10))

#Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech

# print(find_most_common_words('./data/obama_speech.txt', 10)) #a
# print(find_most_common_words('./data/michelle_obama_speech.txt', 10)) #b
# print(find_most_common_words('./data/donald_speech.txt', 10)) #c
# print(find_most_common_words('./data/melina_trump_speech.txt', 10)) #d

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
import string
from data.stop_words import stop_words
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def remove_support_words(text, stop_words):
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return " ".join(filtered)

def check_text_similarity(txt1, txt2):
    with open(txt1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(txt2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    text1 = remove_support_words(text1, stop_words)
    text2 = remove_support_words(text2, stop_words)

    text1 = text1.split()
    text2 = text2.split()

    counter1 = Counter(text1)
    counter2 = Counter(text2)

    similarity = counter1 & counter2
    similarity_list = list(similarity.elements())

    all_text = len(text1) + len(text2) - len(similarity_list)

    percentage = 100 * len(similarity_list)/all_text
    return f'{percentage}%'

# print(check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt'))


#Find the 10 most repeated words in the romeo_and_juliet.txt
# print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

#Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import csv
python_count = 0
javascript_count = 0
java_count = 0

with open('./data/hacker_news.csv') as f:
    # csvreader = csv.reader(f)
    for row in f.readlines():
        row = row.lower()
        if 'python' in row:
            python_count += 1
        if 'javascript' in row:
            javascript_count += 1
            row = row.replace('javascript', '')
        if 'java' in row and 'javascript' not in row:
            java_count += 1

print(python_count)
print(javascript_count)
print(java_count)