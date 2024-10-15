import sys
import streamlit as st
st.title("Bankamatik")
st.write("Merhaba, bu benim ilk Streamlit uygulamam!")
mail_list=[
    {"isim":"Turker", "yas":"25", "yer":"ankara", "mail":"turker@hotmail.com", "sifre":"7253", "bakiye": 23500},
    {"isim":"Necip", "yas":"32", "yer":"istanbul", "mail":"necip@hotmail.com", "sifre":"4327", "bakiye": 188000},
    {"isim":"Dursun", "yas":"53", "yer":"izmir", "mail":"dursun@hotmail.com", "sifre":"1098", "bakiye": 1550000}
]
y=0
mail=input("Lütfen mail adresinizi giriniz: ")
sifre=input("Lütfen şifrenizi giriniz: ")
listgiris=[mail,sifre]
deneme=3
while True: 
    for kullanıcı in mail_list:
        if mail==kullanıcı["mail"] and sifre==kullanıcı["sifre"]:
            st.write("\nHoş geldiniz {} ".format(kullanıcı["isim"]))
            y=1
            break
    if y==1:
        break
   
    deneme-=1
    st.write(f"{deneme} deneme hakkınız kalmıştır.")
    st.write("Lütfen tekrar deneyiniz. ")
    mail=input("Lütfen mail adresinizi giriniz: ")
    sifre=input("Lütfen şifrenizi giriniz: ")
    if deneme==1:
        st.write("Başarısız giriş yaptınız.")
        sys.exit()
    
 #%%           
islem=int(input("\nLütfen yapmak istediğiniz işlem numarasını giriniz. \n1-Para Çekme\n2-Para Yatırma\nNo:"))
if islem==1:
    st.write("\nBakiyeniz {} Türk Lirasıdır.".format(kullanıcı["bakiye"]))
    cekme=int(input("\nLütfen çekmek istediğiniz nakit tutarı giriniz: "))
    while cekme>kullanıcı["bakiye"]:
        st.write("\nLütfen çekmek istediğiniz nakit miktarı, bakiyenizi geçmesin.")
        cekme=int(input("\nLütfen çekmek istediğiniz nakit tutarı giriniz: "))
    st.write(f"\n{cekme} Türk lirasını alabilirsiniz.")
    kullanıcı["bakiye"]=kullanıcı["bakiye"]-cekme
    st.write("\nKalan bakiyeniz: {} Türk lirasıdır".format(kullanıcı["bakiye"]))
    st.write("\nİyi günler dileriz.")
    
elif islem==2:
    st.write("\nBakiyeniz {} Türk Lirasıdır.".format(kullanıcı["bakiye"]))
    
    yatırma=int(input("\nLütfen yatırmak istediğiniz nakit tutarı giriniz: "))
    
    st.write(f"\n{yatırma} Türk lirasını lütfen hazneye yerleştiriniz.")
    
    kullanıcı["bakiye"]=kullanıcı["bakiye"]+yatırma
    st.write("\nBakiyeniz: {} Türk lirası olacak şekilde güncellenmiştir".format(kullanıcı["bakiye"]))
    
    st.write("\nİyi günler dileriz.") 
