import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

rfm = pd.read_csv("data/processed/rfm_data.csv")

X = rfm[['Recency','Frequency','Monetary']]

y = rfm['Churn']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test,pred)

print("Accuracy:",accuracy)

joblib.dump(model,"models/churn_model.pkl")
