import streamlit as st

# Başlık
st.title("Bankamatik")

# Kullanıcı verileri
mail_list = [
    {"isim": "Turker", "yas": "25", "yer": "ankara", "mail": "turker@hotmail.com", "sifre": "7253", "bakiye": 23500},
    {"isim": "Necip", "yas": "32", "yer": "istanbul", "mail": "necip@hotmail.com", "sifre": "4327", "bakiye": 188000},
    {"isim": "Dursun", "yas": "53", "yer": "izmir", "mail": "dursun@hotmail.com", "sifre": "1098", "bakiye": 1550000}
]

# Giriş işlemleri
deneme = 3

while True:
    mail = st.text_input("Lütfen mail adresinizi giriniz: ", "")
    sifre = st.text_input("Lütfen şifrenizi giriniz: ", "", type="password")

    if st.button("Giriş Yap"):
        y = 0
        for kullanıcı in mail_list:
            if mail == kullanıcı["mail"] and sifre == kullanıcı["sifre"]:
                st.success(f"Hoş geldiniz {kullanıcı['isim']}")
                y = 1
                break

        if y == 1:
            break
        else:
            deneme -= 1
            st.warning(f"{deneme} deneme hakkınız kalmıştır.")
            if deneme == 0:
                st.error("Başarısız giriş yaptınız.")
                st.stop()  # Uygulamayı durdur

# İşlem seçimi
islem = st.selectbox("Lütfen yapmak istediğiniz işlem numarasını seçiniz:", ["Para Çekme", "Para Yatırma"])

kullanıcı = next(k for k in mail_list if k["mail"] == mail)  # Giriş yapan kullanıcı bilgilerini al

if islem == "Para Çekme":
    st.write(f"\nBakiyeniz: {kullanıcı['bakiye']} Türk Lirasıdır.")
    cekme = st.number_input("Lütfen çekmek istediğiniz nakit tutarını giriniz:", min_value=0)

    if st.button("Para Çek"):
        if cekme > kullanıcı["bakiye"]:
            st.warning("Lütfen çekmek istediğiniz nakit miktarı, bakiyenizi geçmesin.")
        else:
            kullanıcı["bakiye"] -= cekme
            st.success(f"{cekme} Türk lirasını alabilirsiniz.")
            st.write(f"Kalan bakiyeniz: {kullanıcı['bakiye']} Türk lirasıdır.")
            st.info("İyi günler dileriz.")

elif islem == "Para Yatırma":
    st.write(f"\nBakiyeniz: {kullanıcı['bakiye']} Türk Lirasıdır.")
    yatırma = st.number_input("Lütfen yatırmak istediğiniz nakit tutarını giriniz:", min_value=0)

    if st.button("Para Yatır"):
        kullanıcı["bakiye"] += yatırma
        st.success(f"{yatırma} Türk lirasını lütfen hazneye yerleştiriniz.")
        st.write(f"Bakiyeniz: {kullanıcı['bakiye']} Türk lirası olarak güncellenmiştir.")
        st.info("İyi günler dileriz.")
