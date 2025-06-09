import pandas as pd
import numpy as np

# Student Scores
students = pd.Series([85, 92, 78, 95, 88], index=["Alice", "Bob", "Charlie", "David", "Eve"], name="Test Scores")

# Sales Data
sales = pd.Series([120, 150, 200, 180, 220, 170, 190], index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], name="Daily Sales")

# Movie Ratings
movies = pd.Series([8.5, 7.8, 9.0, 6.5, 8.0], index=["Inception", "The Matrix", "Interstellar", "Avatar", "Titanic"], name="IMDb Ratings")

'''
1. Creating a Series
Question: Create a Pandas Series to store the number of hours worked by employees in a week. 
Use employee names as indices and assign a name to the Series.
'''

hours = [40, 35, 45, 38, 42]
employees = ["John", "Emma", "Liam", "Sophia", "Noah"]

data = pd.Series(hours, index=employees,name="labour data")
print(data)

'''
Question: For the students Series, print its size, data type, name, 
whether its values are unique, and its indices.
'''

print(f"size : {students.size}")
print(f"data types : {students.dtype}")
print(f"name : {students.name}")
print(f"is_unique : {students.is_unique}")
print(f"indicies : {students.index}")

'''
3. Series Methods
Question: Using the sales Series, find:

The first 3 days of sales.
The last 2 days of sales.
A random day’s sales.
The frequency of sales amounts.
The day with the highest sales
'''

first_days = sales.head(3)
print(f"first three days sales \n: {first_days}")

last = sales.tail(2)
print(f"last 2 days \n {last}")

random = sales.sample()
print(f"random day sales : \n{random}")

count = sales.value_counts()
print(f"values count :\n {count}")

high = sales.max()
print(f"highest : \n{high}")

highest = sales.sort_values(ascending=False).head(1)
print(f"highest value :\n {highest}")

'''
4. Mathematical Methods
Question: For the movies Series, calculate the total number of ratings, sum, mean, median, mode, standard deviation, variance,
 minimum, and maximum ratings, and provide a summary of statistics.
'''

print("Count:", movies.count())
print("Sum:", movies.sum())
print("Mean:", movies.mean())
print("Median:", movies.median())
print("Mode:\n", movies.mode())
print("Standard Deviation:", movies.std())
print("Variance:", movies.var())
print("Minimum:", movies.min())
print("Maximum:", movies.max())
print("\nSummary Statistics:\n", movies.describe())



# Student Scores
students = pd.Series([85, 92, 78, 95, 88], index=["Alice", "Bob", "Charlie", "David", "Eve"], name="Test Scores")

'''
5. Indexing and Slicing
Question: For the students Series:

Access Bob’s score.
Slice the scores of Charlie to Eve.
Use fancy indexing to get scores of Alice and David.
'''
print("Bob's score:", students["Bob"])
print("\nScores from Charlie to Eve:\n", students["Charlie":"Eve"])
print("\nScores of Alice and David:\n", students[["Alice", "David"]])


'''
6. Editing a Series
Question: In the sales Series:

Change Monday’s sales to 130.
Add a new day (Holiday) with sales of 250.
Update sales for Wednesday and Thursday to 210 and 190 using fancy indexing.
'''

# Sales Data
sales = pd.Series([120, 150, 200, 180, 220, 170, 190], index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], name="Daily Sales")

mon_sales = sales[0] = 130
print(sales)

new_day = sales["Holyday"] = 250
print(sales)

sales[["Wed","Thu"]] = [210,190]
print(sales)

'''
7. Type Conversion
Question: Convert the movies Series to a list and a dictionary.
'''

print("list :", list(movies))
print("dictionary :",dict(movies))

'''
. Membership Operators
Question: Check if "Inception" is in the movies Series index and if a rating of 9.0 exists in its values.

'''

print("Inception" in movies.index)
print(9.0 in movies.values)



'''
9. Looping
Question: Loop through the students Series and print each student’s name and score.
'''

for i in students.items():
    print(i)

for i in sales.index:
    print(i)

for i in sales.values:
    print(i)

'''
10. Relational Operators
Question: Identify days in the sales Series where sales were at least 180.
'''

print(sales>=180)

high_sales = sales[sales>=180]
print(high_sales)


'''
11. Boolean Indexing
Question: For the movies Series:

Count movies with ratings ≥ 8.0.
Find movies with ratings between 7.5 and 8.5.
'''
print("Movies with rating >= 8.0:", movies[movies >= 8.0].size)
print("\nMovies with rating between 7.5 and 8.5:\n", movies[(movies >= 7.5) & (movies <= 8.5)])

