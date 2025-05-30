class Product:
    def __init__(self,productId, productName, price):
        self.productId = productId
        self.productName = productName
        self.price = price
        print("Ürün oluşturuldu")
    def __len__(self):
        return len(self.price)
    def __str__(self):
        return f"Ürün ID: {self.productId}, Ürün Adı: {self.productName}, Fiyat: {self.price} TL"
    def __repr__(self):
         return f"Ürün ID: {self.productId}, Ürün Adı: {self.productName}, Fiyat: {self.price} TL"

    def __del__(self):
        print(f"{self.productName} ürünü silindi")
pr1=Product("2345","Kalem",10)
print(len(pr1.productName))
print(str(pr1))
print(repr(pr1))
del pr1