from datetime import datetime
# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
# print(day, month, year, hour, minute, timestamp)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
date_format = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(date_format)

#Today is 5 December, 2019. Change this time string to time.
date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)

#Calculate the time difference between now and new year.
new_year = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0) #date doesn't accept hours, minutes and seconds - thats why datetime
time_left = new_year - now
# print(time_left)

# Calculate the time difference between 1 January 1970 and now.
past_date_string = '1 January 1970'
past_data_object = datetime.strptime(past_date_string, '%d %B %Y')
time_diffrence = now - past_data_object
# print(time_diffrence)