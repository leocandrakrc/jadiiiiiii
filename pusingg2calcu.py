import streamlit as st

def konversi_panjang(panjang, satuan):
    konversi = {
        "km": 1000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }
    if satuan in konversi:
        return panjang * konversi[satuan]
    else:
        return None
    
def konversi_waktu(waktu, satuan):
    konversi = {
        "hari": 24 * 60 * 60,
        "jam": 60 * 60,
        "menit": 60,
        "detik": 1
    }
    if satuan in konversi:
        return waktu * konversi[satuan]
    else:
        return None

st.write("# Perhitungan Debit Air Sungai")
st.write("Masukkan satuan panjang untuk merubah ke meter.")

satuan_input_panjang = st.selectbox("Pilih satuan panjang", ("km", "hm", "dam", "m", "dm", "cm", "mm"))
panjang_input = st.number_input("Masukkan panjang: ", min_value=0.0, step=0.1)

panjang_meter = konversi_panjang(panjang_input, satuan_input_panjang)

if st.button("Hitung Konversi Panjang", key="button1"):
    if panjang_meter is not None:
        st.success(f"{panjang_input} {satuan_input_panjang} = {panjang_meter} meter")
    else:
        st.error("Satuan panjang tidak valid.")

st.write("___________________________________________________________")

st.write("Masukkan waktu yang ingin dikonversi.")

satuan_input_waktu = st.selectbox("Pilih satuan waktu", ("hari", "jam", "menit", "detik"))
waktu_input = st.number_input("Masukkan waktu: ", min_value=0.0, step=0.1)

waktu_detik = konversi_waktu(waktu_input, satuan_input_waktu)
if st.button("Hitung Konversi Waktu", key="button2"):
    if waktu_detik is not None:
        st.success(f"{waktu_input} {satuan_input_waktu} = {waktu_detik} detik")
    else:
        st.error("Satuan waktu tidak valid.")

st.write("__________________________________________________________")

st.write("Masukkan volume sungai yang sudah dikonversi ke meter dan masukkan waktu dalam satuan detik.")

panjang = st.number_input("Masukkan panjang sungai (m): ", min_value=0.0, step=0.1)
lebar = st.number_input("Masukkan lebar sungai (m): ", min_value=0.0, step=0.1)
kedalaman = st.number_input("Masukkan kedalaman sungai (m): ", min_value=0.0, step=0.1)
volume = panjang * lebar * kedalaman
waktu = st.number_input("Masukkan waktu (detik): ", min_value=0.0, step=0.1)

if st.button("Hitung Debit", key="button3"):
    debit = volume / waktu
    st.success(f"Hasil perhitungan Volume adalah {volume:.2f} m³")
    st.success(f"Hasil perhitungan Debit adalah {debit:.2f} m³/detik")
