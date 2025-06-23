import numpy as np
import pandas as pd

movies = pd.read_csv("imdb-top-1000.csv")

genres = movies.groupby("Genre")
print(genres)


# find the top 3 genres by total earning
print(movies.groupby("Genre")["Gross"].sum().sort_values(ascending=False).head(3))

# find the genre with highest avg IMDB rating
print(movies.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False).head(1))

# find director with most popularity
print(movies.groupby("Director")['No_of_Votes'].sum().sort_values(ascending=False).head(1))


# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

import pandas as pd

# Sample DataFrame
data = {
    'Department': ['HR', 'Sales', 'Tech', 'Sales', 'Tech', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 80000, 65000, 90000, 55000],
    'Years': [5, 3, 7, 4, 6, 2]
}
df = pd.DataFrame(data)
print(df)

grouped_data = df.groupby("Department")

# len
total_length = len(grouped_data)
print("len",total_length)

# size 

num_size = grouped_data.size()
print("size",num_size)

# first
first = grouped_data.first()
print("first data",first)


# last
last = grouped_data.last()
print("last data",last)

# nth 
nth_data = grouped_data.nth(1)
print("nth data",nth_data)

print(genres.agg("sum"))
# aggregation

movies
genres.agg(
    {
        "Runtime":["min","max"],
        "IMDB_Rating":"max",
        "No_of_Votes": "sum"
    }
)

# Select only numeric columns for aggregation
numeric_cols = movies.select_dtypes(include=np.number).columns
genres[numeric_cols].agg(['min','max','mean','sum'])

movies
genres["Runtime"].agg(["mean","sum","min"])


# group my multiple coulumns
duo = movies.groupby(["Director","Star1"])
duo.size()

# find the most earning actor->director combo
duo["Gross"].sum().sort_values(ascending=False).head(1)

# find the best(in-terms of metascore(avg)) actor->genre combo
movies.groupby(["Star1","Genre"])["Metascore"].mean().reset_index().sort_values("Metascore",ascending=False).head(1)


# agg on multiple groupby
duo.agg({
  "Runtime": ["max","min","mean"],
    "No_of_Votes": "sum",


})


genres.get_group("Drama")


import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Sales': [100, 200, 300, 400, 150]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Group by 'Category' and 'Region
df.groupby(["Category","Region"]).get_group(("B","North"))