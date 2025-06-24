import numpy as np
import pandas as pd

courses = pd.read_csv("courses.csv")
students = pd.read_csv("students.csv")
nov = pd.read_csv("reg-month1.csv")
dec = pd.read_csv("reg-month2.csv")

delivery = pd.read_csv("deliveries.csv")
match = pd.read_csv("matches.csv")

# pd.concat
# df.concat
# ignore_index
# df.append
# mullitindex -> fetch using iloc
# concat dataframes horizontally

print(pd.concat([nov,dec],ignore_index=True))
print(pd.concat([nov,dec],keys=["nov","dec"]))

multi = pd.concat([nov,dec],keys=["nov","dec"])
print(multi.loc[("dec")])
# fetching data 
print(multi.loc[("nov",3)])

# concat dataframes horizontally
print(pd.concat([nov,dec],axis=1,keys=["nov","dec"]))

# joining 

students_df = pd.DataFrame({
    "studentsIDs" : [1,2,3,4],
     "Name": ["Alce","BoB","Charlie","David"]
})
grades_df = pd.DataFrame({
    "studentsIDs":[1,2,5],
    "grade":['A','B','C']
})

inner_join = students_df.merge(grades_df,how="inner",on="studentsIDs")
print(inner_join)

'''
Explanation:

Only StudentID 1 and 2 appear in both DataFrames,
so the result includes only these rows.
StudentID 3, 4 (from students_df) and 5 (from grades_df) are excluded because they don’t exist in both.
'''


# outer function

'''
2. Outer Join
Definition: Returns all rows from both DataFrames, with NaN in places where there’s no match.
'''

outer_merge = students_df.merge(grades_df,how="outer", on="studentsIDs")
print(outer_merge)

#All StudentID values (1, 2, 3, 4, 5) are included.
#For StudentID 3 and 4, there’s no grade, so Grade is NaN.
#For StudentID 5, there’s no name, so Name is NaN.


# left merge

left_join = students_df.merge(grades_df, how='left')
print("Left Join Result:")
print(left_join)


'''
Explanation:

All StudentID values from students_df (1, 2, 3, 4) are included.
StudentID 1 and 2 have matching grades (A, B).
StudentID 3 and 4 have no grades, so Grade is NaN.
StudentID 5 (from grades_df) is excluded because it’s not in the left DataFrame.
'''

# right merge 

right_join = students_df.merge(grades_df, how='right')
print("Right Join Result:")
print(right_join)

'''
All StudentID values from grades_df (1, 2, 5) are included.
StudentID 1 and 2 have matching names (Alice, Bob).
StudentID 5 has no name in students_df, so Name is NaN.
StudentID 3 and 4 (from students_df) are excluded because they’re not in the right DataFrame.
'''

# Alternate syntax for merge
# students.merge(regs)

pd.merge(students,nov,how='inner',on='student_id')