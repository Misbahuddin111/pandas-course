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