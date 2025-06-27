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

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

branch_df3

# sort index
# both -> descending -> diff order
# based on one level
branch_df3.sort_index(ascending=False)
branch_df3.sort_index(ascending=[False,True])
branch_df3.sort_index(level=0,ascending=[False])


# melt 



# Create the DataFrame
df = pd.DataFrame(
    {
        'branch': ['cse', 'ece', 'mech'],
        '2020': [100, 150, 60],
        '2021': [120, 130, 80],
        '2022': [150, 140, 70]
    }
)

# Apply melt to reshape the DataFrame
melted_df = df.melt(id_vars=["branch"],var_name='years',value_name="students")

# Display the result
print(melted_df)

# pivot table

import pandas as pd

# Sample DataFrame
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Sales': [100, 150, 200, 120, 180],
    'Quantity': [5, 7, 10, 6, 8]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

pivot1 = pd.pivot_table(df, 
                        values='Sales', 
                        index='City', 
                        columns='Category', 
                        aggfunc=['sum','mean','max'])
print("\nPivot Table (Average Sales by City and Category):")
print(pivot1)


import numpy as np
import pandas as pd
import seaborn as sns



'''

total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2
1	10.34	1.66	Male	No	Sun	Dinner	3
2	21.01	3.50	Male	No	Sun	Dinner	3
3	23.68	3.31	Male	No	Sun	Dinner	2
4	24.59	3.61	Female	No	Sun	Dinner	4

'''

df = sns.load_dataset('tips')
df.head()

# aggfunc
df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='std')
# margins
df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True)