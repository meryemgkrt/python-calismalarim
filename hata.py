def users(username, city):
    citys=["istanbul", "ankara", "izmir"]
    if type(username) is not str:
        raise TypeError("username must be a string")
    if type(city) is not str:
        raise TypeError("Geçersiz city")
    if city not in citys:
        raise ValueError("Geçersiz city")
try:
    users("örthr", "öflgpt")  # Burada hata oluşur çünkü 123 bir string değil.
except Exception as e:
    print(e)  # Çıktı: username must be a string