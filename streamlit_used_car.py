import pickle
import streamlit as st

# Membaca model
model = pickle.load(open('used_car_prediction_model.sav', 'rb'))

# Judul web
st.title('Used Car Price Prediction')

# Features
brand_encoded = st.number_input('Masukan nama brand mobil')
engine_size = st.number_input('Berapa engine sizenya?')
year = st.number_input('Mau cari yang tahun berapa?')
mileage = st.number_input('Mileage berapa?')
min_mpg = st.number_input('Min mpg berapa?')
max_mpg = st.number_input('Max mpg berapa?')
third_row_seating = st.number_input('Third row?')

# Code Prediction
predict = ''

# Membuat tombol prediksi
if st.button('Tes Harga Mobil') :
    predict = model.predict(
        [[brand_encoded, engine_size, year, mileage, min_mpg, max_mpg, third_row_seating]]
    )
    st.write ('Estimasinya dalam USD: ', predict)
    st.write ('Estimasinya dalam IDR: ', predict * 15000)
