class User:
    def __init__(self,username,name,surname,birtday):
        self.username = username
        self.name = name
        self.surname = surname
        self.birtday = birtday
        print("User created:", self.username, self.name, self.surname, self.birtday)
    def info(self):
        return f"{self.username} kullanıcı adıyla {self.name} {self.surname} olarak kaydedildi. Doğum tarihi: {self.birtday}"
    def calculateAge(self):
        return f"{self.name} kullanıcısının yasi {2025-self.birtday}"

user1 = User("john_doe", "John", "Doe", 1990)
user2=User("Mnk", "Meryem", "Kaya", 1998)
print(user1.username, user1.name, user1.surname, user1.birtday)
print(user2.username, user2.name, user2.surname, user2.birtday)

print(user2.info())
print(user1.calculateAge())
print(user2.calculateAge())