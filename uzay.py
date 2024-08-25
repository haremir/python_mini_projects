"""
aşşağıdaki linkte json tipinde veri var biz bu veriyle oynadık
uzaydaki insan sayısını ve bun insanların bilgilerini çektik
"""

import os, requests
os.system("cls")

feedback = requests.get("http://api.open-notify.org/astros.json")
human = feedback.json()["number"]

print(f"şuan da uzayda {human} insan var")

print("uzayda ki insanların bilgileri:\n")

for i in feedback.json()["people"]:
    print(i["name"],"-----", i["craft"])
    