""" def ret (a,b):
    return a*b
print(ret(5,6))

def coz (a,b):
    return a%b
print(coz(54,6)) """


""" ccc """

""" def toplam ():
    return 454+545

sonuc = toplam()*3
print(sonuc)


def islem ():
    return 23/3
sonuc = islem()*3
print(sonuc)     """

""" def toplam():
    return 44+75
sonuc =toplam()/2

print(sonuc)
print(type(sonuc)) """

""" saat =22
def selamla():
    if saat<12:
        return "Günaydın"
    elif saat<18:
        return "İyi Günler"
    elif saat<20:
        return "İyi Akşamlar"
    else:
        return "İyi Geceler"
sonuc = selamla() + ", Meryem"
print(sonuc) """

""" gün = "Salı"

def gun_ismi():
    if gün == "Pazartesi":
        return "Bugün Pazartesi"
    elif gün == "Salı":
        return "Bugün Salı"
    elif gün == "Çarşamba":
        return "Bugün ��arşamba"
    elif gün == "Perşembe":
        return "Bugün Perşembe"
    elif gün == "Cuma":
        return "Bugün Cuma"
    elif gün == "Cumartesi":
        return "Bugün Cumartesi"
    elif gün == "Pazar":
        return "Bugün Pazar"
    else:
        return "Geçersiz gün"
sonuc = gun_ismi() + ", Meryem"
print(sonuc) """

notlar = [45, 65, 75, 85, 95]

def not_ortalamasi():
    toplam= 0 
    for notu in notlar:
        toplam += notu
        ortalama = toplam / len(notlar)
        return ortalama
    return 0
sonuc = not_ortalamasi()
print(sonuc)