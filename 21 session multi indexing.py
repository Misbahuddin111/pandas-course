import numpy as np
import pandas as pd

# multi indexing
multi_indx = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=multi_indx)
print(a)
# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
multi_tuples = pd.MultiIndex.from_tuples(multi_indx)
print(multi_tuples)

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
print(multiindex)

# 2. pd.MultiIndex.from_product()
print(pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]]))


temp = pd.MultiIndex.from_product([["ece","cse","cs"],[2019,2020,2021,2022]])
print(temp)

# creating a series with multiindex object
temp_series = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12],index=temp)
print(temp_series)


# how to fetch items from such a series
print(temp_series['cse'])

# unstack ( unstack convert the multiindexing series into dataframe)
r= temp_series.unstack()
print(r)

# stack convert the dataframe into multi indexing series
print(r.stack())

branch = pd.DataFrame(
    [
          [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index= multiindex,
    columns= ["avg_pkg","students"]
)
print(branch)

print(branch["students"])

'''
Stacking: Moves data from columns to rows, 
typically converting a level of the column index into a level of the row index.
'''


'''
Unstacking: Moves data from rows to columns,
converting a level of the row index into a level of the column index
'''



import pandas as pd

# Create a sample DataFrame with MultiIndex columns
data = {
    ('A', 'X'): [1, 2, 3],
    ('A', 'Y'): [4, 5, 6],
    ('B', 'X'): [7, 8, 9],
    ('B', 'Y'): [10, 11, 12]
}
df = pd.DataFrame(data, index=['p', 'q', 'r'])
print("Original DataFrame:")
print(df)

'''
output

   A     B   
   X  Y  X   Y
p  1  4  7  10
q  2  5  8  11
r  3  6  9  12

'''

# stacking 

# Stack the DataFrame (innermost column level 'X', 'Y' becomes rows)
stacked = df.stack()
print("\nStacked DataFrame:")
print(stacked)

# output 
'''
       A   B
p X    1   7
  Y    4  10
q X    2   8
  Y    5  11
r X    3   9
  Y    6  12
'''


# unstacking

# Unstack the stacked DataFrame (innermost row level 'X', 'Y' becomes columns)
unstacked = stacked.unstack()
print("\nUnstacked DataFrame:")
print(unstacked)

# output
'''
A     B   
   X  Y  X   Y
p  1  4  7  10
q  2  5  8  11
r  3  6  9  12
'''
'''
Key Points
Stacking makes data taller by moving column levels to rows.
Unstacking makes data wider by moving row levels to columns.
Use the level parameter to control which index level to pivo
'''

