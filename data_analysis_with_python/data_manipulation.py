import pandas as pd

df = pd.read_csv("../data/data.csv")

# first 5 rows.
print(df.head(5))
# last 5 rows.
print(df.tail(5))
print(df.describe())
print(df.dtypes)

# Handling missing values.
print(df.isnull())
print(df.isnull().any(axis=1)) # axix=0(row)(default) axix=1(column)
print(df.isnull().sum())
print(df.fillna(0)) # fills empty space with value.
df["data_fillNA"] = df['Maxpulse'].fillna(df['Maxpulse'].mean())
print(df["data_fillNA"])
df = df.rename(columns={'Pulse':'Dhadkan'}) # change name
print(df)
 # change data type.
df["New_Maxpulse"]=df["Maxpulse"].astype(float)
print(df)

df["New_Maxpulse"]=df["Maxpulse"].apply(lambda x:x**2)
print(df)

# Data aggregating and grouping.
grouped_mean = df.groupby('Dhadkan')['Calories'].mean() # grouped by 'Dhadkan' and mean of calories after grouping.
print(grouped_mean)
grouped_mean = df.groupby(['Dhadkan','Maxpulse'])['Calories'].mean()
print(grouped_mean)
grouped_sum = df.groupby(['Dhadkan','Maxpulse'])['Calories'].sum()
print(grouped_sum)

# aggregate multiple functions.
grouped_agg = df.groupby(['Dhadkan','Maxpulse'])['Calories'].agg(['mean','sum', 'count'])
print(grouped_agg)


# merging and joining dataframes.
df1 = pd.DataFrame({'Key': ['A', 'B', 'C'],'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'D'],'Value2': [4, 5, 6]})

# merge dataframe on the key columns.
df=pd.merge(df1, df2, on="Key", how="inner")
print(df)
df=pd.merge(df1, df2, on="Key", how="outer")
print(df)
df=pd.merge(df1, df2, on="Key", how="left")
print(df)
df=pd.merge(df1, df2, on="Key", how="right")
print(df)