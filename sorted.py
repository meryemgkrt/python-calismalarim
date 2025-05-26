user= [
    {"isim":"Ali","post":[], "email":"ali@gmail.com"},
    {"isim":"Veli","post":["post1, post2"], "email":"veli@gmail.com"},
    {"isim":"Ahmet","post":["post1, post2,post3"], "email":"", "phone":"123456789"},
    
]

sonuc= sorted(user, key=len)
sonuc= sorted(user, key=len, reverse=True)
sonuc= sorted(user, key=lambda u:u["isim"])

araclar= [
    {"title":"Audi", "price":900000},
    {"title":"Mercedes", "price":1000000},
    {"title":"BMV", "price":1500000}
]
sonuc= sorted(araclar, key= lambda arac: arac["title"])
sonuc= sorted(araclar, key= lambda arac: arac["price"], reverse=True)
sonuc= sorted(araclar, key= lambda arac: arac["price"], reverse=False)
sonuc= list(map(lambda arac: arac["title"],sorted(araclar, key= lambda arac: arac["price"], reverse=True) ))


print(sonuc)