import os
os.system("cls")

#soru girilen kelimeyi istenildiği kadar ekrana yazdır
"""
word = input("ekrana gostermek istediginiz kelimeyi giriniz: ")
count = int(input("kac kez ekranda gosterimesini istiyorsunuz: "))

def loop(word,count):
    while count>0:
        print(word)
        count-=1
loop(word,count)
"""

# kendine gelen sınırsız parametereyi bir listede tutsun
"""
def linker(*params):
    list0 =[]
    for i in params: 
        list0.append(i)

    return list0

list1 = linker(5,9,34,82,8)
print(list1)
"""

#gönderilen 2 sayı arasından asal sayıalrı bul

def asal_founder(number1, number2):
    for number in range(number1, number2+1):
        if number > 1:
            for count in range(2,number):
                if number % count == 0:
                    break
                else:
                    print(number)


x=int(input("asal kontrol yapmak istediginiz 1. sayiyi giriniz: "))
y=int(input("asal kontrol yapmak istediginiz 2. sayiyi giriniz: "))
asal_founder(x,y)
