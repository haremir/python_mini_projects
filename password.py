import os
import random
import time
os.system("cls")

password=""
character_pool = ("qwertyuopilkjhgfdsazxcvbnmQWERTYUPİLKJHGFDSAZXCVBNM1234567890,._<>!%#")

def password_genator():
    global password
    global character
    global character_pool

    len_passpword=int(input("how long should your password be? "))
    print("")
    if len_passpword < 6:
        print("dude pls create long password")
        print("you will back password generator pls wait..")
        time.sleep(1.5)
        print("")

    else:
        while len_passpword > 0:
            character = random.choice(character_pool)
            password += character
            len_passpword -= 1

        print("-"*50)
        print("Your Special password")
        print(password)
        print("")
        print("-"*50)

while True:
    password=""
    password_genator()
    dosya=open("passwords.txt","a")
    veri=password +"\n"
    dosya.write(veri)
    dosya.close