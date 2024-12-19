from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from model.cleaning_invoices_test_data import X, y
import joblib

le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Inisialisasi KNN (dengan k=3 misalnya)
knn_model = KNeighborsClassifier(n_neighbors=6)
knn_model.fit(X, y_encoded)

dct_model = DecisionTreeClassifier();
dct_model.fit(X, y_encoded);

# Menyimpan model ke file
joblib.dump({"model": knn_model,"encoder": le}, 'model_knn_and_encoder.pkl')
joblib.dump({"model": dct_model,"encoder": le}, 'model_dct_and_encoder.pkl')
