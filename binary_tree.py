import os
os.system("cls")

#200303006 Harun Emirhan BOSTANCI
#200303047 Enes Fatih TAŞTAN

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def insert(root, key):
    if root is None:
        return Node(key)

    else:
        if root.data == key:
            return
        elif root.data > key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def  inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def height(root):
 
    if root is None:
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    return max(leftAns, rightAns) + 1


#sayaç tut sayaç sıfır ise bu kök
#sayaç sayesinde kaçıncı katmanda olduğumuzu görebilicez

backup_list = []
count = 0
var = True
while var:
    print("-"*35)
    print(" binary search tree programı\n",
          "ağacınızın derinliğini görmek için '-1' değerini tuşlamayı unutmayın\n",
          "ağaca eklemeyi bitirmek için '0' rakamına basınız.")

    key = int(input(" eklemek istediğiniz değeri giriniz:  "))
    
    
    for i in backup_list:
        if i == key:
            print("eklenmek istenen numara hali hazırda eklenmiştir tekrar ekleme yapılmayacaktır! ")
            var = False
            insert(root, key)
    if key == -1:
        print("yüksekliğiniz: ", height(root)) 

    elif key == 0:
        print("-"*35,"\nBinary Tree ")
        inorder(root)  
    
    else:
        if count == 0:
            root = Node(key)
            backup_list.append(key)
            count += 1
        else:
            insert(root, key)  
            backup_list.append(key)  



print(backup_list)
# diziye aktar her eklemek istediğimiz elemanı ayrı bir dizide tut öncesinde dizide dön varsa uyarı ver mesaja tura devam ettir countine ile
#
