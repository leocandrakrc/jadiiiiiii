import streamlit as st
st.set_page_config(page_title="AIR PERMUKAAN KELOMPOK 8 PLI",page_icon=":microscope:")

# Sidebar
menu = ["Artikel", "Calculator"] 
selected = st.sidebar.selectbox("TEKNIK PENGAMBILAN SAMPEL AIR PERMUKAAN",menu)




#isian
if selected == "Artikel":
    st.title("TEKNIK PENGAMBILAN SAMPEL :blue[AIR PERMUKAAN]")
    
    st.subheader("Pengertian Air Permukaan - Perhitungan Debit Air - Fungsi Pengukuran Debit Air")
    st.write("Air permukaan merupakan air yang terkumpul di atas tanah atau di mata air, sungai danau, lahan basah atau laut. Air permukaan berhubungan dengan air bawah tanah atau air atmosfer. Air permukaan dapat dibedakan menjadi dua jenis yaitu: Perairan Darat dan Perairan Laut.")
    st.write("Perairan Darat adalah air permukaan yang berada di atas daratan, misalnya seperti rawa-rawa, danau, sungai, dan lain sebagainya.")
    st.write("Perairan Laut adalah air permukaan yang berada di lautan luas.")

    st.subheader("Menghitung Debit Air Permukaan")
    st.write("Debit adalah jumlah aliran air (volume) yang mengalir melalui suatu penampang dalam waktu tertentu, umumnya dinyatakan dalam satuan volume/waktu yaitu (m³/detik). Yaitu dengan rumus berikut.")
    st.write("Debit= Volume (m³)/detik")

    st.subheader("Fungsi Pengukuran Debit Air")
    st.write("Pengukuran debit air penting dalam penelitian atau monitoring kualitas air permukaan karena dapat memberikan informasi tentang jumlah air yang sedang mengalir pada titik sampling. Debit air yang tinggi dapat menunjukkan aliran air yang kuat, yang dapat mempengaruhi penyebaran atau distribusi polutan. Di sisi lain, debit air yang rendah dapat mengindikasikan aliran yang lambat atau bahkan stagnan, yang mungkin menyebabkan penumpukan atau akumulasi polutan.")
    st.write("Selain itu, pengukuran debit air juga penting dalam menghitung beban polutan. Beban polutan adalah jumlah total polutan yang diangkut oleh aliran air dalam periode waktu tertentu. Dengan mengetahui debit air, kita dapat mengalikan konsentrasi polutan dalam air dengan debit tersebut untuk mengestimasi jumlah polutan yang masuk atau keluar dari suatu wilayah.")
    st.write("Dalam praktiknya, debit air dapat diukur menggunakan berbagai metode, seperti pengukuran langsung menggunakan perangkat pengukur debit, pengukuran dengan menggunakan perangkat pengukur kecepatan aliran air, atau dengan menggunakan model matematika yang memperhitungkan berbagai parameter hidrologi yang relevan.")



elif selected == "Calculator":
        st.write("# Perhitungan Debit Air Sungai")
        st.write("Masukkan volume sungai yang sudah dikonversi ke meter dan masukkan waktu dalam satuan detik.")

        panjang = st.number_input("Masukkan panjang sungai (m): ", min_value=0.0, step=0.1)
        lebar = st.number_input("Masukkan lebar sungai (m): ", min_value=0.0, step=0.1)
        kedalaman = st.number_input("Masukkan kedalaman sungai (m): ", min_value=0.0, step=0.1)
        volume = panjang * lebar * kedalaman
        waktu = st.number_input("Masukkan waktu (detik): ", min_value=0.0, step=0.1)

        if st.button("Hitung"):
            debit = volume / waktu
            st.success(f"Hasil perhitungan Volume adalah {volume:.2f} m³")
            st.success(f"Hasil perhitungan Debit adalah {debit:.2f} m³/detik")
            
