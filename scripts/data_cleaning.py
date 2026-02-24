import pandas as pd

df = pd.read_excel("data/raw/OnlineRetail.xlsx")

df.dropna(inplace=True)

df = df[df['Quantity'] > 0]

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

df.to_csv("data/processed/cleaned_data.csv", index=False)
df.to_excel("excel/cleaned_data.xlsx", index=False)

print("Data Cleaning Completed")
