sayilar = [1, 2, 3, 4, 5]

""" for i in sayilar:
    print(i)
print(dir(sayilar)) """
iterator = iter(sayilar)
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