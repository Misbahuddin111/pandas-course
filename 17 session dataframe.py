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

# fetching cols from files 
print(movies["release_date"])