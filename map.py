sayilar=[-10,-2,3,-4,5,6,7,8,9]
sayilar_str=["10","2","3","4","5","6","7","8","9"]
isimler=["Ali","Veli","Ayşe","Fatma"]
kullanicilar= [
    {"ad":"Ali","yas":25,"sehir":"İstanbul"},
    {"ad":"Veli","yas":30,"sehir":"Ankara"},
    {"ad":"Ayşe","yas":28,"sehir":"İstanbul"},
    {"ad":"Fatma","yas":32,"sehir":"Bursa"}
]
kareleri=[]

for sayi in sayilar:
    kareleri.append(sayi**2)
""" print(kareleri) """

def kare_al(sayi):
    return sayi**3
küpleri=list(map(kare_al,sayilar))
küpleri= list(map(lambda x:x**3,sayilar))

sonuc=list(map(int,sayilar_str))
sonuc=list(map(abs,sayilar))
sonuc =list(map(float,sayilar))
sonuc=list(map(str.capitalize,isimler))
sonuc= list(map(str.upper,isimler))
sonuc=list(map(len,isimler))
sonuc= list(map(lambda x: x["ad"] + " " + str(x["yas"]) + " " + x["sehir"], kullanicilar))

print(sonuc)