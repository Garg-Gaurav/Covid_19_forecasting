import numpy as np
import pandas as pd

train = pd.read_csv("train.csv")
train.head()
train['Province_State'] = train['Province_State'].fillna('NA')
countries=train.groupby('Country_Region')
print(countries.nunique())
for cou in countries:
    print(cou)

'''print(train['Country_Region'].nunique())

print(train['ConfirmedCases'])
print(train['Date'].min())
print(train['Date'].max())'''

test = pd.read_csv("test.csv")
test.head()

print(test['Date'].min())
print(test['Date'].max())

train['Province_State'].fillna('', inplace=True)
train['Date'] = pd.to_datetime(train['Date'])
train['day'] = train.Date.dt.dayofyear
train['Weekday'] = (train['day'] // 5 == 1).astype(float)

train.head()