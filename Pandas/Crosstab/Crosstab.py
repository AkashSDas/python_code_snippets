# ###### Crosstab ######

# Crosstab(Also called Contingency table):
#     In statistics, a contingency table(cross tabulation or crosstan) is a type of table in a matrix format that displays the (multivariate) frequency distribution of the variables
# =================================
# Improting pandas module
import pandas as pd
# =================================
data = {
  'Name': ['Kathy', 'Linda', 'Peter', 'John', 'Fatima', 'Kadir', 'Dhaval', 'Sudhir', 'Parvir', 'Yan', 'Juan', 'Liang'],

  'Nationality': ['USA', 'USA', 'USA', 'USA', 'Bangladesh', 'Bangladesh', 'India', 'India', 'India', 'China', 'China', 'China'],

  'Sex': ['Female', 'Female', 'Male', 'Male', 'Female','Male', 'Male', 'Male', 'Male','Female', 'Female','Male'],

  'Age': [23, 18, 19, 22, 31, 25, 35, 31, 37, 52, 58, 43],

  'Handedness': ['Right', 'Right', 'Right', 'Left', 'Left', 'Left', 'Left', 'Left', 'Right', 'Right', 'Left', 'Left']
}

df = pd.DataFrame(data)
print(df)
# =================================
# crosstab is on pandas method not on dataframe

print(pd.crosstab(df.Nationality, df.Handedness))
print(pd.crosstab(df.Sex, df.Handedness))

# To get total use margins set margins parameter to True
print(pd.crosstab(df.Sex, df.Handedness, margins=True))

# To have multiple variable at column level pass the list of elements containing those variables
print(pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins=True))

# To have multiple variable in row level pass the list of elements containing those variables
print(pd.crosstab([df.Sex, df.Nationality], df.Handedness, margins=True))

# To get percentage of Handedness of particular Sex
print(pd.crosstab([df.Sex], [df.Handedness], normalize='index'))
# =================================
# To know average age of particular Sex

import numpy as np

print(pd.crosstab([df.Sex], [df.Handedness], values=df.Age, aggfunc=np.average))

# There are many other statistics operations that can be preformed
