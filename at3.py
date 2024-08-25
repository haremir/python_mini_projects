import os
os.system("cls")

def max_subarray_n2(list, a):
    count = list[0] # sayaçımıza listemizin ilk elemanını atıyoruz

    for i in range(a): #listemizin uzunluğu kadar ilerlememizi sağlayacak
        mult = list[i] #listemizin ilk elemanını atıyoruz böylece en büyük değer karşılaştırması yapacağız 

        for j in range(i + 1, a):# listemizdeki her bir elemanı her biriyle kontrol etmemizi sağlayacak
            count = max (count, mult) # büyük olan değeri count değerine atıyoruz
            mult += list[j] # mult değişkenimizi listedeki sıradaki elemanla güncelliyoruz

        count = max(count, mult) # burada en büyük 2 değerimiz olmuş oljuyor büyük olanı counta atıyoruz

    return count    # en büyük değerimizi geri dönderiyoruz

def max_subarray_n3(list, a):
    count = list[0]# sayaçımıza listemizin ilk elemanını atıyoruz
    for i in range(a):# boş bir döngü ile zaman karmaşıklığımızı artırıyoruz

        for i in range(a):#listemizin uzunluğu kadar ilerlememizi sağlayacak
            mult = list[i]#listemizin ilk elemanını atıyoruz böylece en büyük değer karşılaştırması yapacağız 

            for j in range(i + 1, a):# listemizdeki her bir elemanı her biriyle kontrol etmemizi sağlayacak
                count = max (count, mult)# büyük olan değeri count değerine atıyoruz
                mult += list[j]# mult değişkenimizi listedeki sıradaki elemanla güncelliyoruz

            count = max(count, mult) # burada en büyük 2 değerimiz olmuş oljuyor büyük olanı counta atıyoruz

    return count    # en büyük değerimizi geri dönderiyoruz


list = [] # boş bir liste açıyoruz
a = int(input("diziye kaç değer eklemek istiyorsunuz? ")) # listemiz için uzunluk bilgisi alıyoryuz

for i in range(a): # listemize elemanları ekliyoruz
    temp = int(input(f"{i + 1}. değerinizi ekleyiniz: ")) # önce ara değere atıyoruz
    list.append(temp) # ara değerimizi listemize ekliyoruz

print("zaman karmaşıklığı n kare :",max_subarray_n2(list, a))#zaman karmaşıklığı n kare olan fonksiyonumuzu çağırıyoruz
print("zaman karmaşıklığı n küp  :",max_subarray_n3(list, a))#zaman karmaşıklığı n küp- olan fonksiyonumuzu çağırıyoruz

