import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
"Age":[22,30,40,50,60],
"Salary":[20000,30000,35000,40000,550000,59000],
"Purchased":[0,0,1,1,1]
}
df = pd.DataFrame(data)

x = df[["Age","Salary"]]
y = df["Purchased"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 42)

model = LogisticRegression()  //train logisticregression
model.fit(x_train,y_train)

y_pred = model.predict(x_test)  //preiction
print("Predicted:",y_Pred)
print("Actual:",y_test.values)

score = model.score(x_test,y_test)  //accuracy
print("Accuracy:",score)












