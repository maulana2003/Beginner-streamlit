import streamlit as st 

st.title("Penghitung rumus fisika sederhana")
st.write(""" Web Ini adalah aplikasi penghitung Rumus Fisika""")

pilihan = ['Luas','Volume','percepatan(a)','Massa Jenis(p)','Gaya(F)','Energi Potensial(Ep)']
option = st.selectbox ('Tolong pilih salah satu',pilihan)
st.write("Kamu memilih opsi",option)




if option == 'Luas' :
    panjang = st.number_input("Masukkan panjang :")
    Lebar = st.number_input("Masukkan Lebar : ")
    luas = panjang * Lebar
    st.write ("Luasnya adalah : ",luas) 

if option == 'Volume' :
    panjang = st.number_input ("Masukkan panjang : ")
    Lebar = st.number_input("Masukkan Lebar : ")
    Tinggi =st.number_input("Masukkan Tinggi : ")
    volume = panjang * Lebar * Tinggi
    st.write ("Volumenya adalah : ", volume)
    
if option == 'percepatan(a)' :
    kecepatan = st.number_input("Masukkan kecepatan (v) : ",value = 0)
    waktu = st.number_input ("Masukkan waktu(t) : ", value = 1)
    percepatan = kecepatan / waktu
    st.write ("Percepatannya adalah : ", percepatan)

if option == 'Massa Jenis(p)' :
    Massa = st.number_input ("Masukkan Massa : ",value = 0)
    Volume = st.number_input ("Masukkan volume : ",value = 1)
    MasJen = Massa / Volume
    st.write (" Massa Jenisnya adalah : ", MasJen)

if option == 'Gaya(F)' :
    Massa = st.number_input ("Massukkan Massa (m): ")
    percepatan = st.number_input ("Masukkan Percepatan (a) : ")
    Gaya = Massa * percepatan
    st.write ("Gaya yang didapat adalah :", Gaya)

if option == 'Energi Potensial(Ep)':
    Massa = st.number_input("Masukkan Massa (m): ")
    percepatang = st.number_input ("Masukkan Percepatan Gravitasi (m/s^2)")
    tinggi = st.number_input ("Masukkan tinggi dari permukaan tanah : ")
    EP = Massa * percepatang * tinggi
    EPtotal = st.write ("Energi Potensialnya adalah :",EP)




