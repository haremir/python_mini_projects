import os #projede kullanılan kütüphaneler
import random 
os.system("cls")# bir önceki çalışmanın çıktılarını terminalden siler


def random_search(target):#aranan değeri parametre olarak gönderiyoruz
    for i in range(len(table)+3):#sütun üzerinde geziniyoruz     
        for j in table :#satır üzerinde geziniyoruz            
            if j[i] == target:#tablo üzerinde bulunduğumuz değer hedefle eşleşiyormu diye kontrol ediyoruz
                print(f"{counter+1}. tur {target} aranan sayımız.")
                #eşleşiyorsa eğer tur sayımızı ve aranan sayımızı ekrana basıyoruz
                print(j[i],"aranan değer bulunmuştur!") #aranan değer bulundu çıktısı veriyoruz
                print(f"satır değeri {table.index(j)}\nsütun değeri {i}") # satır ve sütun konumlarını ekrana basıyoruz
                print("-"*35)#döngüdeki görsel karmaşıklığı gidermek için 



def repeat_number_count(repeat_value):# paremetre olarak aranacak olan tekrarlı değeri gönderiyoruz
    repeat_value_counter = 0 #sayaç açıyoruz
    for i in range(len(table)+3):#sütun üzerinde geziniyoruz
        for j in table :#satır üzerinde geziniyoruz
            if repeat_value == j[i]:#kontrol ettiğimiz değer tabloda var mı diye kontrol ediyoruz
                repeat_value_counter += 1#varsa sayacı 1 arttırıyoruz
    print(f"{repeat_value} değerinden {repeat_value_counter} kadar var ")
    #aranan değerimizden kaç tane olduğu ekrana bastırıyoruz


def picking_random_element_table():
    
    for i in range(0,50): # 50 kez random seçim yapmak istiyoruz
        random_x = random.choice(table)# rastgele bir satır seçiyoruz
        random_value = random.choice(random_x)# seçilen rastgele bir satırdan bir değer seçiyoruz
        random_list.append(random_value)#seçilen random değerimizi boş bir listeye atıyoruz



def average(vektor): 
# Random list imizi fonksiyona parametre olarak gönderiyoruz ve rahat kullanmak üzere vektör olarak tanımlıyoruz
    data_count = len(vektor)# vektör listesinn uzunluğunu alıyoruz
    if data_count <= 1:# listemizin uzunluğu eğer 1 veya 1'den küçük mü diye kontrol ediyoruz
        return vektor #vektörü döndürüyoruz
    else: # 1'den büyük ise vektörün toplam rakamlarını adede bölerek ortalamayı buluyoruz..							
        return sum(vektor) / data_count



def standard_deviation(vektor):	
    #Random list imizi fonksiyona parametre olarak gönderiyoruz ve rahat kullanmak üzere vektör olarak tanımlıyoruz
    sd = 0.0  #For döngüsünde değer alabilmesi için “sd” adlı float bir değişken yaratıyoruz...
    data_count = len(vektor)
    if data_count <= 1:	#datacount 1 den küçük veya eşit mi diye kontrol ediyoruz
        return 0.0 #“if” bloğunda eğer veri adedi 1 veya 1'den küçük ise standart sapma 0 olarak döner.

    else:
    #“Else” de for döngüsü ile her bir değişken alınır float’a dönüştürülüp listemizin 
    # ortalamasından çıkarıldıktan sonra karesi alınarak “sd” değişkenindeki değer ile toplanır.
        for _ in vektor:
            sd += (float(_) - average(vektor)) ** 2  #ortalama alınırken yukarıdaki (def average) fonksiyonunu kullandık.
        sd = (sd / float(data_count)) ** 0.5 # Geriye kalan matematiksel işlemler yapılarak standart sapma bulunur.
        return sd


table =[[10 ,30 ,45 ,50 ,58 ,71 ,79 ,86 ,89 ,93 ,99 ,107,112],
        [13 ,34 ,48 ,66 ,69 ,78 ,85 ,88 ,94 ,96 ,100,115,118], 
        [15 ,44 ,51 ,67 ,72 ,83 ,87 ,91 ,97 ,103,105,117,121], 
        [17 ,46 ,53 ,70 ,74 ,84 ,90 ,93 ,98 ,104,109,120,189], 
        [23 ,55 ,64 ,77 ,81 ,93 ,101,111,116,122,130,147,201], 
        [37 ,65 ,73 ,80 ,82 ,106,110,119,125,129,152,169,205], 
        [39 ,68 ,76 ,102,108,113,114,124,131,137,161,178,210],
        [40 ,93 ,123,126,140,144,148,150,157,160,162,202,267],
        [43 ,128,133,135,149,164,166,171,177,183,192,204,301],
        [400,500,600,700,800,900,901,902,903,904,905,906,909]]
        #2 boyutlu arama tablomuz

random_list = [] #boş bir liste oluşturduk böylece random sayılarımızı burda tutabiliriz
search_list=(30,107,51,93,162,123,111,134,300) # arama tuple ı oluşturduk



for counter in range(0,50):#50 kez tekrarlanmasını istiyoruz
    target = random.randint(0,1000)#0 ile 1000 arasında değer seçiyoruz random olarak
    random_search(target)#hedefimizin listede olup olmadığına bakıyoruz


for repeat_value in search_list: #arama listesi üzerinde geziniyoruz
    repeat_number_count(repeat_value)
    #arama listesindeki değerlerin tekrarlanma sayılarının hesaplıyoruz


picking_random_element_table()#tablodan 50 tane rastgele değer seçiyoruz
print("-"*35)#görsellik için
print(standard_deviation(random_list))#random alınan sayıların standart sapmasını hesaplıyoruz 
print(average(random_list))#random alınan sayıların ortalaması
