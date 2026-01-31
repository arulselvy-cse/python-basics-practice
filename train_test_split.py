x = df["Gender"]  //feature
y = df["Purchased"]  //target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_states=42)
