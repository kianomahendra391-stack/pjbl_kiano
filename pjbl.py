import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = ":fire:"
)

with st.sidebar:
    col1, col2, col3, = st.columns([1,2,1])
    with col2:
        st.image("RealMadrid.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi","Persegi Panjang","Lingkaran","Segitiga","Jajar Genjang"])
    st.caption("Dibuat dengan :fire: oleh **Kiano Mahendra**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung Luas dan Keliling Persegi")
        sisi=st.number_input("Masukkan Sisi Persegi")
        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung Luas dan Keliling Persegi Panjang")
        panjang = st.number_input("Masukkan Panjang Persegi Panjang")
        lebar = st.number_input("Masukkan Lebar Persegi Panjang")
        if st.button("Hitung", type):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi Panjang: {luas}")
            st.success(f"Keliling Persegi Panjang: {keliling}")
            st.snow()
    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung Luas dan Keliling Segitiga")
        alas = st.number_input("Masukkan Alas Segitiga")
        tinggi = st.number_input("Masukkan Tinggi Segitiga")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        if st.button("Hitung", type):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.success(f"Luas Segitiga: {luas}")
            st.success(f"Keliling Segitiga: {keliling}")
            st.snow()
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung Luas dan Keliling Lingkaran")
        jari_jari = st.number_input("Masukkan Jari-jari Lingkaran")
        if st.button("Hitung", type):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            st.success(f"Luas Lingkaran: {luas}")
            st.success(f"Keliling Lingkaran: {keliling}")
            st.snow()
    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung Luas dan Keliling Jajar Genjang")
        alas = st.number_input("Masukkan Alas Jajar Genjang")
        tinggi = st.number_input("Masukkan Tinggi Jajar Genjang")
        sisi_miring = st.number_input("Masukkan Sisi Miring") 
        if st.button("Hitung",type):
            luas = alas * tinggi
            Keliling = 2 * (alas + sisi_miring)
            st.success(f"Luas Jajar Genjang: {luas}")
            st.success(f"Keliling Jajar Genjang: {Keliling}")
            st.snow()       
    case _:
        st.error("Terjadi Kesalahan")      