""" diller =[ "Python", "C", "C++", "Java" ]

index =0
for i in diller:
    print (f"{index} .{i}")
    index +=1 """

ogrenciler =[ "Ali", "Veli", "Ayşe", "Fatma" ]
index = 0
""" index = 0

for i in ogrenciler:
    print(f"{index+1} : {i}")
    index += 1 """
""" 
obje = enumerate(ogrenciler)
print(type(obje))
print(list(obje)) """

sayilar =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

""" no =enumerate(sayilar)
print(list(no))
print(type(no)) """

for index,value in enumerate(ogrenciler):
    print(f"{index+1} - {value}")



