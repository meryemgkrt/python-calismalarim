""" class Product:
    def __init__(self,name,price,isActive=True):
        self.name= name
        self.price= price
        self.isActive= isActive
        print("Product created:", self.name, self.price)
p1=Product("Laptop"," 1500")
p2=Product("Phone"," 800", False)
p3=Product("Tablet"," 600")
print(p1.name, p1.price, p1.isActive)
print(p2.name, p2.price, p2.isActive)
print(p3.name, p3.price, p3.isActive) """

class Urun:
    def __init__(self, ad,fiyat, aktif=True):
        self.ad = ad
        self.fiyat = fiyat
        self.aktif = aktif
        print("Urun olusturuldu:", self.ad, self.fiyat)
urun1 = Urun("Laptop", "1500")
urun2 = Urun("Telefon", "800", False)
urun3 = Urun("Tablet", "600")
print(urun1.ad, urun1.fiyat, urun1.aktif)
print(urun2.ad, urun2.fiyat, urun2.aktif)
print(urun3.ad, urun3.fiyat, urun3.aktif)
