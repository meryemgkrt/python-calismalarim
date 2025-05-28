class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        print(f"Active users: {cls.active_users}")
    
    @classmethod
    def str_class(cls, str_def):
        username, name, surname, age = str_def.split(",")
        return cls(username, name, surname, int(age))
    
    def __init__(self, username, name, surname, age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
    
    def UserName(self):
        return f"{self.username}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.username} çıkış yaptı."

User.display_active_users()  # Active users: 0
user5 = User.str_class("meryemgkrt,Meryem,Kurt,38")
print(user5.username)  # meryemgkrt
# veya
print(user5.UserName())  # meryemgkrt