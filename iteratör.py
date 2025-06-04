sayilar = [1, 2, 3, 4, 5]

""" for i in sayilar:
    print(i)
print(dir(sayilar)) """
""" iterator = iter(sayilar)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
isimler=["Ahmet", "Mehmet", "Ayşe", "Fatma"]
iteratör_adlar=iter(isimler)
while True:
    try:
        print(next(iteratör_adlar))
    except StopIteration:
        break
    
ogrenciler= [
    {"isim": "Ali", "notlar": [90, 85, 88]},
    {"isim": "Ayşe", "notlar": [95, 80, 78]},
    {"isim": "Mehmet", "notlar": [70, 75, 80]}
]
iteratör_ogrenciler=iter(ogrenciler)
while True:
    try:
        ogrenci = next(iteratör_ogrenciler)
        print(f"Öğrenci: {ogrenci['isim']}, Notlar: {ogrenci['notlar']}")
    except StopIteration:
        break """
    
arabalar=[
    {"marka": "Toyota", "model": "Corolla", "yil": 2020},
    {"marka": "Honda", "model": "Civic", "yil": 2019},
    {"marka": "Ford", "model": "Focus", "yil": 2021}
]
iteratör_arabalar=iter(arabalar)
while True:
    try:
        araba = next(iteratör_arabalar)
        print(f"Araba: {araba['marka']} {araba['model']}, Yıl: {araba['yil']}")
    except StopIteration:
        break