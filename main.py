# " w " : ( Write ) yazma modu . Dosyayı konumda oluşturur .
# " a " : ( Append ) ekleme . Dosya konumda yoksa oluşturur .
# " x " : ( Create ) oluşturma . Dosya zaten varsa hata verir .
# " r " :  ( Read ) okuma . varsayılan . dosya konumda yoksa hata verir
"""
file = open ( " newfile.txt","a",encoding='utf-8')

file.write("\nmustafa bey 2\n")
file.close()

"""
"""

file = open("text.txt","x")
file.close()

"""

"""
file = open("deneme.txt","r",encoding="utf-8")
print(file)

for i in file:
    print(i)

file.close()

"""
"""
file = open("deneme.txt","r",encoding="utf-8")

a= file.read()
print(a)

file.close()

"""
"""
file = open("deneme.txt","r",encoding="utf-8")

a= file.read(9)
print(a)

print(file.readline()) #her calıstıgında bir satır okur

"""










"""




file = open("newfile1.txt","r",encoding="utf-8")

countent=file.read()
file.close()

with open("newfile1.txt","r",encoding="utf-8") as file:  #with kullanımı ile dosya kapatmaya gerek yoktur
    countent = file.read()
    countent=file.read()



"""

