import os
os.system("cls")
def vize_ort():
    global vize_ortalaması #fonksiyon dışında kullanabilmen için gerekiyor
    vize_sayisi = int(input("kaç vizeye girdin: "))
    toplam_not = 0 
    for i in range(vize_sayisi):
        vize_not = int(input(f"{i+1}. vizeden kaç aldın: "))
        toplam_not +=vize_not#i artıyor ve her seferinde kaç aldığını soruyor en sondada toplam notda topluyor hepsini 
    vize_ortalaması = toplam_not / vize_sayisi
    print("vize ortalaman " f"{vize_ortalaması}" )
vize_ort() # bu fonksiyonu bitiriyor   
final = int(input("Finalden kaç aldın : "))
#oğuzdan aldım
def quiz_ort():
    global quiz_ortalaması #fonksiyon dışında kullanabilmen için gerekiyor
    quiz_sayisi = int(input("kaç quize girdin: "))
    toplam_not = 0 
    for i in range(quiz_sayisi):
        quiz_not = int(input(f"{i+1}. quizden kaç aldın: "))
        toplam_not +=quiz_not#i artıyor ve her seferinde kaç aldığını soruyor en sondada toplam notda topluyor hepsini 
    quiz_ortalaması = toplam_not / quiz_sayisi
    print("quiz ortalaman " f"{quiz_ortalaması}" )
quiz_ort()    # bu fonksiyonu bitiriyor 
#oğuzdan aldım
#bunu kendim yaptım ama oğuzunki ile aynı mantık
def ödev_ort():
    global ödev_ortalaması#fonksiyon dışında kullanabilmen için gerekiyor
    ödev_sayisi = int(input("kaç tane ödev yaptın: "))
    toplam_not = 0
    for j in range (ödev_sayisi):
        ödev_not = int(input(f"{j+1}. ödevden kaç aldın: "))
        toplam_not += ödev_not#i artıyor ve her seferinde kaç aldığını soruyor en sondada toplam notda topluyor hepsini 
    ödev_ortalaması = toplam_not / ödev_sayisi
    print("ödev ortalaman " f"{ödev_ortalaması}" )
ödev_ort() # bu fonksiyonu bitiriyor   
#bunu kendim yaptım ama oğuzunki ile aynı mantık
#burda oranları kullanıcının belirlemesine çalıştım
vize_etkisi = float(input("vizelerin ganoyu yüzde kaç etkiliyor: "))
vize_etkisi /= 100
final_etkisi = float(input("finallerin ganoyu yüzde kaç etkiliyor: "))
final_etkisi /= 100
quiz_etkisi = float(input("quizlerin ganoyu yüzde kaç etkiliyor :"))
quiz_etkisi /= 100
ödev_etkisi = float(input("ödevlerin ganoyu yüzde kaç etkiliyor: "))
ödev_etkisi /= 100
#burda oranları kullanıcının belirlemesine çalıştım
#bilgisayar programlama gano hesaplaması

gano = float(vize_ortalaması*vize_etkisi + final*final_etkisi + quiz_ortalaması*quiz_etkisi + ödev_ortalaması*ödev_etkisi )
gano /= 25
#kalıp kalmadığını belirten kod
print(f"{gano:0.3} ganoya sahipsin")
if gano >= float(2):
    print("geçtiniz")
else :
    print("kaldınız")
#kalıp kalmadığını belirten kod