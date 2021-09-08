import csv
import pandas as pd

df = pd.read_csv('final_stars_3.csv')

print(df.shape)

# del df["Constellation"]
# del df["Mass1"]
# del df["Distance1"]
# del df["Radius1"]
# del df["Unnamed: 0"]
# del df["Unnamed: 5"]
del df["Unnamed: 0.1"]

print(df.shape)
print("deleted")

df.to_csv("final_stars_4.csv")