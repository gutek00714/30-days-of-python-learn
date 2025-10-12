# Exercise 1
#1 Declare an empty list
# lst = list()



#(2, 3, 4 together)
#2 Declare a list with more than 5 items
#3 Find the length of your list
#4 Get the first item, the middle item and the last item of the list
# lst = [1, 2, 'banana', 3, 6, 'car']

# print(len(lst))

# first = lst[0]
# middle = lst[2]
# last = lst[-1]
# print(first, middle, last)



#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_types = ['kaziu', 27, 170, 'single', 'poznan']



#(6 - 26 together)
#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#7 Print the list using print()
#8 Print the number of companies in the list
#9 Print the first, middle and last company
#10 Print the list after modifying one of the companies
#11 Add an IT company to it_companies
#12 Insert an IT company in the middle of the companies list
#13 Change one of the it_companies names to uppercase (IBM excluded!)
#14 Join the it_companies with a string '#;  '
#15 Check if a certain company exists in the it_companies list.
#16 Sort the list using sort() method
#17 Reverse the list in descending order using reverse() method\
#18 Slice out the first 3 companies from the list
#19 Slice out the last 3 companies from the list
#20 Slice out the last 3 companies from the list
#21 Slice out the middle IT company or companies from the list
#22 Remove the first IT company from the list
#23 Remove the middle IT company or companies from the list
#24 Remove the last IT company from the list
#25 Remove all IT companies from the list
#26 Destroy the IT companies list
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# print(it_companies)

# print(len(it_companies))

# first = it_companies[0]
# middle = it_companies[3]
# last = it_companies[-1]
# print(first, middle, last)

# it_companies[0] = 'Samsung'
# print(it_companies)

# it_companies.append('Ebay')

# it_companies.insert(2, 'Xiaomi')

# it_companies[1] = it_companies[1].upper()

# x = '#;  '.join(it_companies)
# print(x)

# print(it_companies.index('Apple'))

# it_companies.sort()
# print(it_companies)

# it_companies.sort(reverse=True)
# print(it_companies)

# first3 = it_companies[0:3]
# print(first3)

# last3 = it_companies[-3:]
# print(last3)

# middle3 = it_companies[2:5]
# print(middle3)

# it_companies.pop(0)
# print(it_companies)

# it_companies.remove('Apple')
# print(it_companies)

# it_companies.pop()
# print(it_companies)

# it_companies.clear()
# print(it_companies)

# del it_companies



#(27, 28 together)
#27 Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
#28 After joining the lists in question 27. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# full = front_end + back_end
# print(full)

# full_stack = full.copy()
# full_stack.insert(5, 'Python')
# print(full_stack)

# full_stack.insert(6, 'SQL')
# print(full_stack)



#Exercise 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()

# print(min(ages))
# print(max(ages))

# min_age = min(ages)
# max_age = max(ages)
# ages.append(min_age)
# ages.append(max_age)
# print(ages)

# ages.sort()
# print(len(ages))
# middle1 = ages[5]
# middle2 = ages[6]
# median = (middle1 + middle2) / 2
# print(median)

# average_age = sum(ages) / 12
# print(average_age)

# range = max(ages) - min(ages)
# print(range)

# abs_min = abs(min_age - average_age)
# abs_max = abs(max_age - average_age)
# print(abs_min, abs_max)



# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(len(countries)) #193
middle = (len(countries) - 1) // 2 #96
mid_countries = countries[middle]
print(mid_countries)

a_list = countries[:97]
print(len(a_list))

a = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_a, second_a, third_a, *scandic = a
print(first_a)
print(scandic)