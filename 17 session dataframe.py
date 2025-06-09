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
print(movies.shape)
print(ipl.shape)

# dtypes (data type of every column)

print("data type :", movies.dtypes)

# index ( show the total no of index)
print("index",ipl.index)

#columns (show the total no of columns )
print("columns :",movies.columns)
# values ( show all values in a file)
print('values :', ipl.values)

# head ( print first five elements)

# tail (print last five elements)

# info (give informTION)

# desceibe ( give mathmatical summary)

# isnull ( show null values in columns)

# duplicated (show duplicated values in rows)

# rename (change the name of heading)



#  MATH FUNCTIONS

