sayilar=[1,2,3,4,5,6,7,8,9,10]
harfler=["a","b","c","d","e","f","g","h","i","j"]
isimler=["muhendis","doktor","ogretmen","yazilimci","mimar"]
sonuc=max(isimler, key=len)
sonuc= [len(isim) for isim in isimler]
sonuc= min([len(isim) for isim in isimler])
sonuc= min(isimler, key=lambda isim: isim[0])


araclar= [
    {"title":"Audi", "price":900000},
    {"title":"Mercedes", "price":1000000},
    {"title":"BMV", "price":1500000}
]

sonuc= min(araclar, key=lambda a:a["price"])
sonuc= max(araclar, key=lambda a:a["price"])["title"]

sonuc=0

for i in araclar:
    if i["price"] > sonuc:
        sonuc=i["price"]
print(sonuc)