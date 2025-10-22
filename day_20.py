#Exercise 1
# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt' #the link was dead so I found another one.
# import requests
# from collections import Counter
# import re
# url = 'https://www.gutenberg.org/cache/epub/47960/pg47960.txt'

# response = requests.get(url)
# text = response.text
# text = text.replace('\r', ''.replace('\n', ''))
# words = re.findall(r'\b[A-Za-z]+\b', text.lower())
# words_count = Counter(words)
# print(words_count.most_common(10))



# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
import statistics

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()

weights = [cat['weight']['metric'] for cat in cats]
cat_weight_list = []
for i in weights:
    string = i.split()
    a = int(string[0])
    b = int(string[2])
    average = (a + b) / 2
    cat_weight_list.append(average)

# print(min(cat_weight_list))
# print(max(cat_weight_list))
# print(statistics.mean(cat_weight_list))
# print(statistics.median(cat_weight_list))
# print(statistics.stdev(cat_weight_list))

lifespan = [cat['life_span'] for cat in cats]
lifespan_list = []
for i in lifespan:
    string = i.split()
    a = int(string[0])
    b = int(string[2])
    average = (a + b) / 2
    lifespan_list.append(average)

# print(min(lifespan_list))
# print(max(lifespan_list))
# print(statistics.mean(lifespan_list))
# print(statistics.median(lifespan_list))
# print(statistics.stdev(lifespan_list))

from collections import defaultdict

country_breed_list = defaultdict(list)

for i in cats:
    country = i.get('origin', 'Unknown')
    breed = i.get('name', 'Unknown')
    country_breed_list[country].append(breed)

print(country_breed_list)