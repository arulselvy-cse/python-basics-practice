import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from skleran.metrics import accuracy_score,confusion_matrix

data = {
    "Age": [22, 25, 47, 52, 46, 56],
    "Salary": [20000, 25000, 60000, 80000, 75000, 90000],
    "Purchased": [0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

x = df[["Age","Salary"]]
y = df["Purchased"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_states=42)

model = DecisionTreeClassifier(max_depth=3)   #causes overfitting (3)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
print("Accuracy:",acc)

cm = confusion_matrix(y_test,y_pred)
print(cm)










