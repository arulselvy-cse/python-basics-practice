import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
data = {
    "Age": [22, 25, 47, 52, 46, 56],
    "Salary": [20000, 25000, 60000, 80000, 75000, 90000],
    "Purchased": [0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

x = df[["Age","Salary"]]
y = df["Purchased"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_states=42)

from sklearn.preprocessing import StandardScaler #import scaler

scaler = StandardScaler()    #apply scaling
x_train = scaler.fit_transfrom(x_train) 
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=3) #crear\te KNN model
model.fit(x_train,y_train)   #train model 
y_pred = model.predict(x_test)  # predict
print("Predictes:",y_pred)
print("Actual:",y_test.values)

acc = accuracy_score(y_test,y_pred)  #evaluation
print("Accuracy:",acc)

cm = confusion_matrix(y_test,y_pred)  #confusion matrix
print(cm)














