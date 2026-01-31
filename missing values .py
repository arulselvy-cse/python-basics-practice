print(df.isnull())   // Checak missing values
print(df.isnull().sum())   //count missing values
df_clean = df_dropna()   //remove rows with missingvalues

df["Age"].fillna(df["age"].mean(),inplace = True) //fill mv
df["Gender"].fillna(df["Gender"].mode()[0],inplace=True) //categorical value

