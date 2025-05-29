""" class Hayvan:
    def __init__(self,isim):
        self.isim=isim
    def __ses(self):
        print(f"{self.isim} ses çıkarıyor")
        
class Köpek(Hayvan):
        def ses(self):
            print(f"{self.isim} havlıyor")
class Kedi(Hayvan):
        def ses(self):
            print(f"{self.isim} miyavlıyor")
            
köpek=Köpek("Karabaş")
kedi=Kedi("Pamuk")

köpek.ses()
kedi.ses()
         """
         
class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("personel oluşturuldu")
    def info(self):
        print(f"{self.name} {self.surname}, {self.age} yaşında bir personel")
        
class Student(Person):
    def __init__(self,name,surname,age,number):
        super().__init__(name,surname,age)
        self.number = number
        
        print("öğrenci oluşturuldu")
    def ortalam_al(self):
        print(f"{self.number} numaralı öğrencinin ortalaması alıyor")
        
class Teacher(Person):
    def __init__(self,name,surname,age,branch):
        super().__init__(name,surname,age)
        self.branch = branch
        print("öğretmen oluşturuldu")
    def teach(self):
        print(f"{self.name} {self.surname} {self.branch} dersini anlatıyor")    

p1=Person("Ali","Yılmaz",30)
p1.info()
s1=Student("Ahmet","Demir",20,123)
s1.info()
print(f"Öğrenci numarası: {s1.number}")
s1.ortalam_al()
t1=Teacher("Ayşe","Kara",40,"Matematik")
t1.info()
print(f"Öğretmen branşı: {t1.branch}")
t1.teach()

