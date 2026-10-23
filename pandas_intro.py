import pandas as pd

df = pd.read_csv("data.txt", names=["Name", "Age", "City"])
print(df)