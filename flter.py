yaslar= [4,1,18,20,25,30,35,40,45,50,55,60]
isimler=["Ali","Veli","Ayşe","Fatma"]

kullanicilar=[{"isim":"Ali","yas":19,"sehir":"İstanbul"},{"isim":"Veli","yas":22,"sehir":"İstanbul"},{"isim":"Ayşe","yas":17,"sehir":"Ankara"},{"isim":"Fatma","yas":25,"sehir":"Ankara"}]
def yetiskin(x):
    if x <= 18:
        return True
    else:
        return False
sonuc= list(filter(yetiskin,yaslar))
sonuc =list(filter(lambda x: x>=18,yaslar))
sonuc= list(filter(lambda x: x%2==1,yaslar))
sonuc=list(filter(lambda x: x[0]=="A",isimler))
sonuc=list(filter(lambda x: x[0] in ["A","F","V"],isimler))
sonuc=list(filter(lambda x: x["yas"]>=18 and x["sehir"]=="İstanbul", kullanicilar))
sonuc=list(map(lambda x: x.capitalize(), filter(lambda x: x[0] in ["A","V"], isimler)))


user= [
{"isim":"Ali","post":[]},
{"isim":"Veli","post":["post1","post2"]},
{"isim":"Ayşe","post":["post1"]},
{"isim":"Fatma","post":["post1","post2","post3"]}
]

sonuc=list(filter(lambda u : len(u["post"])>=2, user))
sonuc= list(map(lambda u:u["isim"].upper(), filter(lambda u: len(u["post"])>=2, user)))
sonuc= [user["isim"]]
print(sonuc)