import pandas as pd

df = pd.read_excel("P1.xlsx")

df.to_csv("P1.csv", sep=";", index=False, encoding="utf-8")
