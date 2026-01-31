import pandas as pd
import numpy ad np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
"Hours":[1,2,3,4,5],
"Marks":[35,40,50,60,70]
}
df = pd.DataFrame(data)
print(df)

x = [["Hours"]]
y = ["Marks"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

model = LinearRegression()  //Create model
model.fit(x_train,y_train)  //train model

y_pred = model.predict(x_test)  //predciton
print("Predicted Marks:",y_pred)
print("Actual Marks:",y_pred.values)  //converts into array format(values)

score = model.score(x_test,y_test)   //evaluation
print(:Model accuracy(R2 score):",score)   //m.s returns r square score








