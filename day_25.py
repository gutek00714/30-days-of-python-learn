import pandas as pd

#Exercise 1
# Read the hacker_news.csv file from data directory
df = pd.read_csv('./data/hacker_news.csv')
# print(df)

# Get the first five rows
# print(df.head())

# Get the last five rows
# print(df.tail())

#Get the title column as pandas series
title = df['title']
# print(title)

#Count the number of rows and columns 
# print(len(title)) #number of rows - 20099
# print(len(df.columns)) #number of columns - 7


# Filter the titles which contain python
filtered_titles = title[title.str.contains('python', case=False, na=False)]   #na=False - ignores NaN(missing) values     case=False - ignore capitalization
# print(filtered_titles)


# Filter the titles which contain JavaScript
filtered_titles_javasctipt = title[title.str.contains('JavaScript', case=False, na=False)]
# print(filtered_titles_javasctipt)