from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

X = [[1.05],
[1.15],
[1.2],
[1.25],
[1.3],
[1.35],
[1.4],
[1.45],
[1.55],
[1.6],
[1.65],
[1.7],
[1.8],
[1.9],
[2],
[2.05],
[2.1],
[2.2],
[2.25],
[2.4],
[2.5],
[2.55],
[2.9],
[3],
[3.05],
[3.15],
[3.2],
[3.25],
[3.3],
[3.35],
[3.4],
[3.5],
[3.6],
[3.85],
[3.9],
[3.95],]

y = ["Danger",
"Danger",
"Danger",
"Danger",
"Danger",
"Danger",
"Danger",
"Danger",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Warning",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Normal",
"Health",
"Health",
"Health",
"Health",
"Health",]

# Memuat model knn dari file
data = joblib.load('model_knn_and_encoder.pkl')

le = data["encoder"]
model = data["model"]

data2 = joblib.load('model_dct_and_encoder.pkl')

le2 = data2["encoder"]
model2 = data2["model"]

y_encoded = le.fit_transform(y)
y_pred = model.predict(X)
y_pred2 = model2.predict(X)

accuracy = accuracy_score(y_encoded, y_pred)
accuracy2 = accuracy_score(y_encoded, y_pred2)

print(f"accuracy: {accuracy}")
print(f"accuracy2: {accuracy2}")
# print(f"y_pred: {le.inverse_transform(y_pred)}")
# print(f"y: {y}")

X = [[2.95], [3.65], [2.45], [2.7], [2.8], [1], [3.1], [3.1], [1], [2.35], [2.6], [3.8], [1.75], [2.95], [3.65], [1.5], [3.55], [2.35], [1.95], [
    3.75], [2.65], [2.15], [2.85], [2.75], [3.8], [3.7], [1.85], [2.95], [1.95], [3.45], [2.3], [2.8], [2.8], [1], [2.7], [2.3], [4], [1.1],]

# Output labels (y)
y = ["Normal", "Health", "Warning", "Normal", "Normal", "Danger", "Normal", "Normal", "Danger", "Warning", "Normal", "Health", "Warning", "Normal", "Health", "Warning", "Health", "Warning", "Warning",
     "Health", "Normal", "Warning", "Normal", "Normal", "Health", "Health", "Warning", "Normal", "Warning", "Normal", "Warning", "Normal", "Normal", "Danger", "Normal", "Warning", "Health", "Danger"]

y_encoded = le.fit_transform(y)
y_pred = model.predict(X)
y_pred2 = model2.predict(X)

accuracy = accuracy_score(y_encoded, y_pred)
accuracy2 = accuracy_score(y_encoded, y_pred2)

print(f"accuracy: {accuracy}")
print(f"accuracy2: {accuracy2}")