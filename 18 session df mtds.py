
import numpy as np
import pandas as pd
movies = pd.read_csv("movies.csv")
ipl = pd.read_csv("ipl-matches.csv")
# value_counts
# sort_values
# rank
# sort index
# set index
# rename index -> rename
# reset index
# unique & nunique
# isnull/notnull/hasnans
# dropna
# fillna
# drop_duplicates
# drop
# apply
# isin
# corr
# nlargest -> nsmallest
# insert
# copy

# sort_values(series and datafrme)
x = pd.Series([3,4,6,7,2,4,6,8])
print(x.sort_values())


# sort values in dataframe
sort_movies = movies.sort_values("title_x")
print(sort_movies)


movies.sort_values(['year_of_release','title_x'],ascending=[True,False])

# sort_index(series and dataframe)
marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
marks_sort = pd.Series(marks)
marks_sort.sort_index(ascending=False)


print(movies.sort_index())

# set_index(dataframe) -> inplace
set_index = movies.set_index("title_x")
print(set_index)

# reset_index(series + dataframe) -> drop parameter

print(set_index.reset_index())
print(set_index.set_index("imdb_id"))

# how to replace existing index without loosing
print(set_index.reset_index().set_index("poster_path"))


