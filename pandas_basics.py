import pandas as pd 
data = {
"Name":["Arul","ruby","madd"],
"marks":[85,98,78],
"passed":["yes","yes","yes"]
}
df = pd.DataFrame(data)
print(df)
df = pd.read_csv("data.csv")
print(df)  #reading csv file
print(df.head())  #first 5
print(df.tail())  #last 5
print(df.info())  #information
print(df.describe()) # DATA understanding
print(df["Marks"]) #select columns
print(df["Name","Marks"]])

hight_marks = df[df["Marks"] > 70]  #filtering
print(high_marks)








