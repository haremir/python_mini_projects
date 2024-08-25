import os,time,string
os.system("cls")

alphabet=string.ascii_lowercase
key_number=int(input("anahtar sayı girin"))
def encryption():
    global encrypted_message

    message =input("şifrelenecek mesajınızı girin: ")
    encrypted_message=""
    
    messageLength = 0
    for i in message:
        if i not in alphabet:
            encrypted_message += i
        elif messageLength%2 == 0:
            encrypted_message += alphabet[(alphabet.index(i)+((key_number*11)//2)) % len(alphabet)]
        elif  messageLength%2 != 0:
            encrypted_message += alphabet[(alphabet.index(i)-((key_number*4)//3)) % len(alphabet)]
        messageLength += 1
    reverse_encrypted_message=encrypted_message[::-1]       
    print("şifreli mesajınız:",reverse_encrypted_message)


def analysis():
    reverse_encrypted_message=input("şifreli mesajı girin: ")
    encrypted_message =reverse_encrypted_message[::-1]
    message=""
    encryptedMessageLength = 0
    for i in encrypted_message:
        if i not in alphabet:
            message += i
        elif encryptedMessageLength%2 == 0:
            message += alphabet[(alphabet.index(i)-((key_number*11)//2)) % len(alphabet)]
        elif  encryptedMessageLength%2 != 0:
            message += alphabet[(alphabet.index(i)+((key_number*4)//3)) % len(alphabet)]
        encryptedMessageLength += 1

    print("çözümlenmiş mesajınız:",message)


while True:
    os.system("cls")
    print("şifreleme için 1'e bas\nçözümleme için 2'ye bas\nçıkış için 3'e bas")
    oparation=int(input("işlem: "))
    if oparation == 1:
        encryption()
        time.sleep(10)
        
    elif oparation == 2:
        analysis()
        time.sleep(10)
    elif oparation == 3:
        quit()
    else:
        print("lütfen geçerli bir işlem giriniz")
        
"""
bu kodun saf hali bozma sakın!!!
bozduysansa grupta alperen atmıştı ordan alırsın
ama bozma

"""