import numpy as np
import pandas as pd

courses = pd.read_csv("courses.csv")
nov = pd.read_csv("reg-month1.csv")
dec = pd.read_csv('reg-month2.csv')
students = pd.read_csv('students.csv')

# 1. find total revenue generated
regs = pd.concat([nov,dec],ignore_index=True)
total_revenue = regs.merge(courses,how="inner",on='course_id')["price"].sum()
print(total_revenue)


# 2. find month by month revenue
temp_df = pd.concat([nov,dec],keys=["nov","dec"]).reset_index()
temp_df.merge(courses,how="inner",on="course_id").groupby("level_0")["price"].sum()


# 3. Print the registration table
# cols -> name -> course -> price
regs.merge(students,how="inner",on="student_id").merge(courses,how="inner", on="course_id")[["name","course_name","price"]]

# 4. Plot bar chart for revenue/course
regs.merge(courses,how="inner",on="course_id").groupby("course_name")["price"].sum().plot(kind="bar")


# 5. find students who enrolled in both the months
common_student_id = np.intersect1d(nov['student_id'],dec['student_id'])
print(common_student_id)


# 6. find top 3 students who did most number enrollments
regs.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3)


# 7. find top 3 students who spent most amount of money on courses
regs.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3)


