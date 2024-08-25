from random import random
x= int(random() * 100)
while True:
    sayi= int(input("bir sayı tahmin et: "))
    if sayi == x:
        print("heyt bee münnecim mübarek münneccim")
        break
    elif sayi > x:
        print("indir onu yiğidim indir")
    elif sayi < x:
        print("niye öyle diyorsunuz beyfendi! Alındım, gücendim sen biraz daha yükselt onu")
    else: 
        print("1 ile 100 arasında tutucan yiğido")