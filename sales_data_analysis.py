import pandas as pd

df=pd.read_csv("sales_data.csv")

# clean column names
df.columns = df.columns.str.strip().str.lower()

# convert date column
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

#profit column
df['profit'] = df['revenue'] - df['cost']

#revenue by region
print(df.groupby('region')['revenue'].sum())

#Profit by product
print(df.groupby('product')['profit'].sum())

df.columns = df.columns.str.strip().str.lower()

df.groupby("region")["revenue"].sum()
df.groupby("product")["profit"].sum()

#monthly trend
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

df.groupby("month")["revenue"].sum()

print(df)



