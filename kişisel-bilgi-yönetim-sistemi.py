# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:39:06 2024

@author: Atakan
"""

kullanicilar={}
def bilgi_ekle():
    ad=input("lütfen isminizi giriniz:")
    soyad=input("lütfen soyadınızı giriniz:")
    yas=input("lütfen yaşınızı giriniz:")
    eposta=input("lütfen eposta adresininizi giriniz:")
    telno=input("lütfen telefon numaranızı giriniz:")

    kullanici={"ad":ad,"soyad":soyad,"yas":yas,"eposta":eposta,"telno":telno}

    kullanicilar[ad] = kullanici
    print(f"{ad} {soyad} kullanıcılar bölümüne eklenmiştir")

def bilgi_guncelle():
    while True:
        ad=input("lütfen bilgilerini güncellemek istediğiniz kullanıcının ismini giriniz:")
        if ad not in kullanicilar:
            print(f"{ad} isminde bir kullanıcı bulunmamaktadır")
        else:
            break
    print("1.Yaşını güncelle")
    print("2.E-posta adresini güncelle")
    print("3.Telefon numarasını güncelle")

    secim=input("lütfen güncellemek istediğin bilgi seçiniz:(1-3)")

    if secim=="1":
        yeni_yas=input("lütfen kullanıcının yeni yaşını giriniz:")
        kullanicilar[ad]["yas"]=yeni_yas
        print(f"{ad} isimli kullanıcının yaşı güncellenmiştir")
    elif secim=="2":
        yeni_eposta=input("lütfen kullanıcının yeni e-posta adresini giriniz:")
        kullanicilar[ad]["eposta"]=yeni_eposta
        print(f"{ad} isimli kullanıcının e-postası güncellenmiştir")
    elif secim=="3":
        yeni_telno=input("lütfen kullanıcının yeni telefon numarasını giriniz:")
        kullanicilar[ad]["telno"]=yeni_telno
        print(f"{ad} isimli kullanıcının telefon numarası güncellenmiştir")
    else:
        print("girdiğiniz isimde bir kullanıcı bulunmamaktadır")

def bilgi_sil():
    ad=input("lütfen bilgilerini silmek istediğiniz kullanıcının ismini giriniz:")

    if ad in kullanicilar:
        del kullanicilar[ad]
        print(f"{ad} isimli kullanıcı ve bilgileri silindi")

def bilgi_goruntule():
    if not kullanicilar:
        print("herhangi bir kullanıcı bilgisi bulunamadı")

    else:
        for key,value in kullanicilar.items():
            print(f"kullanici bilgileri:{kullanicilar}")

while True:
    print("1.Kullanıcı bilgileri ekleme:")
    print("2.Kullanıcı bilgi güncelleme")
    print("3.Kullanıcı bilgi silme")
    print("4.Kullanıcı bilgileri görüntüleme")
    print("5.Çıkış")

    secim=input("lütfen seçiminizi yapınız:(1-5)")

    if secim=="1":
        bilgi_ekle()
    elif secim=="2":
        bilgi_guncelle()
    elif secim=="3":
        bilgi_sil()
    elif secim=="4":
        bilgi_goruntule()
    elif secim=="5":
        print("Çıkış yapılıyor..")
        break
