class User:
    active_users = 0
    def __init__(self,username,name, surname, age):
        self.username= username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
    
    def UserName(self):
        return f"{self.username}"
    def logout(self):
        User.active_users -= 1
        return f"{self.username} çıkış yaptı."
    
print(f"Active users: {User.active_users}")
user1= User("meryemgkrt","Meryem", "Kurt", 38)
user2= User("john_doe", "John", "Doe", 35)
user3= User("jane_doe", "Jane", "Doe", 30)
user4=User("alice_smith", "Alice", "Smith", 28)
print(user2.logout())
print(user3.logout())
print(f"Active users: {User.active_users}")