import numpy as np
import pandas as pd

data = [
    [100,80,10],
    [90,83,8],
    [100,90,8]
]
data_frame = pd.DataFrame(data,columns= ["iq","marks", "pakage"])
print(data_frame)

# dataframe through dictionaries

school_record = {
    "name": ["Misbah", "DAud","Amar","Abdullah"],
    "roll no":[448,456,463,483],
    "skills":["web","Ai","machine learning","devops"]
}

school_data = pd.DataFrame(school_record)
print(school_data)

movies = pd.read_csv("movies.csv")
#print(movies)

ipl = pd.read_csv("ipl-matches.csv")
#print(ipl)

# dataFrame methods and attributtes

# shape (shape tell you the no of rows and columns in a file)
#print(movies.shape)
#print(ipl.shape)

# dtypes (data type of every column)

# print("data type :", movies.dtypes)

# index ( show the total no of index)
# print("index",ipl.index)

# columns (show the total no of columns )
# print("columns :",movies.columns)

# values ( show all values in a file)
# print('values :', ipl.values)

# head ( print first five elements)
print(f"first five movies name\n:{movies.head()}")

# tail (print last five elements)
print(f"last five movies names {ipl.tail()}")

# info (give informTION)
print(f"information {movies.info()}")

# desceibe ( give mathmatical summary)
print(f"describe mathmatical overview {ipl.describe()}")

# isnull ( show null values in columns)
print(f"this functions tells there are how many null values {ipl.isnull()}")

# duplicated (show duplicated values in rows)
print("duplicates values", ipl.duplicated().sum())

# rename (change the name of heading)

data_frame.rename(columns={"iq": "iqss","marks" : "total_nums"},inplace=True)
print(data_frame)

# maths methods 

print(data_frame.sum(axis=1))

# for all sum the values is add in columns by default if want to add value by rows then we changed the axis to 1

# fetching cols from files (we can fectch cols like same indexing we use name)
print(movies["release_date"])

# selecting rows from files 
print(school_data.set_index("name",inplace=True))
print(school_data.iloc[0:2])

# now fetch rows by name

print(school_data)
print(school_data.loc["Abdullah"])

# in both loc and iloc fancy indexing is possible
print(school_data.loc[["Misbah","Amar","DAud"]])

import pandas as pd




'''
Key Differences
loc uses labels (e.g., 'x', 'A') and is inclusive of the end label.
iloc uses integer indices (e.g., 0, 1) and is exclusive of the end index.
Use loc for label-based indexing, iloc for position-based indexing.
These examples cover common use cases for selecting data in pandas. Let me know if you need more specific scenarios!
'''

# selecting rows and columns
# fetch data from files in rows and columns (movies.loc(columns,rows))

print(movies.loc[0:5,"title_x":"poster_path"])

# now by indexing 
print(movies.iloc[0:4,0:3])

# add new coloumns 
new_columns = movies["country"]  = "india"
print(movies)
