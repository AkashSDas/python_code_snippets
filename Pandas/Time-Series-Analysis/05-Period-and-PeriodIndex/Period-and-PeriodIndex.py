# ###### Period and PeriodIndex ######

# =================================
# Importing modules
import pandas as pd
import numpy as np
# =================================
# ### Yearly Time Period ###

y = pd.Period('2019')
# It will create an object
print(y)

# A-DEC --> Period is Annual and is ending at DECEMBER

print(y.start_time)
print(y.end_time)
# =================================
# ### Monthly Time Period ###

m = pd.Period('2019-1', freq='M')
print(m)
print(m.start_time)
print(m.end_time)
# =================================
# ### We can perform Arithmetic Operation with Period Objects ###

m = pd.Period('2019-1', freq='M')
print(m+1)

# If it was at the end of the year it will take you to the year
m = pd.Period('2019-12', freq='M')
print(m+1)

# It is fully aware of the calendar
# =================================
# ### Daily Time Period ###

d = pd.Period('2019-02-28')
print(d)
# It will automatically derive the day frequency but you also explicitly add freq='D'

# If it was a leap year then will automatically take us to from yyyy-02-28 to yyyy-02-29 if add 1 to d
d = pd.Period('2016-02-28', freq='D')
print(d)
print(d+1)
# =================================
# ### Hourly Frequency ###

h = pd.Period('2016-02-28 23:00:00', freq='H')
print(h)
print(h.start_time)
print(h.end_time)
print(h+1)
print(h-5)

# We can acheive the same result by Pandas offsets
print(h + pd.offsets.Hour(1))
print(h + pd.offsets.Hour(5))
print(h + pd.offsets.Hour(-5))
# =================================
# ### Quterly Time Period ###

# ---------------------------------
# In Financial Time Series Analysis people often use Quterly Time Period because companies report their financals based on quaterly
# 1Q means 3 months
# It starts from Jan-March and so on 
# ---------------------------------
q = pd.Period('2019Q1')
print(q)

# 'Q-DEC' --> Quater ending in Dec

# Performing operation
print(q+1)
# ---------------------------------
# There are companies whose fiscal year doesn't aligns with the calendar one like Walmart
# Most of the companies are from Jan-Dec but for Walmart it is from Feb-Jan
# For this 

q = pd.Period('2019Q1', freq='Q-JAN')

# Q-JAN - it means that my fiscal year end at JAN

# It can be verified by this
print(q.start_time)
# ---------------------------------
# We can also use asfreq to convert this frequency to some other frequency
q = pd.Period('2019Q1')

# Converting this quaterly frequency to monthly freuency
print(q.asfreq('M', how="start"))
print(q.asfreq('M', how="end"))

# how parameter specifies how we want to do it
print(q.asfreq('D', how="start"))
print(q.asfreq('D', how="end"))
# ---------------------------------
# Performing operations

q = pd.Period('2019Q1', freq='Q-JAN')
q2 = pd.Period('2019Q2', freq='Q-JAN')

print(q2)
print(q2-q)

# It returns months between the quater, here it is 1
q3 = pd.Period('2020Q2', freq='Q-JAN')
print(q3-q)
# 5 months

# We cannot perform arithmetic such as quaterly and hourly it doesn't makes sence
# =================================
# ### period_range ###

idx = pd.period_range('2011', '2019', freq='Q-JAN')
print(idx)

print(idx[0])
# It is '2011Q4'

print(idx[0].start_time)
print(idx[0].end_time)
# Since it's end time is on 2011-01-31 23:59:59.999999999 therefore it is Q4

# If we don't want to give end date we can just give period
idx = pd.period_range('2011', periods=10, freq='Q-JAN')
print(idx)
# =================================
# ### to_timestamp and to_period ###

# Creating a Series
ps = pd.Series(np.random.randn(len(idx)), idx)
print(ps)
print(ps.index)

# PeriodIndex is great to retrive information for certain range
print(ps['2011'])

# To quater between a range
print(ps['2011':'2014'])

# To convert Period Index into Datetime Index
pst = ps.to_timestamp()
print(pst)
print(pst.index)

# To convert Datetime Index into Period Index
pst = pst.to_period()
print(pst)
print(pst.index)
# =================================
# ### PeriodIndex ###

df = pd.read_csv('wmt.csv')
print(df)

df.set_index('Line Item', inplace=True)
print(df)

# To transpose the table use the T attribute
df = df.T
print(df)

print(df.index)
# Here the index is of type object which is string type

# To convert this index into a period index
df.index = pd.PeriodIndex(df.index, freq='Q-JAN')
print(df.index)

# To perform some operation overall the PeriodIndex we use map()
df['start date'] = df.index.map(lambda x: x.start_time)
print(df)

df['end date'] = df.index.map(lambda x: x.end_time)
# The above line will gives time also
print(df)

# To just get the end date use the below line
df['end date'] = df.index.map(lambda x: x.asfreq('D', how='end'))
print(df)
