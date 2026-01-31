import pandas as pd

df = {
"Gender":["Male","Female","Male","Female"]
"Purchase":["Yes","No","No","Yes"]
}
df = pd.DataFrame(data)

from sklearn_preprocesssing import LabelEncoder
le = LabelEncoder  //creating object
df["Gender"] = le.fit_transform(df["Gender"])
df["Purchase"] = le.fit_transform(df["Purchased"])
print(df)
