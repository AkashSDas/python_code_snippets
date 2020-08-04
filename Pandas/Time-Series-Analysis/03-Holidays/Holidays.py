# ###### Holidays ######

# Since there are some holidays related to calender which cannot be handeled by date_range(), for this we need other holiday calender
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('apple_stocks.csv')
print(df)
# =================================
# ### Holiday Calander ###

# ---------------------------------
# Creating a date range having Business as frequency

rng = pd.date_range(start='7/1/2017', end='7/21/2017', freq='B')
print(rng)

# It includes 7/4/2019 (American Independece Day)
# ---------------------------------
# Since on 4th of July there is American Independece so we have exclude that date since stock was not trading on that date
# ---------------------------------
# Importing required modules for Holiday calander

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
# ---------------------------------
usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())
print(usb)

rng = pd.date_range(start='7/1/2017', end='7/21/2017', freq=usb)
# Here it excludes 7/4/2019
print(rng)

df.set_index(rng, inplace=True)
print(df)
# =================================
# ### To define our own custom Holiday Calendar ###

from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday

# ---------------------------------
class myBirthdayCalendar(AbstractHolidayCalendar):
  rules = [
    Holiday('My Birthday', month=4, day=12)
  ]

# Creating instance of Birthday Calendar and supplying it as an argument
myc = CustomBusinessDay(calendar=myBirthdayCalendar())
print(myc)

rng = pd.date_range(start='4/1/2017', end='4/21/2017', freq=myc)
print(rng)
# ---------------------------------
# If holiday comes on weekend that it is observed on nearest workday 
# If Holiday on Sat then Fri will be Holiday
# If Holiday on Sun then Mon will be Holiday
# ---------------------------------
class myBirthdayCalendar(AbstractHolidayCalendar):
  rules = [
    Holiday('My Birthday', month=4, day=15, observance=nearest_workday)
  ]
  
# On day 15 it is Sat therefore on 14 that is Fri there should be an holiday and for that we have to pass obeservance=nearest_workday

myc = CustomBusinessDay(calendar=myBirthdayCalendar())
print(myc)

rng = pd.date_range(start='4/1/2017', end='4/21/2017', freq=myc)
print(rng)
# ---------------------------------
# There are other values for obseravnce
# ---------------------------------
# In Egypt there are holidays on Friday and Saturday
# Our CustomBusinessDay has an argument weekmasks='Mon Tue Wed Thu Fri' 
# To handel difference in holidays of Egypt we have to change the weekmask arguments
# ---------------------------------
b = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')

rng = pd.date_range(start='4/1/2017', end='4/21/2017', freq=b)
print(rng)
# ---------------------------------
c = CustomBusinessDay(weekmask='Sun Mon')

rng = pd.date_range(start='4/1/2017', end='4/21/2017', freq=c)
print(rng)
# ---------------------------------
# When there are holidays on custom days it can provided by argument holidays inside CustomBusinessDay and the format should be ---> 2017-07-04

d = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu', holidays=['2017-07-04'])

rng = pd.date_range(start='4/1/2017', end='4/21/2017', freq=d)
print(rng)
