
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
# sort values in dataframe
movies.sort_values("title_x",inplace=True)
print(movies)
