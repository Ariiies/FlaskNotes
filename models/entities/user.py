from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, lastname="",username="", correo="", password=""):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.username = username
        self.correo = correo
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)
    
    def __str__(self):
        return (f"this user is: {self.name}, {self.lastname}, {self.username},{self.correo}, {self.password}")
#print(generate_password_hash("aries"))
