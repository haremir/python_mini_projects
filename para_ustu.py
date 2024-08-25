import os
os.system("cls")

tutar = float(input("tutarı girin: "))
alinan = float(input("alınan para: "))
para_ustu = alinan - tutar
if para_ustu > 0:
    if para_ustu >= 100 and int(para_ustu) / 100 >= 1:
        print("{} adet yüzlük banknot ver.".format(int(para_ustu / 100)))
        para_ustu -= int(para_ustu / 100) * 100
    if para_ustu >= 50 and int(para_ustu) / 50 > 0:
        print("{} adet ellilik banknot ver.".format(int(para_ustu / 50)))
        para_ustu -= int(para_ustu / 50) * 50
    if para_ustu >= 20 and int(para_ustu) / 20 > 0:
        print("{} adet yirmilik banknot ver.".format(int(para_ustu / 20)))
        para_ustu -= int(para_ustu / 20) * 20

    if para_ustu >= 10 and int(para_ustu) / 10 > 0:
        print("{} adet onluk banknot ver.".format(int(para_ustu / 10)))
        para_ustu -= int(para_ustu / 10) * 10

    if para_ustu >= 5 and int(para_ustu) / 5 > 0:
        print("{} adet beşlik banknot ver.".format(int(para_ustu / 5)))
        para_ustu -= int(para_ustu / 5) * 5
    if para_ustu > 0:
        print("kalan para üstü: {}".format(para_ustu))
elif para_ustu == 0:
    print("iyi günler efendim")
elif para_ustu < 0:
    print("yetersiz bakiye")