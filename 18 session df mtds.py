
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


import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate a large dataset (100,000 rows)
n_rows = 100_000
data = {
    'order_id': range(1, n_rows + 1),
    'customer_id': np.random.randint(1000, 5000, n_rows),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Toys', None], n_rows, p=[0.3, 0.3, 0.2, 0.15, 0.05]),
    'price': np.random.uniform(5, 500, n_rows).round(2),
    'quantity': np.random.randint(1, 10, n_rows),
    'region': np.random.choice(['North', 'South', 'East', 'West', None], n_rows, p=[0.25, 0.25, 0.25, 0.2, 0.05]),
    'order_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 730)) for _ in range(n_rows)]
}
df = pd.DataFrame(data)

# Introduce duplicates for testing
df = pd.concat([df, df.sample(n=1000, random_state=42)]).reset_index(drop=True)

# Extract a Series for testing
s = df['price']

print(f"Dataset shape: {df.shape}")
# Output: Dataset shape: (101000, 7)

df_counts = df[['product_category', 'region']].value_counts()
print(df_counts.head())