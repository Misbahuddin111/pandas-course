import numpy as np
import pandas as pd

print(pd.Timestamp('2025/5/13'))

# object (dttpes)
print(type(pd.Timestamp('2025/5/13')))

# variations 

temp = pd.Timestamp(('2025,june,28'))
print(temp)

# providing time also

time = pd.Timestamp(("2025/june/16 10:30 pm"))
print(time)

# using datetime.datetime object

import datetime as dt
x=pd.Timestamp(2023,4,15,9,50)
print(x)

# why separate objects to handle data and time when python already has datetime functionality?

'''
syntax wise datetime is very convenient
But the performance takes a hit while working with huge data. List vs Numpy Array
The weaknesses of Python's datetime format inspired the NumPy team to add a set of 
native time series data type to NumPy.
The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of
dates to be represented very compactly.


'''
import numpy as np

date = np.array('2015-07-04', dtype=np.datetime64)
print(date)

print(date + np.arange(13))

# DatetimeIndex Object

# A collection of pandas timestamp


# from strings
print(type(pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1'])))

# using python datetime object
pd.DatetimeIndex([dt.datetime(2023,1,1),dt.datetime(2022,1,1),dt.datetime(2021,1,1)])

# using pd.timestamps
dt_index = pd.DatetimeIndex([pd.Timestamp(2023,1,1),pd.Timestamp(2022,1,1),pd.Timestamp(2021,1,1)])

# using datatimeindex as series index

print(pd.Series([1,2,3],index=dt_index))

# date_range function

# generate daily dates in a given range
pd.date_range(start='2023/1/5',end='2023/2/28',freq='3D')


# B -> business days
pd.date_range(start='2023/1/5',end='2023/2/28',freq='B')


# W -> one week per day
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='W-THU'))


# H -> Hourly data(factor)
pd.date_range(start='2023/1/5',end='2023/2/28',freq='6H')


# M -> Month end
pd.date_range(start='2023/1/5',end='2023/2/28',freq='M')


# MS -> Month start
pd.date_range(start='2023/1/5',end='2023/2/28',freq='MS')


# A -> Year end
pd.date_range(start='2023/1/5',end='2030/2/28',freq='A')


# using periods(number of results)
pd.date_range(start='2023/1/5',periods=25,freq='M')


# to_datetime function

# simple series example

s = pd.Series(['2023/1/1','2022/1/1','2021/1/1'])
pd.to_datetime(s).dt.day_name()



# with errors
s = pd.Series(['2023/1/1','2022/1/1','2021/130/1'])
pd.to_datetime(s,errors='coerce').dt.month_name()



