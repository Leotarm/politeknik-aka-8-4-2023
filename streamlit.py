#library
import streamlit as st

#write
st.title("SOFTWARE PERKALIAN")
st.write("ini adalah aplikasi yang dibuat menggunakan streamlit")

#input 
number1 = st.number_input("masukkan bilangan pertama")
st.write("bilangan pertama adalah:", number1)

#input 
number2 = st.number_input("masukkan bilangan kedua")
st.write("bilangan kedua adalah:", number2)

#hasil
hasil = number1*number2

if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol hitung')