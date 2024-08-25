import os
os.system("cls")

#dizi aç boyutunu kullanıcıdan al diziyi kullanıcıdan doldur

#kullanıcıdan dizi boyutu alıyoruz.

size = int(input("please enter the list size: "))
print("") # terminal ekranında karışıklığı gidermek için
my_list = [] # boş bir liste tanımlıyoruz


i = 0
while i<size:
    crew = int(input(f"please enter the {i}. crew: "))
    my_list.append(crew)
    i+=1
#burada dizi boyutumuzu aldık ve içerisini doldurduk

def insertion_sort():
    for i in range(1, len(my_list)): #burada 1'den listeimizin uzunluğuna kadar giden bir for döngüsü kurduk
        for j in range(i - 1, -1, -1): #i'nin bir eksiğinden -1 e kadar birer birer giden bir döngü kurduk 
            if(my_list[j] > my_list[j + 1]): #burada listemizin ilk elemanı sonraki elemanından büyük mü diye kontrol ettik
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j] #burada iki değerin yerini değiştirmiş 
                #olduk böylece ilk eleman ikinci oldu, ikinci eleman birinci oldu


    print(my_list)#listemizi yazdırdık



def merge_sort(my_list):
    size = len(my_list) #rekürsifle yoladığımız her listenin boyutunu ölçüyoruz altaki if bloğuna girip giremeyeceğini kontrol etmek için
    if size > 1: 
        middle = size // 2
        left_list = my_list[:middle] #0.indexten middle değerine kadar olan değerleri left_liste atadık
        right_list = my_list[middle:]# middle değerinden son değere kadar olan değerleri right_liste atadık
 
        merge_sort(left_list)
        merge_sort(right_list)
        #burada diziyi 2 li eleman kalana kadar rekürsif yöntemiyle parçalıyoruz

        l_crew, r_crew, m_crew = 0, 0, 0 # sol sağ ve benim listem için 0 dan başlayan index değerleri atıyorum
         
        left_size = len(left_list)
        right_size = len(right_list)
        while l_crew < left_size and r_crew < right_size: #soldaki eleman soldaki dizinin uzunluğunudan ve sağdaki eleman sağdaki dizinin
                                                          #uzunluğundan küçük mü diye kontrol ediyoruz
    
            if left_list[l_crew] < right_list[l_crew]: #soldaki dizinin küçük olan elemanı sağdakinden de küçük mü diye kontrol ediyoz
              my_list[m_crew] = left_list[l_crew] #ana listemizin ortanca değerini soldaki listemizin küçük değeri yapıyoruz
              l_crew += 1 #sol listenin indexini bir artırıyoruz
            else: # eğer yukaradaki durumun tam tersi ise 
                my_list[m_crew] = right_list[r_crew] #ana listemizin ortanca değerini sağdaki listemizin küçük değeri yapıyoruz
                r_crew += 1 # sağ listemizin indexini bir artırıyoruz
             
            m_crew += 1 # ana listemizin ortanca değerini döngüdeki her tur için birer birer artmasını sağlıyoruz böylece diğer dizileri de  
                        # kontrol edebilicez
    
 
        
        while l_crew < left_size: # solda ki eleman sol dizinin boyutundan küçük olduğu sürece çalışır
            my_list[m_crew] = left_list[l_crew] # listemizin ortanca elemanınını soldaki listemizin soldaki elemanına atıyoruz
            l_crew += 1 # sol indexi 1 arttırıyoruz
            m_crew += 1 # bizim listemizin indexini 1 arttırıyoruz
 
        while r_crew < right_size: #sağda ki eleman sağ dizinin boyutundan küçük olduğu sürece çalışır
            my_list[m_crew]=right_list[r_crew] # listemizin ortanca elemanınını sağdaki listemizin sağdaki elemanına atıyoruz
            r_crew += 1 # sağ indexi 1 arttırıyoruz
            m_crew += 1 # bizim listemizin indexini 1 arttırıyoruz

print("-"*25 ,"\nINSERTION SORT") # göresllik için
insertion_sort() # insertion sort fonksiyonunu çağırıyoruz
print("-"*25 ,"\nMERGE SORT") # göresllik için
merge_sort(my_list) # göresllik için
print(my_list) # merge sortu çağırıyoruz
print("-"*25) # göresllik için

