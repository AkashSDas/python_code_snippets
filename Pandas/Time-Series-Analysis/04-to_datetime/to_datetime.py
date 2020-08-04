# ###### to_datetime ######

# Most common problem in data analysis is the lack of unformity in structure of input data this is since dates can be written in many string formats
# =================================
# Importing pandas module
import pandas as pd
# =================================
# To handel dates we use the to_datetime method

dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dates))
# =================================
# To handel different time formats also we use the to_datetime method

dates = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dates))
# =================================
# ### dayfirst ###

# ---------------------------------
# Date Formats:
# US --> mm/dd/yyyy
# Europe --> dd/mm/yyyy
# ---------------------------------
# So if we have something like

print(pd.to_datetime("5/1/2017"))

# It will go by US format i.e. mm/dd/yyyy
# ---------------------------------
# To handel Europe dates set the dayfirst parameter to True

print(pd.to_datetime("5/1/2017", dayfirst=True))
# =================================
# ### format ###

# We can use our custom format also by giving format argument

print(pd.to_datetime("5$1$2017", format='%d$%m$%Y'))
print(pd.to_datetime("5#1#2017", format='%d#%m#%Y'))
# =================================
# ### errors ###

# When we pass in a garbage string(an invalid date) we will get an error, the reason is that in to_datetime documentation errors are said to be raised since invaid string will cause exception. 
# ---------------------------------
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105', 'abc']

# To ignore invalid string pass errors='ignore' argument
print(pd.to_datetime(dates, errors='ignore'))
# Here since we have one invalid date i.e. 'abc' and we have passed errors='ignore' which will ignore all datetime and not perform datetime conversion for any of the date

# To ingnore just the invalid string and perform datetime conversion for others pass errors='coerce' argument
print(pd.to_datetime(dates, errors='coerce'))
# Here the invalid string will be converted to NaT(Not a Timestamp)
# =================================
# ### What if we input a datetime that is coming in Epoch(unix time) ###

# Epoch(unix time) is number of seconds that have passed since Jan 1, 1970 00:00:00 UTC
# ---------------------------------
t = 1501356749
print(pd.to_datetime(t, unit='s'))

# unit parameter is the unit of our time i.e. s(second), ns(nano second), etc
# unit='ns' by default unit is ns(nano second)
# But the t supplied is seconds(s) from Jan 1970
# ---------------------------------
# We can also convert the samething as datetime index by passing an array 

dt = pd.to_datetime([t], unit='s')
print(dt)
# ---------------------------------
# ### view ###

# To covert it back to Epoch use the view method

print(dt.view('int64'))

# It converts it by datetime index into integer 64
# It returns extra datetime, those are nano seconds
