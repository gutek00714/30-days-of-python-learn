#Exercise 1
# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/')

import requests
from bs4 import BeautifulSoup
import json

# url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# response = requests.get(url)
# status = response.status_code
# # print(status) # 200

# content = response.content
# soup = BeautifulSoup(content, 'html.parser')

# data = {}

# for section in soup.find_all(['h2', 'h3', 'h4']):
#     headline = section.get_text(strip=True) #quick facts & stats, community, campus, academics

#     list_after_headline = section.find_next_sibling(['ul']) # find ul list right after the headline

#     if list_after_headline:
#         facts = []

#         for i in list_after_headline.find_all('li'): #loop through all the li items
#             text = i.get_text(strip=True)
#             facts.append(text)
        
#         data[headline] = facts #add everything to data dictionary


# with open('bu_site.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)      #this sctipt gets only the lists from the site - community and academics.



# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# url = 'https://archive.ics.uci.edu/datasets'
# response = requests.get(url)
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')

# data = [
#     # 'links' : [a['href'] for a in soup.find_all('a', href=True)],
#     # 'headings': [h.get_text(strip=True) for h in soup.find_all('h2')],
#     # 'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')]  # this metod doesn't work because it shows all the links, than all the headings and all paragraphs. It's chaos. 
# ]

# for h2 in soup.find_all('h2'):
#     a = h2.find('a', href=True)
#     if not a:
#         continue

#     heading = a.get_text(strip=True)
#     link = a['href']

#     p = h2.find_next_sibling('p')
#     paragraph = p.get_text(strip=True)

#     data.append({
#         'link': link,
#         'heading': heading,
#         'paragraph': paragraph
#     })

# with open('datasets.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)



# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})   # the page was blocking the request. headers={'User-Agent': 'Mozilla/5.0'} helped
content = response.content
soup = BeautifulSoup(content, 'html.parser')

data = []

table = soup.find('table', class_='wikitable')


for row in table.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    if row_data:
        data.append(row_data)

with open('presidents.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)