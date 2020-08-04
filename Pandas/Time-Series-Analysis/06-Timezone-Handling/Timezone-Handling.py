# ###### Timezone Handling ######

# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('msft.csv', header=1, index_col='Date Time', parse_dates=True)
print(df)
# =================================
# Two Types of DateTime Objects in Python
#   1. Naive(No timezone awareness)
#   2. Time zone aware datetime
# =================================
# ### Converting navie datetimeindex to timezone aware datetimeindex ###

print(df.index)
# This datetimeindex in naive

# We can convert naive datetimeindex into timezone aware datetimeindex
df = df.tz_localize(tz='US/Eastern')
print(df.index)

# Converting to Berlin timezone
df = df.tz_convert(tz='Europe/Berlin')
print(df.index)
# =================================
from pytz import all_timezones

print(all_timezones)

df = df.tz_convert(tz='Asia/Kolkata')
print(df.index)

# This will also have same effect
df.index = df.index.tz_convert(tz='Asia/Kolkata')
print(df.index)

rng = pd.date_range(start='1/1/2019', periods=10, freq='H')
print(rng)
# This will give naive time zone index

rng = pd.date_range(start='1/1/2019', periods=10, freq='H', tz='Asia/Kolkata')
print(rng)
# This will give time zone aware index since we have passed the tz parameter
# ================================
# date_range will accepts two type of timezones 
#   1. pytz timezone
#   2. dateutil
# =================================
# ### dateutil ###

rng = pd.date_range(start='1/1/2019', periods=10, freq='H', tz='dateutil/Asia/Kolkata')
print(rng)
# =================================
# Difference between pytz and dateutil:
#   1. pytz has all pre definied time zones
#   2. dateutil will use all the time zones available in operating system
# =================================
# ### Arithmetic Between Two Time Zones ###

rng = pd.date_range(start='2019-01-01 00:00:00', periods=10, freq='30min')

s = pd.Series(range(10), index=rng)
print(s)

# Berlin Time Zone
b = s.tz_localize(tz='Europe/Berlin')
print(b)

# Mumbai Time Zone
m = s.tz_localize(tz='Asia/Kolkata')
print(m)

# Adding Mumbai's and Berlin's timezones
print(b+m)

# At all places it will give NaN, only the place where the two timezones will align it will give its result of addition nad it will internally convert it into UTC
