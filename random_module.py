""" import random 
sonuc=dir(random)
sonuc=random.random()
sonuc=random.random()*10
sonuc=int(random.uniform(10,100))
sonuc=random.randint(1,100)
user= ["ali","ayşe","ahmet","fatma", "mehmet"]
sonuc=user[random.randint(0,len(user)-1)]
sonuc=random.choice(user)
liste= list(range(1,11))
sonuc=liste
liste=range(100)

sonuc=random.sample(liste,3)
sonuc=random.sample(user,4)
print(sonuc) # random modülündeki tüm fonksiyonları ve değişkenleri listele """

from datetime import datetime

sonuc =dir(datetime)
sonuc = datetime.now()
sonuc = datetime.today()
sonuc =datetime.today().strftime("%Y-%m-%d %H:%M:%S")
sonuc= datetime.now().minute
sonuc= datetime.now().hour
sonuc=datetime.now().day
sonuc=datetime.now().month
sonuc=datetime.now().year
sonuc=datetime.now().second
sonuc = datetime.ctime(datetime.now())
from datetime import datetime

sonuc = datetime.now().strftime("%X")
sonuc = datetime.now().strftime("%d/%m/%Y")
sonuc = datetime.now().strftime("%A/%d/%m/%Y")



""" birthday = datetime(1986, 1, 1)  # Doğum yılına ek olarak ay ve gün de belirtmemiz gerekiyor
bugun = datetime.now()

yas = bugun.year - birthday.year """

""" # Eğer doğum günü henüz gelmemişse, yaştan 1 çıkarıyoruz
if (bugun.month, bugun.day) < (birthday.month, birthday.day):
    yas -= 1 """

""" 
dogumGunu= datetime(1987, 1, 1)  
bugun= datetime.now()
yas=bugun.year - dogumGunu.year
print(yas) """

""" from datetime import datetime, timedelta

simdi = datetime.now()
sonuc= simdi + timedelta(100)
sonuc = simdi + timedelta(days=100, minutes=20)
sonuc = simdi - timedelta(days=100, minutes=20)

print(sonuc) """

import os

""" sonuc = dir(os)
sonuc= os.name """
""" os.chdir("..") """
""" os.chdir("D:\\") """
""" os.mkdir("deneme") """
""" os.makedirs("deneme/deneme2") """
""" os.rename("deneme","dn") """
""" sonuc= os.getcwd()
print(sonuc) """

""" sonuc=os.listdir("//Users")
print(sonuc) """

""" sonuc = os.listdir("/Users")
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya) """
        
        
""" sonuc=os.listdir("C:\\")
print(sonuc) """

""" sonuc=os.listdir("/Users")
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya) """    
        
sonuc=os.stat("random_module.py")
sonuc=sonuc.st_size/1024
print(sonuc)