import pickle
import streamlit as st

mokas_model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi harga mobil bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

mokas_predict = ''

if st.button('Estimasi Harga'):
    mokas_predict = mokas_model.predict(
        [[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi harga mobil dalam EUR : ', mokas_predict)
    st.write('Estimasi harga mobil dalam IDR (Juta) : ', mokas_predict*19110*1e-6)