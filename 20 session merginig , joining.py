import numpy as np
import pandas as pd

courses = pd.read_csv("courses.csv")
students = pd.read_csv("students.csv")
nov = pd.read_csv("reg-month1.csv")
dec = pd.read_csv("reg-month2.csv")

delivery = pd.read_csv("deliveries.csv")
match = pd.read_csv("ipl-matches.csv")

# pd.concat
# df.concat
# ignore_index
# df.append
# mullitindex -> fetch using iloc
# concat dataframes horizontally

print(pd.concat([nov,dec],ignore_index=True))
print(pd.concat([nov,dec],keys=["nov","dec"]))