import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Prediksi Harga Rumah")

# Baca data dari CSV
df = pd.read_csv("data_rumah.csv")

# Model
X = df[["Luas", "Tipe", "Lantai", "Cluster"]]
y = df["Harga"]
model = LinearRegression()
model.fit(X, y)

# Slider Inputs
st.subheader("Masukkan Data Rumah :")

luas = st.slider("Luas Rumah (m²)", min_value=40, max_value=300, step=10, value=100)
tipe = st.slider("Tipe Rumah", min_value=30, max_value=90, step=5, value=60)
lantai = st.slider("Jumlah Lantai", min_value=1, max_value=3, step=1, value=2)
cluster = st.slider("Cluster (0 = biasa, 1 = elit)", min_value=0, max_value=1, step=1, value=1)


# Prediksi
input_data = [[luas, tipe, lantai, cluster]]
predicted_price = model.predict(input_data)[0]

st.success(f"Prediksi Harga Rumah: Rp {predicted_price:,.0f} juta")

