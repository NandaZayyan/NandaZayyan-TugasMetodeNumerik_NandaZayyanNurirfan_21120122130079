import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Langkah 1: Persiapan Data
data = pd.read_csv('C:\\Users\\nanda\\OneDrive\\Desktop\\New folder')

# Melihat lima baris pertama data
print(data.head())

# Langkah 2: Membuat Model Regresi Linear
# Memisahkan fitur (TB) dan target (NT)
X = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 5].values

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()

# Melatih model pada data latih
model.fit(X_train, y_train)

# Memprediksi nilai NT untuk data uji
y_pred = model.predict(X_test)

# Menghitung galat RMS
rms = mean_squared_error(y_test, y_pred, squared=False)
print("Root Mean Squared Error:", rms)

# Plot titik data dan hasil regresinya
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Hubungan Durasi Waktu Belajar dan Nilai Ujian')
plt.xlabel('Durasi Waktu Belajar (TB)')
plt.ylabel('Nilai Ujian (NT)')
plt.show()
