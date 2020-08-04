# ###### import datetime ######

# =================================
# While working with datetime the terms naive datetime and aware datetime are very common
# Naive datetimes --> They don't have enough info to determine things like timezone or daylight savings times but they are easier to work with if you don't want high level of details
# Aware datetimes --> If you need that high level of details then these have enough info to determine timezone or keeptrack of daylight savings times
# =================================
# ### Naive datetimes ###

# =================================
# ### datetime.date() ###

d = datetime.date(2019, 7, 24)
# The format is (%Y, %m, %d)
# Do not include leading 0's, if you did that then you will get Syntax Error
print(d)
# =================================
# ### datetime.date.today() ###

tday = datetime.date.today()

print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())       # Monday 0 Sunday 6
print(tday.isoweekday())    # Monday 1 Sunday 7
# =================================
# ### datetime.timedelta() ###

# Python timedelta object is used to perform datetime manipulations in an easy way. The timedelta class is part of datetime module
# timedelta are simply difference between two dates and times

# ----------------------------------
tdelta = datetime.timedelta(days = 7)
# This timedelta is of 7 days (our duration is is of 7 days)
# ----------------------------------
# To get what will be date after 7 days
print(tday + tdelta)

# To get what was the date before 7 days
print(tday - tdelta)
# ----------------------------------
# If we subtract/add a date from a date we will get timedelta
# For understanding:
# date2 = date1 + timedelta
# timedelta = date1 + date2
# ----------------------------------
# For example: To check how many days are remaing for birthday(12/04/2020), bday --> birthday

bday = datetime.date(2020, 4, 12)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds()) # total_seconds() is a method
# =================================
# ### datetime.time() ####

# With datetime.time() we will be working with hrs, mins, sec, micro sec
# By default it is naive

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
# =================================
# ### datetime.datetime() ####

dt = datetime.datetime(2019, 8, 24, 9, 30, 45, 100000)

# ----------------------------------
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
# ----------------------------------
# We can also work with timedelta

tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)
# ----------------------------------
# ### datetime.datetime.today() ###

dt_today = datetime.datetime.today() 
print(dt_today)
# This returns current local datetime with a timezone of NONE
# ----------------------------------
# ### datetime.datetime.now() ###

dt_now = datetime.datetime.now()         
print(dt_now)
# Gives an option to pass in a timezone, if you leave timezone empty the it is then same as .today()
# ----------------------------------
# ### datetime.datetime.utcnow() ###

dt_utcnow = datetime.datetime.utcnow()  
print(dt_utcnow)
# It's not a timezone aware datetime, this gives us the current UTC time but timezone info is still set to NONE
# =================================
# ### pytz ###

# pytz is a third party package. Install it using pip
# ---------------------------------
# Importing pytz package
import pytz
# ---------------------------------
# Always work with UTC while working with timezone
# ---------------------------------
dt = datetime.datetime(2019, 8, 24, 11, 17, 13, tzinfo=pytz.UTC)
print(dt) 
# To make it timezone aware we have added --> tzinfo=pytz.UTC
# +00:00 this is UTC offset
# --------------------------------- 
# To get current UTC time that is timezone aware there are two methods:
#   1. .now()
#   2. .utcnow()

# 1. .now()
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# 2. .utcnow()
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# datetime.datetime.now() is more prefered due to less typing
# ---------------------------------
# This loop can be used to get all timezones

for tz in pytz.all_timezones:
    print(tz)
# =================================
# ### Covert UTC timezone to certain timezone ###

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_my_place = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
# Here we have passed 'Asia/Kolkata', the timezone that we want
print(dt_my_place)
# =================================
# ### Make naive datetime timezone aware ###
# =================================
# ### To convert local time to another timezone (timezone aware) ###

# ---------------------------------
dt_my_place = datetime.datetime.now() # not timezone aware
print(dt_my_place)

dt_singapore = dt_my_place.astimezone(pytz.timezone('Asia/Singapore'))
# If it is run then it will give an error since astimezone() cannot be applied to a naive datetime
# ---------------------------------
# This is a navie datetime

dt_my_place = datetime.datetime.now()
my_place_tz = pytz.timezone('Asia/Kolkata')

# Running a localize method to make "dt_my_place" timezone aware
dt_my_place = my_place_tz.localize(dt_my_place)
# Here we have passed(dt_my_place) the datetime that we want to loacailze

print(dt_my_place) # now this datetime is timezone aware

# Now we can run this line since we have made "dt_my_place" timezone aware
dt_singapore = dt_my_place.astimezone(pytz.timezone('Asia/Singapore'))
print(dt_singapore)
# =================================
# ### Different formats to display datetime ###

# These formats are avialable in Python Documentation

dt_my_secret_place = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))

# ---------------------------------
# 1. isoformat()

print(dt_my_secret_place.isoformat()) 
# It is international standard format
# ---------------------------------
# 2. strftime() 

print(dt_my_secret_place.strftime('%B %d %Y'))  
# Here datetime is converted into string
# ---------------------------------
# 3. strptime()

# Sometimes you have string and you want to convert it to datetime, for that we use strptime() method
dt_str = 'August 24 2019'

dt = datetime.datetime.strptime(dt_str, '%B %d %Y')
# The first argument is what we want to convert
# The second argument is the format that the string is in
print(dt)
# ---------------------------------
# strftime : Datetime to String
# strptime : String to Datetime
