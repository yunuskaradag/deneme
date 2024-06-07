import streamlit as st
import pandas as pd

# Sayfa yapılandırması
st.set_page_config(page_title='Data Visualizer', layout='centered', page_icon='📊')

# Başlık
st.title('📊 Data Visualizer')

# CSV dosyası yükleme
uploaded_file = st.file_uploader("CSV dosyasını yükleyin", type=["csv"])

if uploaded_file is not None:
    # CSV dosyasını okuma
    df = pd.read_csv(uploaded_file)

    st.write("Yüklenen Veri")
    st.write(df)

    # İşlem butonu
    if st.button("Başlat"):
        # Verileri işlem
        grouped_df = df.groupby('müşteri')['satış_tutarı'].sum().reset_index()

        st.write("İşlenen Veri")
        st.write(grouped_df)

        # Excel dosyasını indirme
        output = pd.ExcelWriter("sonuc.xlsx", engine='openpyxl')
        grouped_df.to_excel(output, index=False, sheet_name='Sonuçlar')
        output.save()

        # Excel dosyasını kullanıcıya sunma
        with open("sonuc.xlsx", "rb") as file:
            btn = st.download_button(
                label="Excel Dosyasını İndir",
                data=file,
                file_name="sonuc.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
