class Arabalar:
    def __init__(self, arabaId, marka,model,yil,price):
        self.arabaId = arabaId
        self.marka = marka
        self.model = model
        self.yil = yil
        self.price = price
    def __str__(self):
        return f"Araba ID: {self.arabaId}, Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}, Fiyat: {self.price} TL"
    def __repr__(self):
        return f"Arabalar({self.arabaId}, '{self.marka}', '{self.model}', {self.yil}, {self.price})"
    def __eq__(self, other):
        if isinstance(other, Arabalar):
            return (self.arabaId == other.arabaId and
                    self.marka == other.marka and
                    self.model == other.model and
                    self.yil == other.yil and
                    self.price == other.price)
        return False
    def __lt__(self, other):
        if isinstance(other, Arabalar):
            return self.price < other.price
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Arabalar):
            return self.price <= other.price
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Arabalar):
            return self.price > other.price
        return NotImplemented
araba1 = Arabalar(1, "Toyota", "Corolla", 2020, 200000)
araba2 = Arabalar(2, "Honda", "Civic", 2021, 220000)
print(araba1)
print(str(araba1))
print(repr(araba1))
print(str(araba2))
print(repr(araba2))
