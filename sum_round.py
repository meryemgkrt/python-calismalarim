sayi= [5,4,12,14,25]

sonuc=sum(sayi,45)

urunler=[
    {"urun": "elma", "fiyat": 16},
    {"urun": "armut", "fiyat": 14},
    {"urun": "muz", "fiyat": 12},
    {"urun": "çilek", "fiyat": 14},
    
]
product=[
    {"ur1":"kitap", "quantity": 2},
    {"ur2":"kalem", "quantity": 3},
    {"ur3":"defter", "quantity": 4},
    {"ur4":"silgi", "quantity": 15},
    {"ur5":"kalemtraş", "quantity": 5},
]

sonuc=sum(urun["quantity"] for urun in product)
sonuc= round(1.658,2)
print(sonuc)