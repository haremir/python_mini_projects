import cv2, numpy as np

path="C:\\Users\\emirh\\Desktop\\opencv denemeler\\picture" #türkçe isim kullanınca hata alıyon
path_manzara = path + "\\manzara.jpg"
path_gri_manzara = path + "\\gri-manzara.jpg"
#sürekli yolu yazmamak için yolu path e atadım her resim için yeni değiken atayıp path + resmin adı yapıp onu okutucam

img1 = cv2.imread(path_manzara)
img2 = cv2.imread(path_gri_manzara)

assert not isinstance(img1,type(None))
assert not isinstance(img2,type(None))



print(img1.shape)
print(img2.shape)


img1 = cv2.resize(img1, (0,0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)

img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)

yatay = np.hstack(img1,img2)
dikey = np.vstack(img1,img2)

cv2.imshow("dikey",dikey)
cv2.imshow("yatay",yatay)

cv2.waitKey(0)
cv2.destroyAllWindows()