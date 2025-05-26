""" sonuc= any([True, False, True])
print(sonuc)
sonuc= all([True, False, True])
print(sonuc) """


sayilar=[0,1,2,3,4,5,6,7,8,9]

sonuc=any(bool(sayi) for sayi in sayilar)
sonuc=all(bool(sayi) for sayi in sayilar if sayi>0)
sonuc=all([sayi%2==0 for sayi in sayilar if sayi%2==0])

isimler=["Ali","Veli","Ayşe","Fatma"]
sonuc=[isim[0]=="A" for isim in isimler]
sonuc=any([isim[0]=="G" for isim in isimler])

print(sonuc) # True