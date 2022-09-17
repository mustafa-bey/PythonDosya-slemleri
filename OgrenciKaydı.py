def ortalama(satir):
    satir = satir[: - 1]
    liste = satir.split(' : ')
    ogrenci_adı=liste[0]
    notlar=liste[1].split(',')

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ort=(not3+not2+not1)/3

    if ort>90 and ort<=100:
        harf="AA"
    elif ort>85 and ort<=89:
        harf="BA"
    elif ort>80 and ort<=84:
        harf="BB"
    elif ort>75 and ort<=79:
        harf="CB"
    elif ort>70 and ort<=74:
        harf="CC"
    elif ort>65 and ort<=69:
        harf="DC"
    elif ort>60 and ort<=64:
        harf="DD"
    elif ort>50 and ort<=59:
        harf="FD"
    elif ort<=49:
        harf = "FF"

    return ogrenci_adı+ " : "+harf+"\n"

def ortalamalari_oku():
    file = open("sınav_sonucları.txt","r",encoding="utf-8")

    for i in file:
        print(ortalama(i))


def not_gir():
    ad=input("Öğrencı adı = ")
    soyad=input("Öğrencı soyadı = ")
    not1=input("Öğrencı 1.notu = ")
    not2=input("Öğrencı 2.notu = ")
    not3=input("Öğrencı 3.notu = ")

    with open("sınav_sonucları.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+" : "+not1+" "+not2+" "+not3+"\n")

def notları_kaydet():
    pass

while True:
    islem= input(" 1) Notları Okuyun\n "
                 "2) Notları Girin\n "
                 "3) Notları Kaydedin\n"
                 " 4) Çıkış Yapın \n")

    if islem=="1":
        ortalamalari_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notları_kaydet()
    else:
        break