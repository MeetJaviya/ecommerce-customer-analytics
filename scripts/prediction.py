import joblib

model = joblib.load("models/churn_model.pkl")

sample = [[30,5,500]]

prediction = model.predict(sample)

print("Churn Prediction:",prediction)
